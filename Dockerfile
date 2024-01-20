FROM python:alpine

RUN mkdir /images

WORKDIR /app
ADD requirements.txt .

RUN pip install -r requirements.txt

ADD main.py .

EXPOSE 80
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
