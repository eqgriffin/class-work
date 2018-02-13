hours = float(input('Enter Hours\n'))
rate = float(input('Enter Rate\n'))
if hours > 40:
	x = hours - 40
else:
	x = 0
pay = (40+(x*1.5))*rate
print('Pay: $', pay)
