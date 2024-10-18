class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        longestDays = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if stack and t > stack[-1][1]:
                while stack and t > stack[-1][1]:
                    topi,topt = stack.pop()
                    longestDays[topi] = i - topi
            stack.append([i,t])
        return longestDays