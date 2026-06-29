import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, up, down = data[idx:idx + 3]
        idx += 3
        heights = data[idx:idx + n]
        idx += n
        parachute = True
        answer = n
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > up:
                answer = i + 1
                break
            if diff < -down:
                if parachute:
                    parachute = False
                else:
                    answer = i + 1
                    break
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
