from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train("chatterbot.corpus.portuguese")

chatbot.train(
    "/Users/gabriel.francisco/workspace/hackaton/chatterbot-sample/questions.yml",
    "/Users/gabriel.francisco/workspace/hackaton/chatterbot-sample/cupom.yml",
    "/Users/gabriel.francisco/workspace/hackaton/chatterbot-sample/lost_items.yml"
)

def get_response(question):
    print("User: " + question)
    print(chatbot.get_response(question))

get_response("Oi, como você tá?")
get_response("Bem também.")
get_response("Estou com um problema, pode me ajudar?")
get_response("então, eu acabei de receber uma cobrança indevida")
get_response("acho que foi durante o cadastro")
get_response("Ah, obrigado então!")
get_response("Vish, acho que tenho mais uma dúvida.")
get_response("A tem mais uma coisa, esqueci meu guarda-chuva no carro")




# print(chatbot.get_response("Como posso adicionar novos cupons?"))
# print(chatbot.get_response("E pra ver os meus cupons?"))
# print(chatbot.get_response("É só isso. Obrigado!"))
