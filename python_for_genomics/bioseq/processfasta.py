#!/Anaconda/python  # in unix, put this in front to run from terminal

"""
example of writing function to be used from command readline
"""


import sys
import getopt

print(sys.argv)
filename = sys.argv[0]

try:
    ftest = open(filename)
except IOError():
    print("%s not found" % filename)


def usage():
    print("""
    processfasta.py <filename> [-h] [-l <length>]
    <filename> has to be fasta format
    -h       print this message
    -l <length> filter all sequences with length smaller then given length
    """)


o, a = getopt.getopt(sys.argv[1:], "l:h", ["length", "help"])
opts = {}
seqlen = 0

for k, v in o:
    opts[k] = v
if "-h" in opts.keys():
    usage()
    sys.exit()
if len(a) < 1:
    usage()
    sys.exit("input fasta file is missing")
if "-l" in opts.keys():
    if int(opts['l'] < 0):
        print("length of sequence should be larger than 0")
        sys.exit()
    seqlen = opts['-l']

f = open(filename, "r")
seqs = {}   # initialize dictionary
for line in f:
    line = line.rstrip()
    if line[0] == ">":
        words = line.split()
        # extract seq name only
        name = words[0][1:]
        # initialize dictionary entry -> key
        seqs[name] = ""
        # when not at first line, enter sequence -> value
    else:
        seqs[name] = seqs[name] + line
f.close()

"""
for i in range(0, len(seqs)):
    if len(seqs.values()[i]) < seqlen:
        seqs.pop(seqs.values()[i])
"""
