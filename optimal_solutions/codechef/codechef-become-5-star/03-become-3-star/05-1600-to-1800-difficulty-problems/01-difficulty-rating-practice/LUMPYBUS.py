


def solve():
    def ans(A, P, Q):
        A.sort()
        result = 0
        for a in A:
            if 2*Q + P >= a:
                q_cons = min(Q, a // 2)
                p_cons = min(P, a - 2*q_cons)
                if P > 0 or a % 2 == 0:
                    Q -= q_cons
                    P -= p_cons
                    result += 1
            else:
                break

        return result


    if __name__ == '__main__':
        T = int(input().rstrip())
        for i in range(0, T):
            [_, P, Q] = list(map(int, input().rstrip().split(' ')))
            A = list(map(int, input().rstrip().split(' ')))
            print(ans(A, P, Q))


if __name__ == "__main__":
    solve()
