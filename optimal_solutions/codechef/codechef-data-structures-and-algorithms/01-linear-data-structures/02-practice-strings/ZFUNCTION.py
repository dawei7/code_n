


def solve():
    def compute_prefix(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
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


    def search(text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0:
            return 0  # Edge case: empty pattern

        lps = compute_prefix(pattern)
        i = 0  # index for text
        j = 0  # index for pattern

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1

            if j == m:
                return i - j  # match found
            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1


if __name__ == "__main__":
    solve()
