# ex 18

# take multiple arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# the *args above is useless
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes a single argument:
def print_one(arg1):
    print(f"arg1: {arg1}")

# and this takes none:
def no_thanks():
   print("Hello.")

print_two("Potato", "Tomato")
print_two_again("Banana", "Apple")
print_one("Cookies")
no_thanks()
