def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    s = data[2]
    res_length = 0
    res_sub = None
    maxDistinct = min(26, n // k)
    for d in range(maxDistinct, 0, -1):
        window_size = d * k
        if window_size > n:
            continue
        freq = [0] * 26
        for i in range(window_size):
            freq[ord(s[i]) - 97] += 1

        def is_good():
            countDistinct = 0
            for x in freq:
                if x != 0:
                    countDistinct += 1
                    if x != k:
                        return (False, 0)
            return (countDistinct == d, countDistinct)
        good, _ = is_good()
        if good:
            print(window_size)
            print(s[0:window_size])
            return
        for i in range(1, n - window_size + 1):
            freq[ord(s[i - 1]) - 97] -= 1
            freq[ord(s[i + window_size - 1]) - 97] += 1
            good, _ = is_good()
            if good:
                print(window_size)
                print(s[i:i + window_size])
                return
    print('IMPOSSIBLE')


if __name__ == "__main__":
    solve()
