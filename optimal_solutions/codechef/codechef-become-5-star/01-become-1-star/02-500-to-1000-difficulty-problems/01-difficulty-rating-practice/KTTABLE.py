import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    results = []
    for _ in range(T):
        N = int(input_data[idx])
        idx += 1
        A = [int(x) for x in input_data[idx:idx + N]]
        idx += N
        B = [int(x) for x in input_data[idx:idx + N]]
        idx += N
        count = 0
        prev_time = 0
        for i in range(N):
            available_time = A[i] - prev_time
            if available_time >= B[i]:
                count += 1
            prev_time = A[i]
        results.append(str(count))
    print('\n'.join(results))


if __name__ == "__main__":
    solve()
