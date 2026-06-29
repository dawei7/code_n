


def solve():
    MOD = 1000000007

    def compute_sum_of_squares(arr):
        total_sum = 0
        for num in arr:
            total_sum = (total_sum + (num * num) % MOD) % MOD
        return total_sum

    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr = [num % MOD for num in arr]
        result = compute_sum_of_squares(arr)
        print(result)


if __name__ == "__main__":
    solve()
