FROM python:3.9.7-slim-buster
WORKDIR /drf-app
COPY . .
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
EXPOSE 8080
CMD ["python","manage.py","runserver","0.0.0.0:8080"]
