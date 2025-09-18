def Frequency(arr):
    mp = {}
    n = len(arr)
    # Count frequencies
    for num in arr:
        mp[num] = mp.get(num, 0) + 1

    # Initialize min and max frequency and corresponding elements
    max_freq = 0
    min_freq = n
    max_ele = None
    min_ele = None

    # Find the elements with highest and lowest frequency
    for element, count in mp.items():
        if count > max_freq:
            max_freq = count
            max_ele = element
        if count < min_freq:
            min_freq = count
            min_ele = element

    print("The highest frequency element is:", max_ele)
    print("The lowest frequency element is:", min_ele)

# Example usage:
arr = [10, 5, 10, 15, 10, 5]
Frequency(arr)
