def solve():
    n = int(input())
    fans = 0
    a = list(map(int, input().split()))
    m1 = {}
    pre = [0] * (n + 1)
    sum_val = 0
    m1[0] = 1
    for i in range(1, n + 1):
        sum_val += a[i - 1]
        fans += m1.get(sum_val - i, 0)
        m1[sum_val - i] = m1.get(sum_val - i, 0) + 1
    print(fans)

def main():
    freq = 1
    while freq > 0:
        solve()
        freq -= 1


if __name__ == "__main__":
    solve()
