import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# -----------------------
# Ask Gemini
# -----------------------
def ask_gemini(conversation):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        return response.text


    except ClientError as e:

        if "RESOURCE_EXHAUSTED" in str(e):

            print("Gemini Error: quota exceeded")

            return (
                "⚠️ ZeeBot is temporarily rate-limited.\n"
                "Please wait a little while and try again."
            )

        print("Gemini Client Error:", e)

        return (
            "⚠️ ZeeBot encountered a Gemini API error."
        )


    except Exception as e:

        print("Unexpected Gemini Error:", e)

        return (
            "⚠️ ZeeBot encountered an unexpected error."
        )


# -----------------------
# Convert Database Messages
# -----------------------
def convert_messages(messages):

    conversation = []

    for message in messages:

        role = "user"

        if message.role == "assistant":
            role = "model"

        conversation.append(
            {
                "role": role,
                "parts": [
                    {
                        "text": message.content
                    }
                ]
            }
        )

    return conversation


# -----------------------
# Generate Chat Title
# -----------------------
def generate_chat_title(first_message):

    prompt = f"""
Generate a very short title (maximum 5 words)
for this conversation.

Only return the title.

Message:
{first_message}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()


    except ClientError as e:

        if "RESOURCE_EXHAUSTED" in str(e):

            print("Title Generation Error: quota exceeded")

            return "New Chat"

        print("Title Generation Error:", e)

        return "New Chat"


    except Exception as e:

        print("Unexpected Title Error:", e)

        return "New Chat"