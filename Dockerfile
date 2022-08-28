FROM python:3.9-slim

COPY requirements.txt .

RUN pip install -r requirements.txt


WORKDIR /app
COPY . /app/

CMD ["python3"],"app.py",CMD["python3","m","streamlit","RUN","--host:0.0.0.0"]