FROM python:3.12
COPY requirements.txt /
COPY scripts/mongo_insertion.py /

RUN pip install --no-cache-dir -r /requirements.txt

CMD ["python", "./mongo_insertion.py"]
