


def solve():
    T = int(input())
    for i in range(T):
        user_input = input().split()
        L = int(user_input[0])
        R = int(user_input[1])

        L = 2*L
        R = 2*R

        print(R-L+1)


if __name__ == "__main__":
    solve()
