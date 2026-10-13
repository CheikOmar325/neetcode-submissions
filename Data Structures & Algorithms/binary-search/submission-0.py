class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #highest element in nums
        high = len(nums)-1
        low = 0
        
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
        