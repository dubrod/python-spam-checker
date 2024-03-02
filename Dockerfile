FROM --platform=linux/amd64 python:3.10-slim

# required for pip install using git/ssh (you prob won't need and can remove to reduce image size)
RUN apt-get update && \
  apt-get install -y git

WORKDIR /app

# add requirements (add your requirements if you have any, if not skip)
COPY ./requirements.txt /app/requirements.txt

# install package dependencies (if needed, if no skip)
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# add source code
COPY ./app /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]