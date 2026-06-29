import bisect
import sys
input = sys.stdin.readline

def solve():
    t = int(input().strip())
    for _ in range(t):
        n, q = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        for _ in range(q):
            query = list(map(int, input().strip().split()))
            if query[0] == 0:
                i, x = (query[1], query[2])
                arr[i - 1] = x
            else:
                y = query[1]
                left = bisect.bisect_left(arr, y)
                if left == len(arr) or arr[left] != y:
                    sys.stdout.write('-1\n')
                else:
                    right = bisect.bisect_right(arr, y) - 1
                    sys.stdout.write(f'{left + 1} {right + 1}\n')


if __name__ == "__main__":
    solve()
