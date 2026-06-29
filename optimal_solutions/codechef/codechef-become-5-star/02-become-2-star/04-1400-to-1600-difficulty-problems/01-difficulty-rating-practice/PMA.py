# cook your dish here


def solve():
    for _ in range(int(input())):
        n=int(input())
        nums=list(map(int, input().split()))
        for i in range(n):
            nums[i]=abs(nums[i])
        add=sorted(nums[0:n:2])
        minus=sorted(nums[1:n:2],reverse = True)
        if add[0] < minus[0]:
            add[0],minus[0]=minus[0],add[0]
        print(sum(add)-sum(minus))


if __name__ == "__main__":
    solve()
