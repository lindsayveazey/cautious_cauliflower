# ex 16

# recall when using argv, I need to call this script and any actionable files in the prompt!
from sys import argv

# calling this script and an unnamed file
script, filename = argv

# here, I'm giving the program alternate options it will recite back
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")

# input prompts me to, of course, type input
input("?")

# opening the file to write/edit into it (thus the w)
print("Opening the file...")
target = open(filename, 'w')

# truncating a file means limiting its size
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# input prompts me to write some code
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# writing my code into the file with new lines after each insertion
print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}")

# the end
print("And finally, we close the file.")
target.close()
