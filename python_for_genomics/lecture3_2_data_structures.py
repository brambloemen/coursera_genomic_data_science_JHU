#!/Anaconda/python  # in unix, put this in front to run from terminal
"""
tuples: store multiple elements in single variable
"""
t = 1, 2, 3
print(t)
t = (1, 2, 3)
print(t)

"""
 sets: unordered collection without duplicates
"""
brca1 = {'DNA repair', 'zinc ion binding', 'etc...', 'DNA repair'}
print(brca1)

brca2 = {"string1", "string2", 'zinc ion binding', "DNA repair"}

brca1 | brca2  # union operation
brca1 & brca2  # intersection
brca1 - brca2  # only elements in brcaa1 (difference)

"""
dictionaries: key-value pairs to look things up later
"""
tf_motif = {
    'SP1': 'gggcgg',
    'C/EBP': 'attgcgcaat'
}

# use square brackets to access tf_motif value by its key
print("the recognition sequence motif of SP1 is %s." % tf_motif['SP1'])

# assing new key to dictionary
tf_motif['AP-1'] = 'tgagtca'

# modify dictionary
tf_motif['AP-1'] = 'tga(g/c)tca'

# delete from library
del tf_motif['AP-1']

# add multiple keys at once
tf_motif.update({'SP-1': 'ggcggg', 'c/EBP': 'attgcgcaat', 'oct-1': 'atgcaaa'})
len(tf_motif)

# list all tf_motif elements
list(tf_motif.keys())
list(tf_motif.values())
sorted(tf_motif.keys())
