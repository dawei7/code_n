# cook your dish here


def solve():
    for i in range(int(input())):
        p = input()

        dots = [len(i)+1 for i in p.split('#') if i]

        #count of days
        days = 0
        #maximum jump they practised
        jump = 1        #initial value

        for i in range(len(dots)):
            if jump < dots[i]:
                jump = dots[i]
                days+=1

        print(days)


if __name__ == "__main__":
    solve()
