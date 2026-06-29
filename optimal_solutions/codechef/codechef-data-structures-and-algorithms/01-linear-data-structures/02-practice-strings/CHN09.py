


def solve():
    t = int(input())

    while t > 0:
        t -= 1
        s = input()
        arr = [0] * 26  # Array to hold frequency of each character
        maxi = 0

        for ch in s:
            arr[ord(ch) - ord('a')] += 1
            maxi = max(maxi, arr[ord(ch) - ord('a')])

        print(len(s) - maxi)


if __name__ == "__main__":
    solve()
