from flask import Flask, rendrer_template

def create_app():

    app = Flask(__name__)

    app.route('/')
    def hello_world():
        return 'Hello, World!'
    return app