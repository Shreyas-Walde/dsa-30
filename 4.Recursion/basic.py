count = 0
def infinite():
    # count = 0        # will reinitiate count = 0
    
    global count     # Tells Py to use the global 'count'
    if (count == 3):
        return 
    
    print(count)
    count+=1
    infinite()


def main():

    infinite()
    return 0

main()


###  Second Approach 
def infinite(count):
    if count == 3:
        return     
    print(count)
    count += 1
    infinite(count)  # Pass the updated count to the next call

def main():
    infinite(0)  # Start with count = 0
    return 0

main()