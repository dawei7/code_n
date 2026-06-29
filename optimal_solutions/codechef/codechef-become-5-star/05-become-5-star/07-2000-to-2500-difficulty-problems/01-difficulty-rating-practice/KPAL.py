


def solve():
    for _ in range(int(input())):
    	n, k = map(int, input().split())
    	a = list(map(int, input().split()))
    	if n == k:
    		print('Yes' if a == a[::-1] else 'No')
    		continue
    	if n%2 == 1 or k%2 == 1:
    		print('Yes')
    		continue
    	print('Yes' if sum(a)%2 == 0 else 'No')


if __name__ == "__main__":
    solve()
