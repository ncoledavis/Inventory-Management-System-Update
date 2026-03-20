def duplicate_zeros(inventory):
    n = len(inventory)
    zeroes = inventory.count(0)

    for i in range(n - 1, -1, -1): 
        new_index = i + zeroes
        if new_index < n:
            inventory[new_index] = inventory[i]
            
        if inventory[i] == 0:
            zeroes -= 1
            if i + zeroes < n:
                inventory[i + zeroes] = 0

arr = [3,2,1,0]
duplicate_zeros(arr)
print(arr)