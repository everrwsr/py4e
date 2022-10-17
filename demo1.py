def doNothing():
    pass

doNothing()
def doSomething():
    print("This is a hello message form doSomething")
    
doSomething()

def isLeaf(year):
    leaf = False
    if year % 4 == 0:
        leaf = True
        if year % 100 == 0 and year % 400 != 0:
            leaf = False
    return leaf

isLeaf(9)