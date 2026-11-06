
import os
from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(
        timeout=120000
    )
)

try:
    print("Sending request to Gemini...")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Explain how AI works in a few words"
    )

    print("Gemini response:")
    print(response.text)

except Exception as e:
    print("Error occurred:", e)
