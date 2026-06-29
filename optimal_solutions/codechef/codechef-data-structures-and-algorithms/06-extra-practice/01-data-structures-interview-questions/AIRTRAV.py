import heapq

def solve(arr):
    n = len(arr)
    res = 1
    pq = []
    cur = 0
    for i in range(n):
        while pq and cur < i:
            cur += -heapq.heappop(pq)
            res += 1
        if cur < i:
            return -1
        heapq.heappush(pq, -arr[i])
    return res

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(solve(arr))


if __name__ == "__main__":
    solve()
