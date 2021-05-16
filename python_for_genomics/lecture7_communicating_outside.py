#!/Anaconda/python  # in unix, put this in front to run from terminal

"""
opening files in different modes
"""

"""
f = open("example", "r")  # open in read mode
f = open("example", "w")  # open in write mode ! will return empty file
f = open("example", "a")  # open in append mode
"""


try:
    e = open("example.BAM", "r")
except IOError:
    print("the file doesn't exist!")


tst = open("example.fasta", "r")  # open in read mode

for line in tst:
    print(line)

print(tst.read())   # returns nothing: because we finished reading file
print(tst.seek(0))  # go to position in file
print(tst.read())   # now should return something


tst.seek(0)
print(tst.readline())   # read only one line
tst.close()  # stop reading file

f = open("example", "a")
f.write("this is an additional line")
f.close()


"""
read in fasta file and put seqs in dictionary
"""


f = open("example.fasta", "r")
seqs = {}   # initialize dictionary
for line in f:
    line = line.rstrip()
    if line[0] == ">":
        words = line.split()
        # extract seq name only
        name = words[0][1:]  # start in first word, start at 2nd char (no ">")
        # initialize dictionary entry -> key
        seqs[name] = ""
    # when not at first line, enter sequence -> value
    else:
        seqs[name] = seqs[name] + line
f.close()

# try to delete short sequences
seqlen = 20
print(list(seqs.keys()))
for i in range(0, len(seqs)):
    print(i)
    if len(list(seqs.values())[i]) < seqlen:
        seqs.pop(list(seqs.keys())[i])


for name, seq in seqs.items():
    print(name, seq)

"""
import sys
print(sys.argv)

import getopt
def usage(): ...


# colon indicates that value is needed
o, a = getopt.getopt(sys.argv[1:], "l:h", ["length", "help"])
opts = {}
seqlen = 0

for k, v in o:
    opts[k] = v
if "-h" in opts.keys():
    usage(); sys.exit()     # semicolon for multiple statement on one line
if len(a) < 1:
    usage(); sys.exit("input fasta file is missing")
if "-l" in opts.keys():
    if int(opts['l'] < 0) :
        print("length of sequence should be larger than 0"); sys.exit()
    seqlen = opts['-l']
"""

"""
note about unix environment:

stdin: stream data going into file, unless specified otherwise: keyboard
stdout: going out, unless specified otherwise: terminal
stderr: output error messages
"""
