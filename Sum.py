Number1 = int(input("Enter a Number: "))
Number2 = int(input("Enter another Number: "))

Sum = Number1 + Number2

if Sum > 100:
	print ("They add up to a big number")

elif Sum <= 100:
	print ("They add up to " + str(Sum))
