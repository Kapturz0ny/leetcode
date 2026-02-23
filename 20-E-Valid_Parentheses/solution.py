class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for c in s:
            if c in matching_brackets.keys():
                stack.append(c)
            elif c in matching_brackets.values():
                if len(stack) > 0:
                    return False
                last_op_bracket = stack.pop()
                if matching_brackets[last_op_bracket] != c:
                    return False
        if len(stack) > 0:
            return False
        return True