# Bubble Sort
# Time: O(n^2)
# Space: O(1)

A = [-5,3,2,1,-3,4,2,-1]
N = [1,2,3,4,5,6,7]

def bubble(arr):
    n = len(arr)
    for i in range(n):
        didswap = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswap = True
        
        if not didswap:
            break
bubble(A)
print(A)