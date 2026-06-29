


def solve():
    def totalSubarrays(arr, N, K):
        ans = 0
        i = 0

        while i < N:
            if arr[i] > K:
                i += 1
                continue

            count = 0
            while i < N and arr[i] <= K:
                i += 1
                count += 1

            ans += (count * (count + 1)) // 2

        return ans

    def countSubarrays(arr, N, K):
        count1 = totalSubarrays(arr, N, K - 1)
        count2 = totalSubarrays(arr, N, K)
        ans = count2 - count1
        return ans

    if __name__ == "__main__":
        N, K = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(countSubarrays(arr, N, K))


if __name__ == "__main__":
    solve()
