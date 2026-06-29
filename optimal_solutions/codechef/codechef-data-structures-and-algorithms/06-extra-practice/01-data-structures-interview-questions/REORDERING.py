import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        custom_order = data[index]
        index += 1
        order_map = {ch: i for i, ch in enumerate(custom_order)}
        n = int(data[index])
        index += 1
        arr = data[index:index + n]
        index += n
        arr.sort(key=lambda s: [order_map[ch] for ch in s])
        output_lines.extend(arr)
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    solve()
