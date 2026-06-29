import sys

def insert_basis(basis: list[int], value: int) -> None:
    x = value
    for bit in range(10, -1, -1):
        if not x >> bit & 1:
            continue
        if basis[bit]:
            x ^= basis[bit]
        else:
            basis[bit] = x
            return

def maximize_with_basis(basis: list[int], value: int) -> int:
    ans = value
    for bit in range(10, -1, -1):
        ans = max(ans, ans ^ basis[bit])
    return ans

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = (data[idx], data[idx + 1])
        idx += 2
        basis = [0] * 11
        for value in data[idx:idx + n]:
            insert_basis(basis, value)
        idx += n
        out.append(str(maximize_with_basis(basis, k)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
