a = [1,2,3]    # in python list is dynamic array
print(a) 

a.append(5) # insert at end
print(a)

a.pop()  # last element delete
print(a)

# not at the end - o(n)
a.insert(2, 90)
#^ at position 2 insert 90 
print(a) 
# other values shifts without overwriting

# Modify an element
a[0] = 7  # changing 1 number in array
print(a)

# accessing elements at given index
print(a[2]) # 90


# Checking if in array has element - O(n)
if 7 in a:
    print(True)

