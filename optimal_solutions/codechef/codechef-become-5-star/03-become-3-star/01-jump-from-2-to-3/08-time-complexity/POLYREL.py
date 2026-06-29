import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    pointer = 1
    results = []
    for _ in range(t):
        n = int(input_data[pointer])
        pointer += 1
        pointer += 2 * n
        total_sides = n
        current_n = n
        while True:
            child_sides = current_n // 2
            if child_sides >= 3:
                total_sides += child_sides
                current_n = child_sides
            else:
                break
        results.append(str(total_sides))
    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == "__main__":
    solve()
