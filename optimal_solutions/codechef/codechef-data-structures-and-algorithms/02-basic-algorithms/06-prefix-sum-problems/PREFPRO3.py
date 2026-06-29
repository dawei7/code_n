


def solve():
    class Solution:
        def count_subarrays_with_sum_k(self, arr, k):
            n = len(arr)
            pre = [0] * n

            for i in range(n):
                pre[i] = arr[i]
                if i != 0:
                    pre[i] += pre[i - 1]

            fans = 0
            for i in range(n):
                for j in range(i, n):
                    if i == 0:
                        if pre[j] == k:
                            fans += 1
                    elif pre[j] - pre[i - 1] == k:
                        fans += 1

            return fans


if __name__ == "__main__":
    solve()
