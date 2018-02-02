from flask import Flask, jsonify, request
from flask_cors import CORS
from bot import ChatBot
from chatterbot.utils import nltk_download_corpus

from token_replacer import TokenReplacer, Image, Link


from token_replacer import Link

import uuid

app = Flask(__name__)
CORS(app, resources = {r"/bot": {"origins": "*"}})

chatbot = ChatBot()

tokens = {
    'link:achados_e_perdidos': Link('achados_e_perdidos', 'Aqui', 'https://99taxis.zendesk.com/hc/pt-br/requests/new?ticket_form_id=322427'),
    'img:go99': Image('go99', 'https://big.assets.huffingtonpost.com/ngWipN.gif')
}

@app.route('/bot', methods=['POST'])
def answer():
    body = request.get_json(force=True)

    conversation_id = body.get("conversation_id", str(uuid.uuid1()))
    question = body['question']

    answer = chatbot.answer(conversation_id, question)

    response = {}
    response['question'] = question
    response['conversation_id'] = conversation_id
    response['answer'] = answer.text

    return jsonify(response)


nltk_download_corpus('corpora/stopwords')
app.run(host="0.0.0.0")   