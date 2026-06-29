import sys


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        idx += 1
        s = data[idx]
        idx += 1
        runs = [[] for _ in range(26)]
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            runs[s[i] - 97].append(j - i)
            i = j
        answer = 0
        for lengths in runs:
            if not lengths:
                continue
            lengths.sort(reverse=True)
            answer = max(answer, lengths[0] - 1)
            if len(lengths) > 1:
                answer = max(answer, lengths[1])
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
