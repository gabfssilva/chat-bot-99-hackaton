import re

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

class TokenReplacer:
    def __init__(self, entries):
        self.entries = entries

    def replace(self, text):
        ocurrences = re.findall(r'@([\w:_]+)', text)
        for item in ocurrences:
            text = text.replace('@' + item , self.entries[item].render())
        return text    