class Point(object): ## class point with argument object
    def __init__(self, x, y): 
        self.x = x
        self.y = y

class Rect(object): ##rect class with argument object
    def __init__(self, p1, p2):
        '''Store the top, bottom, left and right values for points
               p1 and p2 are the (corners) in either order
        '''
        self.left   = min(p1.x, p2.x)
        self.right  = max(p1.x, p2.x)
        self.bottom = min(p1.y, p2.y)
        self.top    = max(p1.y, p2.y)

def overlap(r1,r2):
    '''Overlapping--- to check-- overlap both horizontally & vertically
    '''
    hoverlaps = True ##boolean values
    voverlaps = True  
    if (r1.left > r2.right) or (r1.right < r2.left): ##putting conditions
        hoverlaps = False
    if (r1.top < r2.bottom) or (r1.bottom > r2.top): 
        voverlaps = False
    return hoverlaps and voverlaps ##returning values 

if __name__ == '__main__': 
    p1 = Point(1,1)
    p2 = Point(3,3)
    r1 = Rect(p1,p2)
    p3 = Point(2,2)
    p4 = Point(4,4)
    r2 = Rect(p3,p4)

    print ("r1 ,r2 : Overlap in either direction:")
    print (overlap(r1,r2))
    print (overlap(r2,r1)) 

    p5 = Point(3,6)     # overlaps horizontally but not vertically
    p6 = Point(12,11)
    r3 = Rect(p5,p6)

    print ("r1,r3 : Should not overlap, either way:")
    print (overlap(r1,r3))
    print (overlap(r3,r1))

    print ("r2 ,r3 : Same as that")
    print (overlap(r2,r3))
    print (overlap(r3,r2))

    p7 = Point(7,7)
    p8 = Point(11,10)
    r4 = Rect(p7,p8)    # completely inside r3

    print ("r4 is totally enclosed in r3 ")
    print (overlap(r3,r4))
    print (overlap(r4,r3))

    print ("r4  is nowhere near r1  nor r2 ")
    print (overlap(r1,r4))

    p09 = Point(13,11)
    p10 = Point(19,13)
    r5  = Rect(p09,p10)

    p11 = Point(13,9)
    p12 = Point(15,14)
    r6  = Rect(p11,p12)

    print ("r5 and r6 cross without corner overlap")
    print (overlap(r5,r6))
    print (overlap(r6,r5))
