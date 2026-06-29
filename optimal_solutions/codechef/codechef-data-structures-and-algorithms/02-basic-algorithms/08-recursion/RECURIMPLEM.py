


def solve():
    class Solution:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        def parseDigits(self, s, idx, num, sign):
            # Base case: end of string or non-digit
            if idx >= len(s) or not s[idx].isdigit():
                return sign * num

            digit = ord(s[idx]) - ord('0')
            num = num * 10 + digit

            # Clamp during recursion to avoid overflow
            if sign == 1 and num > self.INT_MAX:
                return self.INT_MAX
            if sign == -1 and -num < self.INT_MIN:
                return self.INT_MIN

            return self.parseDigits(s, idx + 1, num, sign)

        def myAtoi(self, s: str) -> int:
            i = 0
            n = len(s)

            # 1. Ignore leading whitespaces
            while i < n and s[i] == ' ':
                i += 1

            # 2. Check sign
            sign = 1
            if i < n and (s[i] == '+' or s[i] == '-'):
                if s[i] == '-':
                    sign = -1
                i += 1

            # 3. Recursively read digits
            result = self.parseDigits(s, i, 0, sign)

            # 4. Clamp final result
            if result > self.INT_MAX:
                return self.INT_MAX
            if result < self.INT_MIN:
                return self.INT_MIN

            return result


if __name__ == "__main__":
    solve()
