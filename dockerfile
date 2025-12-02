FROM python:3.9.9-slim-buster
WORKDIR /app
COPY ./app
RUN apt update-y && apt install awscli -y
RUN pip install -r requirement.txt
CMD["Python3","app.py"]