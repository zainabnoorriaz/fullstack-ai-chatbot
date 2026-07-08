console.log("JS loaded");


const messagesContainer = document.getElementById("messages");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-btn");
const newChatButton = document.getElementById("new-chat-btn");
const chatList = document.getElementById("chat-list");

let currentChatId = null;

async function createChat() {


    const response = await fetch(
        "http://127.0.0.1:8000/chats",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({})
        }
    );

    const chat = await response.json();

    currentChatId = chat.id;

    console.log("Current Chat:", currentChatId);

}
async function loadChats() {

    const response = await fetch(
        "http://127.0.0.1:8000/chats"
    );

    const chats = await response.json();

    chatList.innerHTML = "";

    chats.forEach(function(chat) {

        // Main row
        const chatItem = document.createElement("div");

        chatItem.style.display = "flex";
        chatItem.style.justifyContent = "space-between";
        chatItem.style.alignItems = "center";
        chatItem.style.padding = "8px";
        chatItem.style.marginBottom = "5px";

        // Chat title
        const title = document.createElement("span");

        title.textContent = "💬 " + chat.title;
        title.style.cursor = "pointer";

        title.addEventListener("click", function () {

            loadConversation(chat.id);

        });

        // Delete button
        const deleteButton = document.createElement("button");

        deleteButton.textContent = "🗑️";
        deleteButton.style.cursor = "pointer";
        deleteButton.style.border = "none";
        deleteButton.style.background = "transparent";
        deleteButton.style.fontSize = "16px";

        deleteButton.addEventListener("click", async function(event) {

            event.stopPropagation();

            if (confirm("Delete this chat?")) {

                await deleteChat(chat.id);

            }

        });

        chatItem.appendChild(title);
        chatItem.appendChild(deleteButton);

        chatList.appendChild(chatItem);

    });

}
async function loadConversation(chatId) {

    currentChatId = chatId;

    const response = await fetch(
        `http://127.0.0.1:8000/chats/${chatId}`
    );

    const chat = await response.json();

    messagesContainer.innerHTML = "";

    chat.messages.forEach(function(message) {

        addMessage(
            message.role,
            message.content
        );

    });

    console.log("Conversation loaded:", chat.title);

}
async function deleteChat(chatId) {

    const response = await fetch(
        `http://127.0.0.1:8000/chats/${chatId}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    console.log(data);

    // If the deleted chat was open, clear the messages
    if (currentChatId === chatId) {

        messagesContainer.innerHTML = "";

        currentChatId = null;

    }

    await loadChats();

}
async function sendMessage(message) {
    
    if (currentChatId === null) {

    await createChat();

}

    console.log("Starting fetch");


    try {

        const response = await fetch(
            `http://127.0.0.1:8000/chats/${currentChatId}/messages`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    content: message
                })
            }
        );


        console.log("Fetch finished");

        console.log("Status:", response.status);


        const data = await response.json();


        console.log("Backend:", data);



        // Add user message

        addMessage(
            "user",
            data.user_message.content
        );
        await loadChats();



        // Add assistant message

        addMessage(
            "assistant",
            data.assistant_message.content
        );


    }


    catch(error) {

        console.error("Fetch error:", error);

    }

}




function addMessage(role, content) {


    console.log("Adding bubble:", role, content);



    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");



    const avatar = document.createElement("div");

    avatar.classList.add("avatar");



    const bubble = document.createElement("div");

    bubble.classList.add("bubble");



    bubble.textContent = content;



    if (role === "user") {


        messageDiv.classList.add("user-message");

        avatar.textContent = "🌸";


        messageDiv.appendChild(bubble);

        messageDiv.appendChild(avatar);


    }


    else {


        messageDiv.classList.add("ai-message");

        avatar.textContent = "🤖";


        messageDiv.appendChild(avatar);

        messageDiv.appendChild(bubble);


    }



    messagesContainer.appendChild(messageDiv);


}




sendButton.addEventListener("click", function(event) {


    event.preventDefault();



    const message = messageInput.value.trim();



    if (!message) {

        return;

    }



    console.log("User:", message);



    sendMessage(message);



    messageInput.value = "";


});
newChatButton.addEventListener("click", async function () {

    await createChat();

    messagesContainer.innerHTML = "";

    await loadChats();

    console.log("New chat created:", currentChatId);

});
loadChats();