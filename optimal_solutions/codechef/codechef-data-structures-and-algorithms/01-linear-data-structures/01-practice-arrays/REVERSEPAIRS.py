


def solve():
    class Solution:
        def merge(self, nums, low, mid, high):
            count = 0
            j = mid + 1

            # Count reverse pairs
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))

            # Merge step
            temp = []
            i, j = low, mid + 1

            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= high:
                temp.append(nums[j])
                j += 1

            # Copy back the sorted elements
            for k in range(low, high + 1):
                nums[k] = temp[k - low]

            return count

        def mergeSort(self, nums, low, high):
            if low >= high:
                return 0

            mid = low + (high - low) // 2
            count = 0

            count += self.mergeSort(nums, low, mid)
            count += self.mergeSort(nums, mid + 1, high)
            count += self.merge(nums, low, mid, high)

            return count

        def reversePairs(self, nums):
            return self.mergeSort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    solve()
