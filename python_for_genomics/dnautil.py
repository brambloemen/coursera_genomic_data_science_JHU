#!/Anaconda/python  # in unix, put this in front to run from terminal
"""
function to count gc percentage
"""


def gc(dna):
    "computes gc percentage of sequence"
    nbases = dna.count('n')

    # use \ for newline
    gcpercent = float(dna.count('g') + dna.count('c')) * 100\
        / (len(dna) - nbases)
    return gcpercent


"""
function for finding stop stop_codons
"""


def has_stop_codon_frame(dna, frame=0):
    "this functions checks if dna has stop codon IN FRAME"
    stop_codon_found = False    # initialize variable
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower()  # make sure to read in lowercase
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found


"""
create a function that returns reverse complement
"""


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
    letters = [basecomplement[base] for base in letters]
    return "".join(letters)  # first create string, apply join method


def reverse_complement(dna):
    "return the reverse complement"
    dna = reverse_string(dna)
    dna = complement(dna)
    return dna
