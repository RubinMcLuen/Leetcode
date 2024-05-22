class EvaluateReversePolishNotation:
    def __init__(self, tokens):
        self.tokens = tokens
    
    def evaluate_reverse_polish_notation_stack(self):
        stack = []
        for token in self.tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))

        return stack.pop()