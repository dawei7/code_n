import sys

def nearest_diff(left_bits: int, right_bits: int, target: int) -> int:
    best = 10 ** 18
    if left_bits.bit_count() > right_bits.bit_count():
        left_bits, right_bits = (right_bits, left_bits)
    bits = left_bits
    min_right = (right_bits & -right_bits).bit_length() - 1
    max_right = right_bits.bit_length() - 1
    while bits:
        lsb = bits & -bits
        left_sum = lsb.bit_length() - 1
        want = target - left_sum
        if want <= min_right:
            diff = abs(left_sum + min_right - target)
            if diff < best:
                best = diff
                if best == 0:
                    return 0
        elif want >= max_right:
            diff = abs(left_sum + max_right - target)
            if diff < best:
                best = diff
                if best == 0:
                    return 0
        else:
            upper_bits = right_bits >> want
            if upper_bits:
                right_sum = want + ((upper_bits & -upper_bits).bit_length() - 1)
                diff = abs(left_sum + right_sum - target)
                if diff < best:
                    best = diff
                    if best == 0:
                        return 0
            lower_mask = right_bits & (1 << want + 1) - 1
            if lower_mask:
                right_sum = lower_mask.bit_length() - 1
                diff = abs(left_sum + right_sum - target)
                if diff < best:
                    best = diff
                    if best == 0:
                        return 0
        bits ^= lsb
    return best

def solve(values: list[int], k: int) -> float:
    values.sort()
    n = len(values)
    median_position = (k + 1) // 2
    left_count = median_position - 1
    right_count = k - median_position
    prefix = [[0] * (k + 1) for _ in range(n + 1)]
    prefix[0][0] = 1
    for i, value in enumerate(values, 1):
        prefix[i] = prefix[i - 1][:]
        for count in range(min(i, k), 0, -1):
            prefix[i][count] |= prefix[i - 1][count - 1] << value
    suffix = [[0] * (k + 1) for _ in range(n + 1)]
    suffix[n][0] = 1
    for i in range(n - 1, -1, -1):
        value = values[i]
        suffix[i] = suffix[i + 1][:]
        for count in range(min(n - i, k), 0, -1):
            suffix[i][count] |= suffix[i + 1][count - 1] << value
    best = 10 ** 18
    for i, median in enumerate(values):
        if i < left_count or n - i - 1 < right_count:
            continue
        left_bits = prefix[i][left_count]
        right_bits = suffix[i + 1][right_count]
        if left_bits and right_bits:
            target = (k - 1) * median
            best = min(best, nearest_diff(left_bits, right_bits, target))
    return best / k

def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, k = (data[idx], data[idx + 1])
        idx += 2
        values = data[idx:idx + n]
        idx += n
        out.append(f'{solve(values, k):.3f}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
