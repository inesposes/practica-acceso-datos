FROM python:3.13
COPY scripts/mongo_insertion.py /
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir pymongo

CMD ["python", "./mongo_insertion.py"]
