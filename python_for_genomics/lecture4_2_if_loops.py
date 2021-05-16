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

"""
combination of conditions & loops
"""
protein = "SDVIHRYKLMSWYXRSFVRSWAOFRDEKL"
for i in range(1, len(protein)):
    if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
        print("protein contains invalid amino acid %s at position %d"
              % (protein[i], i))

# NOTE: break out of loops
for i in range(1, len(protein)):
    if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
        print("protein contains invalid amino acid")
        break

# continue: continue executing loop
protein = "SDVIHRYKLMSWUYXRSFVRSWAOFRDEKL"
corr_protein = ""
for i in range(1, len(protein)):
    if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
        continue
        corr_protein = corr_protein + protein[i]
print("corrected sequence: %s" % corr_protein)

# else in loops
N = 10
for y in range(2, N):
    for x in range(2, y):
        if y % x == 0:
            print(y, "equals", x, "*", y//x)
            break
        else:
            print(y, "is a prime number")

if "U" in protein:
    pass
else:
    print("U found in protein")
