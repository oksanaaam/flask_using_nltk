# NLP API

A simple NLP API using Python, Flask, and NLTK with Swagger documentation. This API provides endpoints for text tokenization, part-of-speech (POS) tagging, and named entity recognition (NER).

## Requirements

- Python 3.x
- Virtual environment for dependency management

## Setup Instructions


1. Clone the Repository

```
   git clone https://github.com/oksanaaam/flask_using_nltk.git
   cd flask_using_nltk
```

2. Create and Activate a Virtual Environment

Create a virtual environment to manage your dependencies.
```
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
```

3. Install Dependencies

Install the required Python packages using pip.

   `pip install -r requirements.txt`

4. Run the Application

Start the Flask server.

   `python app.py`

The server will start running at http://127.0.0.1:5000/.

## API Endpoints

To test all the endpoints of your REST API, you can use an API testing tool like Postman or curl.  
For running tests you can use `python -m unittest tests/test_api.py`

### Tokenize Text
URL: /nlp/tokenize
Method: POST
Request Body:
```json
{
  "text": "Hello, my name is Oksana."
}
```
Response:
```json
["Hello",",","my","name","is","Oksana"]
```
![tokenize.png](img_for_README.md%2Ftokenize.png)

### POS Tagging
URL: /nlp/pos_tag
Method: POST
Request Body:
```json
{
  "text": "Hello, my name is Oksana."
}
```
Response:
```json
[["Hello","NNP"],[",",","],["my","PRP$"],["name","NN"],["is","VBZ"],["Oksana","NNP"]]
```
![pos_tag.png](img_for_README.md%2Fpos_tag.png)

### Named Entity Recognition (NER)
URL: /nlp/ner
Method: POST
Request Body:
```json
{
  "text": "Harry is common first name in London."
}
```
Response:
```json
[{"word": "Harry", "label": "PERSON"}, {"word": "London", "label": "GPE"}]
```
![ner.png](img_for_README.md%2Fner.png)

## Swagger Documentation

Swagger documentation for the API is available at http://127.0.0.1:5000/.
