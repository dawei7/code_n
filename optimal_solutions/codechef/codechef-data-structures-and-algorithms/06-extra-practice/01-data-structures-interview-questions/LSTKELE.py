import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        k = int(input_data[index + 1])
        index += 2
        arr = list(map(int, input_data[index:index + n]))
        index += n
        arr.sort()
        selected = arr[:k]
        results.append(' '.join(map(str, selected)))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
