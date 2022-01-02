ar = [1,2,3,4,10,11, "Hello"]

def simpleArraySum(ar):
	sum = 0
	for num in range(len(ar)):
		x = isinstance(ar[num],str)
		if x == True:
			continue
		else:
			sum += ar[num]
	return sum


print(simpleArraySum(ar))