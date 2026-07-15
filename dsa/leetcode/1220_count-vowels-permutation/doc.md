# Count Vowels Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1220 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-vowels-permutation/) |

## Problem Description

### Goal

Given an integer `n`, count the strings of length `n` that contain only the lowercase vowels `a`, `e`, `i`, `o`, and `u` and obey all of these adjacency rules:

- Each `a` may be followed only by `e`.
- Each `e` may be followed only by `a` or `i`.
- Each `i` may be followed by any vowel except `i`.
- Each `o` may be followed only by `i` or `u`.
- Each `u` may be followed only by `a`.

Return the number of valid strings modulo $M=10^9+7$.

### Function Contract

**Inputs**

- `n`: The required string length, where $1\le n\le2\cdot10^4$.

**Return value**

- The number of vowel strings of length `n` satisfying every transition rule, reduced modulo $M$.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `5`

Each individual vowel is valid.

**Example 2**

- Input: `n = 2`
- Output: `10`

The valid strings are `ae`, `ea`, `ei`, `ia`, `ie`, `io`, `iu`, `oi`, `ou`, and `ua`.

**Example 3**

- Input: `n = 5`
- Output: `68`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Summarize a prefix by its final vowel.** Track five counts for valid strings of the current length ending in `a`, `e`, `i`, `o`, and `u`. Strings with the same last vowel have identical legal choices for the next position, so their internal characters no longer need to be retained.

**Reverse the stated transitions to update ending counts.** A new string ending in `a` may come from previous endings `e`, `i`, or `u`; one ending in `e` comes from `a` or `i`; one ending in `i` comes from `e` or `o`; one ending in `o` comes only from `i`; and one ending in `u` comes from `i` or `o`. Compute all five new values from the old tuple simultaneously and reduce them modulo $M$.

**Why the recurrence counts every valid string once.** Removing the last character from a valid length-$\ell$ string leaves one valid length-$(\ell-1)$ prefix and an allowed transition to its final vowel. Conversely, appending any permitted successor to a counted prefix creates a valid longer string. The predecessor groups are disjoint because a complete string has one final vowel, so the recurrence neither omits nor duplicates strings. Starting with one string per vowel at length one and summing the five counts after `n` positions gives the answer.

#### Complexity detail

Each of the `n - 1` extensions performs a fixed number of arithmetic operations, so the time is $O(n)$. Only five rolling counts are retained, giving $O(1)$ auxiliary space. Modular reduction keeps every stored value bounded by $M$.

#### Alternatives and edge cases

- **Enumerate every valid string:** Recursive generation follows the rules directly but visits exponentially many prefixes before reducing the final count.
- **Full dynamic-programming table:** Storing five counts for every length is correct and takes $O(n)$ space, but older rows are never needed.
- **Matrix exponentiation:** Encoding the transitions in a $5\times5$ matrix reduces time to $O(\log n)$, though the constant-size matrix machinery is more complex than required here.
- **Length one:** No adjacency rule is applied, so all five vowels count.
- **Simultaneous updates:** Every new count must use the previous length's tuple; overwriting one count early corrupts later transitions.
- **Modulo placement:** Reducing after each fixed-size sum is equivalent to reducing only at the end and prevents unbounded integers.

</details>
