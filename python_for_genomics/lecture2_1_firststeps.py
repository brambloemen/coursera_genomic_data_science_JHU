# intro to python

# numerics

print(5 + 5)
#
print(10.5-2*3)

# ** -> raise to power
print(2**5)

# floor division
print(10//3)

# modulus
print(10 % 3)

# types of numbers: integer vs float (=real numbers)
type(5)
type(5.6)
#  in python 2: this would return an integer, in py
type(12/5)

# complex numbers
type(3+2j)


# strings
print('atg')
print("atg")

# escape characters
print("this is a codon, isn't it?")
print("this is a \" codon, isn't it?")

# multiple lines: triple quotes
# when running the following from terminal, \n will appear
"""this is a codon
isnt it"""
# but not when printing, running script
print("""this is a codon
isnt it""")

# string operations
print("this is" + " a codon, isn't it")  # concatenate
print("this is" * 5)  # replicate
print("is" in "this is")  # check if one occurs in other
print("is" not in "this is")
