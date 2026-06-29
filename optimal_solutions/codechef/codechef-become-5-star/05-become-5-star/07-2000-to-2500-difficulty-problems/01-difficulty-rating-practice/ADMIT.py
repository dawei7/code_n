# cook your dish 
# cook your dish here


def solve():
    n=int(input())
    for i in range(n):
        X, P = map(int,input().split())
        cRank = list(map(int,input().split()))
        sRank = list(map(int,input().split()))
        student =[]
        for i in range(P):
            c = list(map(int, input().split()))
            d = sorted(c[1:], key=lambda x: cRank[x-1])
            student.append([i, c[0], d])
        sort_student = sorted(student, key= lambda x: sRank[x[0]])
        clgs_filed = [False] * X
        choice = 0
        for i in sort_student:
            ch = 0
            for j in i[2]:
                if(clgs_filed[j-1] == False):
                    clgs_filed[j-1] = True
                    ch = j
                    break
            if(i[0] == 0):
                choice = ch
                break
        print(choice)


if __name__ == "__main__":
    solve()
