
itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()
    
    if(userChoice == "1"):
        print("What item do you want to add to the backpack?")
        itemToAdd = input()
        
        ####### YOUR CODE HERE ######
        #add the item to the backpack
        ####### YOUR CODE HERE ######\
        itemsInBackpack.append(itemToAdd)
        
    if(userChoice == "2"):   
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()
        
        ####### YOUR CODE HERE ######
        #Print out if the user's item is in the backpack
        ####### YOUR CODE HERE ######
        if  itemToCheck == len(itemsInBackpack[0:]):
            print ("You Packed That Item!")
        else:
            print ("You Didn't Pack That Item!")
    
    if(userChoice == "3"): 
        sys.exit()
