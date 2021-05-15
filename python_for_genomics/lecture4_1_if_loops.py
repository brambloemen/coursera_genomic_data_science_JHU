#!/Anaconda/python  # in unix, put this in front to run from terminal
dna = input("Enter a DNA sequence: ")

if 'n' in dna:
    nbases = dna.count('n')
    print("The DNA sequence contains %d undefined bases." % nbases)
else:
    print("The DNA sequence doesn't contain any undefined bases.")

dna = input("Enter a DNA sequence: ")

if 'n' in dna:
    nbases = dna.count('n')
    print("The DNA sequence contains %d undefined bases." % nbases)
elif 'N' in dna:
    nbases = dna.count('N')
    print("The DNA sequence contains %d undefined bases." % nbases)
else:
    print("The DNA sequence doesn't contain any undefined bases.")

#   comparison operators + membership (in/not in): skipped
#   identity operators: see if two items point to same object
alphabet = ['a', 'c', 'g', 't']
newalphabet = alphabet[:]
alphabet == newalphabet  # checks if two items contain same values
alphabet is newalphabet  # checks if both items point to same object in memory

#   logical operators
if 'n' in dna or 'N' in dna:
    nbases = dna.count('n') + dna.count('N')
    print("The DNA sequence contains %d undefined bases." % nbases)
else:
    print("The DNA sequence doesn't contain any undefined bases.")
