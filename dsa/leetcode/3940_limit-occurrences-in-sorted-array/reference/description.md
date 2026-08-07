### 1. Description

You are given a **sorted** integer array `nums` and an integer `k`.

Return an array such that each **distinct** element appears **at most** `k` times, while preserving the relative order of the elements in `nums`.

Note: If a distinct element appears **at least** `k` times, then it must appear **exactly** `k` times in the resulting array.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty list of integers sorted in non-decreasing order.
- `k`: The positive maximum number of copies to retain for each distinct value.

**Return value**

Return a list containing the elements of `nums` in their original relative order, with each distinct value occurring `min(frequency, k)` times.

The app-local function may resize and return `nums` itself. The returned list is judged by its values; internal capacity and discarded elements beyond its new logical length are irrelevant.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,1,2,2,3]

**Explanation:**

Each element can appear at most 2 times.

- The element 1 appears 3 times, so only 2 occurrences are kept.

- The element 2 appears 2 times, so both occurrences are kept.

- The element 3 appears 1 time, so it is kept.

Thus, the resulting array is `[1, 1, 2, 2, 3]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3], k = 1

**Output:** [1,2,3]

**Explanation:**

All elements are distinct and already appear at most once, so the array remains unchanged.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$

- `nums` is sorted in non-decreasing order.

- $1 \le k \le \text{nums.length}$

### 5. Follow-up

- Can you solve this in-place using $\mathcal{O}(1)$ extra space?

- Note that the space used for returning or resizing the result does not count toward the space complexity mentioned above, as some languages do not support in-place resizing.