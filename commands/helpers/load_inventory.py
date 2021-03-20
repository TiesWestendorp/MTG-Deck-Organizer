from helpers.file_to_dict import file_to_dict

def load_inventory():
    """Load the inventory"""
    return file_to_dict('../data/inventory.txt')
