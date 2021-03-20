from copy import deepcopy

def cardlist_union(cardlist1, cardlist2):
    """Unite two cardlist dictionaries"""
    cards = deepcopy(cardlist1)
    for name, amount in cardlist2.items():
        if name not in cards:
            cards[name] = 0
        cards[name] = max(cards[name], amount)
    return cards

def cardlist_union_n(cardlists):
    """Unite n cardlist dictionaries"""
    if len(cardlists) == 0:
        return {}
    if len(cardlists) == 1:
        return cardlists[0]
    return cardlist_union(cardlists[0], cardlist_union_n(cardlists[1:]))
