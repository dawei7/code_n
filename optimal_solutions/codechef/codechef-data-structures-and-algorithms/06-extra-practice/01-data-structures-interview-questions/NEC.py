def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    res = []
    for _ in range(t):
        n = int(input_data[index])
        k = int(input_data[index + 1])
        index += 2
        pearls = input_data[index:index + n]
        index += n
        k %= n
        rotated = pearls[k:] + pearls[:k]
        res.append(' '.join(rotated))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
