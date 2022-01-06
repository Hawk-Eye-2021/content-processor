from flask_restful import Resource
from flask import request


class ProcessorController(Resource):

    def post(self):
        parts = request.json
        entities = []
        for part in parts:
            entities.append({part: '-1'})
        return entities
