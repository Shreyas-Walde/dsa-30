# Inseration sort
# Time: O(n^2), Space: O(1)

a =  [9,5,3,2,1,6,2,4]

def insertion_sort(arr):
    n = len(arr) # 8

    for i in range(1,n):
        j= i
        while j> 0 and arr[j-1] > arr[j]:
            
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j-=1    

insertion_sort(a)
print(a)