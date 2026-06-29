import sys

def possible(o1: int, o2: int, districts: list[int]) -> int:
    n = o1 * o2
    doubled = districts + districts
    prefix = [0] * (2 * n + 1)
    for i, value in enumerate(doubled, 1):
        prefix[i] = prefix[i - 1] + value
    states_needed = o1 // 2 + 1
    district_needed = o2 // 2 + 1
    for start in range(o2):
        won_states = 0
        for state in range(o1):
            left = start + state * o2
            ones = prefix[left + o2] - prefix[left]
            if ones >= district_needed:
                won_states += 1
                if won_states >= states_needed:
                    return 1
    return 0

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        o1, o2 = (data[idx], data[idx + 1])
        idx += 2
        n = o1 * o2
        districts = data[idx:idx + n]
        idx += n
        out.append(str(possible(o1, o2, districts)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
