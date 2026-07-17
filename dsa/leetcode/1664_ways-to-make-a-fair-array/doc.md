# Ways to Make a Fair Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1664 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ways-to-make-a-fair-array/) |

## Problem Description
### Goal
Choose exactly one 0-indexed position from `nums` and remove its element. Every later element shifts one position to the left, so its index parity changes, while earlier elements retain their indices.

An array is fair when the sum of values at even indices equals the sum at odd indices. Count how many removal positions produce a fair remaining array. Each position is a separate choice even when several values are equal.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

Return the number of indices whose removal makes the shifted array fair.

### Examples
**Example 1**

- Input: `nums = [2, 1, 6, 4]`
- Output: `1`

Only removing index 1 leaves `[2, 6, 4]`, whose even and odd sums are both 6.

**Example 2**

- Input: `nums = [1, 1, 1]`
- Output: `3`

Removing any position leaves `[1, 1]`, which is fair.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate the current left and right regions by parity.** First total the values at original even indices and original odd indices. During a left-to-right scan, maintain the corresponding sums for elements strictly before the candidate index and for elements strictly after it.

**Remove the candidate before testing.** Subtract `nums[i]` from the right sum matching the original parity of `i`. The left-side elements keep their parity after removal, but every right-side element shifts left and swaps parity. The resulting even sum is therefore `left_even + right_odd`, while the resulting odd sum is `left_odd + right_even`.

**Count equality and advance the boundary.** If those two expressions match, removing the current index is valid. Then add the current value to its original-parity left sum so the next iteration has the correct partition. This order ensures the removed value belongs to neither side during its test.

**Why every candidate is evaluated exactly.** Before testing index `i`, the left totals contain precisely indices below `i` and the right totals contain precisely indices above `i`. The parity transformation is deterministic: only the suffix shifts. Thus the two computed sums are exactly the even and odd sums of the array obtained by deleting `i`, and checking every index counts all and only fair removals.

#### Complexity detail

The initial parity totals and candidate scan each process $n$ values once, giving $O(n)$ time. Four running sums and the answer counter use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Four prefix arrays:** Store even and odd prefix and suffix sums for every boundary. This also gives $O(n)$ time but uses $O(n)$ extra space.
- **Rebuild after every removal:** Materializing each candidate array and resumming its parities costs $O(n^2)$ time.
- **Forget the suffix parity swap:** Comparing original even and odd totals after subtraction is wrong because all later indices change parity.
- Removing the only element leaves an empty array with both parity sums equal to zero.
- Equal values at different indices remain distinct removal choices.
- The valid index may be at either endpoint, where one side of the partition is empty.
- An originally fair array does not imply that any particular removal keeps it fair.
- Positive values can produce zero, one, several, or all indices as valid choices.

</details>
