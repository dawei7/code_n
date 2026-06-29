# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()
        if a == b:
            print("0")
        else:
            count = 0
            n = []
            l = len(a)
            for i in range(l):
                if a[i] != b[i] and i not in n:
                    count = count + 1
                    p = i
                    while a[p] != b[p]:
                        n.append(p)
                        p = p + 2
                        if p >= l:
                            break
            print(count)


if __name__ == "__main__":
    solve()
