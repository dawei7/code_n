# Number of Steps to Reduce a Number in Binary Representation to One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1404 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Bit Manipulation, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/) |

## Problem Description

### Goal

A positive integer is provided as a binary string `s` with no leading zeroes. Repeatedly change the represented number until it becomes one.

When the current number is even, divide it by two. When it is odd and greater than one, add one. Each division or addition counts as one step. Return the number of steps required to reach one. The binary input may be much longer than a machine integer.

### Function Contract

**Inputs**

- `s`: a binary representation of length $n$, where $1 \le n \le 500$, `s[0] == "1"`, and no leading zeroes occur.

**Return value**

- The number of prescribed even divisions and odd increments needed to reduce the represented value to one.

### Examples

**Example 1**

- Input: `s = "1101"`
- Output: `6`

**Example 2**

- Input: `s = "10"`
- Output: `1`

**Example 3**

- Input: `s = "1"`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Process bits with a pending carry.** Scan from the least significant bit toward, but not including, the leading bit. A carry records whether an earlier odd increment has propagated into the unprocessed prefix.

If the current bit plus carry is odd, the represented suffix first needs an addition and then a division, contributing two steps; the carry becomes one. If the effective bit is even, only division is needed, contributing one step. An effective value of two is even and keeps the carry for the next position.

After every non-leading bit has been removed conceptually, a remaining carry turns the leading `1` into binary `10`, requiring one final division. Otherwise the number is already one. This exactly simulates each operation's effect without materializing the intermediate potentially longer binary strings.

#### Complexity detail

The scan examines $n - 1$ bits once, taking $O(n)$ time. The step count and one carry bit use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Convert to an integer:** Repeated arithmetic is simple in arbitrary-precision languages but violates fixed-width portability and makes costs depend on big-integer operations.
- **Rewrite the binary string:** Explicit additions and immutable suffix removal can copy $O(n)$ characters per operation, taking $O(n^2)$ time.
- **Already one:** `"1"` requires zero operations.
- **Power of two:** Every trailing zero is removed by one division.
- **Carry through ones:** Adding one to a suffix of ones propagates left and may create a new leading bit.
- **Effective bit two:** A stored `1` plus carry is even; division removes its zero suffix but the carry remains for the next bit.

</details>
