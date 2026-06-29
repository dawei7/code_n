


def solve():
    t = int(input())
    for i in range(t):
      a,b,c,d = list(map(int,input().split(' ')))
      e = (100+d)/100*a
      if (e>=b and e<=c):
        print("YES")
      else :
        print("NO")


if __name__ == "__main__":
    solve()
