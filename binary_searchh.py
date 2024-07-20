
#count the number of rotation to sort the array x

def count_rotation(nums):
    """Given a list of integers, write a function that returns the number of times the list is rotated"""
    
    lo = 0
    hi = len(nums)
    
    while lo <= hi:
        mid = (lo + hi ) // 2
        
        if mid > 0 and nums[mid] < nums[mid-1]:
            return [mid]
        
        elif nums[mid] >  nums[mid-1]:
            lo = mid + 1
        
            
        else:
             hi = mid - 1
             
    return 0

num1 = [5,6,7,0,2,3,4]
num2 = [3,4,5,6,7,0,2]

print(count_rotation(num2))
    