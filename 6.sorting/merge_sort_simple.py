def merge_sort(arr):
# Base case: arrays with 1 or 0 elements are already sorted
    n = len(arr)

    if n <=1:
        return arr
    m = n//2 # middle point

    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    return merge(left,right)

def merge(left,right):
    merged = []
    l = r = 0
  # Merge both arrays while both have items
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    # If left or right still has items, add them all
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged





a = [9, 5, 3, 2, 1, 6, 2, 4]
print(merge_sort(a))