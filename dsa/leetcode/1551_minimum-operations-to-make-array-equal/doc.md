# Minimum Operations to Make Array Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1551 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-equal/) |

## Problem Description
### Goal
For a positive integer `n`, consider the length-$n$ array defined by `arr[i] = 2 * i + 1` for every zero-based index `i`. Thus, the array contains the first $n$ positive odd numbers.

In one operation, choose two indices and decrease one selected value by one while increasing the other selected value by one. Determine the minimum number of operations needed to make every array element equal. Each operation preserves the total sum, and the input guarantees that equality is achievable.

### Function Contract
**Inputs**

- `n`: the array length, where $1 \le n \le 10^4$.

**Return value**

The minimum number of paired decrement/increment operations required to make all values in the implicitly defined array equal.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `2`
- Explanation: The array is `[1, 3, 5]`; transferring two units from five to one produces `[3, 3, 3]`.

**Example 2**

- Input: `n = 6`
- Output: `9`
- Explanation: The array's average is six, and the total deficit of values below six is nine.

**Example 3**

- Input: `n = 1`
- Output: `0`
- Explanation: A one-element array is already equal.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Identify the only possible final value**

The sum of the first $n$ positive odd numbers is $n^2$, so their average is $n$. Because every operation transfers one unit without changing the sum, all elements must finish at value $n$.

**Count the unavoidable deficit below the average**

Each operation can supply one missing unit to a value below $n$, and the same operation removes one surplus unit from a value above $n$. The total deficit therefore is both a lower bound on the operation count and achievable by pairing deficits with surpluses.

If $n=2k$, the deficits form the odd sequence $2k-1, 2k-3, \ldots, 1$, whose sum is $k^2$. If $n=2k+1$, the middle element already equals $n$, and the deficits are $2k, 2k-2, \ldots, 2$, summing to $k(k+1)$. Both cases equal

$$
\left\lfloor \frac{n^2}{4} \right\rfloor.
$$

Integer division computes this expression directly as `n * n // 4`.

#### Complexity detail

The algorithm performs a fixed number of integer arithmetic operations independent of $n$, so it takes $O(1)$ time and $O(1)$ auxiliary space. It never constructs the implicit array.

#### Alternatives and edge cases

- **Sum every lower-half deficit:** this directly follows the transfer interpretation but takes $O(n)$ time.
- **Simulate unit transfers:** moving one unit per iteration takes time proportional to the answer, which can be $O(n^2)$.
- For $n=1$, the formula returns zero.
- Even and odd lengths have different deficit sequences but the same floor formula.
- The final common value is forced to be $n$ by sum preservation.
- Every operation fixes at most one unit of total deficit, establishing minimality.
- Multiplication should occur in a sufficiently wide integer type in languages with fixed-width arithmetic.

</details>
