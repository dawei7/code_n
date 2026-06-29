def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    c = int(data[2])
    tanny_notes = list(map(int, data[3:3 + n]))
    purgi_notes = list(map(int, data[3 + n:3 + n + m]))
    purgi_set = set(purgi_notes)
    for note in tanny_notes:
        if c - note in purgi_set:
            sys.stdout.write('YES')
            return
    sys.stdout.write('NO')


if __name__ == "__main__":
    solve()
