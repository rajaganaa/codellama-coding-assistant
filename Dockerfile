FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install transformers peft torch bitsandbytes accelerate fastapi uvicorn
COPY app.py .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
