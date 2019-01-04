## importing overlap function from line_overlap
from line_overlap import overlap

# method main
if __name__ == '__main__':
    try:                     ## using try
        line1=[]             ## Empty line 1
        line2=[]             ## Empty line 2
        for i in range(2):
            ## console input
            coordinate_1 = float(input('{0}.Type co-ordinate for Line 1: \n'.format(i+1)))
            line1.append(coordinate_1) ## appending coordianate 1
        for i in range(2):
            ## console input
            coordinate_2 = float(input('{0}.Type co-ordinate for Line 2: \n'.format(i+1)))
            line2.append(coordinate_2)  ##appending coordianate 2

        # making line equal to Tuple
        line1 = tuple(line1)
        line2 = tuple(line2)

        # Calling function Overlap
        result = overlap(line1, line2)
        print(result)

    # Exception handling for entering invalid inputs
    except ValueError: ## except after using try
        print('\n') ## for next line
        print('_' * 42)
        print('Characters and strings not allowed\n'
              "Please type 2 co-ordinate \n{0}".format('_' * 42))
