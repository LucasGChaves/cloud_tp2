FROM python:3.12.8-slim-bullseye

WORKDIR /model

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "fp.py"]