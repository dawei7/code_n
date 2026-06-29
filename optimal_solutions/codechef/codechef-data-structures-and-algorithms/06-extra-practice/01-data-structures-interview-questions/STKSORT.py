def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        A = list(map(int, input_data[index:index + n]))
        index += n
        stack = []
        expected = 1
        for num in A:
            stack.append(num)
            while stack and stack[-1] == expected:
                stack.pop()
                expected += 1
        results.append('YES' if expected - 1 == n else 'NO')
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
