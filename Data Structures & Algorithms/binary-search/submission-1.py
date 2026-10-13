class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #highest element in nums
        high = len(nums)-1 #final element of the list
        low = 0 #lowest element of the list
        
        while high >= low:
            mid = (high + low) // 2
            guess = nums[mid]

            if guess == target:
                return (mid)
            
            if guess < target:
                low = mid + 1 #remove elements too high
            
            if guess > target:
                high = mid - 1 # remove elements too low

        return (-1)
        