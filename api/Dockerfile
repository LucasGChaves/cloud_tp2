FROM python:3.12.8-slim-bullseye

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos necessários para o container
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da API para o container
COPY . .

# Definir as variáveis de ambiente para o Flask
ENV FLASK_APP=app.py

# Expor a porta 5000 para acesso externo
EXPOSE 5000

# Comando para iniciar o Flask quando o container for iniciado
CMD ["flask", "run", "--host=0.0.0.0"]