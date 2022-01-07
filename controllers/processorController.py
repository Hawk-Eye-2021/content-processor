
from flask_restful import Resource
from flask import request, jsonify

from entityExtractor import extract_entities


class ProcessorController(Resource):

    def post(self):
        content = request.get_json(force=True, silent=True, cache=False)['content']

        entities = set()
        part_entities = extract_entities(content)
        for part_entity in part_entities:
            entities.add(part_entity)
        return list(entities)
