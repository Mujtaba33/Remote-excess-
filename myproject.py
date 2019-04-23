for i in range(1,6):
	for j in range (i,6):
		print(" ",end=" ")
	for k in range(1,i*2):
		if(k%2==0):
			print("7",end=" ")
		else:
			print("5",end=" ")
	print("")