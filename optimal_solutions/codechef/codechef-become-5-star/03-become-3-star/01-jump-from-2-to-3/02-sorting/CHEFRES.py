# cook your dish here

#from collections import deque,Counter
#from math import ceil, floor


def solve():
    def Binary_Search(lista, N, x):

        left = 0
        right = N - 1

        while left <= right:
            mid = (left + right) // 2
            if lista[mid] == x:
                return True, mid  # Found
            elif lista[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return False, left-1        # The left closest

    def innum():
        return int(input())
    def inmany():
        return map(int,input().split())
    def inlist():
        return list(inmany())

    for T in range(innum()):

        N,M = inmany()
        Open  = []
        Begin = set()
        End   = set()
        for i in range(N):
            b,e = inmany()
            Open.append(b)
            Open.append(e)
            Begin.add(b)
            End.add(e)
        Open.sort()

        for i in range(0,M):
            people = innum()
            ans,ind = Binary_Search(Open,2*N,people)

            if (ans) and (people in Begin):
                print(0)

            else:
                if ind == 2*N-1:
                    print(-1)
                elif (Open[ind] in Begin):
                    print(0)
                else:
                    newOpen = Open[ind+1]
                    print(newOpen-people)


if __name__ == "__main__":
    solve()
