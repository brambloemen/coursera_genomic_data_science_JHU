geneex = ["gene", 5.16e-08, 0.00138511, 7.33e-08]  # create a list

print(geneex[-1])

geneex[0] = "Lif"
print(geneex)

motif = "nacggggtc"
# motif[0] = "a"  # gives error: strings are immutable

print(geneex[-3:])  # slice the list
print(geneex[:])  # duplicates the list

geneex[1:3] = 6.09e-07
print(geneex)

# lists can be concatenated
print(geneex + [5.16e-08, 0.00138517])

print(len(geneex))  # len applies to both strings and lists

del geneex[1]  # delete second element

geneex = geneex.extend([5.16e-08, 0.00138511])

print(geneex.count("Lif"))  # count method also applies to lists
print(geneex.reverse())

stack = ["a", "b", "c", "d"]
stack.append("e")  # append not equal to extend:
# appending a list would result in this list being counted as only one element
print(stack)

print(stack.pop())  # takes last element and removes it

mylist = [5, 7, 3, 4, 5]
print(sorted(mylist))
print(mylist.sort())  # sorted() does not modify, .sort() does

# also sort alphabetically
