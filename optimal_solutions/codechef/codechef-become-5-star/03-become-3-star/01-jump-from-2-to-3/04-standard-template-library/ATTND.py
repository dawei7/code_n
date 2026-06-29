# cook your dish here
from collections import Counter


def solve():
    for _ in range(int(input())):
        n = int(input())
        st = []
        for s in range(n):
            st.append(tuple(input().split()))
        c = Counter([x for x, y in st])
        for x,y in st:
            if c[x] == 1:
                print(x)
            else:
                print(x,y)


if __name__ == "__main__":
    solve()
