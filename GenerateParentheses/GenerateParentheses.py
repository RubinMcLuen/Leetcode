class GenerateParentheses:
    def __init__(self, n):
        self.n = n

    def generate_parentheses_stack(self):
        stack = []
        res = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == self.n:
                res.append("".join(stack))
                return
            
            if open_count < self.n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()

            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()

        backtrack(0, 0)
        return res
