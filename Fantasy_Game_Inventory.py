def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k + ':' + str(v))
        item_total = item_total + v

    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for k in range(len(addedItems)):
        inventory.setdefault(addedItems[k], 0)
        inventory[addedItems[k]] +=1
    return (inventory)

inventory = {'line': 4, 'torch': 6, 'gold coin': 44, 'dagger': 2, 'arrow': 100}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'arrow', 'knife', 'sword']

newInventory = addToInventory(inventory, dragonLoot)
displayInventory(newInventory)
print("Inventory updated.")