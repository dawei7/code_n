import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out_lines = []
    for _ in range(t):
        d_count = int(data[idx])
        idx += 1
        N = int(data[idx])
        idx += 1
        digits = data[idx:idx + d_count]
        idx += d_count
        k = d_count
        nonzero = [d for d in digits if d != '0']
        if N <= k:
            out_lines.append(digits[N - 1])
            continue
        N_remaining = N - k
        L = 2
        power = k
        if not nonzero:
            out_lines.append('0')
            continue
        while True:
            block = len(nonzero) * power
            if N_remaining <= block:
                break
            N_remaining -= block
            L += 1
            power *= k
        offset = N_remaining - 1
        first_index = offset // power
        first_digit = nonzero[first_index]
        rem_offset = offset % power
        sub_digits = []
        factor = power // k
        rem = rem_offset
        for i in range(L - 1):
            d_index = rem // factor
            sub_digits.append(digits[d_index])
            rem %= factor
            if factor > 1:
                factor //= k
            else:
                factor = 1
        number = first_digit + ''.join(sub_digits)
        out_lines.append(number)
    sys.stdout.write('\n'.join(out_lines))


if __name__ == "__main__":
    solve()
