def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    output = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        max_sum = 0
        current_sum = 0
        found_non_negative = False
        for i in range(n):
            num = int(input_data[idx])
            idx += 1
            if num >= 0:
                found_non_negative = True
                current_sum += num
            else:
                if current_sum > max_sum:
                    max_sum = current_sum
                current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
        if not found_non_negative:
            output.append('0')
        else:
            output.append(str(max_sum))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
