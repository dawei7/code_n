# cook your dish here


def solve():
    T = int(input())
    for i in range(T):
        N = int(input())
        F = list(map(int, input().split()))
        initial_fuel=F[0]
        dist_travelled=0
        for _ in range(N-1):
          if initial_fuel>0:
            initial_fuel-=1 
            dist_travelled+=1
            initial_fuel+=F[dist_travelled]
          else:
            break 
        print(dist_travelled+initial_fuel)


if __name__ == "__main__":
    solve()
