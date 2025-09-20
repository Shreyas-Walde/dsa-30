# Inseration sort
# Time: O(n^2) | best O(n), Space: O(1)

a =  [9,5,3,2,1,6,2,4]

def insertion_sort(arr):
    n = len(arr) # 8

    for i in range(1,n):     # index from 1 to n=7
        for j in range(i,0,-1): # index j 7 - 1 
            if arr[j-1] > arr[j]: # 9 > 5
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

insertion_sort(a)
print(a)