import sys

def precompute(arr: list[int], cap: int) -> list[int]:
    n = len(arr)
    if all((value == 1 for value in arr)):
        return [cap] * n
    if all((value == 0 for value in arr)):
        return [0] * n
    zero = arr.index(0)
    runs: list[tuple[list[int], int]] = []
    i = 1
    while i <= n:
        pos = (zero + i) % n
        if arr[pos] == 0:
            i += 1
            continue
        positions = []
        while i <= n and arr[(zero + i) % n] == 1:
            positions.append((zero + i) % n)
            i += 1
        runs.append((positions, len(positions)))
    lengths = sorted((length for _, length in runs), reverse=True)
    global_best = lengths[0]
    second_best = lengths[1] if len(lengths) > 1 else 0
    max_count = sum((1 for length in lengths if length == global_best))
    answer = [min(global_best, cap)] * n
    for positions, length in runs:
        other = global_best if length != global_best or max_count > 1 else second_best
        for offset, start_pos in enumerate(positions):
            if offset == 0:
                continue
            split_best = max(other, offset, length - offset)
            answer[start_pos] = min(split_best, cap)
    return answer

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    q = int(tokens[1])
    cap = int(tokens[2])
    arr = [int(x) for x in tokens[3:3 + n]]
    queries = tokens[3 + n].decode()
    answers = precompute(arr, cap)
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
