from typing import List
from math import ceil

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        memory = []
        for token in tokens:
            match(token):
                case '+':
                    num2 = int(memory.pop())
                    num1 = int(memory.pop())
                    memory.append(num1+num2)
                case '-':
                    num2 = int(memory.pop())
                    num1 = int(memory.pop())
                    memory.append(num1-num2)
                case '*':
                    num2 = int(memory.pop())
                    num1 = int(memory.pop())
                    memory.append(num1*num2)
                case '/':
                    num2 = int(memory.pop())
                    num1 = int(memory.pop())
                    result = num1/num2
                    if result > 0:
                        memory.append(num1//num2)
                    else:
                        memory.append(ceil(num1/num2))
                        
                case _:
                    memory.append(token)

        return memory[0]
                