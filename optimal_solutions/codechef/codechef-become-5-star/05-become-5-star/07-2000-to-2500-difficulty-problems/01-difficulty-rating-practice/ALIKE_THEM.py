# ALIKE_THEM
from math import pow


def solve():
    MOD = 1000000007
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        p = list(map(int, input().split()))
        a = list(map(int, input().split()))
        count = 0
        flag = True
        no_zero = a.count(0)
        non_zero = 0
        non_zero_flag = False
        for i in range(n):
            a[i] = a[p[i]-1]
            if a[i] == 0:
                if p[i]-1 >= i:
                    count += 1
            else:
                if not non_zero_flag:
                    non_zero = a[i]
                    non_zero_flag = True
                elif non_zero != a[i] and non_zero_flag:
                    flag = False
                    break
        power = no_zero - (count if non_zero_flag else count-1)
        if not flag:
            print(0)
        else:
            result = 1
            while power != 0:
                result = (result * m) % MOD
                power -= 1
            print(result)


if __name__ == "__main__":
    solve()
