from dotenv import load_dotenv
import os
import base64
from groq import Groq

# Setting up GROQ API key
load_dotenv()
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')


# convert image to required format
def encode_image(image_path):
    image_file = open(image_path, 'rb')
    return base64.b64encode(image_file.read()).decode('utf-8')


# Setup multimodal LLM
# query="Is there something wrong with my face?"
# model="llama-3.2-90b-vision-preview"
def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    # Extract and return the content of the response
    response_content = chat_completion.choices[0].message.content
    return response_content