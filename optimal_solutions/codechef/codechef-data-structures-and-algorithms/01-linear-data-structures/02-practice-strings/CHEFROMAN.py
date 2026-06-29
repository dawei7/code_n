


def solve():
    def romanToInt(s):
        def roman_value(c):
            return {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }.get(c, 0)

        result = 0
        n = len(s)

        for i in range(n):
            current = roman_value(s[i])
            next_val = roman_value(s[i+1]) if i + 1 < n else 0

            if current < next_val:
                result -= current
            else:
                result += current

        return result


if __name__ == "__main__":
    solve()
