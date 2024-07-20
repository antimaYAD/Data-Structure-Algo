#binary search with (log n) - Time Complexity

# Alice and Bob Card problem

#linear search (Brute Force method type 1 to solve the problems)
def located_card(card,query):
    
    position = 0
    for i in range(len(card)):
        if card[i] == query:
            position = i + 1
            return position
    return -1

#Linear search (Brute Force method type 2 to solve the problems)
def located_cards(card,query):
        
    position = 0
    while position < len(card):
        if card[position] == query:
           
            return position
        position += 1
    return -1
 

cr = [10,9,8,7,5]
item = 11

# print(located_card(cr,item))  

 
#
