from copy import deepcopy

#
# Sum two cardlist dictionaries
#
def cardlist_sum(cardlist1, cardlist2):
    cards = deepcopy(cardlist1)
    for name, amount in cardlist2.items():
        if name not in cards:
            cards[name] = 0
        cards[name] = cards[name] + amount
    return cards

#
# Sum n cardslist dictionaries
#
def cardlist_sum_n(cardlists):
    if len(cardlists) == 0:
        return {}
    if len(cardlists) == 1:
        return cardlists[0]
    return cardlist_sum(cardlists[0], cardlist_sum_n(cardlists[1:]))
