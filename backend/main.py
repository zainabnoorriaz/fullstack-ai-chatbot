from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine
import crud
import schemas

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://127.0.0.1:5501"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Database session
# -----------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------
# Create a new chat
# -----------------------
@app.post("/chats")
def create_chat(chat: schemas.ChatCreate, db: Session = Depends(get_db)):
    return crud.create_chat(db, chat)


# -----------------------
# Get all chats
# -----------------------
@app.get("/chats", response_model=list[schemas.Chat])
def get_all_chats(db: Session = Depends(get_db)):
    return crud.get_all_chats(db)


@app.get("/chats/{chat_id}", response_model=schemas.Chat)
def get_chat(chat_id: int, db: Session = Depends(get_db)):
    return crud.get_chat(db, chat_id)

@app.delete("/chats/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    return crud.delete_chat(db, chat_id)


# -----------------------
# Send message
# -----------------------
@app.post("/chats/{chat_id}/messages")
def create_message(
    chat_id: int,
    message: schemas.MessageCreate,
    db: Session = Depends(get_db)
):
    print(f"Received message for chat {chat_id}")

    return crud.create_message(db, chat_id, message)


# -----------------------
# Home
# -----------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Chatbot Backend!"
    }