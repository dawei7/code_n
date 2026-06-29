from collections import Counter


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        C = Counter(s)
        if len(C)==1:
            print(1 if n%2==0 else 2)
        else:
            odd = 0
            for i in C:
                if C[i]%2:
                    odd += 1
            if n%2==0:
                print(0 if odd else 1)
            else:
                print(0 if odd>1 else 1)


if __name__ == "__main__":
    solve()
