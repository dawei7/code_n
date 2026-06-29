


def solve():
    for _ in range(int(input())):
    	n, k = map(int, input().split())
    	freq = {}
    	for c in input():
    		if c in freq: freq[c] += 1
    		else: freq[c] = 1
    	if max(freq.values()) - min(freq.values()) > k:
    		print(-1)
    		continue
    	ans = ''
    	alpha = sorted(freq.keys())
    	for i in range(n):
    		for c in alpha:
    			if freq[c] == 0: continue
    			freq[c] -= 1
    			if max(freq.values()) - min(freq.values()) <= k:
    				ans += c
    				break
    			freq[c] += 1
    	print(ans)


if __name__ == "__main__":
    solve()
