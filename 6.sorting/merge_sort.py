# Merge Sort
# Time: O(n log n)
# Space: O(n) - Note: can be Log n, but this is harder to write

A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
#     0  1  2  3   4   5  6  7  8
def merge_sort(arr):
    n = len(arr) # 9 

    if n == 1:
        return arr
# Divide    

    m = n // 2 # m = middle point
    L = arr[:m]  # up untill m (from begining - excluding m)
    R = arr[m:] #including m till the end.

    L = merge_sort(L)
    R = merge_sort(R)

    l,r = 0,0  # # Pointers for L and R           [-5, 3, 2, 1], [-3, -3, 7, 2, 2]
    L_len = len(L)   # 4
    R_len = len(R)   # 5

    sorted_arr = [0] * n    # hash?  0(n)
    
# Merge--------------------------------------------------------    
    i = 0
#         0 < 3         0 < 2
    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]   # choose L
            l+=1
        else:
            sorted_arr[i] = R[r]   # choose R
            r+=1

        i+=1

    while l < L_len:
        sorted_arr[i] = L[l]
        l+=1
        i+=1

    while r < R_len:
        sorted_arr[i] = R[r]
        r+=1
        i+=1

    return sorted_arr

print("Before:",A)
print("After: ",merge_sort(A))