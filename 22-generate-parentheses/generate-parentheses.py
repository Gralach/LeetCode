class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, result = [], []
        openP, closedP = 0, 0

        def backtrack(openP,closedP):
            if openP==closedP==n:
                result.append(''.join(stack))
                return
            if openP < n:
                stack.append("(")
                backtrack(openP+1, closedP)
                stack.pop()
            if openP > closedP:
                stack.append(")")
                backtrack(openP, closedP+1)
                stack.pop()
        backtrack(openP, closedP)
        return result
            