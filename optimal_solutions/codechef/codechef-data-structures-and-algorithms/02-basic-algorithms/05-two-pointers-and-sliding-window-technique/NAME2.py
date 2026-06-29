# cook your dish here


def solve():
    def checkSub(m , w):

        l1 = len(m)
        l2 = len(w)
        i = 0
        j = 0 

        while i < l1 and j < l2:
            if m[i] == w[j]:
                i+=1 
                j+=1 
            else:
                j+=1 #j is ptr => str

        if i == l1:
            return True 
        return False
    t = int(input())
    for _ in range(t):
        m , w = input().split()

        if checkSub(m, w) or checkSub(w , m):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    solve()
