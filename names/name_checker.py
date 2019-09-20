# This solution uses a binary search tree 

class NameChecker:
    def __init__(self, data):  # create constructor. 
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):               # INSERTING INCOMING DATA
        if data > self.data:              # if incoming data is larger than node data
            if self.right:                # go down right branch
                self.right.insert(data)   # insert into right branch
            else:
                self.right = NameChecker(data)  # create another branch
        elif data < self.data:                  # if incoming data is lower than node data
            if self.left:                       # go down left branch     
                self.left.insert(data)          # insert into left branch
            else:
                self.left = NameChecker(data)   # create another branch

    def contains(self, target):           # HANDLING DATA
        if target == self.data:           # bullseye return.  return true
            return True
        elif target > self.data:          # check if target is higher than node data
            if self.right:                # check if available on right
                return self.right.contains(target)  # return the target data
            return False                            # if not, return a false
        else:                                       # check to see if it's lower
            if self.left:                 # check the left branch
                return self.left.contains(target)  # return taget data if there
            return False                  # or return false