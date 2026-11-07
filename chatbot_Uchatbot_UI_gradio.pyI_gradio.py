
# import gradio as gr
# from google import genai

# # 1. Initialize Gemini client
# client = genai.Client(
#     api_key="your GEMINI API KEY GOES HERE""
# )

# # 2. Define chatbot function
# def chatbot(message, history):

#     # Convert Gradio history into Gemini conversation format
#     conversation = []

#     for msg in history:
#         conversation.append({
#             "role": msg["role"],
#             "parts": [{"text": msg["content"]}]
#         })

#     # Add current user message
#     conversation.append({
#         "role": "user",
#         "parts": [{"text": message}]
#     })

#     # Send conversation to Gemini
#     response = client.models.generate_content(
#         model="gemini-3.8-flash",
#         contents=conversation
#     )

#     return response.text


# # 3. Create Gradio Chat Interface
# demo = gr.ChatInterface(
#     fn=chatbot,
#     title="Gemini AI Chatbot",
#     description="Ask your questions to Gemini AI",
#     textbox=gr.Textbox(
#         placeholder="Ask something to Gemini...",
#         container=True
#     )
# )

# # 4. Launch application
# if __name__ == "__main__":
#     demo.launch()


import gradio as gr
from google import genai
from google.genai import types

# Initialize Gemini client
client = genai.Client(
    api_key="your GEMINI API KEY GOES HERE",
    http_options=types.HttpOptions(timeout=60000)
)

# Chatbot function
def chatbot(message, history):

    try:
        conversation = []

        # Convert Gradio history into Gemini format
        for msg in history:

            role = msg["role"]

            if role == "assistant":
                role = "model"

            if role not in ["user", "model"]:
                continue

            content = msg["content"]

            if isinstance(content, str) and content.strip():
                conversation.append({
                    "role": role,
                    "parts": [{"text": content}]
                })

        # Add current question
        conversation.append({
            "role": "user",
            "parts": [{"text": message}]
        })

        # Send request to Gemini
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=conversation
        )

        return response.text

    except Exception as e:
        return f"Error communicating with Gemini: {e}"


# Create Gradio interface
demo = gr.ChatInterface(
    fn=chatbot,
    title="Gemini AI Chatbot",
    description="Ask your questions to Gemini AI"
)

# Launch application
if __name__ == "__main__":
    demo.launch()
