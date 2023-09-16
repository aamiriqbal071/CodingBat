def firstHalf(a):
	b=len(a)
	n=int(b/2)
	c=a[:n]
	return(c)


a=input("Enter the word:")
print(firstHalf(a))	