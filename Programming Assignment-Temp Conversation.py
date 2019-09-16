# Author: Jonathan Matson
# Course: CSI-160
def temp_convert (scale=None, temp=None):
  """
This function will convert a number from Celcius to Fahrenheit and vice versa.
Arguments: 
  scale(string): The scale that the program will use, Celcius or Fahrenheit
  temp(float): The The temperature to convert
Returns:
  float: The temperature in Fahrenheit or Celcius.
Assumptions:
  That what entered into scale is a string, and that what is entered into temp is a float.
"""
  if scale == 'F':
      return 'C', (temp - 32.0) * (5.0/9.0)
  elif scale == "C":
      return 'F', (temp * (9.0/5.0)) + 32.0
  elif scale == 'f':
      return 'c', (temp - 32.0) * (5.0/9.0)
  elif scale == "c":
      return 'f', (temp * (9.0/5.0)) + 32.0
  else:
      print("Please select F or C as your temperature!")

scale = input("Please select F or C as your temperature type: ")
temp =  int(input("What is the temperature?: "))
scale2, temp2 = temp_convert(scale, temp)
print(temp, "degrees", scale, "is", round(temp2,1), "degrees", scale2)
