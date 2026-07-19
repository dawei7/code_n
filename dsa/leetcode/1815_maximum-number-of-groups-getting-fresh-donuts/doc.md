# Maximum Number of Groups Getting Fresh Donuts

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/) |
| Frontend ID | 1815 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Memoization, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A donut shop bakes exactly `batchSize` donuts at a time. It must finish serving every donut from the current batch before using any donut from the next batch. The integer array `groups` gives the number of customers in each visiting group, and every customer receives exactly one donut. Once a group begins, all of its customers are served before the next group.

A group is happy when its first customer receives the first donut of a fresh batch rather than a donut left over after the preceding group. The groups may be reordered arbitrarily. Return the largest number of groups that can be made happy.

### Function Contract

**Inputs**

- `batchSize`: an integer $b$ satisfying $1 \le b \le 9$.
- `groups`: a list of $n$ positive group sizes, where $1 \le n \le 30$ and each size is at most $10^9$.
- After removing remainder-zero groups and complementary pairs, let $c_r$ be the remaining count with remainder $r$ for $1 \le r < b$, and define

$$
S = \prod_{r=1}^{b-1}(c_r+1).
$$

**Return value**

- Return the maximum number of groups whose first donut can come from a fresh batch after choosing the best ordering.

### Examples

**Example 1**

- Input: `batchSize = 3, groups = [1,2,3,4,5,6]`
- Output: `4`

One optimal ordering is `[6,2,4,5,1,3]`.

**Example 2**

- Input: `batchSize = 4, groups = [1,3,2,5,2,2,1,6]`
- Output: `4`

The best ordering aligns four group starts with batch boundaries.

**Example 3**

- Input: `batchSize = 2, groups = [1,1,1]`
- Output: `2`

The first and third groups start when no donuts are left over.

### Required Complexity

- **Time:** $O(bS)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Reduce every group to its batch remainder**

Only `group % batchSize` affects the leftover position after that group. A remainder-zero group begins and ends on a batch boundary, so it can always be placed while fresh and counted immediately.

**Remove complementary pairs safely**

Remainders $r$ and $b-r$ sum to one complete batch. Place such a pair when the current leftover is zero: its first group is happy and the pair returns the process to zero, without affecting any other group. Therefore match as many complementary pairs as possible and add one happy group per pair. When $b$ is even, two groups with remainder $b/2$ form the analogous pair.

**Search the residual multiset rather than permutations**

After those reductions, retain the count of each nonzero remainder. A memoized state consists of the count tuple and the current leftover modulo $b$. Try each remainder whose count is positive, decrement it, and update the leftover with `(leftover + remainder) % batchSize`. Serving the chosen group contributes one happy group exactly when the old leftover was zero.

**Why the recurrence is complete**

Groups with the same remainder are interchangeable, so the count tuple loses no ordering information. Every possible residual ordering begins with one available remainder and leaves a smaller state considered by the recurrence. Taking the maximum over those choices therefore covers all orderings. The base reductions are independent zero-sum blocks, so prepending them preserves the optimal residual value while securing their counted happy groups.

#### Complexity detail

Each remainder count ranges from zero through its initial $c_r$, so there are at most $S$ count tuples. The leftover is determined by the removed remainder sum but is carried explicitly for clarity; each cached tuple tries at most $b-1$ next remainders. Time is $O(bS)$ and the cache plus recursion stack use $O(S)$ space. The fixed source limits $b \le 9$ and $n \le 30$, together with complementary-pair reduction, bound the practical state space.

#### Alternatives and edge cases

- **Permute all groups:** It is exact but explores up to $n!$ orders and repeats equivalent remainder arrangements.
- **Greedy complementary pairs only:** The reduction is safe, but unmatched remainder counts can still require nonlocal ordering choices; stopping there may miss the optimum.
- **Bitmask DP over group indices:** It is exact in $O(n2^n)$ time but treats equal remainders as distinct and is infeasible for $n=30$.
- **Batch size one:** Every group starts at a batch boundary, so all groups are happy.
- **Remainder-zero groups:** Count them independently; they never change the leftover.
- **Half-batch remainder:** For even $b$, pair these groups with each other rather than processing the same complementary class twice.
- **Large group sizes:** Reduce them modulo `batchSize`; their quotient consumes whole batches without changing boundary state.
- **Leftover interpretation:** A group is happy based on the leftover before it is served, not after its remainder is added.
- **Final reset:** Returning to zero after the last group creates no additional happy group because no next group exists.

</details>
