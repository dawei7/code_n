# cook your dish here
# cook your dish here


def solve():
    T = int(input())

    for _ in range(T):
        N, A, B = map(int, input().split())
        sarthak_score = 0
        anuradha_score = 0
        EQUINOX_SET = set("EQUINOX")

        for _ in range(N):
            word = input().strip()
            if word[0] in EQUINOX_SET:
                sarthak_score += A
            else:
                anuradha_score += B

        if sarthak_score > anuradha_score:
            print("SARTHAK")
        elif anuradha_score > sarthak_score:
            print("ANURADHA")
        else:
            print("DRAW")


if __name__ == "__main__":
    solve()
