# Find All Anagrams in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 438 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |

## Problem Description
### Goal
Given lowercase strings `s` and `p`, inspect every contiguous substring of `s` whose length equals `len(p)`. A window is an anagram of `p` when it contains exactly the same characters with the same multiplicities, regardless of their order.

Return the zero-based starting indices of all matching windows in any order. Overlapping matches must be included, while a matching character set with incorrect counts does not qualify. If `p` is longer than `s`, return an empty list. The function returns indices rather than the substrings themselves.

### Function Contract
**Inputs**

- `s`: the lowercase text string to search
- `p`: the lowercase pattern whose character multiset must match

**Return value**

- Return all matching start indices in increasing order; overlapping matches are included.

### Examples
**Example 1**

- Input: `s = "cbaebabacd", p = "abc"`
- Output: `[0, 6]`

**Example 2**

- Input: `s = "abab", p = "ab"`
- Output: `[0, 1, 2]`

**Example 3**

- Input: `s = "a", p = "a"`
- Output: `[0]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Only windows with the pattern length can qualify**

Anagrams contain the same number of characters, so maintain a window of exactly `m = len(p)` characters. Count the pattern's letters and the first text window in two 26-entry arrays.

**Slide by updating only the two boundary letters**

After testing a window, remove its outgoing left character and add the new right character. The updated frequency array then describes the next length-`m` substring without recounting its interior.

**Compare character multisets rather than order**

Two lowercase strings of equal length are anagrams exactly when all 26 frequencies agree. Record the current left index whenever the fixed arrays are equal. Because the window advances one position at a time, recorded indices are automatically increasing and overlapping matches remain visible.

**Why every candidate is tested exactly once**

There are $n - m + 1$ length-`m` substrings when $m \le n$. Initialization tests the first, and each slide produces the next consecutive substring by one removal and one addition. No other substring length can be an anagram, so this covers precisely the complete candidate set.

#### Complexity detail

Each text character enters and leaves the window at most once. Comparing 26 counters is constant work for the fixed alphabet, giving $O(n)$ time. Two fixed arrays use $O(1)$ auxiliary space, excluding the output indices.

#### Alternatives and edge cases

- **Counter-based sliding window:** updates a hash table at the boundaries and compares it with the pattern counter; it has the same linear-time class.
- **Recount every substring:** building a new frequency table for each length-`m` window takes $O(nm)$ time.
- **Sort every substring:** comparison is simple but costs $O(nm \log m)$ time.
- **Pattern longer than text:** no candidate window exists.
- **Overlapping matches:** advance by one rather than skipping a matched window.
- **Repeated letters:** exact frequencies, not mere membership, determine a match.

</details>
