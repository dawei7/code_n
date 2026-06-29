import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))
    out = []
    for _ in range(num_test_cases):
        n = int(next(iterator))
        k = int(next(iterator))
        arr = [int(next(iterator)) for _ in range(n)]
        if n == 1:
            dp = [0] * k
            rem = 0
            cnt = 0
            while dp[rem] == 0:
                if cnt != 0:
                    dp[rem] = cnt
                rem = (rem * 10 + arr[0]) % k
                cnt += 1
            ch = str(arr[0])
            out.append(f'{ch * dp[rem]} {ch * cnt}')
            continue
        p = 1
        for i in range(1, n):
            if arr[i] != arr[i - 1]:
                arr[p] = arr[i]
                p += 1
        n = p
        arr = arr[:n]
        mp = [''] * k
        q = deque()
        found = False
        for i in arr:
            rem = i % k
            s = str(i)
            if mp[rem] != '':
                out.append(f'{mp[rem]} {s}')
                found = True
                break
            q.append(rem)
            mp[rem] = s
        if found:
            continue
        vis = [False] * k
        while q:
            rem = q.popleft()
            if vis[rem]:
                continue
            vis[rem] = True
            for i in arr:
                nrem = (rem * 10 + i) % k
                s = mp[rem] + str(i)
                if mp[nrem] != '':
                    out.append(f'{mp[nrem]} {s}')
                    found = True
                    break
                mp[nrem] = s
                q.append(nrem)
            if found:
                break
        else:
            out.append('-1 -1')
    print('\n'.join(out))


if __name__ == "__main__":
    solve()
