


def solve():
    def f(x):
        return x % 999983

    for i in range(5):
        x = int(input())
        print(f"x = {x}, f(x) = {f(x)}")


if __name__ == "__main__":
    solve()
