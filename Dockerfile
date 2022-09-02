FROM python:3.7-slim

WORKDIR /dashboard

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT [ "streamlit" ,"run"]

CMD [ "app.py" ]