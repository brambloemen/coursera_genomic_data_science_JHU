#!/Anaconda/python  # in unix, put this in front to run from terminal

"""
example of writing function to be used from command line
"""


import sys
import getopt

filename = sys.argv[1]
print("processing %s" % filename, "...")

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


o, a = getopt.getopt(sys.argv[2:], "hl:", ["help", "length"])
opts = {}
seqlen = 0

for k, v in o:
    opts[k] = v
print(opts)

if "-h" in opts.keys():
    usage()
    sys.exit()
if "-l" in opts.keys():
    if int(opts['-l']) < 0:
        print("length of sequence should be larger than 0")
        sys.exit()
    seqlen = int(opts['-l'])

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

for i in range(0, len(seqs)):
    if len(list(seqs.values())[i]) < seqlen:
        seqs.pop(list(seqs.keys())[i])
        print("sequence nr %d" % int(i+1), " removed")


for name, seq in seqs.items():
    print(name, seq)
