def count_pretty_numbers(L, R):
    count = 0
    for i in range(L, R + 1):
        last_digit = i % 10
        if last_digit in {2, 3, 9}:
            count += 1
    return count

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        L = int(data[index])
        R = int(data[index + 1])
        index += 2
        results.append(count_pretty_numbers(L, R))
    for result in results:
        print(result)


if __name__ == "__main__":
    solve()
