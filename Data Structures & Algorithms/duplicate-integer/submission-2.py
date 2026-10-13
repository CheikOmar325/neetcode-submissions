class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        #loop through list and store the items in seen, if they are in seen, stop
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False

        