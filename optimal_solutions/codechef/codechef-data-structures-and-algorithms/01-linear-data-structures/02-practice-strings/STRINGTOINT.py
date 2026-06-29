


def solve():
    def myAtoi(s: str) -> int:
        i = 0
        n = len(s)

        # 1️⃣ Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        # 2️⃣ Check sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        result = 0
        has_digits = False

        # 3️⃣ Read digits
        while i < n and s[i].isdigit():
            has_digits = True
            digit = int(s[i])

            # Overflow check BEFORE multiplying
            if sign == 1 and result > (INT_MAX - digit) // 10:
                return INT_MAX
            if sign == -1 and result > (INT_MAX + 1 - digit) // 10:
                return INT_MIN

            result = result * 10 + digit
            i += 1

        if not has_digits:
            return 0

        result *= sign

        # Convert -0 to 0
        if result == 0:
            result = 0

        return result


if __name__ == "__main__":
    solve()
