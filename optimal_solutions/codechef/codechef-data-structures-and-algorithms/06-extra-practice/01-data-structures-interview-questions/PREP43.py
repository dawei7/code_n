def is_palindrome(s):
    return s == s[::-1]

def backtrack(s, start, current, result):
    if start == len(s):
        result.append(current[:])
        return
    for end in range(start + 1, len(s) + 1):
        substr = s[start:end]
        if is_palindrome(substr):
            current.append(substr)
            backtrack(s, end, current, result)
            current.pop()

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    outputs = []
    for _ in range(t):
        s = data[index]
        index += 1
        partitions = []
        backtrack(s, 0, [], partitions)
        partitions.sort()
        outputs.append(str(len(partitions)))
        for part in partitions:
            outputs.append(' '.join(part) + ' ')
    sys.stdout.write('\n'.join(outputs))


if __name__ == "__main__":
    solve()
