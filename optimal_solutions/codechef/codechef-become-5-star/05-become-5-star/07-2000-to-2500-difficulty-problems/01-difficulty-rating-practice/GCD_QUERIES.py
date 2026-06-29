


def solve():
    maxn = 10**6 + 10
    prf = [0] * maxn
    for i in range(2, maxn):
    	if prf[i] > 0: continue
    	for j in range(i, maxn, i):
    		prf[j] = i

    for _ in range(int(input())):
    	n = int(input())
    	mapper = {}
    	id = 0
    	a = list(map(int, input().split()))
    	vals = [ ]
    	mark = [0]*n
    	for i in range(n):
    		x = a[i]
    		while x > 1:
    			p = prf[x]
    			if p not in mapper:
    				mapper[p] = id
    				vals.append([ ])
    				id += 1
    			vals[mapper[p]].append(i)

    			while x%p == 0: x //= p
    	for i in range(id):
    		vals[i].sort(key = lambda x: -a[x])

    	ord = list(range(n))
    	ord.sort(key= lambda x: -a[x])

    	q = int(input())
    	queries = list(map(int, input().split()))

    	for x in queries:
    		primes = []
    		while x > 1:
    			p = prf[x]
    			while x%p == 0: x //= p
    			primes.append(p)

    		choice = -1
    		for p in primes:
    			if p not in mapper: continue
    			loc = mapper[p]
    			while vals[loc]:
    				if mark[vals[loc][-1]]: vals[loc].pop()
    				else:
    					who = vals[loc][-1]
    					if choice == -1 or a[who] < a[choice]: choice = who
    					break
    		if choice == -1:
    			while mark[ord[-1]] == 1: ord.pop()
    			choice = ord[-1]

    		print(a[choice], end = ' ')
    		mark[choice] = 1


if __name__ == "__main__":
    solve()
