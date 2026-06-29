# cook your dish here


def solve():
    for __ in range(int(input())):
        n, k = map(int, input().split())
        l = sorted(list(map(int, input().split())))
        total_sum, i = 0, 0

        while i < n:
            if k > 0 and l[i] < 0:
                total_sum += l[i] * -1
                k -= 1
            elif l[i] > 0: total_sum += l[i]
            i += 1

        print(total_sum)


if __name__ == "__main__":
    solve()
