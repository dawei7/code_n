# cook your dish here


def solve():
    testcase_no=int(input())
    for testcases in range(testcase_no):
        n = int(input())
        s=input()
        # x = map(int,input().split())
        # a = list(map(int,input().split()))
        odd=0
        eve=0
        for i in range(n):
            if s[i]=='1':
                if i%2==0:
                    eve+=1
                else:
                    odd+=1
        if eve>0 and odd>0:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    solve()
