arr = []

def one_pointer(i,arr,n):
    if i>= n//2:
        return
    arr[i],arr[n-i-1] = arr[n-i-1], arr[i]

    one_pointer(i+1,arr,n)

def main():
    global arr
    arr = [1, 2, 7, 8, 9]  # 0 - 4
    n = len(arr) # no. elements -> 5

    one_pointer(0, arr, n)    
    
    print("Reversed array:", arr)

# Run the code
if __name__ == "__main__":
    main()
