import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        nxt = [(i + arr[i] + 1) % n for i in range(n)]
        state = [0] * n
        answer = 0
        for start in range(n):
            if state[start]:
                continue
            path_index = {}
            cur = start
            while state[cur] == 0 and cur not in path_index:
                path_index[cur] = len(path_index)
                cur = nxt[cur]
            if cur in path_index:
                answer += len(path_index) - path_index[cur]
            for node in path_index:
                state[node] = 1
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
