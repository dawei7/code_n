


def solve():
    T = int(input())
    for z in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()

        print((nums[n-1]-nums[0])*nums[n-2])


if __name__ == "__main__":
    solve()
