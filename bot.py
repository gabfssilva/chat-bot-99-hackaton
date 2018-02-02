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
		    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
			logic_adapters=[
              {
                'import_path': 'chatterbot.logic.BestMatch'
              },
              {
                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                'threshold': 0.50,
                'default_response': 'Eu não entendi. Bem, eu sou um robozinho meio lerdo e preciso que você explique de uma forma detalhada com palavras chaves para que eu entenda melhor. Pode refazer a sua pergunta?'
              }
            ]
		)

		self.chatbot.train("chatterbot.corpus.portuguese.conversations")
		self.chatbot.train("chatterbot.corpus.portuguese.greetings")
		self.chatbot.train("./corpus")

	def answer(self, conversation_id, question):
	    response = self.chatbot.get_response(question)
	    return response    
