import re
import random

class Link:
    def __init__(self, token, text, href):
        self.token = token
        self.text = text
        self.href = href

    def render(self):
        return '<a class="follow_link" target="_blank" href="' + self.href + '">' + self.text +'</a>'    

class Image:
    def __init__(self, token, href):
       self.token = token
       self.href = href

    def render(self):
        return '<img src="' + self.href + '"/>'

class RandomGif:
    def __init__(self, token, links):
        self.links = links
        self.token = token

    def render(self):
        return '<br/><div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="' + random.choice(self.links) + '" width="70%" height="70%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>'


class TokenReplacer:
    def __init__(self, entries):
        self.entries = entries

    def replace(self, text):
        ocurrences = re.findall(r'@([\w:_]+)', text)
        for item in ocurrences:
            if item in self.entries:
                text = text.replace('@' + item , self.entries[item].render())
        return text