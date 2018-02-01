import chatterbot 

class ChatBot:
	def __init__(self):
		self.chatbot = chatterbot.ChatBot(
		    'Ron Obvious',
		    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
		)

		self.chatbot.train("chatterbot.corpus.portuguese")
		self.chatbot.train(
		    "./questions.yml",
		    "./cupom.yml",
		    "./lost_items.yml"
		)

	def answer(self, conversation_id, question):
	    response = self.chatbot.get_response(question)
	    return response

# get_response("Oi, como você tá?")
# get_response("Bem também.")
# get_response("Estou com um problema, pode me ajudar?")
# get_response("então, eu acabei de receber uma cobrança indevida")
# get_response("acho que foi durante o cadastro")
# get_response("Ah, obrigado então!")
# get_response("Vish, acho que tenho mais uma dúvida.")
# get_response("A tem mais uma coisa, esqueci meu guarda-chuva no carro")
