def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    t = int(input_data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index:index + n]))
        index += n
        arr.sort()
        used = [False] * n
        current = []
        result = []

        def backtrack():
            if len(current) == n:
                result.append(current[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and arr[i] == arr[i - 1] and (not used[i - 1]):
                    continue
                used[i] = True
                current.append(arr[i])
                backtrack()
                current.pop()
                used[i] = False
        backtrack()
        output_lines.append(str(len(result)))
        for perm in result:
            output_lines.append(' '.join(map(str, perm)) + ' ')
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    solve()
