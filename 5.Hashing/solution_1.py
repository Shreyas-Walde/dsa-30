
def countFrequencies(nums, n):
        # Your code goes here
        
        #precompute 
    mp = {}                        # dict
    for i in range(n):             
        if nums[i] in mp:          # check num already in mp <dict>     
            mp[nums[i]] +=1         # then increment
        else:                      # check if not
            mp[nums[i]] = 1         # just increment by 1
        # Build the result list of pairs
        result = []   
        for key in mp:      # <dict> = {key:value}
            result.append([key, mp[key]]) # store and append in list
    print(result)
    

if __name__ == '__main__':
    nums = [10, 5, 10, 15, 10, 5]
    n = len(nums)
    countFrequencies(nums, n)