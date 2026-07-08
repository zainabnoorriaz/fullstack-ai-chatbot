from sqlalchemy.orm import Session

import models
import schemas
from ai_service import (
    ask_gemini,
    convert_messages,
    generate_chat_title,
)


# -----------------------
# Create Chat
# -----------------------
def create_chat(db: Session, chat: schemas.ChatCreate):

    new_chat = models.Chat(
        title="New Chat",
        is_title_generated=False
    )

    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)

    return new_chat


# -----------------------
# Send Message
# -----------------------
def create_message(db: Session, chat_id: int, message: schemas.MessageCreate):

    chat = db.query(models.Chat).filter(
        models.Chat.id == chat_id
    ).first()

    if chat is None:
        return {"error": "Chat not found"}

    # Save user message
    user_message = models.Message(
        chat_id=chat_id,
        role="user",
        content=message.content
    )

    db.add(user_message)
    db.commit()
    db.refresh(user_message)

    # Get conversation history
    messages = db.query(models.Message).filter(
        models.Message.chat_id == chat_id
    ).all()

    conversation = convert_messages(messages)

    # Ask Gemini
    ai_response = ask_gemini(conversation)

    # Save assistant response
    assistant_message = models.Message(
        chat_id=chat_id,
        role="assistant",
        content=ai_response
    )

    db.add(assistant_message)
    db.commit()
    db.refresh(assistant_message)

    # Generate title only once
    if not chat.is_title_generated:
        chat.title = generate_chat_title(message.content)
        chat.is_title_generated = True

        db.commit()
        db.refresh(chat)

    return {
        "user_message": {
            "id": user_message.id,
            "role": user_message.role,
            "content": user_message.content
        },
        "assistant_message": {
            "id": assistant_message.id,
            "role": assistant_message.role,
            "content": assistant_message.content
        }
    }


# -----------------------
# Get All Chats
# -----------------------
def get_all_chats(db: Session):
    return db.query(models.Chat).all()


# -----------------------
# Get One Chat
# -----------------------
def get_chat(db: Session, chat_id: int):
    return db.query(models.Chat).filter(
        models.Chat.id == chat_id
    ).first()


# -----------------------
# Delete Chat
# -----------------------
def delete_chat(db: Session, chat_id: int):

    chat = db.query(models.Chat).filter(
        models.Chat.id == chat_id
    ).first()

    if chat is None:
        return {"error": "Chat not found"}

    db.delete(chat)
    db.commit()

    return {
        "message": "Chat deleted successfully"
    }