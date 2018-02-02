from flask import Flask, jsonify, request
from flask_cors import CORS
from bot import ChatBot
from chatterbot.utils import nltk_download_corpus

import nltk

from token_replacer import TokenReplacer, Image, Link


from token_replacer import Link, RandomGif, Image

import uuid

app = Flask(__name__)
CORS(app, resources = {r"/bot": {"origins": "*"}})

entries = {
    'link:achados_e_perdidos': Link('achados_e_perdidos', 'aqui', 'https://99taxis.zendesk.com/hc/pt-br/requests/new?ticket_form_id=322427'),
    'link:contato': Link('contato', 'aqui', 'https://99taxis.zendesk.com/hc/pt-br/requests/new?ticket_form_id=322427'),
    'link:contato_motorista': Link('contato_motorista', 'aqui', 'https://99taxis.zendesk.com/hc/pt-br/requests/new?ticket_form_id=322427'),
    'link:play_store_99': Link('play_store_99', 'Play Store', 'https://play.google.com/store/apps/details?id=com.taxis99&hl=pt'),
    'link:play_store_driver_99': Link('play_store_driver_99', 'Play Store', 'https://play.google.com/store/apps/details?id=com.nineninetaxis.driver&hl=pt'),
    'link:apple_store_99': Link('apple_store_99', 'Apple Store', 'https://itunes.apple.com/br/app/99-t%C3%A1xi-e-carro-particular/id553663691?mt=8'),
    'link:fale_conosco': Link('fale_conosco', 'Fale Conosco', 'https://99app.com/fale-conosco/'),
    'link:99': Link('99', 'https://99app.com/', 'https://99app.com/'),
    'link:faq': Link('faq', 'FAQ', 'https://99taxis.zendesk.com/hc/pt-br'),
    'img:go99': Image('go99', 'https://big.assets.huffingtonpost.com/ngWipN.gif'),
    'randomgif:questions': RandomGif('questions', [
        'https://giphy.com/embed/cMVgEhDeKzPwI'
    ])
}

tokenReplacer = TokenReplacer(entries)
chatbot = ChatBot(tokenReplacer)

@app.route('/bot', methods=['POST'])
def answer():
    body = request.get_json(force=True)

    conversation_id = body.get("conversation_id", str(uuid.uuid1()))
    question = body['question']

    answer = chatbot.answer(conversation_id, question)

    response = {}
    response['question'] = question
    response['conversation_id'] = conversation_id
    response['answer'] = answer

    return jsonify(response)

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

nltk_download_corpus('corpora/stopwords')
app.run(host="0.0.0.0")   
