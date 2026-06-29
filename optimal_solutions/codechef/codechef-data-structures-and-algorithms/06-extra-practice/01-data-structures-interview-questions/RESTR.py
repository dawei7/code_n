def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        s = input_data[index]
        index += 1
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        max_freq = max(freq)
        others = n - max_freq
        groups = (max_freq + 1) // 2
        if others >= groups - 1:
            results.append('YES')
        else:
            results.append('NO')
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
