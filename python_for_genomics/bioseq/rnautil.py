#!/Anaconda/python  # in unix, put this in front to run from terminal
"""
function to count gc percentage
"""


def rna_gc(rna):
    "computes gc percentage of sequence"
    nbases = rna.count('n')

    # use \ for newline
    gcpercent = float(rna.count('g') + rna.count('c')) * 100\
        / (len(rna) - nbases)
    return gcpercent


"""
function for finding stop stop_codons
"""


def rna_has_stop_codon_frame(rna, frame=0):
    "this functions checks if dna has stop codon IN FRAME"
    stop_codon_found = False    # initialize variable
    stop_codons = ['uga', 'uag', 'uaa']
    for i in range(frame, len(rna), 3):
        codon = rna[i:i+3].lower()  # make sure to read in lowercase
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found


"""
create a function that returns reverse complement
"""


def rna_reverse_string(seq):
    "reverse sequence"
    return seq[::-1]


def rna_complement(seq):
    "return complementary sequence"
    basecomplement = {"a": "u", "g": "c", "u": "a", "c": "g",
                      "A": "U", "G": "C", "U": "A", "C": "G",
                      "n": "n", "N": "N"}
    letters = list(seq)  # define list
    """
    same as using a for loop to append each item into an empty list
    """
    letters = [basecomplement[base] for base in letters]
    return "".join(letters)  # first create string, apply join method


def rna_reverse_complement(rna):
    "return the reverse complement"
    rna = rna_reverse_string(rna)
    rna = rna_complement(rna)
    return rna
