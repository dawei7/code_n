


def solve():
    def sum_minus_smallest():
        t = int(input())
        for _ in range(t):
            n = int(input())
            v = list(map(int, input().split()))
            total_sum = sum(v)
            smallest_element = min(v)
            print(total_sum - smallest_element)

    sum_minus_smallest()


if __name__ == "__main__":
    solve()
