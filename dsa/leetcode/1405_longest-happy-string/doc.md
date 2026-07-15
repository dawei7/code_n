# Longest Happy String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1405 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/longest-happy-string/) |

## Problem Description

### Goal

Three integers `a`, `b`, and `c` give the available quantities of the letters `"a"`, `"b"`, and `"c"`. Construct a string using no more than each available quantity.

The string is happy when it contains none of `"aaa"`, `"bbb"`, or `"ccc"` as a substring. Return any happy string with the maximum possible length. Not every available character must be used when one letter is too numerous to separate safely, and different maximum-length answers are allowed.

### Function Contract

**Inputs**

- `a`, `b`, and `c`: available nonnegative counts, each at most 100, with at least one character available.

Let $N = a + b + c$.

**Return value**

- Any longest string over `"a"`, `"b"`, and `"c"` that respects the three budgets and has no run of three equal letters.

### Examples

**Example 1**

- Input: `a = 1, b = 1, c = 7`
- Output: one valid answer is `"ccaccbcc"`.

**Example 2**

- Input: `a = 7, b = 1, c = 0`
- Output: one valid answer is `"aabaa"`.

**Example 3**

- Input: `a = 2, b = 2, c = 2`
- Output: any six-character happy arrangement within the budgets.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Store the positive remaining counts in a max-heap of at most three `(count, letter)` entries. At each step, tentatively take the most abundant letter.

If appending it would create three equal trailing characters, take the second-most abundant letter instead. Append that fallback, decrement and reinsert it when copies remain, then restore the blocked first entry unchanged. If no fallback exists, no character can be appended and construction stops. Otherwise append the most abundant letter normally and reinsert its reduced count.

Choosing the largest currently legal count prevents the dominant supply from becoming harder to separate later. When the largest is temporarily illegal, some different letter is necessary; choosing the largest alternative preserves the same balance. If the heap offers no alternative, every remaining character equals the forbidden trailing pair, proving that no longer happy extension exists. Thus the greedy process reaches maximum possible length.

#### Complexity detail

Each appended character performs a constant number of heap operations on at most three entries, so $O(\log 3)=O(1)$ work per output character and $O(N)$ total time. The heap has at most three entries and uses $O(1)$ auxiliary space, excluding the returned string.

#### Alternatives and edge cases

- **Memoized exhaustive search:** Try every legal next letter for every remaining-count state. It finds an optimum but can require $O(abc)$ states and store long suffix results.
- **Always take the largest:** Ignoring the last two output characters can create a forbidden triple even when another letter remains available.
- **Dominant letter:** Some copies must remain unused when the other letters cannot provide enough separators.
- **Only one letter:** At most two copies can be returned.
- **Balanced counts:** Every character can be used.
- **Multiple answers:** Character order need not match a sample; validity and maximum length determine correctness.

</details>
