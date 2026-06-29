# cook your dish here


def solve():
    def createPos(A,B, nums):
        # Assumming A and B may be the sum and the sub 

        found = False
        a = (A+B)//2
        b = (A-B)//2

        if a >= 1 and b >= 1 and max(a,b) <= 10**4:
            local = sorted([A,B,a*b,a//b])
            if  local == nums:
                found = True

        if found:
            return(found,[a,b])

        A,B = B,A
        a = (A+B)//2
        b = (A-B)//2

        if a >= 1 and b >= 1 and max(a,b) <= 10**4:
            local = sorted([A,B,a*b,a//b])
            if  local == nums:
                found = True

        if found:
            return(found,[a,b])
        else:
            return(found,[-1,-1])


    for T in range(int(input())):

        nums = sorted(map(int,input().split()))

        pos = [-1,-1]
        for i in range(3):
            for j in range(i+1,4):
                ans = createPos(nums[i],nums[j], nums)
                if ans[0]:
                    pos = ans[1]
                    break

        print(*pos)


if __name__ == "__main__":
    solve()
