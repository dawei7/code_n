# cook your dish here


def solve():
    for _ in range(int(input())):
        a,b = map(int,input().split())

        n = abs(a - b)
        if n == 1:
            print(1)
        else:
            count = 2
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    count += 2 
                if i*i == n:
                    count -= 1
            print(count)


if __name__ == "__main__":
    solve()
