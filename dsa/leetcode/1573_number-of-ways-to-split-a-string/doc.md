# Number of Ways to Split a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1573 |
| Difficulty | Medium |
| Topics | Math, String |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-split-a-string/) |

## Problem Description
### Goal

Given a binary string `s`, place two cuts between characters so that the string becomes three nonempty contiguous substrings. Different pairs of cut positions count as different splits.

The character order remains unchanged, the first cut must precede the second, and neither cut may leave an empty part. Zeros may occur anywhere in the three substrings and do not need to be distributed equally.

Count the splits for which all three substrings contain the same number of `1` characters. Two splits are distinct when either cut occupies a different gap, even if their one-counts are identical. Return the count modulo $1{,}000{,}000{,}007$.

### Function Contract
**Inputs**

- `s`: A binary string of length $N$, where $3 \le N \le 10^5$.

**Return value**

Return the number of pairs of cut positions that create three nonempty substrings with equal one-counts, modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `s = "10101"`
- Output: `4`

**Example 2**

- Input: `s = "1001"`
- Output: `0`

**Example 3**

- Input: `s = "0000"`
- Output: `3`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate impossible and all-zero totals**

Let $T$ be the total number of ones. If $T$ is not divisible by three, equal one-counts are impossible. If $T=0$, every nonempty three-part split works. There are $N-1$ gaps between characters, and choosing any two of them gives

$$
\binom{N-1}{2}=\frac{(N-1)(N-2)}{2}
$$

valid splits.

**Count choices in the two zero gaps**

Otherwise, each part must contain $q=T/3$ ones. The first cut must occur after the $q$-th one and before the $(q+1)$-st one. If those ones occur at indices $a$ and $b$, there are $b-a$ possible cut gaps, including every intervening zero placement.

Likewise, if the $(2q)$-th and $(2q+1)$-st ones occur at indices $c$ and $d$, the second cut has $d-c$ choices. The two choices are independent, so their product is the answer. A scan that records only these four boundary positions uses constant extra space.

Every valid split must cross those exact one-count boundaries, so it is represented by one choice from each gap. Conversely, any such pair gives exactly $q$ ones to all three nonempty parts. This establishes a bijection between valid splits and the product of gap sizes.

#### Complexity detail

Counting ones and locating the four boundary positions each scan the $N$ characters once, giving $O(N)$ time.

Only counters and four indices are retained, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Store all one positions:** the same two gap sizes can be read from a list of one indices. This remains $O(N)$ time but uses $O(N)$ space in the worst case.
- **Prefix counts with every cut pair:** precompute prefix one-counts and test all two-cut combinations. It is correct but requires $O(N^2)$ time.
- **Recount sliced substrings:** testing each cut pair with substring counts can grow to $O(N^3)$ time.
- **Total not divisible by three:** no equal split exists, regardless of zero placement.
- **All zeros:** every pair of distinct gaps works, so use the binomial formula.
- **No zeros between boundary ones:** that boundary contributes exactly one cut choice.
- **Many boundary zeros:** each extra gap creates another distinct split even though the three one-counts stay unchanged.
- **Leading and trailing zeros:** they do not create boundary choices outside the required one groups because all three substrings must remain nonempty and contain their assigned ones when $T>0$.
- **Modulo arithmetic:** apply the modulus to the final combinatorial count or gap product.

</details>
