num1=9
if num1>1:
	for i in range(2,num1):
		if (num1%i)==0:
			print(" number is not a prime number",num1)
			break		
	else:
		print("number is a prime number")
	