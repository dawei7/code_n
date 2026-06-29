import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        target = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        arr.sort()
        quadruples = []
        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                left, right = (j + 1, n - 1)
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]
                    if total == target:
                        quadruples.append((arr[i], arr[j], arr[left], arr[right]))
                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        quadruples.sort()
        output_lines.append(str(len(quadruples)))
        for quad in quadruples:
            output_lines.append(' '.join(map(str, quad)) + ' ')
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    solve()
