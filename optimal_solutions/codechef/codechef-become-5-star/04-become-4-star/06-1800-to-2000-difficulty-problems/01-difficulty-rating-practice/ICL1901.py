# cook your dish here
#1001


def solve():
    for _ in range(int(input())):
        #I swapped n and k by accident...oops
        K, N = list(map(int, input().split()))
        X = str(K)
        if X[0] != X[1] and X[1] != X[2] and X[2] != X[0]: print("27"); continue
        if X[0] == X[1] == X[2]: print('1'); continue
        if N >= 2: print(8)
        else: print(7)



    # 112
    # 112112
    # 111
    # 211
    # 121
    # 122
    # 112
    # 221
    # 212

    # 111111
    # 999999


if __name__ == "__main__":
    solve()
