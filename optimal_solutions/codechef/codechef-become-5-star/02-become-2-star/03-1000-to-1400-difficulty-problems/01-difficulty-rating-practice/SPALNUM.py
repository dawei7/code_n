


def solve():
    T = int(input())
    for i in range(T):
        L, R = map(int, input().split())
        P = []
        for j in range(1, 10):
            P.append(j) 
        for j in range(11, 110, 11):
            P.append(j)
        for j in range(101, 201, 10):
            P.append(j)
        for j in range(202, 302, 10):
            P.append(j) 
        for j in range(303, 403, 10):
            P.append(j) 
        for j in range(404, 504, 10):
            P.append(j) 
        for j in range(505, 605, 10):
            P.append(j) 
        for j in range(606, 706, 10):
            P.append(j) 
        for j in range(707, 807, 10):
            P.append(j) 
        for j in range(808, 908, 10):
            P.append(j) 
        for j in range(909, 1009, 10):
            P.append(j) 
        for j in range(1001, 2101, 110):
            P.append(j) 
        for j in range(2002, 3102, 110):
            P.append(j) 
        for j in range(3003, 4103, 110):
            P.append(j) 
        for j in range(4004, 5104, 110):
            P.append(j) 
        for j in range(5005, 6105, 110):
            P.append(j) 
        for j in range(6006, 7106, 110):
            P.append(j) 
        for j in range(7007, 8107, 110):
            P.append(j) 
        for j in range(8008, 9108, 110):
            P.append(j) 
        for j in range(9009, 10109, 110):
            P.append(j) 
        for k in range(10, 100):
            for l in range(0, 10):
                K = str(k)
                P.append(int((K) + str(l) + K[1] + K[0]))
        S = []
        for pali in P:
            if pali >= L and pali <= R:
                S.append(pali)
        print(sum(S))


if __name__ == "__main__":
    solve()
