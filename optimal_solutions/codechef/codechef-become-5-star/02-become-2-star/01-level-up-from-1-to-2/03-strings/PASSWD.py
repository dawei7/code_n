


def solve():
    def is_secure_password(s):
        special_chars = {'@', '#', '%', '&', '?'}

        length = len(s) >= 10
        small = any(c.islower() for c in s)
        large = any(c.isupper() for c in s[1:-1])  # Skip first and last character
        digit = any(c.isdigit() for c in s[1:-1])
        spec = any(c in special_chars for c in s[1:-1])

        return length and small and large and digit and spec

    t = int(input())

    for _ in range(t):
        password = input().strip()
        print("YES" if is_secure_password(password) else "NO")


if __name__ == "__main__":
    solve()
