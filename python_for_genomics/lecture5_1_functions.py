#!/Anaconda/python  # in unix, put this in front to run from terminal
dna = "atgcaattgcgncaagttgnccccnacctttagccgtata"

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


print(gc(dna), "%")

help(gc)
