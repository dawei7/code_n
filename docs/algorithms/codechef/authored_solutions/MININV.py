for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	pref_freq = [0]*(n+2)
	suf_freq = [0]*(n+2)
	for x in a: pref_freq[x] += 1
	ans = 0
	cur = 0
	for i in reversed(range(1, n)):
		cur -= pref_freq[a[i]] * suf_freq[a[i]-1] + pref_freq[a[i]+1] * suf_freq[a[i]]
		suf_freq[a[i]] += 1
		pref_freq[a[i]] -= 1
		cur += pref_freq[a[i]] * suf_freq[a[i]-1] + pref_freq[a[i]+1] * suf_freq[a[i]]
		ans = max(ans, cur)
	print(ans)
