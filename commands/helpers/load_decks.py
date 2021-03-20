import os
from helpers.file_to_dict import file_to_dict

def load_decks():
    """Load all known decks into a filename->dictionary dictionary"""
    deck_dictionary = {}
    for filename in os.listdir('../data/decks'):
        deck_dictionary[filename] = file_to_dict(os.path.join('../data/decks', filename))
    return deck_dictionary
