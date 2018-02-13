try:
	x = float(input('Please enter 0.0 to 1.0: '))
except: 
	print ('bad score')
	quit()
	
def computegrade(x):
	if x >= 0.9:
		print("A")
	elif x >= 0.8:
		print ("B")
	elif x >= 0.7:
		print ("C")
	elif x >= 0.6:
		print ("D")
	elif x < 0.5:
		print ("F")