# Magical String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 481 |
| Difficulty | Medium |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/magical-string/) |

## Problem Description
### Goal
The magical string begins `122112122122...`, contains only `1` and `2`, and is self-describing: when divided into maximal runs of equal symbols, the sequence of run lengths is the magical string itself. Run symbols alternate between `1` and `2`.

Given a positive prefix length `n`, return how many symbols equal `1` among the first `n` positions. Generate only as much of the sequence as needed, using its already produced run-length entries to extend it. For $n = 1$, the answer is `1`; when the requested prefix ends inside a run, count only symbols whose positions fall within that prefix.

### Function Contract
**Inputs**

- `n`: the prefix length to inspect

**Return value**

- The number of ones in the first `n` symbols of the infinite magical string

### Examples
**Example 1**

- Input: `n = 6`
- Output: `3`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 0`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Seed the self-describing prefix**

The magical string begins `1, 2, 2`. Starting at index two, each existing symbol says how many copies belong to the next generated run. A read pointer consumes these run lengths while the output list grows.

**Alternate the generated symbol**

The initial next symbol is `1`. Append it either once or twice according to the current run-length symbol, advance the read pointer, and toggle between `1` and `2` using `3 - symbol`. Continue until at least `n` symbols exist.

**Why generation remains synchronized**

Every read entry corresponds to exactly one maximal run in output order. Appending its requested count and toggling guarantees adjacent runs use different symbols. Inductively, the consumed run-length sequence equals the generated prefix, preserving the defining property.

**Count only the requested prefix**

The final run may extend past position `n`. Slice or inspect only the first `n` entries when counting ones so the extra generated symbol is not included.

#### Complexity detail

Each generated symbol is appended once and only a constant number beyond `n` are needed, giving $O(n)$ time. The generated prefix uses $O(n)$ space.

#### Alternatives and edge cases

- **Count ones during append:** avoids a final scan by incrementing only for positions below `n`.
- **Generate from scratch for every prefix length:** is correct but repeats earlier construction and takes $O(n^2)$ total work.
- **String-character storage:** works like an integer list but requires conversions for run lengths.
- **$n = 0$:** the empty prefix contains no ones.
- **$n \le 3$:** return the count from the seed prefix without reading beyond it.
- **Overshooting final run:** exclude appended positions at indices `n` and above.
- **Run length values:** the construction uses only one or two, matching the alphabet of the magical string.

</details>
