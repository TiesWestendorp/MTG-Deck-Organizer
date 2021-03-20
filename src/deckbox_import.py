import os
import requests
from html.parser import HTMLParser

void = ["area", "base", "br", "col", "embed", "hr", "img", "input", "keygen", "link", "menuitem", "meta", "param", "source", "track", "wbr"]

def find_deck_ids(user_id, folder):
    class UserParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.location = []
            self.folder = []
            self.last_folder_label = None
            self.next_is_folder_label = False
            self.ids = []
        def handle_starttag(self, tag, attrs):
            if tag not in void:
                self.location.append((tag, attrs))
            if tag == "li":
                if ('class', 'submenu_entry folder') in attrs:
                    self.next_is_folder_label = True
                elif ('class', 'submenu_entry deck ') in attrs:
                    if folder in [None, self.folder]:
                        for (attr, val) in attrs:
                            if attr == 'id':
                                self.ids.append(val[5:])
            elif tag == "ul" and ('class', 'folder') in attrs:
                self.folder.append(self.last_folder_label)
                self.last_folder_label = None
        def handle_endtag(self, tag):
            if tag not in void:
                popped = self.location.pop()
                if popped[0] == "ul" and ('class', 'folder') in popped[1]:
                    self.folder.pop()
        def handle_data(self, data):
            if self.next_is_folder_label:
                self.last_folder_label = data
            self.next_is_folder_label = False

    response = requests.get("https://deckbox.org/users/{}".format(user_id))
    if not response.ok:
        raise response.reason
    parser = UserParser()
    parser.feed(response.content.decode("utf-8"))
    return parser.ids

def download_deck(deck_id):
    class DeckParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.text = ""
            self.started = False
            self.done = False
        def handle_starttag(self, tag, attrs):
            if tag == "body":
                self.started = True
            if tag == "strong":
                self.done = True
        def handle_data(self, data):
            if self.started and not self.done:
                self.text += data.strip() + "\n"

    response = requests.get("https://deckbox.org/sets/{}/export".format(deck_id))
    if not response.ok:
        raise response.reason
    parser = DeckParser()
    parser.feed(response.content.decode("utf-8"))
    file_name = "../data/decks/deckbox-{}.txt".format(deck_id)
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, "w") as file:
        file.write(parser.text.strip())

def deckbox_import(user_id, folder):
    deck_ids = find_deck_ids(deckbox_user_id, deckbox_folder)
    for deck_id in deck_ids:
        download_deck(deck_id)
    print("Added {} decks".format(len(deck_ids)))

if __name__ == "__main__":
    from config import deckbox_folder, deckbox_user_id
    deckbox_import(deckbox_user_id, deckbox_folder)
