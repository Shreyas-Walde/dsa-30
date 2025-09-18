# Read input array
n = int(input("int: "))
arr = list(map(int, input("list: ").split()))

# Precompute frequencies using a dictionary (like C++ map)
mp = {}
for i in arr:
    mp[i] = mp.get(i, 0) + 1 # if i -> count | not then 0 

# Optional: iterate over map (uncomment if you want displaying all key->value pairs)
# for k, v in mp.items():
#     print(f"{k}->{v}")

# Process queries
q = int(input("Int: "))
queries = list(map(int, input("In list: ").split()))
for number in queries:
    print(mp.get(number, 0))
