import sys
from collections import deque

def answers_for_starts(arr: list[int], frame: int) -> list[int]:
    n = len(arr)
    frame = min(frame, n)
    doubled = arr + arr
    window_sums = []
    current = sum(doubled[:frame])
    window_sums.append(current)
    for i in range(frame, 2 * n):
        current += doubled[i] - doubled[i - frame]
        window_sums.append(current)
    span = n - frame + 1
    dq: deque[int] = deque()
    answers = [0] * n
    for i, value in enumerate(window_sums):
        while dq and window_sums[dq[-1]] <= value:
            dq.pop()
        dq.append(i)
        while dq and dq[0] <= i - span:
            dq.popleft()
        start = i - span + 1
        if 0 <= start < n:
            answers[start] = window_sums[dq[0]]
    return answers

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    frame = int(tokens[1])
    q = int(tokens[2])
    arr = [int(x) for x in tokens[3:3 + n]]
    queries = tokens[3 + n].decode()
    answers = answers_for_starts(arr, frame)
    rotations = 0
    out: list[str] = []
    for ch in queries[:q]:
        if ch == '!':
            rotations = (rotations + 1) % n
        else:
            start = (n - rotations) % n
            out.append(str(answers[start]))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
