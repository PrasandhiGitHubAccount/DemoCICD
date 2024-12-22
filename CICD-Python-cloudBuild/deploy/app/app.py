from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello world, This is my 1st Application'
if __name__=='__main__':
        app.run()