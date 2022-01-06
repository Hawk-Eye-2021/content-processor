
from flask_restful import Resource
from flask import request

from entityExtractor import extract_entities


class ProcessorController(Resource):

    def post(self):
        parts = request.json
        entities = set()
        for part in parts:
            part_entities = extract_entities(part)
            for part_entity in part_entities:
                entities.add(part_entity)
        return list(entities)
