


def solve():
    def are_anagrams(str1, str2):
        if len(str1) != len(str2):
            return False
        count = [0] * 256
        for c1, c2 in zip(str1, str2):
            count[ord(c1)] += 1
            count[ord(c2)] -= 1
        return all(c == 0 for c in count)

    t = int(input())
    for _ in range(t):
        str1 = input()
        str2 = input()
        print("YES" if are_anagrams(str1, str2) else "NO")


if __name__ == "__main__":
    solve()
