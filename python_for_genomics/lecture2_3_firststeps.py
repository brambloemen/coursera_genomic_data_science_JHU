
# #!/Anaconda/python  # in unix, put this in front to run from terminal
# to find where python is: which python
# by default, program is not executable --> chmod a+x script.py
dna = "atgccgccaaattcggcgatgatgaccttg"
n_c = dna.count("c")
n_g = dna.count("g")

dna_length = len(dna)

""" another way to add comments
of
multiple
lines
"""

gc_percent = (n_c + n_g) * 100.0 / dna_length

print(gc_percent)
