for i in range(1,6):
	for j in range (i,6):
		print(" ",end=" ")
	for k in range(1,i*2):
		if(k%2==0):
			print("7",end=" ")
		else:
			print("5",end=" ")
	print("")
	
	
	
	
		
rowsize=int(input("enter no of rows"))
for row in range(rowsize+1):
	for space in range(rowsize,row,-1):
		print(" ",end=" ")
	colsize=((row*2)-1)
	for col in range(colsize):
		if(col%2==0):
			print("*",end=" ")
		else:
			print("6",end=" ")
	print()
for row in range(rowsize-1,0,-1):
	for space in range(rowsize,row,-1):
		print(" ",end=" ")
	colsize=((row*2)-1)
	for col in range(colsize):
		if(col%2):
			print("6",end=" ")
		else:
			print("*",end=" ")
	print()