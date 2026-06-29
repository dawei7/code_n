import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        max_prod = arr[0]
        min_prod = arr[0]
        answer = arr[0]
        for num in arr[1:]:
            if num < 0:
                max_prod, min_prod = (min_prod, max_prod)
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            answer = max(answer, max_prod)
        results.append(str(answer))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
