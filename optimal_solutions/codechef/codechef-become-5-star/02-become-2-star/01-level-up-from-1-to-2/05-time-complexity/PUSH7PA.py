


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        hf = {}
        maximum_sum = 0

        for num in a:
            if num not in hf:
                hf[num] = 1
            else:
                hf[num] += 1

        for key, value in hf.items():
            maximum_sum = max(maximum_sum, key + value - 1)

        print(maximum_sum)


if __name__ == "__main__":
    solve()
