def threeNumberSum(nums, target):
    if not nums or len(nums) < 3:
        return []
    
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        # Avoid duplicate triplets: if current element is same as previous, skip
        if i > 0 and nums[i] == nums[i-1]:
            continue


        low, high = i + 1, len(nums) - 1
        
        while low < high:
            s = nums[i] + nums[low] + nums[high]
            
            if s == target:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1


                # Avoid duplicates: increment 'low' until a new number is found
                while low < high and nums[low] == nums[low - 1]:
                    low += 1


                # Avoid duplicates: decrement 'high' until a new number is found
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            
            elif s < target:
                low += 1
            else:
                high -= 1


    return res

