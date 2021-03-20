#
# Convert a cardlist to a dictionary where entries look like:
#   card name -> amount of cards with that name
#
def cardlist_to_dict(file_name):
    cards = dict()
    with open(file_name, 'r') as file:
        for line_number, line in enumerate(file):
            try:
                line = line.strip()
                first_space = line.find(' ')
                amount = int(line[:first_space])
                name   = line[first_space+1:]
                if name not in cards:
                    cards[name] = 0
                cards[name] += amount
            except ValueError:
                raise ValueError("Failed to parse line {} of {}: '{}'".format(line_number+1, file_name, line))
    return cards
