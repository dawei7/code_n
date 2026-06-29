# cook your dish here


def solve():
    def count_pairs(matrix,i):
        count=0
        for x in matrix:
            if x[i]=='1':
                count+=1
        return count
    def count_collision(x):
        y=x*(x-1)//2
        return y

    for _ in range(int(input())):
        n,m=map(int,input().split())
        matrix = []
        for i in range(n):
            s=input()
            matrix.append(list(s))
        sum1=0
        for j in range(m):
            d=count_pairs(matrix,j)
            z=count_collision(d)
            sum1+=z
        print(sum1)


if __name__ == "__main__":
    solve()
