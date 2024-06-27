import nltk
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from nltk import word_tokenize, pos_tag, ne_chunk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Initialize Flask and Flask-RESTx
app = Flask(__name__)
api = Api(app, version='1.0', title='NLP API',
          description='A simple NLP API using NLTK with Swagger documentation')

ns = api.namespace('nlp', description='NLP operations')

# Models for Swagger documentation
token_model = api.model('Tokenize', {
    'text': fields.String(required=True, description='Text to be tokenized')
})

pos_tag_model = api.model('POSTag', {
    'text': fields.String(required=True, description='Text for POS tagging')
})

ner_model = api.model('NER', {
    'text': fields.String(required=True, description='Text for named entity recognition')
})


# Endpoints with Swagger documentation
@ns.route('/tokenize')
class Tokenize(Resource):
    @ns.expect(token_model)
    def post(self):
        data = request.get_json()
        text = data.get('text', '')
        tokens = word_tokenize(text)
        return jsonify(tokens)


@ns.route('/pos_tag')
class POSTag(Resource):
    @ns.expect(pos_tag_model)
    def post(self):
        data = request.get_json()
        text = data.get('text', '')
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        return jsonify(pos_tags)


@ns.route('/ner')
class NER(Resource):
    @ns.expect(ner_model)
    def post(self):
        data = request.get_json()
        text = data.get('text', '')
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        chunks = ne_chunk(pos_tags)
        entities = [{'word': ' '.join(c[0] for c in chunk), 'label': chunk.label()}
                    for chunk in chunks if hasattr(chunk, 'label')]
        return jsonify(entities)


# Add namespace to API
api.add_namespace(ns)

if __name__ == '__main__':
    app.run()
