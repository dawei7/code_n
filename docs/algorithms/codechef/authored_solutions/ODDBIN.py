import sys


MAX_M = 15
PREV = [[0] * (1 << m) for m in range(MAX_M + 1)]
BIT = [[0] * (1 << m) for m in range(MAX_M + 1)]
COEFF = [[0] * (1 << m) for m in range(MAX_M + 1)]
for m in range(1, MAX_M + 1):
    for mask in range(1, 1 << m):
        lsb = mask & -mask
        bit = lsb.bit_length() - 1
        previous = mask ^ lsb
        PREV[m][mask] = previous
        BIT[m][mask] = bit
        bits = mask.bit_count()
        value = 1 << (bits - 1)
        COEFF[m][mask] = value if bits & 1 else -value


def odd_coefficients(exponents: list[int]) -> int:
    m = len(exponents)
    size = 1 << m
    common = [0] * size
    common[0] = (1 << 60) - 1
    answer = 0
    prev = PREV[m]
    bit = BIT[m]
    coeff = COEFF[m]
    for mask in range(1, size):
        value = common[prev[mask]] & exponents[bit[mask]]
        common[mask] = value
        answer += coeff[mask] << value.bit_count()
    return answer


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        m = data[idx]
        idx += 1
        exponents = data[idx : idx + m]
        idx += m
        out.append(str(odd_coefficients(exponents)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
