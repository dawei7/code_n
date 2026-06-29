


def solve():
    s = input()
    known_chars = set(s) 
    t = int(input()) 

    for _ in range(t):
        word = input() 
        can_read = True

        for ch in word:
            if ch not in known_chars:
                can_read = False
                break

        if can_read:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
