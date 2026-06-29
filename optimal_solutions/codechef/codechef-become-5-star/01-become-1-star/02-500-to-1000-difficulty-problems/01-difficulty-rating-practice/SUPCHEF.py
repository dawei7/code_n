# cook your dish here


def solve():

    x, y, z = map(int, input().split())
    
    if y*z < x:
        return "YES"
    else:
        return 'NO'

n = int(input())

for _ in range(n):
    print(solve())


if __name__ == "__main__":
    solve()
