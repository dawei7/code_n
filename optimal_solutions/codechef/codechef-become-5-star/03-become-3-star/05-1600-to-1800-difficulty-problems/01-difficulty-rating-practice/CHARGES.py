


def solve():
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        s = list(input())
        qi = [int(i)-1 for i in input().split()]
        if n == 1:
            print("0\n"*k)
            continue
        tot = 0
        prev = s[0]
        for i in s[1:]:
            if prev == i == "1" or prev == i == "0":
                tot += 2
            else:
                tot += 1
            prev = i
        for i in qi:
            s[i] = "0" if s[i] == "1" else "1"
            if i == 0:
                if s[i] == s[i+1]:
                    tot += 1
                else:
                    tot -= 1
            elif i == n - 1:
                if s[i] == s[i-1]:
                    tot += 1
                else:
                    tot -= 1
            else:
                if s[i] == s[i + 1]:
                    tot += 1
                else:
                    tot -= 1
                if s[i] == s[i-1]:
                    tot += 1
                else:
                    tot -= 1
            print(tot)


if __name__ == "__main__":
    solve()
