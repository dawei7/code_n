def generate_parenthesis(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    backtrack('', 0, 0)
    return result

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
        valid_parentheses = generate_parenthesis(n)
        valid_parentheses.sort()
        output_lines.append(str(len(valid_parentheses)))
        output_lines.extend(valid_parentheses)
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    solve()
