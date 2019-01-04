# Function that accepts two lines on x-axis
def overlap(line1, line2):
    ## Flag
    found = False
    result = str(line1) + ' & ' + str(line2) + ' do not overlap'
    pos = 0                      ## position of Lines (INDEX)

    for i in range(2):
        # evaluates negative integers
        if line1[i] < 0 and line2[i] < 0:
            while pos < len(line1) and not found:
                if line2[pos] >= line1[0] or line2[pos] >= line1[1]:
                    found = True
                    result = str(line1) + ' & ' + str(line2) + ' overlaps on x-axis'
                else:
                    pos += 1
        # evaluates positive integers
        else:
            while pos < len(line1) and not found:
                if line2[pos] <= line1[0] or line2[pos] <= line1[1]:
                    found = True
                    result = str(line1) + ' & ' + str(line2) + ' overlaps on x-axis'
                else:
                    pos += 1
    return '\n' + result
