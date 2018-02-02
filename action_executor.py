import re

class Form:
    def __init__(self, token, fields):
        self.token = token
        self.fields = fields

    def render(self):
        form = '<form id="' + self.token + '" class="' + self.token + '">'
        form += '<dl>'
        for item in self.fields:
            form += '<dt>' + item.renderLabel() + '</dt>'
            form += '<dd>' + item.renderInput() + '</dd>'
        form += '</dl>'
        form += '<div>' + FormButton(self.token, 'Enviar').render() + '</div>'
        form += '</form>'
        return form
            
class FormInputText:
    def __init__(self, token, name, placeholder):
        self.token = token
        self.name = name
        self.placeholder = placeholder

    def renderLabel(self):
        return '<label for="' + self.token + '">' + self.name + '</label>'

    def renderInput(self):
        return '<input type="text" name="' + self.token + '" placeholder="' + self.placeholder + '" />'

class FormButton:
    def __init__(self, token, text):
        self.token = token
        self.text = text

    def render(self):
        return '<button class="button button-outline" id="actionButton" data-form-name="'+ self.token + '" onclick="sendHistoryFormData();">' + self.text + '</button>' 

class ActionExecutor:
    def __init__(self, actions):
        self.actions = actions

    def replace(self, text):
        result = ''
        ocurrences = re.findall(r'@([\w:_]+)', text)

        print(self.actions)

        for item in ocurrences:
            if item in self.actions:
                text = text.replace('@' + item , '')

                print(item)
                result += '<br/>' + self.actions[item]
        return text + result    