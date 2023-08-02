FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY main.py /app/main.py
COPY packages.json /app/packages.json

CMD [ "python", "-u", "main.py" ]
