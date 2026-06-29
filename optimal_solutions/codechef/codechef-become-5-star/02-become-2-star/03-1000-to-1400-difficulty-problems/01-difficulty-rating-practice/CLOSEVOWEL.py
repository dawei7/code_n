import math


def solve():
    t = int(input())
    for i in range(0,t):
        N = int(input())
        S = input()
        count = 0
        coun = 0
        for j in range(N):
            if(S[j] == 'c'):
                count += 1
            if(S[j] == 'g'):
                count += 1
            if(S[j] == 'l'):
                count += 1
            if(S[j] == 'r'):
                count += 1
        for j in range(N):
            if(S[j] == 'a'):
                coun += 1
            if(S[j] == 'e'):
                coun += 1
            if(S[j] == 'i'):
                coun += 1
            if(S[j] == 'o'):
                coun += 1
            if(S[j] == 'u'):
                coun += 1
        if(coun == N):
            print(1)
        elif(coun != N and count == 0):
            print(1)
        else:
            low = pow(2,count)
            print(low%1000000007)


if __name__ == "__main__":
    solve()
