arr = []
#                0     7
def reverseArr(start, end):
    if start >= end:   # no
        return    
#         0          7          7          0
    arr[start], arr[end] = arr[end], arr[start]   # Swap elements at positions
    
    # Recursive call: move left pointer right, right pointer left
    reverseArr(start + 1, end - 1)
#                  1        6 
def main():
    global arr
    
    arr = [1, 2, 7, 8, 9]
    
    n = len(arr) # no. elements
    
    # Call f(0, r-1) where r-1 is the last index
    reverseArr(0, n -1)    # zero index, n = 8, 8-1 -> 7
    
    print("Reversed array:", arr)


# Run the code
if __name__ == "__main__":
    main()
