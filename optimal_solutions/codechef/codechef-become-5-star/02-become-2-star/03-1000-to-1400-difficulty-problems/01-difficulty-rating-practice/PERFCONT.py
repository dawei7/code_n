# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        arr = list(map(int, input().split()))
        hard_count = 0
        cakewalk_count = 0
        for x in arr:
            if x <= p//10:
                hard_count += 1
            elif x >= p//2:
                cakewalk_count += 1
        if  hard_count==2 and  cakewalk_count ==1:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    solve()
