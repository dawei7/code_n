


def solve():
    def input_list():
        return list(map(int, input().split()))
    def input_str_list():
        return list(map(str,input().split()))
    def input_numbers():
        return map(int,input().split())

    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [[False]*101 for _ in range(n)]
        for i in range(n):
            now = list(map(int, input().split()))
            for cloth in now:
                arr[i][cloth] = True
        memo = [[-1]*((2**n)+5) for _ in range(105)]
        mod = 10**9+7
        def solve(i,mask):
            if mask == (1<<n)-1:
                return 1
            if i>100:
                return 0
            if memo[i][mask]!=-1:
                return memo[i][mask]
            ans = 0
            for j in range(n):
                if mask&(1<<j)==0:  ## hasn't worn anything
                    if arr[j][i]:
                        temp_mask = mask|(1<<j)
                        ans = (ans + solve(i+1,temp_mask))%mod
            ans = (ans + solve(i+1,mask))%mod
            memo[i][mask] = ans
            return ans
        print(solve(1,0))


if __name__ == "__main__":
    solve()
