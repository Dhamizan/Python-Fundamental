def tambah(*a):
    total = 0
    for i in a:
        total += i
    return total

def kurang(*a):
    total = 0
    for i in a:
        total -= i
    return total
    
def bagi(a, b):
    return a // b

def kali(*a):
    total = 0
    for i in a:
        total *= i
    return total

def pangkat(*a):
    total = 0
    for i in a:
        total **= i
    return total
    
def kuadrat(a):
    return a ** 2