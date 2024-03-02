# SPAM Titan Free Version

> A Python based REST API to check spam comments and emails in 1 file.

## Requirements 

- Python
- FAST API
- Docker Hub Account (optional)
- Cloud hosting account ( I'm using Azure )

## Why Python

Python has seen a surge in education and usage lately. From python.org, "Python is a programming language that lets you work more quickly and integrate your systems more effectively." It is remarkable how quickly you can launch a local server and run 1 page of code to do so many functions. This language is also built with speed and scalability in mind. 

## Getting Started

1. Download Python - https://www.python.org/downloads/
2. I used homebrew on mac to install it and PIP 
3. `pip3 install -r requirements.txt`
4. Install FastAPI - https://fastapi.tiangolo.com/#installation - `pip3 install fastapi` on my homebrew install
5. cd into /app
6. `uvicorn main:app --reload` - the server should start running
7. In a new terminal window - `curl -H 'Content-Type: application/json' -d '{"message":"i want to sell you SEO services","email":"badman@email.ru"}' -X POST http://localhost:8000/spam` 
8. You should get a response `{"message":"SEO picked up as spam","email":".ru not allowed","status":400}% `

> That's it! Now you can run python in your preferred cloud service and hit it from your preferred form hook.

## Saving to Docker

1. `docker build -t yourdockerhubusername/spamtitan .`
2. Run docker locally for check `docker run -d --name spamtitan -p 80:80 yourdockerhubusername/spamtitan`
3. Save the image `docker image save -o spamtitan.tar yourdockerhubusername/spamtitan`
4. Push to Docker Hub `docker push yourdockerhubusername/spamtitan`

## Azure

1. azure.microsoft.com
2. "Create a Resource"
3. "Create a Web App"
4. Choose your plan and service settings
5. Choose Docker settings - https://www.youtube.com/watch?v=_LNOg8kU4CE

## MODX Hook

1. add the code in /MODX/spamtitan.snippet.php to a Snippet in your manager
2. Call the snippet as a hook in FormIt