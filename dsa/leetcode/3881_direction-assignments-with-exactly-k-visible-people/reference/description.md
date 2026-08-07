### 1. Description

You are given three integers `n`, `pos`, and `k`.

There are `n` people standing in a line indexed from 0 to $n - 1$. Each person **independently** chooses a direction:

- `'L'`: **visible** only to people on their **right**

- `'R'`: **visible** only to people on their **left**

A person at index `pos` sees others as follows:

- A person `i < pos` is visible if and only if they choose `'L'`.

- A person `i > pos` is visible if and only if they choose `'R'`.

Return the number of possible direction assignments such that the person at index `pos` sees **exactly** `k` people.

Since the answer may be large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `n`: The number of people in the indexed line.
- `pos`: The index of the fixed observer.
- `k`: The exact number of other people who must be visible to that observer.

Every person chooses one of the two directions independently. The observer's own direction does not change whom that observer sees.

Let $m=n-1$ be the number of people other than the observer, and let $P=$10^{9}$+7$.

**Return value**

Return the number of complete `L`/`R` assignments that make exactly `k` of those $m$ people visible, reduced modulo $P$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, pos = 1, k = 0

**Output:** 2

**Explanation:**​​​​​​​

- Index 0 is to the left of $pos = 1$, and index 2 is to the right of $pos = 1$.

- To see $k = 0$ people, index 0 must choose `'R'` and index 2 must choose `'L'`, keeping both invisible.

- The person at index 1 can choose `'L'` or `'R'` since it does not affect the count. Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, pos = 2, k = 1

**Output:** 4

**Explanation:**

- Index 0 and index 1 are left of $pos = 2$, and there is no index to the right.

- To see $k = 1$ person, exactly one of index 0 or index 1 must choose `'L'`, and the other must choose `'R'`.

- There are 2 ways to choose which index is visible from the left.

- The person at index 2 can choose `'L'` or `'R'` since it does not affect the count. Thus, the answer is $2 + 2 = 4$.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 1, pos = 0, k = 0

**Output:** 2

**Explanation:**

- There are no indices to the left or right of $pos = 0$.

- To see $k = 0$ people, no additional condition is required.

- The person at index 0 can choose `'L'` or `'R'`. Thus, the answer is 2.

</div>

### 4. Constraints

- $1 \le n \le 10^{5}$

- $0 \le pos, k \le n - 1$