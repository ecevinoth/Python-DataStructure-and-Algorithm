#####################################
# python sorting advanced tutorials #
#####################################

# [I]. sorting with key func
# 1. how about records with equal keys, what would be the order of sorting?
# Ans: retain the input order sequence
strings = ['aa', 'zz', 'OO', 'AA', 'Z']
print(sorted(strings, key=len))

################################################################################
# how to sort strings without considering case?
# using key func, convert all to lower or upper and then sort the proxy values
strings = ['aa', 'zz', 'OO', 'AA', 'Z']
print(sorted(strings))
print(sorted(strings, key=str.lower))

################################################################################
# [II]. sorting with user defined functions
# 1. sort input string based on last char
strings = ['xc', 'zb', 'yya', 'zzb', 'zd']


# solution
def my_func(s):
    return s[-1]    # it will return last char of input string


print(sorted(strings, key=my_func))

# 2. sort a lists of list based on 2nd item
data = [
    ['four', 4],
    ['three', 3],
    ['one', 1],
    ['two', 2]
]

# solution
print(sorted(data, key= lambda d: d[1]))

################################################################################
# [III]. accessing external resource to sort input list
# Ex: sort top_students based on their grade
students_grade = {
    'dare': 'C',
    'john': 'F',
    'jane': 'A',
    'ken': 'E',
    'raymond': 'D'
}
top_students = ['dare', 'john', 'jane']

# solution
print(sorted(top_students, key=students_grade.__getitem__))
