


def solve():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    pl = [2 ** i - 1 for i in range(26)]
    for _ in range(int(input())):
        k, n = [int(i) for i in input().split()]
        s = ["a"] * k
        n -= k
        if n < 0:
            print(-1)
            continue
        else:
            ii = 0
            while ii < k and n > 0:
                las = -1
                for i in range(26):
                    if pl[i] > n:
                        break
                    las += 1
                n -= pl[las]
                s[ii] = alpha[las]
                ii += 1
            if n == 0:
                print("".join(s))
            else:
                print(-1)


if __name__ == "__main__":
    solve()
