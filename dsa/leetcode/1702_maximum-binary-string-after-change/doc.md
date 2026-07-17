# Maximum Binary String After Change

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1702 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-binary-string-after-change/) |

## Problem Description
### Goal

You are given a binary string `binary`. Any occurrence of `00` may be replaced by `10`, and any occurrence of `10` may be replaced by `01`. Either operation may be applied any number of times and at any positions made available by earlier changes.

Return the greatest binary string reachable under these rules. All reachable strings retain the original length. One binary string is greater than another when its value as a base-two integer is greater, so the earliest differing position determines which equal-length result is better.

### Function Contract
**Inputs**

- `binary`: a string of length $n$ containing only `0` and `1`, where $1 \le n \le 10^5$

**Return value**

The lexicographically and numerically maximum length-$n$ binary string obtainable through the allowed `00` to `10` and `10` to `01` replacements.

### Examples
**Example 1**

- Input: `binary = "000110"`
- Output: `"111011"`

Repeated moves eliminate all but one zero and place that zero at index `3`.

**Example 2**

- Input: `binary = "01"`
- Output: `"01"`

Neither allowed two-character pattern occurs, so the input is already maximal.

**Example 3**

- Input: `binary = "11000"`
- Output: `"11110"`

The two leading ones remain fixed, while the three-zero suffix is transformed to contain one zero at its final position.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Fix the prefix before the first zero**

Find the first `0`. If none exists, the string is already all ones and cannot be improved. Otherwise, every character before that position is `1`. No operation can introduce a zero to the left of this prefix while improving the result, so those leading ones remain part of the maximum string.

The operation `10` to `01` can move a zero left across a one, allowing zeros in the remaining suffix to meet. Whenever two zeros are adjacent, `00` to `10` removes one of them. Repeating these moves can therefore reduce any suffix containing zeros to exactly one zero. A result with fewer zeros is always larger than one with more zeros, so a maximum must perform all possible eliminations.

**Locate the unavoidable zero**

Let `first_zero` be the first zero's index and let `zero_count` be the total number of zeros. Combining the first zero with each of the other `zero_count - 1` zeros advances the surviving zero's boundary by one position. Its final index is consequently `first_zero + zero_count - 1`.

The leading positions can all be made `1`, but the survivor cannot be pushed farther right without either retaining another earlier zero or reversing an improvement. Thus the maximum string consists of `1` everywhere except at that single forced index. Constructing exactly that pattern proves both reachability and maximality: every earlier bit is as large as possible, and the only unavoidable zero is delayed as far as the operations permit.

#### Complexity detail

Finding the first zero, counting all zeros, and constructing the length-$n$ result each take $O(n)$ time. The immutable output string occupies $O(n)$ space; aside from the returned value, only constant-sized counters are needed.

#### Alternatives and edge cases

- **Repeated operation simulation:** applying local replacements and restarting a scan can perform quadratic work and obscures the final single-zero structure.
- **Breadth-first search over strings:** exploring reachable states is exponential and unnecessary because the maximum has a direct form.
- **Recompute zero statistics per output position:** this constructs the right answer but repeats full-string scans, taking $O(n^2)$ time.
- **All ones:** no operation applies, so return the original string.
- **Exactly one zero:** no zero can be eliminated; its position is unchanged in the maximum.
- **All zeros:** the result is `1` in every position except the last.
- **Leading ones:** the first-zero index must be included in the survivor formula; counting zeros alone would place it too far left.
- **Equal-length comparison:** maximizing the binary value is equivalent to maximizing lexicographically, so earlier bits have priority.

</details>
