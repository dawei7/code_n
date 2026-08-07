### Approach 1: Simulation

#### Intuition

We can directly simulate the process described in the problem statement since the data range is very small.

Repeat the above process until the non-strictly increasing condition is satisfied or the length of $\textit{nums}$ becomes $1$. If the condition is not met, update the array by merging adjacent pairs into a new element. Repeat the above process until the non-strictly increasing condition is satisfied or the length of $\textit{nums}$ becomes $1$.

#### Implementation

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0

        while len(nums) > 1:
            isAscending = True
            minSum = float("inf")
            targetIndex = -1

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]

                if nums[i] > nums[i + 1]:
                    isAscending = False

                if pair_sum < minSum:
                    minSum = pair_sum
                    targetIndex = i

            if isAscending:
                break

            count += 1
            nums[targetIndex] = minSum
            nums.pop(targetIndex + 1)

        return count
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n^2)$.

  Merging pairs can be done at most $n$ times; checking monotonicity, finding adjacent pairs, and removing elements from the array all take $O(n)$ time, resulting in an overall time complexity of $O(n^2)$.

- Space complexity: $O(1)$.

  Only a few variables are used.

### Approach 2: Simulation + Array Simulation of Linked List

#### Intuition

In addition to directly removing elements from the array, we can also adopt the idea of simulating a linked list to support $O(1)$ deletion operations. Consider maintaining a $\textit{next}$ array, which represents the position of the next element for each index $i$. Since both checking monotonicity and finding the minimum sum of adjacent pairs require sequential traversal of the linear structure, the traversal logic is essentially the same as in Approach 1. The only difference is that during deletion, we update the $\textit{next}$ array so that the target element points directly to the element after its adjacent neighbor.

#### Implementation

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        next_node = list(range(1, len(nums) + 1))
        next_node[-1] = None
        count = 0

        while len(nums) - count > 1:
            curr = 0
            target = 0
            target_adj_sum = nums[target] + nums[next_node[target]]
            is_ascending = True

            while curr is not None and next_node[curr] is not None:
                if nums[curr] > nums[next_node[curr]]:
                    is_ascending = False

                curr_adj_sum = nums[curr] + nums[next_node[curr]]
                if curr_adj_sum < target_adj_sum:
                    target = curr
                    target_adj_sum = curr_adj_sum

                curr = next_node[curr]

            if is_ascending:
                break

            count += 1
            next_node[target] = next_node[next_node[target]]
            nums[target] = target_adj_sum

        return count
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n^2)$.

  The specific analysis is the same as Approach 1, except that the deletion operation can now be completed in $O(1)$.

- Space complexity: $O(n)$.

  The $\textit{next}$ array requires $O(n)$ auxiliary space.

---