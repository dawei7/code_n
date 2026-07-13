# Find the Index of the First Occurrence in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 28 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Two Pointers, String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |

## Problem Description
### Goal
You are given two nonempty strings, `haystack` and `needle`. Search for an interval of `haystack` whose consecutive characters equal the complete `needle` in the same order. Matches may overlap, and characters cannot be skipped.

Return the zero-based starting index of the earliest such occurrence. If no contiguous occurrence exists, return `-1`. A match beginning at index zero takes precedence over every later match, and a needle equal to the entire haystack also begins at zero.

### Function Contract
**Inputs**

- `haystack`: non-empty `str`
- `needle`: non-empty `str`

**Return value**

An `int` containing the first match's zero-based start index, or `-1`.

### Examples
**Example 1**

- Input: `haystack = "sadbutsad", needle = "sad"`
- Output: `0`

**Example 2**

- Input: `haystack = "leetcode", needle = "leeto"`
- Output: `-1`

**Example 3**

- Input: `haystack = "mississippi", needle = "issip"`
- Output: `4`

### Required Complexity

- **Time:** $O(n + m)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**A mismatch can reuse a border of the matched pattern prefix**

Knuth-Morris-Pratt matching stores, for every pattern prefix ending at index `i`, the length of its longest proper prefix that is also a suffix. A **proper** prefix is shorter than the whole prefix. This `lps` value identifies how many already-matched pattern characters can remain useful after a mismatch.

Build the array with `candidate`, the length of the border currently being tested. If `needle[i] = needle[candidate]`, extend the border and record its new length. On a mismatch with a nonzero candidate, replace it by `lps[candidate - 1]` and test the same `needle[i]` again. If the candidate is zero, record zero and advance `i`.

The fallback follows borders of borders. Those are exactly the shorter prefixes that could also be suffixes; restarting at every intermediate length would repeat comparisons and lose the linear bound.

**Scan the haystack without ever rewinding it**

Maintain `matched`, the number of leading needle characters matching the current haystack suffix. On a mismatch with `matched > 0`, fall back to `lps[matched - 1]` and compare the same haystack character again. Only when `matched = 0` may the haystack index advance past a mismatch. On a match, advance both positions.

When `matched` reaches the needle length, the complete occurrence ends at the current haystack position. Its start is `haystack_index - len(needle)` if indices were advanced after matching, or equivalently `current_index - len(needle) + 1` in a for-loop formulation.

**What remains true after every fallback**

Before each haystack comparison, `needle[:matched]` equals the length-`matched` suffix of the processed haystack prefix. If the next characters mismatch, any surviving candidate must be both a suffix of those matched text characters and a prefix of `needle`. The LPS fallback selects the longest such candidate. It therefore discards no possible occurrence while avoiding a backward move in the haystack.

**Trace overlapping partial matches**

For haystack `mississippi` and needle `issip`, the attempt beginning at index 1 matches `issi` and then mismatches. The LPS data finds the longest pattern prefix that is also a suffix of the matched portion, so scanning continues without moving the haystack index backward. The next viable alignment completes at indices `4..8`, and the algorithm returns `4`.

A pattern such as `ababaca` makes the reuse more visible: after matching `ababa`, a mismatch can retain the border `aba` rather than rechecking those three characters from the text.

**Failure links preserve every viable alignment**

On mismatch, the LPS fallback keeps the longest proper pattern prefix already known to equal the current text suffix. The just-tested longer alignment is impossible, and an alignment not corresponding to a border cannot end at the same text position, so no viable candidate is skipped.

The haystack index never moves backward; only the amount of matched pattern is shortened. When the pattern first becomes complete, all earlier text endpoints have already been processed without a complete match. Its computed start is therefore the smallest valid occurrence index.

#### Complexity detail

During LPS construction, the pattern index advances at most `m` times and each fallback shortens `candidate`; the total is $O(m)$. During matching, the haystack index never decreases, and each fallback decreases `matched`, so the scan is $O(n)$. Combined time is $O(n + m)$, and the LPS array uses $O(m)$ auxiliary space.

#### Alternatives and edge cases

- **Try the pattern at every start:** simple but can repeat almost the entire pattern at many positions and require $O(nm)$ time.
- **Rolling hash:** offers expected linear matching and is useful for many patterns, but requires collision handling for deterministic correctness.
- **Built-in search:** often highly optimized, but hides the algorithm and its worst-case contract.
- If $m > n$, no complete occurrence is possible and the scan naturally returns `-1`; an early return is optional.
- The stated contract makes `needle` nonempty. In APIs where an empty needle is allowed, the conventional first-occurrence result is index `0` and should be handled before building LPS.
- Overlapping occurrences are safe because LPS preserves reusable suffixes; this problem returns immediately at the first complete one.

</details>
