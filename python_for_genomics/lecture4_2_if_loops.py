#!/Anaconda/python  # in unix, put this in front to run from terminal
dna = input("Enter a DNA sequence: ")

pos = dna.find('gt', 0)  # position of donor splice site
print(pos)
"""
while loops
"""
while pos > -1:
    print("Donor splice site at position %d" % pos)
    pos = dna.find('gt', pos + 1)
    print(pos)

"""
for loops
"""
motifs = ["attgcc", "agggggtttttcg", "gtagc"]
for m in motifs:
    print(m, len(m))

# range function
for i in range(1, 10, 2):
    print(i)
