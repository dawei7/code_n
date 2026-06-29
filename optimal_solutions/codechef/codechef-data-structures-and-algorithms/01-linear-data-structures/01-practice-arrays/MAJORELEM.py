


def solve():
    class Solution:
        def majorityElement(self, arr):
            candidate = arr[0]
            count = 1

            for num in arr[1:]:
                if num == candidate:
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        candidate = num
                        count = 1
            return candidate  # Guaranteed to exist


if __name__ == "__main__":
    solve()
