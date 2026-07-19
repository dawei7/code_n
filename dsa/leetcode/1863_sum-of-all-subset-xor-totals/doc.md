# Sum of All Subset XOR Totals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1863 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) |

## Problem Description
### Goal
The XOR total of an array is the bitwise XOR of all its elements; the empty
array has XOR total zero. Given `nums`, consider every subset obtainable by
deleting any selection of its indexed elements and add all of those XOR totals.

Subsets are determined by index choices. Consequently, when equal values occur
at different positions, selections that contain the same values can still be
distinct and must each contribute to the sum. Return the complete subset-XOR
sum.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 12$ and
  $1 \le \texttt{nums}[i] \le 20$.

**Return value**

An integer equal to the sum of the XOR totals of all $2^n$ index subsets,
including the empty subset.

### Examples
**Example 1**

- Input: `nums = [1,3]`
- Output: `6`

The four XOR totals are $0$, $1$, $3$, and $1 \mathbin{\mathtt{XOR}} 3=2$.

**Example 2**

- Input: `nums = [5,1,6]`
- Output: `28`

**Example 3**

- Input: `nums = [3,4,5,6,7,8]`
- Output: `480`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count one bit across all subsets**

Consider a bit that is set in at least one array element, and choose one index
whose value contains that bit. Pair every subset that omits this chosen index
with the subset obtained by adding it. The chosen bit is toggled between the
two XOR totals, so exactly one member of every pair has that bit set. Therefore
the bit contributes to exactly $2^{n-1}$ subset XOR totals.

If a bit is absent from every input value, no subset can contain it in its XOR.
Thus the bits that contribute are precisely those set in the bitwise OR of all
elements. Multiplying that OR by $2^{n-1}$ adds each contributing bit's value
the correct number of times:

$$
\text{answer}
=
\left(\bigvee_{x \in \texttt{nums}} x\right)2^{n-1}.
$$

Compute the OR in one pass, then shift it left by $n-1$. The pairing is based
on indices, so it remains valid when multiple positions hold equal values.

#### Complexity detail

The OR pass inspects all $n$ values once and the final shift is constant time,
giving $O(n)$ time. Only the accumulated bit mask is stored, so auxiliary space
is $O(1)$.

#### Alternatives and edge cases

- **Backtracking over subsets:** carrying the current XOR through include/skip
  branches is correct but takes $O(2^n)$ time.
- **Bitmask enumeration:** evaluating every mask is iterative but still
  exponential and may spend another factor of $n$ rebuilding each XOR.
- The empty subset contributes zero and therefore does not change the sum.
- Equal-valued elements at different indices create separately counted
  subsets even when their selected value lists look identical.
- For a one-element array, the answer is the element itself.

</details>
