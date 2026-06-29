def count_divisors(n):
    divisors = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                divisors += 1
            else:
                divisors += 2
        i += 1
    return divisors

def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a == b:
            print(-1)
        else:
            print(count_divisors(abs(a - b)))


if __name__ == "__main__":
    solve()
