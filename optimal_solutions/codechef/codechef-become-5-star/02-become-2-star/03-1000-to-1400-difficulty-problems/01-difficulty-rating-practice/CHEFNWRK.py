import sys

def solve():
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n, k = map(int, line1)
        weights = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return
    for w in weights:
        if w > k:
            print('-1')
            return
    trips = 0
    current_weight = 0
    for w in weights:
        if current_weight + w <= k:
            current_weight += w
        else:
            trips += 1
            current_weight = w
    if current_weight > 0:
        trips += 1
    print(trips)

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line)
        for _ in range(t):
            solve()


if __name__ == "__main__":
    solve()
