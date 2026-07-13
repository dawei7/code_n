# Count and Say

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 38 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-and-say/) |

## Problem Description
### Goal
The count-and-say sequence starts with the string `"1"`. To obtain the next term, read the current term from left to right, divide it into maximal runs of equal digits, and describe each run by writing its length followed by the repeated digit.

Given `n` from `1` through `30`, return the `n`th term as a string. Descriptions concern consecutive groups rather than total frequency: `"21"` is read as one `2` followed by one `1`, not as a combined inventory of the whole string.

### Function Contract
**Inputs**

- `n`: `int` in `[1, 30]`

**Return value**

The nth count-and-say term as a `str`.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `"1"`

**Example 2**

- Input: `n = 4`
- Output: `"1211"`

**Example 3**

- Input: `n = 5`
- Output: `"111221"`

### Required Complexity

- **Time:** $O(L_n)$
- **Space:** $O(L_n)$

<details>
<summary>Approach</summary>

#### General

**Describe maximal runs, not individual equalities**

Start with term `"1"`. To build the next term, scan the current string by maximal runs of equal digits. For a run from `index` up to but not including `following`, append `str(following - index)` and the run digit to a list of fragments. The inner scan must continue to the first different digit so one run is never split into several descriptions.

Repeat this transformation $n - 1$ times.

**Build each next term in one left-to-right pass**

At the start of an outer iteration, `term` is exactly the current sequence term. During its scan, the fragment list describes exactly the maximal runs strictly before `index`, with no run split or merged. Advancing `index` directly to `following` preserves this invariant and guarantees progress.

Accumulate fragments in a mutable list and join once. Repeatedly extending an immutable result string may recopy the entire partial output after every run.

**Trace a representative transition**

Term `1211` has runs `1`, `2`, and `11`. Their descriptions are `11`, `12`, and `21`; concatenating them gives the next term `111221`.

**Maximal runs make each description unique**

Every term has one unique left-to-right partition into maximal runs of equal digits. The inner scan extends a run until the first different digit or the string end, so it finds exactly those boundaries and emits that run's count followed by its digit.

Concatenating the descriptions in run order is therefore precisely the next term's definition. Starting from the fixed base `"1"`, repeating this exact transformation produces term 2, then term 3, and so on until the requested term `n`.

#### Complexity detail

Each generated character is read and written a constant number of times across adjacent transformations. Up to the fixed limit $n \le 30$, total work is proportional to the final-term scale, denoted $O(L_n)$, and the current/next strings use $O(L_n)$ space.

#### Alternatives and edge cases

- **Recursive generation:** expresses the recurrence directly but retains call-stack frames without reducing work.
- **Repeated immutable concatenation:** can copy a growing partial term many times; fragment accumulation plus one join avoids that risk.
- **Regular-expression run grouping:** can be concise but adds parsing machinery to a direct linear scan.
- $n = 1$ returns the seed without performing a transformation. Counts may contain multiple decimal digits in a general run-length encoder, so append the complete decimal count rather than assuming one character.
- Runs must be consecutive: equal digits separated by another digit belong to different descriptions.

</details>
