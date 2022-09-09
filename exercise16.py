from sys import argv

script, filename = argv
print(f"We're going to earase {filename}.")
print("If you don't want that, his CTRL-C (^c).")
print("If you do want that,hit RETURN.")

input("?")

print("Opening  the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
targe.write("\n")
targe.write(line2)
targe.write("\n")
targe.write(line3)
targe.write("\n")

print("And finally, we close it.")
target.close()