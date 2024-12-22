FROM python:3.9-alpine
RUN pip install flask
WORKDIR /myapp
COPY /app/app.py /myapp/main.py
CMD ["python","/myapp/main.py"]