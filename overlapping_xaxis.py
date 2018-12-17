class Point(object):
    def __init__(self, x):
        self.x = x


class axis(object):
    def __init__(self, p1, p2):
        '''Store the left and right values for points
               p1,p2 on axis
        '''
        self.left   = min(p1.x, p2.x)
        self.right  = max(p1.x, p2.x)
       

def overlap(r1,r2):
    '''Overlapping
    '''
    hoverlaps = True
    if (r1.left > r2.right) or (r1.right < r2.left):
        hoverlaps = False

if __name__ == '__main__':
    p1 = Point(1,5)
    p2 = Point(3,3)
    r1 = axis(p1)
    r2 = axis(p2)



    print ("r1,r2  : Overlap ?")
    print (overlap(r1,r2))
    
