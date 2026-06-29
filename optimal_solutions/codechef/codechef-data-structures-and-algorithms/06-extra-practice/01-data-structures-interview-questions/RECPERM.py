def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    output = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        A = list(map(int, data[pos:pos + n]))
        pos += n
        forced = []
        for i in range(n):
            if A[i] == 1:
                forced.append(i + 1)
        ans = []
        prev = 0
        for force in forced:
            block = list(range(prev + 1, force + 1))
            block.reverse()
            ans.extend(block)
            prev = force
        output.append(' '.join(map(str, ans)))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
