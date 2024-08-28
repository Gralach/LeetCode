class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            first = {}
            second = {}
            for i in range(len(s)):
                if s[i] not in first:
                    first[s[i]] = 1
                elif s[i] in first:
                    first[s[i]] += 1
                if t[i] not in second:
                    second[t[i]] = 1
                elif t[i] in second:
                    second[t[i]] += 1

            if first == second:
                return True
            else:
                return False