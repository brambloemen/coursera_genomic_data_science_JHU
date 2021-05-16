#!/Anaconda/python  # in unix, put this in front to run from terminal
import sys

"""
where python looks for modules
"""


sys.path
sys.path.append("D:/Programming/bio_inf_learning/coursera_genomic_data_science_JHU/python_for_genomics")


"""
using modules
"""


import dnautil
dna = "atttggcgatgcctactcagcttag"

dnautil.gc(dna)     # using function from module requires to specifiy module

from dnautil import *  # import like this: names are defined now
gc(dna)


"""
packages
"""


import bioseq.dnautil

bioseq.dnautil.gc('atttggcgatgcctactcagcttag')
