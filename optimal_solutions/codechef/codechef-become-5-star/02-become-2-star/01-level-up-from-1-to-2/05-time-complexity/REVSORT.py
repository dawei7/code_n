# cook your dish here


def solve():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        l = list(map(int, input().split()))
        answer, i = "YES", 0

        while i < n-1:
            if l[i] > l[i+1]:
                if l[i] + l[i+1] > x:
                    answer = "NO"
                    break
                else:
                    t = l[i]
                    l[i] = l[i+1]
                    l[i+1] = t
            i += 1

        print(answer)


if __name__ == "__main__":
    solve()
