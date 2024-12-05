class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","/","*"]
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                evaluation = self.evaluate(a,b,token)
                stack.append(evaluation)
        return int(stack[0])

    def evaluate(self,a,b,operator):
        a = int(a)
        b = int(b)
        match operator:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return int(a / b)
            case _:
                return None