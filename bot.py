import chatterbot 

class ChatBot:
    def __init__(self, tokenReplacer):
        self.tokenReplacer = tokenReplacer

        self.chatbot = chatterbot.ChatBot(
            'Ron Obvious',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            logic_adapters=[
              {
                'import_path': 'chatterbot.logic.BestMatch',
                "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
              },
              {
                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                'threshold': 0.60,
                'default_response': 'Eu não entendi. Bem, eu sou um robozinho meio lerdo e preciso que você explique de uma forma detalhada com palavras chaves para que eu entenda melhor. Pode refazer a sua pergunta?'
              }
            ]
        )

        self.chatbot.train("chatterbot.corpus.portuguese")
        self.chatbot.train("./corpus")

    def answer(self, conversation_id, question):
        response = self.chatbot.get_response(question)
        response = self.tokenReplacer.replace(response.text)
        return response


