FROM python:3.12-slim
COPY requirements.txt /
COPY scripts/api_news.py /
RUN pip install --no-cache-dir -r /requirements.txt

CMD ["python", "./api_news.py"]
