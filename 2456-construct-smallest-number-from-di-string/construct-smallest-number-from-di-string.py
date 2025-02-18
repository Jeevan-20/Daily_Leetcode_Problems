class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = ""
        num = 1  # Start with the smallest digit

        for char in pattern:
            stack.append(str(num))
            num += 1
            if char == 'I':  # Resolve decreasing sequences
                while stack:
                    result += stack.pop()

        # Append the last digit
        stack.append(str(num))
        while stack:
            result += stack.pop()

        return result

