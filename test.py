#Jorge Dettle Meza Dominguez
#16 de agosto del 2018
#

s=12
p=input("dame un numero :")
a=0
m=1


while s==0:
	while p<s:
	
		s=s*p
		p=p+2
	
		if p%2==0:
			p=p+1
		else :
        		while a<(p-1):
				a=a+1
				r=p%a
				if r==0:
					m=0
                 	if m==0:  
		s=s-1

print(p)	
