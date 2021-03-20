import os

def dict_to_file(dict, file_name):
    """Write a dictionary of name->amount entries to disk"""
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as file:
        items = list(dict.items())
        items.sort(key=lambda item: item[0])
        for k,v in items:
            file.write("{} {}\n".format(v, k))
