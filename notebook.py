from collections import UserDict
from note import Note
from datetime import datetime
import os
import pickle


class Notebook(UserDict):
    def __init__(self):
        super().__init__()
        self.filename = 'notes'
        if os.path.exists(self.filename):
            self.load_records()
            self.__id = max([id for id in self])+1
        else:
            self.data = {}
            self.__id = 1

    def load_records(self):
        if (os.path.getsize(self.filename) > 0):
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)
        else:
            self.data = {}

    def save_records(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)

    def create_note(self, text: str):
        id = self.__id
        note = Note(id, text, datetime.now())
        self[id] = note
        self.__id += 1
        self.save_records()
        return f'Note : {id} created.'

    def remove_note(self, id):
        try:
            del self[int(id)]
            self.save_records()
            return f'Note : {id} removed.'
        except KeyError:
            return 'Note not found.'
        except ValueError:
            return 'Invalid note id.'

    def update_note(self, id, new_text):
        try:
            note = self[int(id)]
            note['text'] = new_text
            self.save_records()
            return f'Note : {id} updated.'
        except KeyError:
            return 'Note not found.'
        except ValueError:
            return 'Invalid note id.'

    def search_note(self, keyword):
        return '\n'.join([f'{str(self[k])}' for k in self if keyword.casefold(
        ) in self[k]["text"].casefold()]) if len(self) > 0 else "No notes were found."

    def add_tags(self, id, tags):
        try:
            note = self[int(id)]
            note['tags'] = tags
            self.save_records()
            return f'Tags are added to note {id}.'
        except KeyError:
            return 'Note not found.'

    def remove_tag(self, id, tag):
        try:
            note = self[int(id)]
            for index, item in enumerate(note['tags']):
                if item == tag:
                    note['tags'].pop(index)
                    self.save_records()
                    return f'Tag was removed'
            return 'There is no such tag'
        except KeyError:
            return 'Note not found.'

    def __str__(self):
        return '\n'.join([f'{str(self[k])}' for k in self]) if len(self) > 0 else 'No notes were found.'
