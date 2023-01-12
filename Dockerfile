FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8282

USER 1000

CMD [ "python", "./server.py" ]
