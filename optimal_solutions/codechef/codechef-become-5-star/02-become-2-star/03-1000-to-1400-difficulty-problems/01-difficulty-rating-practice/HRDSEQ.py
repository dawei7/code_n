# cook your dish here


def solve():
    def innum():
        return int(input())

    dic = {}

    A = []
    A.append(0)
    dic[0] = [0]
    N = 1


    for i in range(1,128):
        l = A[N-1]
        n = len(dic[l])
        if n == 1:
            A.append(0)
            dic[0].append(i)
        else:
            dif = dic[l][n-1]-dic[l][n-2]
            A.append(dif)
            if dif not in dic:
                dic[dif] = [i]
            else:
                dic[dif].append(i)
        N += 1

    for T in range(innum()):

        N = innum()
        num = A[N-1]
        res = 0
        for i in range(0,N):
            res += (A[i] == num)

        print(res)


if __name__ == "__main__":
    solve()
