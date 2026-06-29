import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    arr = data[1:1 + n]
    answer = 0
    for bit in range(31):
        count = sum((value >> bit & 1 for value in arr))
        answer += count * (count - 1) // 2 * (1 << bit)
    print(answer)


if __name__ == "__main__":
    solve()
