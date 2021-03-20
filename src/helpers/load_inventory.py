from helpers.cardlist_to_dict import cardlist_to_dict

def load_inventory():
    return cardlist_to_dict('../data/inventory.txt')
