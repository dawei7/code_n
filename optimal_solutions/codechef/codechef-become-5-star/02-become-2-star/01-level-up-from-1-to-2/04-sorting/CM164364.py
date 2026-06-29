# cook your dish here


def solve():
    for _ in range(int(input())):
        num_choc, bro = map(int, input().split())
        havable = num_choc - bro
        lit = set(map(int, input().split()))

        print(min((len(lit)), havable))


if __name__ == "__main__":
    solve()
