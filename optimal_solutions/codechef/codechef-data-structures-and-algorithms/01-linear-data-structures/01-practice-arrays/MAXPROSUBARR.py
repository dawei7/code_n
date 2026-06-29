


def solve():
    def maxProductSubarray(arr, n):
        if n == 0:
            return 0

        maxProd = to32(arr[0])
        currMax = to32(arr[0])
        currMin = to32(arr[0])

        for i in range(1, n):
            num = to32(arr[i])

            # Swap if number is negative
            if num < 0:
                currMax, currMin = currMin, currMax

            # Update current max/min in 32-bit
            currMax = to32(max(num, to32(currMax * num)))
            currMin = to32(min(num, to32(currMin * num)))

            # Update overall max
            maxProd = to32(max(maxProd, currMax))

        return maxProd


if __name__ == "__main__":
    solve()
