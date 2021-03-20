from helpers import load_inventory, cardlist_union, cardlists_union_n, dict_to_file

def inventory_union_decklists(deck_dictionary):
    """Add the cards from decklists missing in inventory to inventory"""
    inventory = load_inventory()
    cardlists = list(deck_dictionary.values())
    new_inventory = cardlist_union(inventory, cardlist_union_n(cardlists))
    dict_to_file(new_inventory, '../data/inventory.txt')

if __name__ == '__main__':
    from helpers import load_decks

    deck_dictionary = load_decks()
    inventory_union_decklists(deck_dictionary)
