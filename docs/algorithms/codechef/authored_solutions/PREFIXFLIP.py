import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        need = [1 if ch == 48 else 0 for ch in s]  # toggles needed for 1
        transitions = [0] * n
        for i in range(1, n):
            transitions[i] = transitions[i - 1] + (need[i] != need[i - 1])
        best = 10**9
        for left in range(0, n - k + 1):
            right = left + k - 1
            inside = transitions[right] - transitions[left]
            best = min(best, inside + need[right])
        out.append(str(best))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
