# cook your dish here
def get_dp(n: int, a: list) -> list:
	lc, rc = [0] * n, [0] * n
	for i in range(n):
		for j in range(n // 2):
			if a[i][j] == "1":
				lc[i] += 1
			if a[i][n - 1 - j] == "1":
				rc[i] += 1
	return [i - j for i, j in zip(lc, rc)]


def solve(n: int, a: list) -> int:
	diff = get_dp(n, a)
	sd = sum(diff)
	asd = abs(sd)
	for d in diff:
		nsd = sd - 2 * d
		asd = min(asd, abs(nsd))
	return asd


t = int(input().strip())
for _ in range(t):
	n = int(input().strip())
	a = []
	for i in range(n):
		a.append(input().strip())
	print(solve(n, a))


if __name__ == "__main__":
    solve()
