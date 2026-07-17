# Minimum Adjacent Swaps for K Consecutive Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1703 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) |

## Problem Description
### Goal

You are given a binary array `nums` and an integer `k`. One move swaps the values at any two adjacent indices. Swaps may move ones across zeros in either direction, and the array may contain more than the `k` ones that ultimately form the desired group.

Return the minimum number of adjacent swaps needed to make some `k` ones occupy consecutive positions. The chosen ones must preserve their relative order: crossing two indistinguishable ones never helps, while each crossed zero contributes one required adjacent swap.

### Function Contract
**Inputs**

- `nums`: a binary array of length $n$, where $1 \le n \le 10^5$
- `k`: the required number of consecutive ones, with $1 \le k \le \sum_i \texttt{nums[i]}$

Let $m$ be the total number of ones in `nums`.

**Return value**

The minimum adjacent-swap count over every possible choice of `k` ones and every consecutive destination block.

### Examples
**Example 1**

- Input: `nums = [1, 0, 0, 1, 0, 1], k = 2`
- Output: `1`

The last two ones can become adjacent by moving the final one left once.

**Example 2**

- Input: `nums = [1, 0, 0, 0, 0, 0, 1, 1], k = 3`
- Output: `5`

Moving the first one right five places produces three consecutive ones at the end.

**Example 3**

- Input: `nums = [1, 1, 0, 1], k = 2`
- Output: `0`

The first two entries already satisfy the requirement.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Choose consecutive ones in occurrence order**

Record the original indices of all ones. An optimal group never skips an occurrence between two chosen ones: replacing an outer chosen one with a skipped inner one cannot increase any movement distance. It is therefore sufficient to inspect each length-`k` window in the ordered list of one positions.

If the selected original positions are `position[j]`, their final consecutive destinations have the form `start + j`. The cost is a sum of `abs(position[j] - (start + j))`. Define an adjusted coordinate `adjusted[j] = position[j] - j`; then the same cost becomes the sum of `abs(adjusted[j] - start)`. Subtracting the occurrence rank removes the one-cell spacing that the chosen ones must retain in the final block. In particular, already-consecutive ones receive identical adjusted coordinates and correctly cost zero.

**Center each window at its adjusted median**

For any fixed window of `k` adjusted coordinates, the sum of absolute distances is minimized by a median. Choose the middle adjusted value and sum distances from all values on its left and right. This median corresponds to the best starting index for the final consecutive block; no separate simulation of swaps or destination positions is needed.

Build prefix sums of the adjusted coordinates. For a window `[left, right)` with median index `middle`, the left distance sum is `median * (middle - left) - (prefix[middle] - prefix[left])`. The right distance sum is `(prefix[right] - prefix[middle + 1]) - median * (right - middle - 1)`. Both expressions are nonnegative because the adjusted positions are non-decreasing.

Slide the window over all $m-k+1$ choices and keep the smallest combined cost. Every feasible optimal group appears as one such window, and the median minimizes its destinations, so the smallest evaluated value is the global optimum.

#### Complexity detail

Scanning `nums`, building adjusted positions and prefix sums, and evaluating at most $m$ windows takes $O(n)$ time because $m \le n$. The adjusted coordinates and prefix sums use $O(m)$ auxiliary space.

#### Alternatives and edge cases

- **Direct swap simulation:** repeatedly moving chosen ones through zeros can take quadratic time and makes it difficult to compare all possible groups.
- **Evaluate every destination block:** trying every start and summing movement for `k` ones repeats work, taking $O(mk)$ or worse.
- **Median of raw indices:** summing distance to one raw position overcharges the mandatory gaps between consecutive destination ones; subtract each occurrence rank first.
- **Arbitrary subsets of ones:** enumerating combinations is unnecessary because an optimum always uses `k` consecutive occurrences.
- **`k = 1`:** any existing one already forms a valid group, so the cost is zero.
- **Already consecutive:** their adjusted coordinates are equal and the computed cost is zero.
- **Even `k`:** either middle adjusted value minimizes the absolute-distance sum; choosing index `left + k // 2` is valid.
- **Extra ones:** ones outside the selected occurrence window do not have to move and contribute no cost.

</details>
