
def cardlist_minus(cardlist1, cardlist2):
    for name, amount in cardlist2.items():
        if name in cardlist1:
            cardlist1[name] = cardlist1[name] - amount
            if cardlist1[name] <= 0:
                del cardlist1[name]
    return cardlist1
