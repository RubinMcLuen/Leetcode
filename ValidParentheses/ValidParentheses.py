class ValidParentheses:
    def __init__(self, s):
        self.s = s

    def valid_parentheses_stack(self):
        m = {"}":"{",
             "]":"[",
             ")":"("}
        
        stack = []
        
        for i in self.s[::-1]:
            if i in m:
                stack.append(i)
            elif i == "{":
                if stack.pop() == "}":
                    continue
                else:
                    return False
            elif i == "[":
                if stack.pop() == "]":
                    continue
                else:
                    return False
            elif i == "(":
                if stack.pop() == ")":
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True