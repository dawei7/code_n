# Change Minimum Characters to Satisfy One of Three Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1737 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/) |

## Problem Description

### Goal

The nonempty strings `a` and `b` contain only lowercase English letters. One operation may replace any one character in either string with any lowercase letter.

Find the minimum operations needed to make at least one of three conditions true: every character in `a` is strictly alphabetically smaller than every character in `b`; every character in `b` is strictly smaller than every character in `a`; or both strings together contain only one distinct letter. Either string may contain up to $10^5$ characters.

### Function Contract

**Inputs**

- `a`: a nonempty lowercase string.
- `b`: another nonempty lowercase string.

Let $N = \lvert a \rvert + \lvert b \rvert$.

**Return value**

- Return the minimum number of single-character replacements needed to satisfy at least one allowed condition.

### Examples

**Example 1**

- Input: `a = "aba", b = "caa"`
- Output: `2`
- Explanation: Changing `b` to `"ccc"` satisfies the first condition, while making both strings all `a` also costs two.

**Example 2**

- Input: `a = "dabadd", b = "cda"`
- Output: `3`
- Explanation: Changing `b` to `"eee"` makes every letter in `a` strictly smaller than every letter in `b`.

**Example 3**

- Input: `a = "aaaa", b = "bbbb"`
- Output: `0`
- Explanation: The first strict-order condition already holds.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count the fixed alphabet**

Build two frequency arrays of length $26$. The alphabet size is constant, so these counts retain everything needed about the strings while discarding their irrelevant character order.

**Evaluate both strict-order directions**

Choose a boundary after some letter from `a` through `y`. To make every character in `a` at most that boundary and every character in `b` above it, change the suffix characters of `a` plus the prefix characters of `b`. Prefix sums of the two frequency arrays give this cost for every boundary. Swap the roles of the strings to evaluate the second condition. A boundary after `z` is excluded because the higher side must contain a lowercase letter and the relation is strict.

**Evaluate one shared distinct letter**

For the third condition, choose one target letter for both strings. If that letter occurs $f$ times across the combined input, exactly $N-f$ positions must change. Keeping the most frequent combined letter minimizes this cost. The answer is the minimum over these shared-letter choices and both directions at all $25$ valid boundaries.

#### Complexity detail

Counting visits each of the $N$ input characters once. Scanning the fixed $26$-letter alphabet takes constant additional work, so total time is $O(N)$. The two frequency arrays always contain $26$ integers and therefore use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Sort both strings:** Sorting supports boundary counts but takes $O(N\log N)$ time and stores reordered characters.
- **Try replacements directly:** Enumerating possible changed strings grows exponentially and ignores that only frequencies affect the conditions.
- **Already strictly ordered:** Return zero without requiring either string to use a single letter.
- **Already one shared letter:** The third condition yields zero even when strict ordering is impossible.
- **Equal boundary letters:** Strictly less forbids the same letter from remaining on both sides of an ordering boundary.
- **One-character strings:** Either ordering direction or the shared-letter condition may be optimal.
- **Boundary at `y`:** The higher side must become all `z`, which remains valid.

</details>
