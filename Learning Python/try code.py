
while True:  
    myStr = input("Please enter a number or q to quit: ")
    if myStr == 'q':
        break #this will make it run forever and can't get out of it
    try:
        myNum= int(myStr)
        for i in myStr:
            print(i)
    except ValueError:
        print("You entered a value which is not a number.")