import math


def solve():
    def Solve(a,n):
        stack=[a[0]]
        score=0
        for i in a[1:]:
            if(len(stack)!=0 and stack[-1]!=i):
                score+=1
                stack.pop()
            else:
                stack.append(i)
        temp=0
        if(stack.count(1)==len(stack)):
            score=score+len(stack)//3
        return score+temp



    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        print(Solve(a,n))


if __name__ == "__main__":
    solve()
