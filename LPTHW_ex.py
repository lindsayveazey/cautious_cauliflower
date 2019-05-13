# ex 21
# more functions

# This addition fx sums two variables, indicated as placeholder variables p and l.
def add(p, l):
    print(f"SUMMING {p} + {l}")
    return p + l

def subtract(p, l):
    print(f"SUBTRACTING {p} + {l}")
    return p - l

def multiply(p, l):
    print(f"MULTIPLYING {p} * {l}")
    return p * l

def divide(p, l):
    print(f"DIVIDING {p} / {l}")
    return p / l

print("Let's do some maths with functions exclusively.")

# We have defined multiple fxs here. Each fx completes its respective operation on the values given inside the parentheses. 
age = add(20, 8)
weight = subtract(150, 15)
age_again = multiply(7, 4)
shoe_size = divide(36, 4)

print(f"Age: {age}, Weight: {weight}, Age (again): {age_again}, Shoe size: {shoe_size}.")

