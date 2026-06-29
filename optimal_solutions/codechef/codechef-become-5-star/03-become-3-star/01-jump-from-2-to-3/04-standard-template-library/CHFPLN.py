# max ways of dividing a no. n without 0 is n-1
# i.e. (1,n-1) (2,n-2) ... (n-1,1)
# eg. 3 : (1,2) (2,1)


def solve():
    def chk():
        n = int(input())
        l = list(map(int, input().split()))
        c = 0 # max distinct points
        d = {} # dictionary : key = element; value = frequency;
        for char in l:
          if char in d:
            d[char] += 1 
          else:
            d[char] = 1
        for i in d:
          if d[i]>i-1:
            c+=i-1
          else:
            c+=d[i]
        print(c)

    t = int(input())
    while t:
        t -= 1
        chk()


if __name__ == "__main__":
    solve()
