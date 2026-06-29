def rotate_matrix_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    index = 0
    t = int(data[index])
    index += 1
    output_lines = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        matrix = []
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            index += n
            matrix.append(row)
        rotated = rotate_matrix_180(matrix)
        for row in rotated:
            output_lines.append(' '.join(map(str, row)))
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    solve()
