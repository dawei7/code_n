# Remove Duplicate Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 316 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-duplicate-letters/) |

## Problem Description
### Goal
Given a nonempty lowercase string `s`, delete selected character occurrences to form a subsequence containing every distinct letter present in `s` exactly once. Retained characters must remain in their original relative order.

Among all subsequences satisfying that coverage, return the lexicographically smallest one. Choosing an early small letter is valid only when every required letter can still appear once afterward, and repeated occurrences cannot remain in the result. Lexicographic comparison uses normal lowercase alphabet order. The output length equals the number of distinct input letters and contains no character absent from the source.

### Function Contract
**Inputs**

- `s`: a nonempty string of lowercase English letters

**Return value**

The lexicographically smallest distinct-letter subsequence of `s`.

### Examples
**Example 1**

- Input: `s = "bcabc"`
- Output: `"abc"`

**Example 2**

- Input: `s = "cbacdcbc"`
- Output: `"acdb"`

**Example 3**

- Input: `s = "bbcaac"`
- Output: `"bac"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A smaller letter may replace a larger tentative choice**

Build the result from left to right in a stack. When a new letter is smaller than the stack top, placing it earlier would improve the lexicographic result. Removing the top is safe only if another occurrence of that removed letter still lies ahead; otherwise removing it would make the required distinct-letter set impossible to complete.

Precompute each letter's last index. For a new letter at index `i`, repeatedly pop a larger stack top while that top's last occurrence is greater than `i`. Stop as soon as the top is smaller, equal, or no longer available later. Then append the new letter.

**One membership set prevents duplicate output letters**

If the current letter is already in the stack, skip it. The earlier copy is already part of the tentative subsequence, and reconsidering a duplicate cannot introduce a new required letter. Whenever a letter is popped, remove it from the membership set so a later copy may be selected again.

For `cbacdcbc`, reading `b` pops `c` because another `c` remains. Reading `a` then pops `b` for the same reason, leaving `a` as the best feasible prefix. Later, `d` cannot be popped when the next `c` arrives because there is no later `d`; the final answer is therefore `acdb`, not the impossible prefix `acd...` with `d` discarded.

**Each retained prefix is the smallest feasible prefix**

Before a new letter is appended, every popped letter is both larger than it and still recoverable later. Replacing those letters with the current one strictly improves the prefix without losing feasibility. The first top that remains cannot be removed safely or would not improve the prefix, so no lexicographically smaller feasible stack prefix exists at that point.

Every distinct letter is eventually retained: a skipped letter is already present, while a popped letter has a guaranteed later occurrence. At the end there is no future input, so the stack contains each distinct letter exactly once. The prefix argument at every append makes that valid result lexicographically smallest.

#### Complexity detail

Each input character is considered once. A selected occurrence is pushed once and can be popped at most once, so all stack operations total $O(n)$ time. The last-position table, stack, and membership set hold at most 26 lowercase letters, which is $O(1)$ space for the fixed alphabet.

#### Alternatives and edge cases

- **Repeatedly test candidate subsequences:** can be correct but may rescan long suffixes for many candidate positions and take $O(n^2)$ time.
- **Sort the distinct letters:** loses the subsequence-order constraint; a string such as `"zyx"` must remain `"zyx"`.
- **Pop every larger stack top:** fails when the removed letter has no later occurrence. The last-position check is essential.
- A one-letter string and a string containing one repeated letter both return that letter. Equal letters are skipped rather than compared in the pop loop.

</details>
