# cook your dish here


def solve():
    seat = int(input())
    for s in range(seat):
      S = int(input())
      if 1<=S<=15: 
        print("Lower", end=" ")
        if 1<=S<=10: 
          print("Double")
        else: 
          print("Single")
      if 16<=S<=30: 
        print("Upper", end=" ")
        if 16<=S<=25: 
          print("Double")
        else: 
          print("Single")


if __name__ == "__main__":
    solve()
