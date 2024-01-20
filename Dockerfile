FROM python:alpine

RUN pip install poetry
RUN mkdir /images

WORKDIR /app
ADD pyproject.toml .
ADD poetry.lock    .

RUN poetry env use system
RUN poetry install

ADD main.py .

EXPOSE 80
ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
