listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
    if newWord == "":
        break

    else:
        listToPrint.append(newWord)

listToPrint.insert(-1, "and")
print (listToPrint)
