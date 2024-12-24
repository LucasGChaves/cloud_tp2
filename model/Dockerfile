FROM python:3.12.8-slim-bullseye

RUN mkdir -p /pickle
RUN mkdir -p /model

WORKDIR /model

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "fp.py"]