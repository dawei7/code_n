# cook your dish here


def solve():
    vaccine=int(input())
    for v in range(vaccine):
      D,L,R = map(int,input().split())
      if(D>=L and D<=R):print("Take second dose now")
      elif(D>R):print("Too Late")
      else:print("Too Early")


if __name__ == "__main__":
    solve()
