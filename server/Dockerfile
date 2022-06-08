FROM python:3

EXPOSE 8081

WORKDIR /apps/userAPI

RUN pip install flask
COPY app.py .

CMD ["python", "app.py"]
