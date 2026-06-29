# cook your dish here


def solve():
    n,m,q = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    col_sum = (n*(n+1))//2
    for target in Q:
            tot_sum = 0
            for i in range(1,n+1):
                tot_sum += m * i
                if tot_sum>target:
                    break
            ans = [m for _ in range(i)]
            val = i
            need = tot_sum - target
            while val:
                if need>=val:
                    need -= val
                    ans[val-1] -= 1
                    if not ans[val-1]:
                        ans.pop()
                else:
                    val -= 1
            print(1,len(ans))
            print(*ans)


if __name__ == "__main__":
    solve()
