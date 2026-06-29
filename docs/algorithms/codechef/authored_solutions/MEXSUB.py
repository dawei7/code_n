import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = [0] + data[idx:idx + n]
        idx += n

        seen = [0] * (n + 2)
        for value in arr[1:]:
            if value <= n:
                seen[value] += 1
        mex = 0
        while seen[mex]:
            mex += 1

        if mex == 0:
            out.append(str(pow(2, n - 1, MOD)))
            continue

        last = [0] * mex
        active = [0] * mex
        # Maintain the minimum last occurrence among values 0..mex-1 using
        # lazy heap entries (last_position, value).
        import heapq

        heap = [(0, value) for value in range(mex)]
        heapq.heapify(heap)

        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[0] = pref[0] = 1

        for i in range(1, n + 1):
            value = arr[i]
            if value < mex:
                last[value] = i
                heapq.heappush(heap, (i, value))
            while heap and last[heap[0][1]] != heap[0][0]:
                heapq.heappop(heap)
            prev_index = heap[0][0]
            if prev_index:
                dp[i] = pref[prev_index - 1]
            pref[i] = (pref[i - 1] + dp[i]) % MOD

        out.append(str(dp[n] % MOD))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
