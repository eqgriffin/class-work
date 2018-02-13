try:
	x = float(input('Please enter 0.0 to 1.0: '))
if x >= 1.0:
	print("Please try again.")
except:
	print('Please enter a number value.')
	quit()
elif x >= 0.9:
	print ("A")
elif x >= 0.8:
	print ("B")
elif x >= 0.7:
	print ("C")
elif x >= 0.6:
	print ("D")
else:
	print ("F")
quit()
