def from_n(i,n):  # 3,3     2,3     1,3    0,3
    if i<1:       # 3<1     2<1     1<1    0<1 True
        return                               # returns
    print(i)      # 3       2       1
    from_n(i-1,n) # 2       1       0  


def main():
    n = int(input("from n: "))
    from_n(n,n)


main()