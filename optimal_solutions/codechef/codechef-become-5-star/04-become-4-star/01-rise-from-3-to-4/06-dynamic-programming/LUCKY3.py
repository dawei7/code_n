import sys

def digits(value: int) -> list[int]:
    result = []
    while value:
        result.append(value % 10)
        value //= 10
    return result or [0]

def count_for_target(number_digits: list[list[int]], target: list[int], powers: list[int]) -> int:
    length = len(target)
    freq = [0] * (1 << length)
    full = (1 << length) - 1
    for ds in number_digits:
        if len(ds) > length:
            continue
        eq_mask = 0
        ok = True
        for pos in range(length):
            digit = ds[pos] if pos < len(ds) else 0
            if digit > target[pos]:
                ok = False
                break
            if digit == target[pos]:
                eq_mask |= 1 << pos
        if ok:
            freq[eq_mask] += 1
    subset_counts = freq[:]
    for bit in range(length):
        for mask in range(1 << length):
            if mask & 1 << bit:
                subset_counts[mask] += subset_counts[mask ^ 1 << bit]
    answer = 0
    for mask in range(1 << length):
        cnt = subset_counts[full ^ mask]
        ways = powers[cnt] - 1
        if mask.bit_count() & 1:
            answer -= ways
        else:
            answer += ways
    return answer

def solve(values: list[int]) -> int:
    number_digits = [digits(value) for value in values]
    powers = [1] * (len(values) + 1)
    for i in range(1, len(powers)):
        powers[i] = powers[i - 1] * 2
    total = 0
    max_length = max((len(ds) for ds in number_digits))
    for length in range(1, max_length + 1):
        for mask in range(1 << length):
            target = [7 if mask >> pos & 1 else 4 for pos in range(length)]
            total += count_for_target(number_digits, target, powers)
    return total

def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n
        out.append(str(solve(values)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
