class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        digits = [0] * (len(num1) + len(num2))
        for left in range(len(num1) - 1, -1, -1):
            for right in range(len(num2) - 1, -1, -1):
                total = (
                    (ord(num1[left]) - ord("0")) * (ord(num2[right]) - ord("0"))
                    + digits[left + right + 1]
                )
                digits[left + right + 1] = total % 10
                digits[left + right] += total // 10
        first = 0
        while digits[first] == 0:
            first += 1
        return "".join(str(digit) for digit in digits[first:])
