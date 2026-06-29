


def solve():
    for _ in range(int(input())):
        num_cats,num_cans=map(int,input().split())
        feed_seq=list(map(int,input().split()))
        cat_arr=[0]*num_cats
        for cat_num in feed_seq:
            cat_arr[cat_num-1]+=1
            if (cat_arr[cat_num-1]-2) in cat_arr:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    solve()
