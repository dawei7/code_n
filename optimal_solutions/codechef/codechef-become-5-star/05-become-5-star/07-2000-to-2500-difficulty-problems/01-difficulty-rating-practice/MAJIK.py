


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p,q = list(map(int,input().split()))
        arr = list(map(int,input().split()))
        arr.sort(reverse=True)
        ans = arr[0] - arr[-1]
        nums = []
        for i in range(1,n-1):
            nums += [abs(arr[i])]
        nums.sort(reverse=True)
        for i in range(min(p+q,n-2)):
            ans += nums[i]
        print(ans)


if __name__ == "__main__":
    solve()
