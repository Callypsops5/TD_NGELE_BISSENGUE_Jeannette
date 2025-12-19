FROM python:3.11-slim

WORKDIR /app

# Installer curl (nécessaire pour healthcheck)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Utilisateur non-root
RUN useradd -m appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /data/db \
    && chown -R appuser:appuser /data /app

USER appuser

EXPOSE 8080

CMD ["sh", "-c", "python init_db.py && python app.py"]
