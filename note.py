from collections import UserDict


class Note(UserDict):
    def __init__(self, id, text, createdate):
        super().__init__()
        self['id'] = id
        self['text'] = text
        self['createdate'] = createdate

    def update(self, new_text):
        self['text'] = new_text

    def __str__(self):
        return f'{self["id"]}: {self["text"]}'
