import sys

def final_temperature(temp, minutes, ambient):
    for _ in range(minutes):
        if temp > ambient + 1:
            temp -= 1
        elif temp < ambient - 1:
            temp += 1
        else:
            temp = ambient
    return temp

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, minutes, ambient, low, high = data[idx:idx + 5]
        idx += 5
        best = None
        for _ in range(n):
            temp, price = (data[idx], data[idx + 1])
            idx += 2
            temp = final_temperature(temp, minutes, ambient)
            if low <= temp <= high:
                best = price if best is None else min(best, price)
        out.append(str(best if best is not None else -1))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
