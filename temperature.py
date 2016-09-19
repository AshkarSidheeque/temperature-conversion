# Python Program to convert temperature in celsius to fahrenheit  and vice versa
# Input is provided by the user in degree celsius


# calculate fahrenheit
def Fahrenheit():
	num = float(input('Enter degree in Celsius: '))
	fahrenheit = (num * 1.8) + 32
	print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit \n' %(num,fahrenheit))

# calculate Celsius
def Celsius():
	num = float(input('Enter degree in Fahrenheit: '))
	celsius = (num - 32) / 1.8
	print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius \n' %(num,celsius))
choice = "Y"
while choice.upper() == "Y":
	# take input from the user
	temp = raw_input('Please type \'1\' for Celsius to Fahrenheit conversion \n Or, type \'2\' for Fahrenheit to Celsius conversion.. \n')
	if int(temp) == 1:
		Fahrenheit()
	elif int(temp) == 2:
		Celsius()
	else:
		print "invalid option"
	choice = raw_input("Enter \"Y\" for continue , \"N\" for stop \n")
