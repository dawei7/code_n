


def solve():
    t = int(input())

    for _ in range(t):
        word = input()
        length = len(word)
        first_half = word[:length // 2]
        second_half = word[(length + 1) // 2:]

        frequency1 = {}
        frequency2 = {}

        for ch in first_half:
            frequency1[ch] = frequency1.get(ch, 0) + 1

        for ch in second_half:
            frequency2[ch] = frequency2.get(ch, 0) + 1

        is_lapindrome = True

        for ch in frequency1:
            if frequency1[ch] != frequency2.get(ch, 0):
                is_lapindrome = False
                break

        print("YES" if is_lapindrome else "NO")


if __name__ == "__main__":
    solve()
