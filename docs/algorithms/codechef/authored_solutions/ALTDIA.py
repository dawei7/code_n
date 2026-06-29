for _ in range(int(input())):
	b, w = map(int, input().split())
	if b+w == 1:
		if b == 1:
			print('B')
		else:
			print('W')
	elif b == 0 or w == 0:
		print(-1)
	else:
		print('B'*b + 'W'*w)
		for i in range(1, b+w):
			if b == 1:
				print(1, i+1)
			else:
				print(i, b+w)
