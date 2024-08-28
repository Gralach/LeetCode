class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for i in nums:
            if i not in dups:
                dups[i] = 1
            else:
                return True
        return False

        