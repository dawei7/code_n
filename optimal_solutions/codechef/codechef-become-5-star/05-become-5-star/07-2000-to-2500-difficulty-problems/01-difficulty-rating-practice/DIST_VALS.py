# cook your dish here


def solve():
    for _ in range(int(input())):
    	n = int(input())
    	a = list(map(int, input().split()))
    	stack = []
    	prev_big = [-1]*n
    	next_big = [-1]*n
    	for i in range(n):
    		while len(stack) > 0:
    			if a[stack[-1]] < a[i]: stack.pop()
    			else: break
    		if len(stack) > 0: prev_big[i] = stack[-1]
    		stack.append(i)
    	stack = []
    	for i in reversed(range(n)):
    		while len(stack) > 0:
    			if a[stack[-1]] < a[i]: stack.pop()
    			else: break
    		if len(stack) > 0: next_big[i] = stack[-1]
    		stack.append(i)
    	difs = set()
    	for i in range(n):
    		if prev_big[i] != -1: difs.add(a[prev_big[i]] - a[i])
    		if next_big[i] != -1: difs.add(a[next_big[i]] - a[i])
    	print(len(difs))


if __name__ == "__main__":
    solve()
