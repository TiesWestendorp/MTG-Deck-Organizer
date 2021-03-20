from helpers import cardlist_minus

def cards_not_in_decks(deck_dictionary, inventory):
    """Lists the cards that you have 'too many of' in your inventory."""
    for name, deck in deck_dictionary.items():
        inventory = cardlist_minus(inventory, deck)
    return inventory

if __name__ == '__main__':
    from helpers import load_decks, load_inventory, dict_to_file

    deck_dictionary = load_decks()
    inventory = load_inventory()

    unused = cards_not_in_decks(deck_dictionary, inventory)
    dict_to_file(unused, '../output/cards-not-in-decks.txt')
