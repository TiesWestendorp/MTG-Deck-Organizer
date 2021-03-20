def cardlist_leq(cardlist1, cardlist2):
    """Check if a cardlist is contained within another"""
    for name, amount in cardlist1.items():
        if name == '__filename__':
            continue
        if name not in cardlist2:
            return False
        if amount > cardlist2[name]:
            return False
    return True
