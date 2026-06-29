


def solve():
    def is_substring(S1, S2):
        len_S1 = len(S1)
        len_S2 = len(S2)

        if len_S2 > len_S1:
            return "NO"

        # Try every starting position of S2 in S1
        for i in range(len_S1 - len_S2 + 1):
            found = True
            for j in range(len_S2):
                if S1[i + j] != S2[j]:
                    found = False
                    break
            if found:
                return "YES"
        return "NO"

    T = int(input().strip())

    for _ in range(T):
        S1 = input().strip()
        S2 = input().strip()
        print(is_substring(S1, S2))


if __name__ == "__main__":
    solve()
