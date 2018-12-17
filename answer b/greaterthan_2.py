x=int(input("(module 2) \nchoose number - ")) ## Console input in integer form
y=int(input("choose number - "))
## defining the function named greaterthan_func_2
def greaterthan_func_2():

## First case of greater than
    if x>y: ##comparing x and y
        print(str(x) + " is greater than " + str(y)) ## converting x and y to string for displaying
## Second case of less than
    elif x<y:
        print(str(x) +" is less than " + str(y)) ## converting x and y to string for displaying
## Third case of equal to
    else:
        print(str(x) + " is equal to " + str(y)) ## converting x and y to string for displaying
