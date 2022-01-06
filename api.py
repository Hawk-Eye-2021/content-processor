from flask import Flask
from flask_restful import Api
from controllers import helloController, processorController

app = Flask(__name__)

api = Api(app)

api.add_resource(helloController.HelloController, '/api/hello')
api.add_resource(processorController.ProcessorController, '/contents')

if __name__ == '__main__':
    app.run(debug=True)
