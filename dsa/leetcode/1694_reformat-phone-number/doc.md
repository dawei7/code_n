# Reformat Phone Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1694 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reformat-phone-number/) |

## Problem Description
### Goal

The string `number` contains decimal digits together with spaces and dashes. First discard every space and dash while preserving the digits' original left-to-right order. Then partition the clean digit sequence into blocks and join consecutive blocks with a single dash.

Take blocks of three digits from the left while more than four digits remain. Format the final suffix according to its length: two or three remaining digits form one block, while four remaining digits become two blocks of two. The result must never contain a one-digit block and can contain at most two two-digit blocks. Return the reformatted phone number.

### Function Contract
**Inputs**

- `number`: a string of length $N$, where $2 \le N \le 100$, containing only digits, spaces, and dashes and containing at least two digits

**Return value**

The digits in their original order, grouped under the three-digit and final-suffix rules with dashes between blocks.

### Examples
**Example 1**

- Input: `number = "1-23-45 6"`
- Output: `"123-456"`

Removing separators leaves six digits, which form two blocks of three.

**Example 2**

- Input: `number = "123 4-567"`
- Output: `"123-45-67"`

After the first three-digit block, the four-digit suffix is divided into two equal blocks.

**Example 3**

- Input: `number = "123 4-5678"`
- Output: `"123-456-78"`

The first six digits form two blocks of three and the last two digits remain together.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Separate cleanup from block decisions**

Scan `number` once and retain only digits. Spaces and dashes carry no information after cleanup, so this produces the exact sequence that must appear in the answer. Keeping cleanup independent also prevents original separator positions from accidentally influencing the new grouping.

**Reserve a legal final suffix**

Maintain an index into the clean digits. While more than four digits remain, append the next three as a block and advance the index by three. Stopping at four or fewer is the crucial rule: consuming another triple from a four-digit suffix would strand one digit, which is forbidden.

At the stopping point, the contract guarantees at least two digits remain. A suffix of two or three is appended as one block. A suffix of four is split at its midpoint into two two-digit blocks. Joining the accumulated blocks with dashes produces exactly one separator between blocks and none at either end.

Every emitted three-digit prefix is required because more than four digits remained at that moment. The final case analysis is exhaustive over the only possible suffix lengths, and each branch creates only blocks of length two or three. Since cleanup and slicing preserve order and consume each digit exactly once, the result satisfies every formatting rule.

#### Complexity detail

The cleanup scan examines the $N$ input characters once, and block construction copies each retained digit a constant number of times, for $O(N)$ time. The clean digit string, block list, and returned string together use $O(N)$ space.

#### Alternatives and edge cases

- **Regular-expression cleanup:** replacing spaces and dashes and then applying the same suffix logic is also linear, but a direct character filter avoids regex machinery.
- **Always take triples greedily:** doing so when exactly four digits remain creates a forbidden one-digit final block.
- **Repeated immutable-string concatenation:** prepending or appending blocks one at a time may copy an increasing prefix repeatedly; collecting blocks and joining once avoids quadratic copying.
- **Two digits:** return one two-digit block with no dash.
- **Three digits:** return one three-digit block with no dash.
- **Four digits:** return exactly two two-digit blocks.
- **Original separators:** leading, trailing, adjacent, or mixed spaces and dashes are all discarded uniformly.

</details>
