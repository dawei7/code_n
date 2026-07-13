# Strange Printer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 664 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/strange-printer/) |

## Problem Description
### Goal
A strange printer can print only a sequence of one repeated character during each turn. In a turn, choose that character and any contiguous interval of positions; the new characters cover whatever the printer placed at those positions in earlier turns.

Given a target string `s`, return the minimum number of turns needed to produce it exactly. A turn may deliberately print beyond the positions that ultimately keep its character because later turns can overwrite part of the interval, and the printer begins with no required target characters on the output.

### Function Contract
**Inputs**

- `s`: a nonempty lowercase string to produce on an initially blank strip

**Return value**

- The minimum number of printer turns needed to finish with exactly `s`

### Examples
**Example 1**

- Input: `s = "aaabbb"`
- Output: `2`

**Example 2**

- Input: `s = "aba"`
- Output: `2`

**Example 3**

- Input: `s = "abcabc"`
- Output: `5`

### Required Complexity

- **Time:** $O(N^3)$
- **Space:** $O(N^2)$

<details>
<summary>Approach</summary>

#### General

**Compress consecutive equal targets**

Adjacent occurrences of the same target character never require separate turns: any plan can extend the turn producing one occurrence across the entire run without harming the final string. Remove consecutive duplicates before building states. This preserves the answer and often substantially reduces the effective length.

**Define the optimum for every interval**

Let `turns(left, right)` be the minimum turns for the compressed substring from `left` through `right`. A safe baseline prints `s[left]` in its own turn and then solves the remaining interval, costing `1 + turns(left + 1, right)`.

For every later position `middle` with `s[middle] = s[left]`, the turn that ultimately produces `s[middle]` can be extended left to produce `s[left]` at no extra cost. The characters strictly between them must still be finished separately. This gives candidate `turns(left + 1, middle - 1) + turns(middle, right)`.

**Why the recurrence covers an optimal print plan**

In an optimal plan, the final target occurrence at `left` is either produced by a turn that produces no equal later target, matching the baseline, or that same turn also produces some later equal position `middle`, matching one of the merge candidates. Overwrites inside the gap are handled entirely by its interval state. Taking the minimum over these exhaustive possibilities is therefore optimal. Memoization ensures each interval is solved once.

#### Complexity detail

There are $O(N^2)$ intervals, and each may examine $O(N)$ merge positions, giving $O(N^3)$ time after compression. Memoized interval results use $O(N^2)$ space, and recursion adds $O(N)$ stack depth.

#### Alternatives and edge cases

- **Bottom-up interval dynamic programming:** computes the same states iteratively with identical asymptotic bounds and avoids recursion.
- **Memo-free recurrence:** is correct but recomputes overlapping intervals and can take exponential time.
- **Print each final run separately:** supplies an upper bound but misses savings from printing equal characters together before overwriting their gap.
- A one-character string needs one turn.
- A string containing one repeated character needs one turn regardless of length.
- Equal characters separated by other targets may share a turn because later turns can overwrite the middle.
- Compression changes state indices but not the required printed result or minimum turn count.

</details>
