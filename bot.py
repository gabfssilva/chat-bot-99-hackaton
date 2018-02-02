import chatterbot 

class Link:
    def __init__(self, token, text, href):
        self.token = token
        self.text = text
        self.href = href

    def render(self):
        return '<a class="follow_link" href="' + self.href + '">' + self.text +'<a/>'    

class Image:
    def __init__(self, token, href):
       self.token = token
       self.href = href

    def render(self):
        return '<img src="' + self.href + '"/>'    

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
			"./ride_finished_after.yml"
		)

	def answer(self, conversation_id, question):
	    response = self.chatbot.get_response(question)
	    return response    
