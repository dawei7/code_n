


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        s = sum(arr)
        if s%n:
            print("No")
        else:
            need = 0
            avg = s // n
            for i in arr:
                if abs(avg-i)%2:
                    need = 1
                    break
                need += avg - i
            if need:
                print("No")
            else:
                print("Yes")


if __name__ == "__main__":
    solve()
