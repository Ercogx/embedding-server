FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Expose port
EXPOSE 8001

# Default command
CMD ["python", "main.py"]
