import sys


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n, budget = int(data[idx]), int(data[idx + 1])
        s = data[idx + 2].decode()
        idx += 3
        answer = 0
        transitions = 0
        used = (-int(s[0])) % 10
        if used <= budget:
            answer = 1
        for i in range(1, n):
            transitions += (int(s[i]) - int(s[i - 1])) % 10
            used = transitions + (-int(s[i])) % 10
            if used > budget:
                break
            answer = i + 1
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
