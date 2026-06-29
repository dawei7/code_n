# cook your dish here


def solve():
    T = int(input())
    for tc in range(T):
    	(n, x) = map(int, input().split(' '))

    	pizza = n * x // 4

    	if n*x % 4 == 0:
    	    print(pizza)
    	else:
    	    print(pizza+1)


if __name__ == "__main__":
    solve()
