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
		    "./lost_items.yml",
			"./rate_driver.yml",
			"./wrong_estimative.yml",
			"./ride_finished_after.yml",
			"./wrong_path.yml"
		)

	def answer(self, conversation_id, question):
	    response = self.chatbot.get_response(question)
	    return response    
