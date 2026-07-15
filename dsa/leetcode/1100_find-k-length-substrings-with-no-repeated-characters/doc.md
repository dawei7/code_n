# Find K-Length Substrings With No Repeated Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1100 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/) |

## Problem Description

### Goal

Given a string `s` and an integer `k`, consider every substring of `s` whose length is exactly `k`. Count how many of those substrings contain no repeated characters.

Substrings are contiguous and are counted by their positions, so identical valid text at different starting indices contributes more than once. The value `k` may exceed the length of `s`; in that case no length-`k` substring exists.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \leq n \leq 10^4$.
- `k`: the required substring length, where $1 \leq k \leq 10^4$.

**Return value**

The number of start indices whose length-`k` substring has pairwise distinct characters.

### Examples

**Example 1**

- Input: `s = "havefunonleetcode", k = 5`
- Output: `6`

The valid windows are `"havef"`, `"avefu"`, `"vefun"`, `"efuno"`, `"etcod"`, and `"tcode"`.

**Example 2**

- Input: `s = "home", k = 5`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(\min(k, 26))$

<details>
<summary>Approach</summary>

#### General

**Reject impossible window lengths.** If `k > n`, no requested substring fits. Because `s` uses only 26 lowercase letters, `k > 26` also makes an all-distinct window impossible. Either condition yields zero immediately.

**Maintain one exact-length window.** Store the frequency of each character in the current window. As `right` advances, add `s[right]`. Once more than `k` characters are present, remove `s[right - k]`, deleting its frequency entry when the count reaches zero. Each character enters and leaves the window once.

**Use the number of distinct keys.** When the window length is `k`, it has no repetition exactly when its frequency map contains `k` keys. Increment the answer for every such position. This counts overlapping windows independently, including repeated window text at different starts.

After each update, the frequency map describes exactly the last at most `k` characters ending at `right`. A full window is valid precisely when its `k` positions also contribute `k` distinct characters. Therefore every valid start is counted once when its right endpoint arrives, and no invalid window is counted.

#### Complexity detail

The scan performs constant expected hash-table work when each of the $n$ characters enters and leaves the window, for $O(n)$ time. At most $min(k,26)$ lowercase-letter keys are stored, giving $O(\min(k,26))$ auxiliary space.

#### Alternatives and edge cases

- **Build a set for every window:** This is simple but repeats up to $k$ character inspections per start, taking $O(nk)$ time.
- **Fixed 26-entry array:** It replaces hashing with indexed counts and uses $O(1)$ space under the lowercase alphabet contract.
- **`k > n`:** No complete window exists, so the result is zero.
- **`k > 26`:** The pigeonhole principle guarantees a repeated lowercase letter in every window.
- **`k = 1`:** Every one-character substring is valid, including repeated letters at different indices.
- **Overlapping valid windows:** Each start position is counted separately even when windows share most characters.

</details>
