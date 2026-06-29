


def solve():
    for _ in range(int(input())):
        len_arr=int(input())
        arr=list(map(int,input().split()))
        max_val=max(min(arr)**2,max(arr)**2)
        neg_arr=[]
        pos_arr=[]
        min_val1=min_val2=min_val3=10**18+1
        for val in arr:
            if val<0:
                neg_arr.append(val)
            else:
                pos_arr.append(val)
        if len(pos_arr)>0:
            min_val1=min(pos_arr)**2
        if len(neg_arr)>0:
            min_val2=max(neg_arr)**2
        if (len(pos_arr)>0) and (len(neg_arr)>0):
            min_val3=max(pos_arr)*min(neg_arr)
        min_val=min(min_val1,min_val2,min_val3)
        print(min_val,max_val)


if __name__ == "__main__":
    solve()
