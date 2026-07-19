# Minimize Maximum Pair Sum in Array

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) |
| Frontend ID | 1877 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For a pair of values $(a,b)$, its pair sum is $a+b$. Once several pairs have been formed, their maximum pair sum is the largest of those individual sums.

Given an even-length integer array `nums`, divide all $N$ elements into exactly $N/2$ pairs. Every occurrence must belong to exactly one pair, including repeated values. Choose the pairing that makes the largest pair sum as small as possible, and return that minimized maximum.

### Function Contract

**Inputs**

- `nums`: an array of even length $N$, where $2 \le N \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- Return the minimum possible maximum pair sum after assigning every array element to exactly one pair.

### Examples

**Example 1**

- Input: `nums = [3,5,2,3]`
- Output: `7`

The pairs `(3,3)` and `(5,2)` have sums $6$ and $7$, so their maximum is $7$.

**Example 2**

- Input: `nums = [3,5,4,2,4,6]`
- Output: `8`

The pairs `(3,5)`, `(4,4)`, and `(6,2)` all have sums at most $8$.

**Example 3**

- Input: `nums = [9,1]`
- Output: `10`

With two elements, the sole pair is forced.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Balance the two extremes**

Sort the numbers into non-decreasing order. Pair the smallest value with the largest, the second smallest with the second largest, and continue inward. Compute each of these $N/2$ sums and return their maximum.

**Why the outermost pair can be fixed**

Let $a$ be the smallest remaining value and $b$ the largest. Consider any pairing in which $b$ is paired with some $x$ instead of $a$, while $a$ is paired with $y$. Replacing those two pairs by $(a,b)$ and $(x,y)$ cannot increase their worst sum: $a+b \le x+b$, and $x+y \le x+b$ because $y \le b$. Thus an optimal pairing exists that joins the two extremes.

**Repeat the exchange**

After fixing $(a,b)$, remove both values. The same argument applies to the smallest and largest values still unpaired. Repeating it constructs every opposite-rank pair without worsening an optimum, so the maximum sum produced by the two-pointer scan is globally minimal. Equal values cause no difficulty because exchanges involving them may simply leave the sums unchanged.

#### Complexity detail

Sorting the $N$ values takes $O(N\log N)$ time, and examining the $N/2$ opposite-rank pairs takes $O(N)$ time. The app-local implementation creates a sorted copy, requiring $O(N)$ space. Its two indices and running maximum use only constant additional storage.

#### Alternatives and edge cases

- **Frequency counting:** Since every value is at most $10^5$, a frequency array and two opposing value pointers can form the same pairs in $O(N+10^5)$ time and $O(10^5)$ space.
- **Quadratic selection sort:** It produces the needed ordering but takes $O(N^2)$ time.
- **Enumerate all pairings:** Exhaustive pairing can confirm tiny examples, but its combinatorial running time is unsuitable for the input bound.
- **Two elements:** They form the only possible pair, so return their sum.
- **Duplicate values:** Treat duplicates as separate occurrences; their relative order after sorting is irrelevant.
- **Already sorted input:** The same outer-to-inner pairing applies without changing the reasoning.
- **Large values:** A pair sum can reach $2\cdot 10^5$, which fits ordinary integer ranges.

</details>
