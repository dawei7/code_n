import sys

def is_power_of_two(value: int) -> bool:
    return value >= 0 and value & value - 1 == 0

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        total = sum(arr)
        if is_power_of_two(total):
            out.append('0')
            continue
        min_index, min_value = min(enumerate(arr, start=1), key=lambda item: item[1])
        target = 1 << total.bit_length()
        needed = target - (total - min_value)
        multiplier = needed // min_value
        out.append(f'1\n1 {multiplier}\n{min_index}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
