from pydantic import BaseModel


# -----------------------
# Requests
# -----------------------

class ChatCreate(BaseModel):
    pass


class MessageCreate(BaseModel):
    content: str


# -----------------------
# Responses
# -----------------------

class Message(BaseModel):
    id: int
    chat_id: int
    role: str
    content: str

    class Config:
        from_attributes = True


class Chat(BaseModel):
    id: int
    title: str
    is_title_generated: bool
    messages: list[Message] = []

    class Config:
        from_attributes = True