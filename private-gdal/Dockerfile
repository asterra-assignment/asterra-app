FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt . 
RUN apk add --no-cache gdal gdal-dev gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
