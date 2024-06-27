import unittest
import json
from app import app


class TestNLPAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_tokenize(self):
        response = self.app.post('/nlp/tokenize', data=json.dumps({'text': 'This is a test sentence.'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, ["This", "is", "a", "test", "sentence", "."])

    def test_pos_tag(self):
        response = self.app.post('/nlp/pos_tag', data=json.dumps({'text': 'This is a test sentence.'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [["This", "DT"], ["is", "VBZ"], ["a", "DT"], ["test", "NN"], ["sentence", "NN"], [".", "."]])

    def test_ner(self):
        response = self.app.post('/nlp/ner', data=json.dumps({'text': 'Rihanna was born in Barbados.'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{"word": "Rihanna", "label": "PERSON"}, {"word": "Barbados", "label": "GPE"}])

    def test_tokenize_no_text(self):
        response = self.app.post('/nlp/tokenize', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_pos_tag_no_text(self):
        response = self.app.post('/nlp/pos_tag', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_ner_no_text(self):
        response = self.app.post('/nlp/ner', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_invalid_json(self):
        response = self.app.post('/nlp/tokenize', data='Invalid JSON', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

        response = self.app.post('/nlp/pos_tag', data='Invalid JSON', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

        response = self.app.post('/nlp/ner', data='Invalid JSON', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)



if __name__ == '__main__':
    unittest.main()
