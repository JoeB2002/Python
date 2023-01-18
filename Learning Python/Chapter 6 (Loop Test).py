##Iterate

#While loop

i = 0
while i <=10:            #CONDITIONAL LOOP
    print(i)
    i+=1
    
#or

i = 0
while i <=10:            #CONDITIONAL LOOP
    print(i)
    i= i + 1
    
print("######################################################################")

#For loop

#range(start,stop,step)

range(5) #just to test by itself

for number in range(3):     #number is a variable 
    print("Success")

#or 
print("######################################################################")


for number in range(3):     #number is a variable 
    print("Success", number)
    
#or
print("######################################################################")


for number in range(1,11):     #number is a variable 
    print("Success", number)
    
#or
print("######################################################################")


for number in range(10):     #number is a variable  
    print("Success", number + 1)
    
print("######################################################################")

for number in range(3):
    print("Success",number,(number + 1) * ".")
    