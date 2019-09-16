numDigits = int(input("Please Enter A Positive Number: "))
count = 1
while numDigits > 1:
         numDigits = numDigits/10
         count = count+1
         if numDigits < 1 or numDigits == 0:
                print("Game Over")
                
print (count)


         
