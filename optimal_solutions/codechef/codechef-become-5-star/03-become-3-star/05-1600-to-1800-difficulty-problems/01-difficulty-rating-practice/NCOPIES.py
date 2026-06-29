import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n, copies = (int(data[idx]), int(data[idx + 1]))
        s = data[idx + 2]
        idx += 3
        ones = s.count(b'1')
        total = ones * copies
        if total == 0:
            out.append(str(n * copies))
            continue
        if total % 2:
            out.append('0')
            continue
        target = total // 2
        prefix = 0
        answer = 0
        for ch in s:
            prefix += ch == ord('1')
            if target >= prefix and ones and ((target - prefix) % ones == 0):
                copy_index = (target - prefix) // ones
                if 0 <= copy_index < copies:
                    answer += 1
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
