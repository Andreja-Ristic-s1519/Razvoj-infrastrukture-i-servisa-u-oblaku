FROM python:3

WORKDIR /apps/userAPIClient

RUN pip install requests
COPY client.py .

CMD ["python", "client.py"]