


def solve():
    for _ in range(int(input())):
        N = int(input())
        A = sorted(list(map(int, input().split())))
        z_value = 0
        i = N-1; j = N
        while i >=0:
            if A[i] == A[j]:
                z_value += 1; i-= 1; j += 1
            else:
                break
        else: print("NO");continue
        if z_value > ((N - z_value) + 1): print('NO')
        else: print("YES")


    # 1 1 1 1 1 1 1 2
    # Not possible

    # 1 1 2 2 | 2 2 3 5
    # 0 4 -4


if __name__ == "__main__":
    solve()
