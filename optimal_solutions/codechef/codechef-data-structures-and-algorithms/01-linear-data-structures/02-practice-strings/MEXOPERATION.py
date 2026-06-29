


def solve():
    def find_max_mex(nums, value):
        freq = [0] * value
        for num in nums:
            rem = num % value
            if rem < 0:
                rem += value
            freq[rem] += 1

        mex = 0
        while True:
            rem = mex % value
            if freq[rem] > 0:
                freq[rem] -= 1
                mex += 1
            else:
                break
        return mex


if __name__ == "__main__":
    solve()
