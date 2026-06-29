import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    t = int(input_data[0])
    index = 1
    result = []
    for _ in range(t):
        s = input_data[index].strip()
        p = input_data[index + 1].strip()
        index += 2
        result.append('1' if p in s else '0')
    sys.stdout.write('\n'.join(result))


if __name__ == "__main__":
    solve()
