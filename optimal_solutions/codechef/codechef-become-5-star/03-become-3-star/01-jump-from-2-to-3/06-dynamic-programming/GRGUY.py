


def solve():
    for i in range(int(input())):
        lane1=input()
        lane2=input()
        size=len(lane2)
        flag=0
        flag1=1
        count=0
        for i in range(size):
            if(lane1[i]=='#'):
                break
            elif(lane2[i]=='#'):
                flag=1
                break
        for i in range(size):
            if(lane1[i]=='#' and lane2[i]=='#'):
                print("No")
                flag1=0
                break
        if(flag1):
            print("Yes")
            for i in range(size):
                if(flag):
                    if(lane1[i]=='#'):
                        count+=1
                        flag=0
                else:
                    if(lane2[i]=='#'):
                        count+=1
                        flag=1
            print(count)


if __name__ == "__main__":
    solve()
