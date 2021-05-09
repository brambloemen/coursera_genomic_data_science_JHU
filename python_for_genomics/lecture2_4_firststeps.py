"""
some more print options
"""
exec(open('lecture2_3_firststeps.py').read())  # --> to run script from python

print("The DNA sequence's GC content is ", gc_percent, " %")

print("The DNA sequence's GC content is %5.3f %%" % gc_percent)  # two percents necesary to print % in final string
# 5.3f: 5 digits, of which 3 after .

print("%d" % 10.6)  # print as integer

"""
reading input
"""

dna = input("enter DNA sequence:")  # always returns string

my_number = input("type number of repeats")
actual_number = int(my_number)
dna = dna * actual_number
print(dna)
