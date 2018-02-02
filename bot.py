import chatterbot 

class ChatBot:
    def __init__(self, tokenReplacer, actionExecutor):
        self.tokenReplacer = tokenReplacer
        self.actionExecutor = actionExecutor

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
                'default_response': 'Eu não entendi. Pode refazer a sua pergunta?'
              }
            ]
        )

        self.chatbot.train("chatterbot.corpus.portuguese.conversations")
        self.chatbot.train("chatterbot.corpus.portuguese.greetings")
        self.chatbot.train("./corpus")

    def answer(self, conversation_id, question):
        response = self.chatbot.get_response(question)
        response = self.tokenReplacer.replace(response.text)
        response = self.actionExecutor.replace(response)
        return response

