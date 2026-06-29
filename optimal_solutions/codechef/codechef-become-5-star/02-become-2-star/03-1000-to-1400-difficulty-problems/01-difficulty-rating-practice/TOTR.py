


def solve():
    t,byte=map(str,input().split())
    salpha="abcdefghijklmnopqrstuvwxyz"
    calpha=salpha.upper()
    for _ in range(int(t)):
        trans=""
        s=input().replace("_"," ")
        for i in s:
            if i.isalpha() and i.isupper():
                index=calpha.index(i)
                trans+=byte[index].upper()
            elif i.isalpha() and i.islower():
                index=salpha.index(i)
                trans+=byte[index]
            else:
                trans+=i
        print(trans)


if __name__ == "__main__":
    solve()
