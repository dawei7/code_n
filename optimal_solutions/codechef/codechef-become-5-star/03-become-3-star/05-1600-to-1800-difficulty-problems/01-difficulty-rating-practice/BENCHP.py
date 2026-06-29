# cook your dish here
from collections import Counter


def solve():
    for _ in range(int(input())):
        n,w,rod = map(int,input().split())
        weights = list(map(int,input().split()))
        my_dict = Counter(weights)
        rem = w - rod
        for key, val in my_dict.items():
            rem -= key*(val - (val%2))
            if rem <= 0:
                print("YES")
                break
        else:
            print("NO")


if __name__ == "__main__":
    solve()
