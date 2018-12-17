x=input("(module 1) \nchoose number - ") ## Console inputs in string
y=input("choose number - ")
## defining the function named greaterthan_func
def greaterthan_func():

## first case of greater than
    if int(x)>int(y): ##converting string input to integer and comparing
        print(x + " is greater than " + y )
## Second case of less than
    elif int(x)<int(y): ##converting string input to integer and comparing
        print(x +" is less than " + y)
## Third case of equal to
    else:
        print(x + " is equal to " + y)
