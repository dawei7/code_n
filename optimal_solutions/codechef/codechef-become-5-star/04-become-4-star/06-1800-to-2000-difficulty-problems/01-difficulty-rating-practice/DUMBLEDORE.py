import sys
input = sys.stdin.read

def solve():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    sum_values = [0] * (10 ** 6 + 100)
    total = 0
    index = 2
    for _ in range(m):
        p = int(data[index])
        t = int(data[index + 1])
        sum_values[p] += t
        total += sum_values[p]
        print(total)
        index += 2


if __name__ == "__main__":
    solve()
