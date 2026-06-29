# cook your dish here


def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        chef_gold = 0.0
        chefu_gold = 0.0
        for _ in range(N):
            G, A, B = map(int, input().split())
            total = A + B
            chef_gold += G * B / total
            chefu_gold += G * A / total
        print(f"{chef_gold:.6f} {chefu_gold:.6f}")


if __name__ == "__main__":
    solve()
