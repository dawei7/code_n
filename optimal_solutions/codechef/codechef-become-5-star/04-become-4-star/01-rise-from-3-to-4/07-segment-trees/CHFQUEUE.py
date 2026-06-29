import sys
MOD = 1000000007

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    arr = data[2:2 + n]
    stack: list[tuple[int, int]] = []
    answer = 1
    for i in range(n - 1, -1, -1):
        value = arr[i]
        while stack and stack[-1][0] >= value:
            stack.pop()
        if stack:
            answer = answer * (stack[-1][1] - i + 1) % MOD
        stack.append((value, i))
    print(answer)


if __name__ == "__main__":
    solve()
