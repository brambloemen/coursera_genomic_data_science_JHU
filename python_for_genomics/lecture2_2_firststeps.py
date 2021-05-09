# lecture 2.2 first steps part two

# variables
codon = 'atg'

dna_sequence = 'gtcgcctaaccgtatattttccccgt'


a = 4
a

b = a
b

b = b+3
b
# keep in mind: case sensitive!!!
# B -> would give error

# more string operations
print(dna_sequence[5])  # give 6th character in string

print(dna_sequence[0])  # indexing starts at 0

print(dna_sequence[4:8])  # give range in string

print(dna_sequence[-5])  # start at end and count backwards

print(dna_sequence[0:3])  # first is included, last excluded
print(dna_sequence[:3])  # omit : implicit "first"

print(len(dna_sequence))    # length


# strings as objects, e.g. can perform methods
print(dna_sequence.count('a'))  # method count on object dna_sequence
print(dna_sequence.count('gc'))

print(dna_sequence.upper())  # change to upper
print(dna_sequence)  # variable value itself didn't change!

print(dna_sequence.find('t'))  # print first occurence of t
print(dna_sequence.find('t', 4))  # start looking from fourth
print(dna_sequence.rfind('t'))  # backwards
