from helpers import cardlist_sum_n

def disjoint_bases(deck_dictionary, inventory):
    """Shows what cards can be kept as minimal base per decklist"""
    used_cards = cardlist_sum_n(list(deck_dictionary.values()))
    base_cards = { name: amount <= inventory.get(name, 0) for (name,amount) in used_cards.items() }

    organized_decks = {}
    for file_name, deck in deck_dictionary.items():
        organized_decks[file_name] = { 'base': {}, 'nonbase': {} }
        for name, amount in deck.items():
            if base_cards[name]:
                organized_decks[file_name]['base'][name] = amount
            else:
                organized_decks[file_name]['nonbase'][name] = amount
    return organized_decks

if __name__ == '__main__':
    from helpers import load_decks, load_inventory, dict_to_file

    deck_dictionary = load_decks()
    inventory = load_inventory()

    for name, split in disjoint_bases(deck_dictionary, inventory).items():
        dict_to_file(split['base'],    '../output/base/{}'.format(name))
        dict_to_file(split['nonbase'], '../output/nonbase/{}'.format(name))
