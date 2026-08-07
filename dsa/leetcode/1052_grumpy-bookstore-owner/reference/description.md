### 1. Description

There is a bookstore owner that has a store open for `n` minutes. You are given an integer array `customers` of length `n` where $\text{customers}[i]$ is the number of the customers that enter the store at the start of the $$i^{\text{th}}$$ minute and all those customers leave after the end of that minute.

During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where $\text{grumpy}[i]$ is `1` if the bookstore owner is grumpy during the $$i^{\text{th}}$$ minute, and is `0` otherwise.

When the bookstore owner is grumpy, the customers entering during that minute are not **satisfied**. Otherwise, they are satisfied.

The bookstore owner knows a secret technique to remain **not grumpy** for `minutes` consecutive minutes, but this technique can only be used **once**.

Return the **maximum** number of customers that can be *satisfied* throughout the day.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

**Output:** 16

**Explanation:**

The bookstore owner keeps themselves not grumpy for the last 3 minutes.

The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

</div>
#### Example 2

<div class="example-block">
**Input:** customers = [1], grumpy = [0], minutes = 1

**Output:** 1

</div>

### 4. Constraints

- $n = \text{customers.length} = \text{grumpy.length}$

- $1 \le minutes \le n \le 2 * 10^{4}$

- $0 \le \text{customers}[i] \le 1000$

- $\text{grumpy}[i]$ is either `0` or `1`.