


def solve():
    cases = int(input())

    stack = list()

    for _ in range(cases):
        a = list(map(int, input().split()))
        if a[0] == -1:
            if len(stack) == 0:
                print("kuchbhi?")
            else:
                print(stack.pop())
        else:
            stack.append(a[1])


if __name__ == "__main__":
    solve()
