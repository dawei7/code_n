# cook your dish here


def solve():
    for _ in range(int(input())):
        a,b,c = list(map(int, input().split()))
        answer = 1
        masks = 1 
        for _ in range(20):
            total = (a&masks !=0) + (b&masks != 0) + (c&masks != 0)
            if total == 1:
                print(0)
                break
            elif total == 3:
                answer *= 4
            masks <<= 1
        else:
            print(answer)


if __name__ == "__main__":
    solve()
