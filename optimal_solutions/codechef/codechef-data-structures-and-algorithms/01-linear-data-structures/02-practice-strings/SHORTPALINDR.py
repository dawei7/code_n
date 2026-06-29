


def solve():
    def compute_lps(s):
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def shortest_palindrome(s):
        if len(s) <= 1:
            return s
        rev = s[::-1]
        combined = s + '#' + rev
        lps = compute_lps(combined)
        to_add = rev[:len(s) - lps[-1]]
        return to_add + s


if __name__ == "__main__":
    solve()
