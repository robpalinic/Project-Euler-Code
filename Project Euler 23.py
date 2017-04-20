#Project Euler 23


#Function to find all divisors

def divisors(n):
	divisor=[]
	for i in range(1,n-1):
		if n%i==0:
			divisor.append(i)
	return divisor


#Find all abundant numbers bewteen 1 and 28123

abundant=[]

for i in range (12 and 28123 ):
	if sum(divisors(i))>i:
		abundant.append(i)

#Create list of all numbers between 24 and 28123

all=list(range(24, 28124))


#Iterate through abudant combinations, removing from list

for i in range(0, len(abundant)):
	for j in range(0, len(abundant)):
		if abundant[i]+abundant[j] in all:
			all.remove(abundant[i]+abundant[j])

print sum(all)+sum(range(0,24))
