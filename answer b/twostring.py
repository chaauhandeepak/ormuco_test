class ValueComparsions:
    def __init__(self, valueone, valuetwo):
        self.val1 = float(valueone)
        self.val2 = float(valuetwo)

    # Greater than Function
    def greater(self):
        condition = self.val1 > self.val2
        return "{0} is greater than {1}".format(self.val1, self.val2) if condition else \
               "{0} is greater than {1}".format(self.val2, self.val1)

    # Less than Function
    def lesser(self):
        condition = self.val1 < self.val2
        return "{0} is lesser than {1}".format(self.val1, self.val2) if condition else \
               "{0} is lesser than {1}".format(self.val2, self.val1)

    # Equal to  Function
    def equal(self):
        condition = self.val1 == self.val2
        return "{0} is equal to {1}".format(self.val1, self.val2) if condition else \
               "{0} is not equal to {1}".format(self.val2, self.val1)
