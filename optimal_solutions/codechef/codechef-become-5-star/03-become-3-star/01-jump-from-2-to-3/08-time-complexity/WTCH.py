


def solve():
    t = int(input())

    while t > 0:

        n = int(input())
        s = input()

        c = 0
        i = 0
        while i < len(s)-1:

            if s[i] == '0' and s[i+1] == '0':
                s = s[:i]+'1'+s[i+1:]
                # print(s)
                i += 1
                c += 1

            elif s[i] == '1':
                i += 1
            i += 1

        if s[n-2] == '0' and s[n-1] == '0':
            c += 1


        print(c)


        t -= 1


if __name__ == "__main__":
    solve()
