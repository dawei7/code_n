


def solve():
    def next_term(s):
        res = ""
        count = 1
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
            else:
                res += str(count) + s[i]
                count = 1
        return res


    def count_and_say(n):
        if n == 1:
            return "1"
        prev = count_and_say(n - 1)
        return next_term(prev)


if __name__ == "__main__":
    solve()
