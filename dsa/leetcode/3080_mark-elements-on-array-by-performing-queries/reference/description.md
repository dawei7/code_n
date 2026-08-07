### 1. Description

You are given a **0-indexed** array `nums` of size `n` consisting of positive integers.

You are also given a 2D array `queries` of size `m` where $\text{queries}[i] = [\text{index}_{i}, k_{i}]$.

Initially all elements of the array are **unmarked**.

You need to apply `m` queries on the array in order, where on the $$i^{\text{th}}$$ query you do the following:

- Mark the element at index $\text{index}_{i}$ if it is not already marked.

- Then mark $k_{i}$ unmarked elements in the array with the **smallest** values. If multiple such elements exist, mark the ones with the smallest indices. And if less than $k_{i}$ unmarked elements exist, then mark all of them.

Return *an array answer of size *`m`* where *$\text{answer}[i]$* is the **sum** of unmarked elements in the array after the *$$i^{\text{th}}$$* query*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]

**Output: **[8,3,0]

**Explanation:**

We do the following queries on the array:

- Mark the element at index `1`, and `2` of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are `nums = [**<u>1</u>**,<u>**2**</u>,2,<u>**1**</u>,2,3,1]`. The sum of unmarked elements is $2 + 2 + 3 + 1 = 8$.

- Mark the element at index `3`, since it is already marked we skip it. Then we mark `3` of the smallest unmarked elements with the smallest indices, the marked elements now are `nums = [**<u>1</u>**,<u>**2**</u>,<u>**2**</u>,<u>**1**</u>,<u>**2**</u>,3,**<u>1</u>**]`. The sum of unmarked elements is `3`.

- Mark the element at index `4`, since it is already marked we skip it. Then we mark `2` of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are `nums = [**<u>1</u>**,<u>**2**</u>,<u>**2**</u>,<u>**1**</u>,<u>**2**</u>,**<u>3</u>**,<u>**1**</u>]`. The sum of unmarked elements is `0`.

</div>
#### Example 2

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **nums = [1,4,2,3], queries = [[0,1]]

**Output: **[7]

**Explanation: ** We do one query which is mark the element at index `0` and mark the smallest element among unmarked elements. The marked elements will be `nums = [**<u>1</u>**,4,<u>**2**</u>,3]`, and the sum of unmarked elements is $4 + 3 = 7$.

</div>

### 4. Constraints

- $n = \text{nums.length}$

- $m = \text{queries.length}$

- $1 \le m \le n \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $\text{queries}[i].length = 2$

- $0 \le \text{index}_{i}, k_{i} \le n - 1$