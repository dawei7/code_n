## Description

You are given an integer array `nums`.

Find the **minimum **length of a subarray that is **not** **identical** to any other **subarray** in `nums`.

Return an integer denoting the **minimum possible length** of such a **subarray**.

Two **subarrays** are considered identical if they have the same length and the same elements in corresponding positions.
### Function Contract

**Input**

- `nums`: A nonempty array of positive integers.

Let $n=\texttt{nums.length}$. Every nonempty interval of consecutive indices defines one subarray occurrence. Equal sequences at different start positions count as different occurrences, including when their index intervals overlap.

**Return value**

Return the minimum length of a subarray sequence that occurs exactly once in `nums`.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [3,3,3]

**Output:** 3

**Explanation:**

- Subarrays of length 1: `[3]` → appears 3 times

- Subarrays of length 2: `[3, 3]` → appears 2 times

- Subarrays of length 3: `[3, 3, 3]` → appears once

The subarray `[3, 3, 3]` is unique, so the smallest unique subarray length is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,1,2,3,3]

**Output:** 1

**Explanation:**

Subarrays of length 1:

- `[2]` → appears 2 times

- `[1]` → appears once

- `[3]` → appears 2 times

The subarray `[1]` is unique, so the smallest unique subarray length is 1.</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,1,2,2,1]

**Output:** 2

**Explanation:**

Subarrays of length 1:

- `[1]` → appears 3 times

- `[2]` → appears 2 times

Subarrays of length 2:

- `[1, 1]` → appears once

- `[1, 2]` → appears once

- `[2, 2]` → appears once

- `[2, 1]` → appears once

There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$