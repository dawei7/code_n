def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    output = []
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        queue = input_data[idx:idx + n]
        idx += n
        friends = input_data[idx:idx + m]
        idx += m
        queue_set = set(queue)
        result = []
        for friend in friends:
            if friend in queue_set:
                result.append('Yes')
            else:
                result.append('No')
        output.append(' '.join(result))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
