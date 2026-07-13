# Combination Sum IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 377 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/combination-sum-iv/) |

## Problem Description
### Goal
Given unique positive integers `nums` and a positive `target`, build ordered sequences by selecting input values with unlimited reuse. A sequence qualifies when the sum of all selected values equals the target exactly.

Return the number of qualifying sequences. Order matters, so two sequences containing the same multiset in different positions count separately. A target with no valid construction returns zero. Because all choices are positive, extensions strictly increase the running sum. The function returns only the count, not the sequences themselves.

### Function Contract
**Inputs**

- `nums`: a list of distinct positive integers
- `target`: a non-negative target sum

**Return value**

- The number of ordered value sequences summing exactly to `target`.

### Examples
**Example 1**

- Input: `nums = [1,2,3], target = 4`
- Output: `7`

**Example 2**

- Input: `nums = [4], target = 13`
- Output: `0`

**Example 3**

- Input: `nums = [2,5], target = 2`
- Output: `1`

### Required Complexity

- **Time:** $O(n \cdot target)$
- **Space:** $O(target)$

<details>
<summary>Approach</summary>

#### General

**Define counts by the final sequence sum**

Let `ways[sum]` be the number of ordered sequences that total `sum`. Set `ways[0] = 1`: the empty sequence is the one foundation from which a first value can be appended.

For each total from one through `target`, consider every number not exceeding that total. A sequence ending with `number` is formed by taking any sequence counted by `ways[total - number]` and appending `number`. Add all such counts.

**Why loop order preserves sequence order**

The outer loop advances the total and the inner loop chooses the final value. Thus `[1,3]` and `[3,1]` arrive through different final-value transitions and are counted separately. Reversing the loops, as in the usual unordered coin-change formulation, would count combinations without order and solve a different problem.

**Why every valid sequence is counted once**

Every non-empty valid sequence has one unique final value. Removing it leaves an ordered sequence whose sum is `total - final`, already counted in the corresponding smaller state because all numbers are positive. Conversely, appending the chosen final value to any sequence from that state creates a valid sequence of the current total. These disjoint final-value groups account for every sequence exactly once.

**Trace target four**

With `[1,2,3]`, the counts progress from `ways[0] = 1` to `1,2,4,7`. The seven target-four sequences end respectively in one, two, or three and include different orders as distinct results.

#### Complexity detail

Let `n = len(nums)`. Each of the `target` positive totals examines up to `n` values, giving $O(n \cdot target)$ time. The one-dimensional table uses $O(target)$ space.

#### Alternatives and edge cases

- **Top-down memoized recursion:** evaluates the same remaining-target states and has the same asymptotic bounds, with recursion overhead.
- **Uncached sequence recursion:** repeats identical remaining sums and grows exponentially.
- **Number-first coin-change DP:** counts unordered multisets instead of ordered sequences and is semantically incorrect here.
- A target of zero has one empty sequence, which supplies the recurrence's base case.
- A number larger than the current total cannot be the final value.
- If no number can build the target, the count remains zero.
- Distinct input values prevent duplicate transitions representing the same appended number.

</details>
