import sys

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    outputs = []
    index = 1
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        count = 0
        while n % 2 == 0:
            count += 1
            n //= 2
        outputs.append('1' if count % 2 == 0 else '0')
    sys.stdout.write('\n'.join(outputs))


if __name__ == "__main__":
    solve()
