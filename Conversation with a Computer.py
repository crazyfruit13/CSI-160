#Author: Jonathan Matson
#Course: CSI-160-03
#This input stores the users name for future use.
name = input("Hello, I am Tharizdun. What is your name?")
#Prints the users name and asks for their favorite color.
print("Hi,",name+'.',"what is your favorite color?")
color = input()
#Asks for their age & GPA.
age = int(input('Mine too. How old are you?'))
gpa = float(input('What is your GPA?'))
#This input asks for how many siblings they have.
siblings = int(input('Wow, you are smart, how many siblings do you have?'))
#Siblings is added by '1', color & GPA are printed to form a sentence.
print('That means you are one of',siblings+1,'kid(s). Is',color,'the favorite color of anyone else in your house? Or do they have a GPA better than',gpa,'?')
response = input()
#Asks for parent age.
parents = int(input("How old is one of your parents?"))
#Calculates how old the parent was when they had the user.
print('That means they were likely',parents-age,'when they had you.')
print(('It was nice meeting you, come talk to me again, sometime.'))
