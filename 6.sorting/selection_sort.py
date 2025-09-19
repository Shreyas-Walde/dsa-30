def selection_sort(arr):
    n = len(arr) # 6 elements
    
    # zero indexing 0 - 5 means n-1 
    for i in range(n-1):  # for idx in last element (n-2)
        mini = i # mini = 13, 
        for j in range(i+1,n): # j in i->n-1
            if arr[j] < arr[mini]: #13<13 no , 9<13
                mini = j                      # mini =9
        
        arr[mini],arr[i] = arr[i],arr[mini]  # swap

    return arr


def main():
# Example:
    arr = [13,46,24,52,20,9]
    print("Before:", arr)
    selection_sort(arr)
    print("After :",arr)
main()