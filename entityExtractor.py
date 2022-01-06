from flair.data import Sentence
from flair.models import SequenceTagger

tagger = None


def init_tagger():
    global tagger
    tagger = SequenceTagger.load('es-ner-large')


def extract_entities(string):
    sentence = Sentence(string)
    tagger.predict(sentence)
    entities = sentence.get_spans('ner')
    entities_texts = []
    for entity in entities:
        entities_texts.append(entity.text)
    return entities_texts
