import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    output = []
    for _ in range(t):
        n = int(input_data[idx])
        target_k = int(input_data[idx + 1])
        idx += 2
        max_possible = n * (n + 1) // 2
        reduction_needed = max_possible - target_k
        result = list(range(1, n + 1))
        current_limit = n - 1
        while reduction_needed > 0:
            deduction_step = min(current_limit, reduction_needed)
            target_index = n - deduction_step
            result[target_index] = 1
            reduction_needed -= deduction_step
            current_limit = deduction_step - 1
        output.append(' '.join(map(str, result)))
    print('\n'.join(output))


if __name__ == "__main__":
    solve()
