# cook your dish here


def solve():
    for i in range(int(input())):
        a=int(input())
        s=input()
        if('I' in s):
            print('INDIAN')
        elif('Y' in s):
            print('NOT INDIAN')
        else:
            print('NOT SURE')


if __name__ == "__main__":
    solve()
