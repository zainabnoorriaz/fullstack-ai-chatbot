# fullstack-ai-chatbot
# 🤖 Full Stack AI Chatbot

A full-stack AI chatbot built with **FastAPI**, **JavaScript**, **HTML/CSS**, **SQLAlchemy**, and the **Google Gemini API**. The chatbot supports multiple conversations, automatically generates chat titles, stores chat history in a database, and provides a clean, responsive user interface.

---

## ✨ Features

* 💬 Create multiple chat conversations
* 🧠 AI responses powered by Google Gemini
* 📝 Automatic chat title generation
* 📚 Persistent chat history using SQLite
* 🗂️ Sidebar displaying previous conversations
* 🗑️ Delete chat conversations
* ⚡ FastAPI REST API backend
* 🎨 Clean frontend built with HTML, CSS, and JavaScript

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Google Gemini API
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

---

## 📁 Project Structure

```text
full_stack_ai_chatbot/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── ai_service.py
│   ├── requirements.txt
│   ├── .env.example
│   └── ...
│
├── front_end/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── assets-screenshots/
```
## 📸 Project Screenshots

### 1️⃣ User Interface
The clean homepage where users can upload PDFs and interact with the AI assistant.

![User Interface](assets/01.interface.png)

---

### 2️⃣ Sidebar Chat History
Previously created conversations are displayed in the sidebar for quick access.

![Sidebar Chats](assets/02.sidebar-chats.png)

---

### 3️⃣ AI Conversation Demo
The assistant answers questions based on the uploaded PDF using Retrieval-Augmented Generation (RAG).

![Conversation Demo](assets/03.conversation-demo.png)

---

### 4️⃣ FastAPI Swagger Documentation
Overview of all available API endpoints.

![Swagger Overview](assets/04.swagger-overview.png)

---

### 5️⃣ Chat API Endpoint
Testing the chat endpoint directly from the FastAPI documentation.

![Swagger Chat Endpoint](assets/05.swagger-create-chat.png)

---

### 6️⃣ FastAPI Response
Backend successfully returns an AI-generated response.

![FastAPI Response](assets/06.response-from-fastapi.png)

---

### 7️⃣ Database Preview
SQLite database storing uploaded PDFs, chunks, and chat history.

![Database Preview](assets/07.database-preview.png)
---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/zainabnoorriaz/fullstack-ai-chatbot.git
cd fullstack-ai-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.\.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Configure your API key

Inside the `backend` folder, create a file named `.env`.

Add your own Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Start the backend

```bash
cd backend
uvicorn main:app --reload
```

### 6. Open the frontend

Open `front_end/index.html` in your browser.

---


## 🎯 Future Improvements

* User authentication
* Streaming AI responses
* Markdown rendering
* File upload support
* Dark/Light theme toggle
* Cloud deployment

---

## 📚 What I Learned

This project helped me gain hands-on experience with:

* Building REST APIs using FastAPI
* Connecting a frontend with a backend
* Working with SQLAlchemy and SQLite
* Integrating the Google Gemini API
* Managing multiple chat conversations
* Using Git and GitHub for version control
* Protecting API keys using environment variables

---

## 👩‍💻 Author

**Zainab Noor Riaz**

Computer Science Student | Aspiring AI Engineer

GitHub: https://github.com/zainabnoorriaz



