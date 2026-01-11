FROM python:3.7.3-alpine3.9

WORKDIR /app

COPY requirements.txt .

ADD . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]
