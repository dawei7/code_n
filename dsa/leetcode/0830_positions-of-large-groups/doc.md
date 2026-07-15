# Positions of Large Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 830 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/positions-of-large-groups/) |

## Problem Description

### Goal

In a lowercase English string `s`, equal consecutive letters form groups. Each group is maximal: it begins either at index `0` or immediately after a different letter, and it ends either at the last index or immediately before a different letter. Represent a group by its inclusive zero-based interval `[start, end]`.

A group is large when it contains at least three characters. Return the intervals of all large groups in increasing order of `start`. Report each maximal group once; a longer run does not also contribute its shorter length-three subranges.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \le n \le 1000$
- Let $g$ be the number of large groups in `s`.

**Return value**

- A list of inclusive intervals `[start, end]`, one for each large maximal group, ordered by increasing `start`

### Examples

**Example 1**

- Input: `s = "abbxxxxzzy"`
- Output: `[[3, 6]]`
- Explanation: `"xxxx"` is the only group whose length is at least three.

**Example 2**

- Input: `s = "abc"`
- Output: `[]`
- Explanation: Each group has length one.

**Example 3**

- Input: `s = "abcdddeeeeaabbbcd"`
- Output: `[[3, 5], [6, 9], [12, 14]]`
- Explanation: The large groups are `"ddd"`, `"eeee"`, and `"bbb"`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(g)$

<details>
<summary>Approach</summary>

#### General

**Keep the start of the current maximal run**

Initialize `run_start = 0` and scan an `end` position from `1` through `len(s)`. A run ends when `end == len(s)` or `s[end] != s[run_start]`. The explicit end-of-string boundary acts like a sentinel and lets the last group follow the same logic as every interior group without indexing beyond the string.

**Record the run before advancing to the next one**

At a boundary, the current group occupies `run_start` through `end - 1` and has length `end - run_start`. Append `[run_start, end - 1]` only when that length is at least `3`, then execute `run_start = end` to begin the next group.

**Why the scan reports exactly the requested intervals**

Between two detected boundaries, every character equals the character at `run_start`; immediately outside that interval is either the string boundary or a different character. The interval is therefore one complete maximal group. The scan processes boundaries from left to right, so each group is considered once and appended intervals are already ordered by start index. The length test includes precisely the groups meeting the large-group threshold.

#### Complexity detail

Let $n$ be the string length and $g$ the number of returned large groups. The boundary pointer advances from `1` through $n$ once, so the time is $O(n)$. Apart from the required list of $g$ two-index intervals, the scan uses constant state; counting the returned output, the space is $O(g)$.

#### Alternatives and edge cases

- **`itertools.groupby`:** Grouping consecutive characters and tracking a cumulative index is also $O(n)$ and concise, but manual boundaries make the inclusive indices explicit.
- **Regular-expression runs:** A pattern such as repeated-character backreferences can locate groups, though it adds engine-specific syntax for a simple linear scan.
- **Expand around every index:** Finding the full equal-character run separately for every position is correct with deduplication but can take $O(n^2)$ time.
- **Length exactly three:** The group qualifies because the threshold is at least three, not greater than three.
- **Run at either boundary:** Groups beginning at index `0` or ending at index `n - 1` must be reported normally.
- **One long run:** Return its single maximal interval rather than every qualifying subinterval.
- **No large group:** Return an empty list.
- **Inclusive endpoint:** Store `end - 1`, since `end` is the first index outside the completed run.

</details>
