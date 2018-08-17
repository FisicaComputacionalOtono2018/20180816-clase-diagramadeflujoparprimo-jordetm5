#jorge dettle meza Dominguez
#!/ de agosto
# funcion





def primo(n) :
        a=1
        m=1
        if n==1:
                m=0
        if n==2 :
                m=1
        else :
                while a<(n-1) :
                        a=a+1
                        r=m%a
                        if r==0:
                                m=0
                                break
        return m
      
        	

  
r=input("dame un numero :")


m=primo(r)
 
if m==1 :
	print("es primo")
else: 
	print("no es primo")                     
                                        
