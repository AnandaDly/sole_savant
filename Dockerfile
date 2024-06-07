# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    wget \
    rsync \
    && rm -rf /var/lib/apt/lists/*

# Create the directory where the file will be saved
RUN mkdir -p model/hugging

# Download the file from Google Drive into the model/hugging directory
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-9ArNjRzwmFUDy8a5Vt5xE_1zck4JdEa' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-9ArNjRzwmFUDy8a5Vt5xE_1zck4JdEa" -O model/hugging/model.safetensors && rm -rf /tmp/cookies.txt

# Copy requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Change working directory before cloning the repository
WORKDIR /tmp

# Clone your own repository from GitHub
RUN git clone https://github.com/AnandaDly/sole_savant

# Move the repository contents to the /app directory using rsync
RUN rsync -a /tmp/sole_savant/ /app/

EXPOSE 8501

# Define a health check for the container
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Set the entry point for the container
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
