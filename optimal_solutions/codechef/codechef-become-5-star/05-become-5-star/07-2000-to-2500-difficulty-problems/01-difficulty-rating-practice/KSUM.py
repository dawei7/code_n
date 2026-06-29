import sys, heapq

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    N, K = (int(input[0]), int(input[1]))
    A = list(map(int, input[2:]))
    pref = [0] * (N + 1)
    for i in range(N):
        pref[i + 1] = pref[i] + A[i]
    pq = []
    for i in range(N):
        heapq.heappush(pq, (-(pref[N] - pref[i]), i, N - 1))
    ans = []
    for _ in range(K):
        neg_sum, l, r = heapq.heappop(pq)
        ans.append(-neg_sum)
        if r > l:
            heapq.heappush(pq, (neg_sum + A[r], l, r - 1))
    print(*ans)


if __name__ == "__main__":
    solve()
