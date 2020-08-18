'''Calculator program'''
def add(num1, num2):
    """Add Function"""
    return num1 + num2

def subtract(num1, num2):
    """Subtract Function"""
    return num1 - num2

def multply(num1, num2):
    """Multiply Function"""
    return num1 * num2

def divide(num1, num2):
    """Divide Function"""
    if num2 == 0:
        raise ValueError('Can not divide bnum2 zero!')
    return num1 / num2

print(add(5, 4))
print(multply(3, 5))
