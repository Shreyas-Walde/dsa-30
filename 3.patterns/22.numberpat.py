def pattern(n):
    size = 2 * n - 1
    for i in range(size): # 2xn-1
        for j in range(size):
            top =i   # rows
            left = j # columns
            right = size - 1 - j
            down = size - 1 - i
            
            # Calculate the min distance from edges
            min_dist = min(top,left, right,down)
            print(n - min_dist ,end=' ')
        print()  

pattern(3)