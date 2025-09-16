def primenum(n):

    count = 0
    squart = int(n ** 0.5)  
    for i in range(1,squart+1):  # 1 , 6
        if n % i == 0:           # 36 / 1 -> 0 remainder
            count+=1  
            if i!= n//i:         # 0 is not equal 36/1  
                count+=1         # 6 != 6  

    if count==2:             
        print("Prime")
    else:
        print("Not Prime") 

primenum(138)