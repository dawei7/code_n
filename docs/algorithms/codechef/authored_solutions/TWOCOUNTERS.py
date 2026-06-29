inf = 10**9
for _ in range(int(input())):
	n, m = map(int, input().split())
	times = list(map(int, input().split()))
	types = list(map(int, input().split()))
	dp = [[-inf, -inf, -inf, -inf, -inf] for _ in range(n+2)]
	dp[0][2] = 0
	ptr = 0
	for i in range(1, n+1):
		for dif in range(5):
			if dif > 0: dp[i][dif] = max(dp[i][dif], dp[i-1][dif-1])
			if dif < 4: dp[i][dif] = max(dp[i][dif], dp[i-1][dif+1])
		if ptr < m and times[ptr] == i:
			if types[ptr] == 1:
				dp[i][4] += 1
				dp[i][3] += 1
				dp[i][2] = max(dp[i][:3])
				dp[i][0] = -inf
				dp[i][1] = -inf
			else:
				dp[i][0] += 1
				dp[i][1] += 1
				dp[i][2] = max(dp[i][2:])
				dp[i][3] = -inf
				dp[i][4] = -inf
			ptr += 1
	print(max(dp[n]))
