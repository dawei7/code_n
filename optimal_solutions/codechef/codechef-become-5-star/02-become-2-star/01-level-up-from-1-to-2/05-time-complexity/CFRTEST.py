def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])
    assert 1 <= T <= 10000
    index = 1
    results = []
    for _ in range(T):
        n = int(data[index])
        assert 1 <= n <= 50
        d = list(map(int, data[index + 1].split()))
        assert all((1 <= x <= 100 for x in d))
        distinct_elements = set(d)
        results.append(str(len(distinct_elements)))
        index += 2
    print('\n'.join(results))


if __name__ == "__main__":
    solve()
