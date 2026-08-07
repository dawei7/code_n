[TOC]

## Solution
---
### Approach 1: Two Arrays

**Intuition**

Instead of checking whether $all(L \le R for L in left for R in right)$, for each index let's only check whether the **largest element to the left** of the current index (inclusive) is less than or equal to the **smallest element to the right** of the current index ($max(left) \le min(right)$).

**Algorithm**

Let's try to find `max(left)` for subarrays $left = nums[:1], left = nums[:2], left = nums[:3], ...$ etc.  Specifically, $\text{max}_{left}[i]$ will be the maximum of subarray `nums[:i+1]`.  They are related to each other: $max(nums[:4]) = max(max(nums[:3]), \text{nums}[3])$, so $\text{max}_{left}[4] = max(\text{max}_{left}[3], \text{nums}[4])$.

Similarly, `min(right)` for every possible `right` can be found in linear time.

Now that we can query `max(left)` and `min(right)` in constant time by checking $\text{max}_{left}[i]$ and $\text{min}_{right}[i]$, we just need to iterate over $\text{max}_{left}$ and $\text{min}_{right}$ to find the first index where $\text{max}_{left}[i-1]$ is less than or equal to $\text{min}_{right}[i]$.

**Implementation**

```python
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        max_left = [None] * N
        min_right = [None] * N

        max_left[0] = nums[0]
        min_right[-1] = nums[-1]

        for i in range(1, N):
            max_left[i] = max(max_left[i - 1], nums[i])

        for i in range(N - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])

        for i in range(1, N):
            if max_left[i - 1] <= min_right[i]:
                return i
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `nums`. We iterate over the input array three times and create two arrays with size $N$ each.

* Space Complexity:  $O(N)$. We use two additional arrays of size $N$ each.

<br />

---

### Approach 2: One Array

**Intuition**

Notice, in the first approach, we iterated from `1` to `N` twice.  Once to create $\text{max}_{left}$ and once to find which index to split the array at.  We can slightly optimize our approach by performing both of these steps in the same for loop.  Doing so will allow us to replace the $\text{max}_{left}$ array with a single variable that tracks the maximum value seen so far ($\text{curr}_{max}$).

> How can we do this? Try to code it up yourself before looking at the solution below.

**Algorithm**

1. Initialize a $\text{min}_{right}$ array with the rightmost value equal to the rightmost value in nums.
2. Iterate over nums in reverse order and at each iteration update the current index of $\text{min}_{right}$ with the minimum value seen so far.
3. Initialize $\text{curr}_{max}$ as the leftmost value in nums.
4. Iterate over nums from left to right and at each iteration, update $\text{curr}_{max}$ as the maximum value seen so far.  When $\text{curr}_{max}$ is less than or equal to the minimum value to the right, then the current index is where `nums` should be split.

**Implementation**

```python
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        min_right = [None] * N
        min_right[-1] = nums[-1]

        for i in range(N - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])

        curr_max = nums[0]
        for i in range(1, N):
            curr_max = max(curr_max, nums[i - 1])
            if curr_max <= min_right[i]:
                return i
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `nums`. We iterate over the input array two times (instead of three times as in the previous approach) and create only one array with size $N$ (as opposed to two as before).

* Space Complexity:  $O(N)$. We use one additional array of size $N$.

<br />

---

### Approach 3: No Arrays

**Intuition**

For this approach, let's consider each number one at a time starting from the left. There are two possibilities for each number, it either **must** be part of the left array, or it **could** be part of the right array.  But how can we tell?

Since the left subarray cannot be empty, we know that it must contain $\text{nums}[0]$.  At the start, $\text{nums}[0]$ is the largest number that must be in the left subarray, let's call this $\text{curr}_{max}$. Since we are asked to split the array such that every number in the right subarray is greater than or equal to the largest number in the left subarray, we know that any number smaller than $\text{curr}_{max}$ must belong to the left subarray.

So let's say $\text{nums}[i]$ is less than $\text{nums}[0]$.  This means $\text{nums}[i]$ must be in the left subarray, and therefore every number to the left of $\text{nums}[i]$ must also belong to the left subarray.  Now, the largest number in `nums` between indices `0` and `i` will become the new $\text{curr}_{max}$ and any number less than $\text{curr}_{max}$ must be part of the left subarray.

As we iterate over `nums` we can keep track of the largest number seen so far that **must** be in the left subarray ($\text{curr}_{max}$) and the largest number seen so far that **could possibly** be in the left subarray ($\text{possible}_{max}$).  Whenever a number is less than $\text{curr}_{max}$ then that number and all of the numbers to its left must belong to the left subarray, and $\text{curr}_{max}$ becomes the largest number seen so far ($\text{possible}_{max}$).

This process can be repeated until we find the last number that **must** be part of the left subarray.

**Algorithm**

With this approach, we can further improve our algorithm's space complexity by getting rid of both arrays. We can achieve this by using three variables to track the maximum value that **must** be in the left subarray, the maximum value that **could possibly** be in the left subarray, and the length of the left subarray:
- $\text{curr}_{max}$ for tracking the maximum value that **must** be in the left part of the given array;
- $\text{possible}_{max}$ for tracking absolute maximum value in the already traversed part of the given array while iterating over it, so that we can extend our `left` part when necessary and update $\text{curr}_{max}$ with $\text{possible}_{max}$ value;
- `length` for storing the length of the left part (this will be our result).

The algorithm is as follows:

1. At first, we set $\text{curr}_{max}$ and $\text{possible}_{max}$ both equal to $\text{nums}[0]$ and `length` equal to 1 (since the left part of the given array cannot be empty, as stated in the problem description)
2. As we iterate over the input array, beginning from the first index (counting from 0), two possibilities exist at each step:
* If $\text{nums}[i]$ is less than $\text{curr}_{max}$, it means that, currently, **not every** element in `left` is less than or equal to every element in `right`, so our condition is violated. Therefore, we need to extend our `left` array, so that it includes all the values up to $\text{nums}[i]$ (inclusive). We update `length` accordingly and set $\text{curr}_{max}$ equal to $\text{possible}_{max}$ because now we know $\text{possible}_{max}$ must be part of the left subarray. We	must now compare every subsequent element starting from $nums[i + 1]$ with the maximum value seen so far.
* Otherwise, if $\text{nums}[i]$ is greater than or equal to $\text{curr}_{max}$, then it doesn't violate any of our conditions, and since we want the left part to be as small as possible, we do nothing except update the $\text{possible}_{max}$ value with $\text{nums}[i]$, if the latter is greater than current $\text{possible}_{max}$ value.
3. After the array traversal is completed, we return `length`.

**Implementation**

```python
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = nums[0]
        possible_max = nums[0]
        length = 1

        for i in range(1, len(nums)):
            if nums[i] < curr_max:
                length = i + 1
                curr_max = possible_max
            else:
                possible_max = max(possible_max, nums[i])

        return length
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `nums`. We iterate over the input array exactly once and each iteration requires only constant time.

* Space Complexity:  $O(1)$. We use only three variables, so the space usage here is constant.