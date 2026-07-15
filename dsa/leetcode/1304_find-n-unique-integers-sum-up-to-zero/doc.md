# Find N Unique Integers Sum up to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1304 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) |

## Problem Description
### Goal
Given a positive integer `n`, construct an array containing exactly `n` integers. Every returned integer must be unique, and the sum of all returned values must equal zero.

Any array satisfying those properties is valid; the values do not need to appear in a prescribed order or match one particular example. Return one such construction.

The contract therefore judges the length, distinctness, and total of the returned values, not a particular arrangement.

### Function Contract
**Inputs**

- `n`: the required array length, where $1 \le n \le 1000$.

**Return value**

Any integer array `result` satisfying $\lvert\texttt{result}\rvert=n$, containing $n$ distinct values, and obeying

$$
\sum_{x \in \texttt{result}} x=0.
$$

### Examples
**Example 1**

- Input: `n = 5`
- Output: `[-2,-1,0,1,2]`
- Explanation: The five values are distinct and sum to zero; many other answers are also valid.

**Example 2**

- Input: `n = 3`
- Output: `[-1,0,1]`

**Example 3**

- Input: `n = 1`
- Output: `[0]`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Build canceling pairs**

For every positive integer $v$ from 1 through $\lfloor n/2\rfloor$, append both $v$ and $-v$. The two values are distinct, and their contribution to the total is $v+(-v)=0$. Different magnitudes produce no duplicates across pairs.

When $n$ is even, these pairs already provide exactly $n$ values. When $n$ is odd, append 0 after the pairs. Zero is different from every nonzero paired value and does not change the sum.

Thus the construction always has the requested length, every value is unique, and the complete sum is zero. Because the contract accepts any valid construction, the semantic validator checks these properties rather than comparing the returned array to one fixed ordering.

#### Complexity detail

Creating and returning $n$ integers takes $O(n)$ time. The result array occupies $O(n)$ space; aside from that required output, the construction uses only constant loop state.

#### Alternatives and edge cases

- **Arithmetic sequence plus balancing value:** Returning `1, 2, ..., n - 1` and their negated sum is also valid, though its magnitudes grow quadratically with $n$.
- **Repeated membership checks:** Searching the partial list before adding each symmetric value preserves correctness but can take $O(n^2)$ time.
- **`n = 1`:** The only one-element zero-sum array is `[0]`.
- **Odd length:** Include zero exactly once after all nonzero pairs.
- **Even length:** Use only positive-negative pairs; zero is unnecessary.
- **Output order:** Reordering a valid set does not change uniqueness or its sum and must remain accepted.

</details>
