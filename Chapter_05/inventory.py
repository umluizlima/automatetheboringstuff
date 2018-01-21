stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v), k)
        total += v
    print('Total number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)
