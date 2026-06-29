# cook your dish here


def solve():
    school=int(input())
    for s in range(school):
      w=int(input())
      if w%7==6:print(w//7+1)
      else: print (w//7)


if __name__ == "__main__":
    solve()
