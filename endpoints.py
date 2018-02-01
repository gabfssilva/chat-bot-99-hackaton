from flask import Flask, jsonify, request
from bot import ChatBot
from chatterbot.utils import nltk_download_corpus

import uuid

app = Flask(__name__)

chatbot = ChatBot()

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
app.run()