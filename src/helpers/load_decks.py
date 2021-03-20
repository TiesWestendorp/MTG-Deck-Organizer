import os
from helpers.cardlist_to_dict import cardlist_to_dict

def load_decks():
    deck_dictionary = {}
    for filename in os.listdir('../data/decks'):
        deck_dictionary[filename] = cardlist_to_dict(os.path.join('../data/decks', filename))
    return deck_dictionary
