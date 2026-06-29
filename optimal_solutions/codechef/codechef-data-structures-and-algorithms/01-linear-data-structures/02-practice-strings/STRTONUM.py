


def solve():
    def string_to_number(s):
        num = 0
        for char in s:
            num = num * 10 + (ord(char) - ord('0'))
        return num


if __name__ == "__main__":
    solve()
