from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import re

app = FastAPI()

badwords = [
     'dogecoin','viagra','porn','sex','babes','gambling','poker','bitcoin','bit.ly','https','bit.ly','free','youtu.be','youtube','example','test','seo','jasper','free'
]

bademails = [
    '.ru','example','test','ericjones','eric.jones'
]

special_characters = re.compile('[@_!#$%^&*()<>?/|}{~:]')

class Input(BaseModel):
     message: str
     email: str

class Response(BaseModel):
     message: str
     email: str
     status: int = 200

#@app.get('/spam')

#def show_words():
#     response = Response(message = "i want to sell you seo",email = "")
#     return jsonable_encoder(response)


@app.post('/spam')

async def check_spam(data: Input):
     message_response = ""
     email_response = ""
     msg_arr = data.message.split()

     for x in msg_arr:
         if x.lower() in badwords:
          message_response = x+" picked up as spam"

         if special_characters.search(x):
          message_response = "Special characters are not allowed" 

     for x in bademails:
         if x.lower() in data.email:
          email_response = x+" not allowed"     

     if message_response == "" and email_response == "":
          return {"status":200}     
     
     response = Response(message = message_response,email = email_response,status = 400)
     return response
