FROM python:3.11-slim

WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip

# Tkinter dependencies (Debian slim needs these)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tk \
    tcl \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libsm6 \
    libice6 \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Default Flask API base in container network:
ENV API_BASE=http://backend:5000

CMD ["python", "gui_app.py"]
