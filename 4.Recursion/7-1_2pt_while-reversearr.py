def printArr(arr,n):
    print("The reversed array is: ",end='')
    for i in range(n):
        print(arr[i],end=' ')

    print()

def reverseArr(arr,n):
    l = 0
    r = n-1 # last element of arr

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1 
    printArr(arr,n)



if __name__ == "__main__":
    arr = [5,4,3,2,1]
    n = len(arr)  # 5 elements
    reverseArr(arr, n) 
                        