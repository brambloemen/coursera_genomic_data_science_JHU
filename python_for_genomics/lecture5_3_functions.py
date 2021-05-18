#!/Anaconda/python  # in unix, put this in front to run from terminal
"""
more complicated slices
"""

dna = "atgcaattgcgncaagttgnccccnacctttagccgtata"
print(dna[0:3])
print(dna[0:10:2])   # step argument: skip every nth character
reverse = dna[::-1]  # step of -1: start at end, go in reverse
print(reverse)


"""
create a function that returns reverse complement
"""


dna = input("enter dna sequence: ")


def reverse_string(seq):
    "reverse sequence"
    return seq[::-1]


def complement(seq):
    "return complementary sequence"
    basecomplement = {"a": "t", "g": "c", "t": "a", "c": "g",
                      "A": "T", "G": "C", "T": "A", "C": "G",
                      "n": "n", "N": "N"}
    letters = list(seq)  # define list
    """
    same as using a for loop to append each item into an empty list
    """
    # translate each base in the list
    letters = [basecomplement[base] for base in letters]
    return "".join(letters)  # apply join method, separator = ""
# join and split methods


def reverse_complement(dna):
    "return the reverse complement"
    dna = reverse_string(dna)
    dna = complement(dna)
    return dna


print(reverse_complement(dna))


# finally, argument *rest can be used to insert many variables,
# these will al be treated the same -> single local var for function
