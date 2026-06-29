def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N, M = map(int, data[0].split())
    special_friends = set(map(int, data[1].split()))
    posts = []
    for i in range(2, 2 + M):
        f, p, *s = data[i].split()
        f = int(f)
        p = int(p)
        s = ' '.join(s)
        posts.append((f, p, s))
    posts.sort(key=lambda x: (x[0] not in special_friends, -x[1]))
    for post in posts:
        print(post[2])


if __name__ == "__main__":
    solve()
