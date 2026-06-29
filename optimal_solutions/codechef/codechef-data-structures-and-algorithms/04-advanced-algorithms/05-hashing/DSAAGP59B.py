def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]
    frequency_map = {}
    for ch in s:
        if ch in frequency_map:
            frequency_map[ch] += 1
        else:
            frequency_map[ch] = 1
    uppercase = sorted([ch for ch in frequency_map if ch.isupper() and frequency_map[ch] >= k])
    lowercase = sorted([ch for ch in frequency_map if ch.islower() and frequency_map[ch] >= k])
    result = uppercase + lowercase
    print(''.join(result))


if __name__ == "__main__":
    solve()
