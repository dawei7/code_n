### 1. Description

You are given an integer array `nums` of length `n` and a 2D array `queries` where $\text{queries}[i] = [l_{i}, r_{i}]$.

Each $\text{queries}[i]$ represents the following action on `nums`:

- Decrement the value at each index in the range $[l_{i}, r_{i}]$ in `nums` by **at most**** **1.

- The amount by which the value is decremented can be chosen **independently** for each index.

A **Zero Array** is an array with all its elements equal to 0.

Return the **maximum **number of elements that can be removed from `queries`, such that `nums` can still be converted to a **zero array** using the *remaining* queries. If it is not possible to convert `nums` to a **zero array**, return -1.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

**Output:** 1

**Explanation:**

After removing $\text{queries}[2]$, `nums` can still be converted to a zero array.

- Using $\text{queries}[0]$, decrement $\text{nums}[0]$ and $\text{nums}[2]$ by 1 and $\text{nums}[1]$ by 0.

- Using $\text{queries}[1]$, decrement $\text{nums}[0]$ and $\text{nums}[2]$ by 1 and $\text{nums}[1]$ by 0.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

**Output:** 2

**Explanation:**

We can remove $\text{queries}[2]$ and $\text{queries}[3]$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3,4], queries = [[0,3]]

**Output:** -1

**Explanation:**

`nums` cannot be converted to a zero array even after using all the queries.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{5}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 2$

- $0 \le l_{i} \le r_{i} < \text{nums.length}$