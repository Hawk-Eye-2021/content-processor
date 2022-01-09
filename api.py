from flask import Flask
from flask_restful import Api
from controllers import helloController, processorController
from entityExtractor import init_tagger

init_tagger()

app = Flask(__name__)

api = Api(app)


api.add_resource(helloController.HelloController, '/api/hello')
api.add_resource(processorController.ProcessorController, '/contents')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
