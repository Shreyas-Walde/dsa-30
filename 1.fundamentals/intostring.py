# Strings

# append to end of string
s = 'hello'

b = s+'z'  # O(n)
print(b)

if 'e' in b:
    print(True)  # O(n)


# Access position 
print(b[4])


# len size

print(len(s))  # O(n)
