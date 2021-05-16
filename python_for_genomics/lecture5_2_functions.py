#!/Anaconda/python  # in unix, put this in front to run from terminal
dna = "atgcaattgcgncaagttgnccccnacctttagccgtata"

"""
function to find stop codon in frame
"""
dna = input("enter a dna sequence: ")


def has_stop_codon(dna):
    "this functions checks if dna has stop codon"
    stop_codon_found = False    # initialize variable
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3].lower()  # make sure to read in lowercase
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found


print(has_stop_codon(dna))


"""
same function, where now you can specify FRAME
"""


def has_stop_codon_frame(dna, frame):
    "this functions checks if dna has stop codon IN FRAME"
    stop_codon_found = False    # initialize variable
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower()  # make sure to read in lowercase
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found


frame = input("specify the frame to look in: ")
frame = int(frame)
print(has_stop_codon_frame(dna, frame))


"""
same function, where frame now has a default value
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


frame = input("specify the frame to look in: ")
frame = int(frame)
print(has_stop_codon_frame(dna, frame))
