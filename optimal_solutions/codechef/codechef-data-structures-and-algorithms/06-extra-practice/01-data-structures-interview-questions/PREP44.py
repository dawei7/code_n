import sys

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        x = int(input_data[i])
        results.append(str(bin(x).count('1')))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
