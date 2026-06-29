for _ in range(int(input())):
	n = int(input())
	s = input()
	if n%2 == 1:
		print('NO')
	else:
		print('YES')
		dif = s.count('1') - s.count('0')
		curdif = 0
		for i in range(n):
			if s[i] == '0':
				curdif -= 1
			else:
				curdif += 1
			if 2*curdif == dif:
				print(1, i+1)
				break
