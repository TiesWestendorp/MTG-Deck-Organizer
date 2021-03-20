# Installation

# Configuration

`import_deckbox` a configuration file: `commands/config/deckbox.py`, that should define:
```
deckbox_user_id = 10209908365296302
deckbox_folder = ['Finished Decks', 'Merge']
```

# Workflow

1. Import cards from desired website, currently supported: http://www.deckbox.org/, or add decklists manually. Cards should be in the following format: "1 Llanowar Elves", with one card name  per line.
  Relevant commands: import_deckbox

2. Add cards to inventory, either through inventory_sum_decklists, inventory_union_decklists or manually.

3. cards_not_in_decks, disjoint_bases, simultaneously_constructible
