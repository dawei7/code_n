# cook your dish here


def solve():
    T = int(input())
    for tc in range(T):
        # x=Chef , Y=Chefina, K=Move per step
        (x, y, k) = map(int, input().split(' '))

        diff = abs(y - x)
        move = diff // k 
        if diff%k > 0:
            move += 1 
        print(move)


if __name__ == "__main__":
    solve()
