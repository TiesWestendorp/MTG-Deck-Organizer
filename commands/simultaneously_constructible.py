from helpers import cardlist_sum_n, cardlist_leq

def simultaneously_constructible(deck_dictionary, inventory):
    """Returns maximal lists of simultaneously constructible decks"""
    def maximal_sets(set, condition_function):
        def __maximal_sets(current, remaining, unused):
            if remaining == []:
                for element in unused:
                    if condition_function(current + [element]):
                        return
                yield current
            else:
                if condition_function(current + [remaining[0]]):
                    yield from __maximal_sets(current + [remaining[0]], remaining[1:], unused)
                yield from __maximal_sets(current, remaining[1:], unused + [remaining[0]])
        return list(__maximal_sets([], set, []))

    def constructible(decks):
        cardlists = list(map(lambda deck: deck_dictionary[deck], decks))
        return cardlist_leq(cardlist_sum_n(cardlists), inventory)

    return maximal_sets(list(deck_dictionary.keys()), constructible)

if __name__ == '__main__':
    from helpers import load_decks, load_inventory

    deck_dictionary = load_decks()
    inventory = load_inventory()

    with open('../output/simultaneously-constructible.txt', 'w') as file:
        for decks in simultaneously_constructible(deck_dictionary, inventory):
            file.write(", ".join(decks) + "\n")
