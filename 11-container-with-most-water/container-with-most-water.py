class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0

        l = 0
        r = len(height)-1

        while r > l:
            water = min(height[l],height[r]) * (r - l)
            if max <  water:
                max = water
            
            if height[l] > height[r]:
                r -= 1
            elif height[l] <= height[r]:
                l += 1
        return max