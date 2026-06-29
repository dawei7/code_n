


def solve():
    for _ in range(int(input())):
        num_bar,height,y1,y2,l=map(int,input().split())
        counter=0
        for _2 in range(num_bar):
            t,x=map(int,input().split())
            if t==1:
                if (height-y1)>x:
                    l-=1
            else:
                if y2<x:
                    l-=1
            if l>=1:
                counter+=1
        print(counter)


if __name__ == "__main__":
    solve()
