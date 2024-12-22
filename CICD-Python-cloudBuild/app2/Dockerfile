FROM python:3.9-alpine
RUN pip install flask
WORKDIR /myapp
COPY /app2/app.py /myapp/main.py
CMD ["python","/myapp/main.py"]