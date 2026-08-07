## Description

You are given an integer array `capacity`, where $\text{capacity}[i]$ represents the capacity of the $$i^{\text{th}}$$ box, and an integer `itemSize` representing the size of an item.

The $$i^{\text{th}}$$box can store the item if$\text{capacity}[i] \ge itemSize$.

Return an integer denoting the index of the box with the **minimum** capacity that can store the item. If multiple such boxes exist, return the **smallest index**.

If no box can store the item, return -1.
### Function Contract

**Inputs**

- `capacity`: A nonempty array whose value at index `i` is the capacity of box
  `i`.
- `itemSize`: The minimum capacity a box needs in order to store the item.

Let $N = \lvert\texttt{capacity}\rvert$. An index `i` is eligible when
`capacity[i] >= itemSize`. Indexing is zero-based.

**Return value**

Return the smallest index among the eligible boxes having minimum capacity.
Return `-1` when no eligible box exists.

### Examples
#### Example 1

<div class="example-block">
**Input:** capacity = [1,5,3,7], itemSize = 3

**Output:** 2

**Explanation:**

The box at index 2 has a capacity of 3, which is the minimum capacity that can store the item. Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** capacity = [3,5,4,3], itemSize = 2

**Output:** 0

**Explanation:**

The minimum capacity that can store the item is 3, and it appears at indices 0 and 3. Thus, the answer is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** capacity = [4], itemSize = 5

**Output:** -1

**Explanation:**

No box has enough capacity to store the item, so the answer is -1.

</div>
### Constraints

- $1 \le \text{capacity.length} \le 100$

- $1 \le \text{capacity}[i] \le 100$

- $1 \le itemSize \le 100$