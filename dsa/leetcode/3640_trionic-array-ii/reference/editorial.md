### Approach: Grouped Loop

#### Intuition

The problem asks us to find a subarray with the maximum sum among all subarrays that consist of three segments. This can be solved in two main steps:

1. Identify subarrays that satisfy the **three-part** requirement.
2. Compute the sum of each such subarray and keep track of the maximum value.

For the first step, by examining the array $\textit{nums}$, we can reuse the idea from [Trionic Array I](https://leetcode.com/problems/trionic-array-i/description/) to identify subarrays that satisfy the **three-segment** pattern. Here, a subarray is considered **maximal** if it cannot be extended further to the left or right while preserving the **increasing–> decreasing–> increasing** structure.

Intuitively, once we identify a maximal three-segment subarray, the next possible three-segment subarray must start at the first element of the third segment of the current one. Based on this observation, we can use a grouped loop to enumerate all maximal three-segment subarrays in linear time.

For the second step, consider a maximal three-segment subarray. The entire second segment must always be included in the sum. Additionally, the second-to-last element of the first segment and the second element of the third segment must also be included. This forms a **minimal** three-segment subarray, where minimal means it cannot be further shortened from either side.

To maximize the sum, we then consider extending this minimal subarray. For the first segment, we compute the maximum cumulative sum from right to left, starting from the third element from the end. Similarly, for the third segment, we compute the maximum cumulative sum from left to right, starting from the third element. These two maximum values are added to the base sum. If either of these values is negative, we treat it as zero, meaning that no additional elements are included from that side.

#### Implementation

```python
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")
        i = 0

        while i < n:
            j = i + 1
            res = 0

            # first segment: increasing segment
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            p = j - 1

            if p == i:  # 没有有效的increasing segment
                i += 1
                continue

            # second segment: decreasing segment
            res += nums[p] + nums[p - 1]
            while j < n and nums[j - 1] > nums[j]:
                res += nums[j]
                j += 1
            q = j - 1

            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q
                continue

            # third segment: increasing segment
            res += nums[q + 1]

            # find the maximum sum of the third segment
            max_sum = 0
            curr_sum = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
                k += 1
            res += max_sum

            # find the maximum sum of the first segment
            max_sum = 0
            curr_sum = 0
            for k in range(p - 2, i - 1, -1):
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
            res += max_sum

            # update answer
            ans = max(ans, res)
            i = q

        return ans
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

---