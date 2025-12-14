FROM python:3.11-slim

WORKDIR /app

# System dependencies (kept minimal)
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PORT=5000
EXPOSE 5000

CMD ["python", "app.py"]
