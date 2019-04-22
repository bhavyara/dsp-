r1=input("enter rows of matrix 1:")
c1=input("enter columns of matrix 1:")
r2=input("enter rows of matrix 2:")
c2=input("enter rows of matrix 2:")
if c1!=r2:
	print("matrix multiplication is not possible")
else:
	a={}
	for i in range(0,r1,1):
		for j in range(0,c1,1):
			a[i,j]=input("enter a number") #asking user for matrix1 elements


	b={}
	for i in range(0,r2,1):
		for j in range(0,c2,1):
			b[i,j]=input("enter a number") #asking user for matrix2 elements
	c={}
	for i in range(0,r1,1):
		for j in range(0,c2,1):
			c[i,j]=0                      #making output marix to zeroes to avoid intial value error 
	for i in range(0,r1,1):
		for j in range(0,c2,1):
			for k in range(0,r2,1):
			
				c[i,j]=c[i,j]+a[i,k]*b[k,j]
	print c
