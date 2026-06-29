


def solve():
    def calculate_modulo(curr, req):
        m1 = curr % 3
        m2 = req % 3
        if m1 == m2:
            return 0
        if m1 < m2:
            return m2 - m1
        return m2 + (3 - m1)

    def calculate_sum_modulo(a):
        ans = 0
        for i in range(3, len(a)):
            ans += calculate_modulo(a[i], a[i - 3])
            a[i] = a[i - 3]
        return ans

    def find_solution():
        n = int(input())
        a = list(map(int, input().split()))

        X = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if (i + j + k) % 3 == 0:
                        X.append([i, j, k])

        result = float('inf')
        for vec in X:
            temp = vec.copy()
            temp.extend(a)
            result = min(result, calculate_sum_modulo(temp))

        print(result)

    if __name__ == "__main__":
        total_tests = int(input())
        for test_no in range(1, total_tests + 1):
            find_solution()


if __name__ == "__main__":
    solve()
