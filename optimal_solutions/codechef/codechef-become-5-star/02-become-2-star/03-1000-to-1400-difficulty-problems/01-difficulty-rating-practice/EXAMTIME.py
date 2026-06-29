


def solve():
    for i in range(int(input())):
        dragon=list(map(int,input().strip().split()))
        sloth=list(map(int,input().strip().split()))
        if sum(dragon)>sum(sloth):
            print("dragon")
        elif sum(dragon)<sum(sloth):
            print("sloth")
        else:
            if dragon==sloth:
                print("tie")
            elif dragon[0]>sloth[0]:
                print("dragon")
            #elif dragon[1]>sloth[1]:
                    #print("dragon")
            elif dragon[0]<sloth[0]:
                print("sloth")
            elif dragon[0]==sloth[0]:
                if dragon[1]<sloth[1]:
                    print("sloth")
                if dragon[1]>sloth[1]:
                    print("dragon")


if __name__ == "__main__":
    solve()
