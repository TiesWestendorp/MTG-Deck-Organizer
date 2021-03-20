from helpers import load_inventory, cardlist_sum, cardlists_sum_n, dict_to_file

def inventory_sum_decklists(deck_dictionary):
    """Add all cards from decklists to inventory"""
    inventory = load_inventory()
    cardlists = list(deck_dictionary.values())
    new_inventory = cardlist_sum(inventory, cardlist_sum_n(cardlists))
    dict_to_file(new_inventory, '../data/inventory.txt')

if __name__ == '__main__':
    from helpers import load_decks

    deck_dictionary = load_decks()
    inventory_sum_decklists(deck_dictionary)
