'''
# ex 19

# long fx

def tofu_and_greens(tofu_count, number_of_kale):
    print(f"You have {tofu_count} types of tofu.")
    print(f"Luckily, I have {number_of_kale} stalks of kale.")

print("We can give function numbers directly.")
tofu_and_greens(2, 3)

print("We can also use variables from the script.")
amount_of_tofu = 2
amount_of_kale = 3

tofu_and_greens(amount_of_tofu, amount_of_kale)

print("We can calculate in the function as well...")
tofu_and_greens(1+1, 2+1)

print("We can combine variables and math.")
tofu_and_greens(amount_of_tofu + 50, amount_of_kale + 71)
'''
# ex 20

# fx and files

from sys import argv

script, input_file = argv
# create a fx called print_all
def print_all(f):
    print(f.read())
# f is the file of interest
def rewind(f):
    f.seek(0)
# printing the line count of f
def print_a_line(line_count, f):
    print(line_count, f.readline())
# renaming the input file as a variable
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now we rewind.")

rewind(current_file)

print("Let's print 3 lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
