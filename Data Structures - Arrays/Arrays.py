# Notes: In Python, Lists are Arrays! 
#        Python Lists are Dynamic, Heterogeneous, and Mutable.

strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used 

# get: c
print(strings[2])
# get: d
print(strings[-1])

# push    
strings.append('e')   # O(1)
# pop
strings.pop()         # O(1)
strings.pop()

# add first element
strings.insert(0, 'x')

# splice
strings.insert(2, 'alien')  # O(n)


print (strings)