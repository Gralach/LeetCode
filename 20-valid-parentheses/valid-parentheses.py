class Solution:
    def isValid(self, s: str) -> bool:
        latest = []
        if len(s) == 1:
            return False
        for i in s:
            if i == "}" or i == "]" or i == ")":
                if len(latest) == 0:
                    return False
                else:
                    if ((latest[-1] == "{" and i == "}") or
                        (latest[-1] == "[" and i == "]") or
                        (latest[-1] == "(" and i == ")")):
                        latest.pop()
                        print("pop")
                    else:
                        return False
            else:
                latest.append(i)
        if len(latest) != 0:
            return False
        else:
            return True

