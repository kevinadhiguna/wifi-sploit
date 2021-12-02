FROM python:3-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY .dockerignore .
COPY password.txt .
COPY username.txt .
COPY wfs.py .

CMD ["python3", "wfs.py"]
