# python sorting
# sorted function
# sorted(list), returns new list, the original list is untouched

a = [5, 1, 4, 3]
print(sorted(a))  # create new sorted list

# alternative function or old method
a.sort()  # inplace sort
print(a)

# sorted functional optional arguments
print(sorted(a, reverse=True))  # case sensitive

strings = ['aaaa', 'BBB', 'z', 'CCCC']
print(sorted(strings, reverse=True))

# custom sorting with key function
# for more complex sorting sorted() takes optional "key=" function
# key function takes one value and return one proxy values is used for list
# comparisons with in the sort
print(sorted(strings, key=len))     # compute length for each elements and sort based on proxy value
