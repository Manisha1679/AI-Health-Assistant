#setting up Groq api key
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#convert image to required format
import base64



def encode_image(image_path):
    # image_path="acne.jpg"
    image_file=open(image_path,"rb") #rb=read binary
    return base64.b64encode(image_file.read()).decode("utf-8")

#setup multimodal llm
from groq import Groq

query="Is there something wrong with my face?"
model="meta-llama/llama-4-scout-17b-16e-instruct"
def analyze_image_with_query(query,model,encoded_image):
    client=Groq()
    
    messages=[
    {
        "role":"user",
        "content":[
            {
                "type":"text",
                "text":query
            },
            {
                "type":"image_url",
                "image_url":{
                    "url":f"data:image/jpeg;base64,{encoded_image}"
              }
            }
          ]
       }
    ] 
    chat_completion=client.chat.completions.create(
    messages=messages,
    model=model
    )
    return chat_completion.choices[0].message.content