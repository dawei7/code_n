


def solve():
    n = int(input())  
    for _ in range(n):
        nums = list(map(int, input().split()))  
        nums.sort()  
        print(nums[1])


if __name__ == "__main__":
    solve()
