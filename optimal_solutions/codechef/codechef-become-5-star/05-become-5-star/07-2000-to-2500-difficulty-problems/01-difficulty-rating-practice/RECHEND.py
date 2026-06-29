# cook your dish here

# cook your dish here


def solve():
    t:int=int(input())
    while(t):
      t-=1
      n:int=int(input())
      b=[]
      for i in range(n):
      	pos=input().split()
      	pos[0],pos[1]=int(pos[0])-1,int(pos[1])-1
      	b.append(tuple(pos))
      b=sorted(b)
      pj=b[0][1]-1
      i=0
      flag=1
      edge=0
      while(True):
        i+=1
        if(pj!=b[i][1]):
            edge=1
        elif(pj==0):
            flag=0
            break
        pj-=1
        if(edge):
            i=n-1
            pj=b[n-1][1]+1
            while(True):
                i-=1
                if(pj!=b[i][1]):
                    break
                elif(pj==n-1):
                    flag=0
                    break
                pj+=1
            break
      if(flag):
          print("YES")
      else:
          print("NO")


if __name__ == "__main__":
    solve()
