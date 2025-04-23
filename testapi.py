from google import genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()  # Loads environment variables from the .env file
api_key = os.getenv("API_KEY")  # Retrieve the API key securely
if not api_key:
    raise ValueError("API key not found. Please set it in the .env file.")

# Initialize genai client with the retrieved API key
client = genai.Client(api_key=api_key)

# Generate content
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words",
)

# Print the response
print(response.text)
