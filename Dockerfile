FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY lesson11.py shop_info.txt ./
EXPOSE 8000
CMD ["uvicorn", "lesson11:app", "--host", "0.0.0.0", "--port", "8000"]