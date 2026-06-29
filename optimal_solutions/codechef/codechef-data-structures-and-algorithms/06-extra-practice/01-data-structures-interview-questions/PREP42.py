def backtrack(arr, start, path, result):
    if path:
        result.append(path[:])
    for i in range(start, len(arr)):
        if i > start and arr[i] == arr[i - 1]:
            continue
        path.append(arr[i])
        backtrack(arr, i + 1, path, result)
        path.pop()

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    outputs = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        arr.sort()
        subsets = []
        backtrack(arr, 0, [], subsets)
        subsets.sort()
        outputs.append(str(len(subsets)))
        for subset in subsets:
            outputs.append(' '.join(map(str, subset)) + ' ')
    sys.stdout.write('\n'.join(outputs))


if __name__ == "__main__":
    solve()
