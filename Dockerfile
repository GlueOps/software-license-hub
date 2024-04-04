FROM python:3.11.8-alpine@sha256:b6bd7d58b4e0f38cd151de9b96fffc9edf647bc6ba490ffe772d5d5eab11acda

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY main.py /app/main.py
COPY packages.json /app/packages.json

CMD [ "python", "-u", "main.py" ]
