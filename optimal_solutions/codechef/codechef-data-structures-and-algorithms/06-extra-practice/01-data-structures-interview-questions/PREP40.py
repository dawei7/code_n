def combination_sum_util(candidates, target, start, current, result):
    if target == 0:
        result.append(current.copy())
        return
    for i in range(start, len(candidates)):
        if candidates[i] > target:
            break
        current.append(candidates[i])
        combination_sum_util(candidates, target - candidates[i], i, current, result)
        current.pop()

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index])
        target = int(data[index + 1])
        index += 2
        arr = list(map(int, data[index:index + n]))
        index += n
        candidates = sorted(set(arr))
        result = []
        combination_sum_util(candidates, target, 0, [], result)
        result.sort()
        output_lines.append(str(len(result)))
        for comb in result:
            output_lines.append(' '.join(map(str, comb)))
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    solve()
