# cook your dish here
from math import gcd


def solve():
    for _ in range(int(input())):
        n,m = map(int,input().split())
        my_list = []
        for i in range(m):
            x,y = map(int,input().split())
            my_list.append([x,y])
        my_list.sort(key = lambda x : [x[0], x[1]], reverse = True)
        before = 0 
        lcm = 1
        result = 0
        for i in range(m):
            pres_l = abs(lcm * my_list[i][1]) // gcd(lcm, my_list[i][1])
            rem = n - (n//pres_l)
            if rem > before:
                result += (rem - before)*my_list[i][0]
            lcm = pres_l
            before = max(before, rem)
            if before >= n:
                break
        print(result)


if __name__ == "__main__":
    solve()
