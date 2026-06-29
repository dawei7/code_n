def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    result = []
    index = 1
    for _ in range(t):
        P = float(input_data[index])
        index += 1
        X = float(input_data[index])
        index += 1
        Y = float(input_data[index])
        index += 1
        Z = int(input_data[index])
        index += 1
        if Z == 1:
            P = P * (1 + Y / 100)
        else:
            P = P * (1 - X / 100)
        result.append('{:.10f}'.format(P))
    sys.stdout.write('\n'.join(result))


if __name__ == "__main__":
    solve()
