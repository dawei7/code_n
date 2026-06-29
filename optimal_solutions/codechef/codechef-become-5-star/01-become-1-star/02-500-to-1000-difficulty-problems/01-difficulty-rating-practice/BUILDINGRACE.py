# cook your dish here


def solve():
    T=int(input())
    for i in range(T):
        A,B,X,Y=map(int,input().split())
        if(A/X<B/Y):
             print("Chef")
        elif(A/X>B/Y):
             print("Chefina")
        else:
             print("Both")


if __name__ == "__main__":
    solve()
