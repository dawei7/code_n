# Maximum Number of Vowels in a Substring of Given Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1456 |
| Difficulty | Medium |
| Topics | String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) |

## Problem Description
### Goal

Given a lowercase English string `s` and an integer `k`, consider every
substring whose length is exactly `k`. A substring is a contiguous sequence of
characters, so its positions must be adjacent in the original string; letters
cannot be skipped or rearranged.

The English vowels for this problem are exactly `a`, `e`, `i`, `o`, and `u`.
Count how many of those vowels occur in each length-$k$ substring and return
the largest count. Repeated vowels count separately, and the answer may range
from $0$ when no eligible window contains a vowel to $k$ when some whole
window consists of vowels.

### Function Contract
**Inputs**

- `s`: a string of $n$ lowercase English letters, where
  $1 \le n \le 10^5$.
- `k`: the required substring length, where $1 \le k \le n$.

**Return value**

Return an integer equal to the maximum number of characters from
`{"a", "e", "i", "o", "u"}` in any contiguous substring of `s` having
exactly length `k`.

### Examples
**Example 1**

- Input: `s = "abciiidef", k = 3`
- Output: `3`
- Explanation: The window `"iii"` contains three vowels, which is the largest
  possible count for a length-$3$ window.

**Example 2**

- Input: `s = "aeiou", k = 2`
- Output: `2`
- Explanation: Every adjacent pair consists only of vowels.

**Example 3**

- Input: `s = "leetcode", k = 3`
- Output: `2`
- Explanation: Windows such as `"lee"`, `"eet"`, and `"ode"` each contain
  two vowels.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Why adjacent windows should share their work**

There are $n-k+1$ candidate substrings. Counting every candidate from scratch
would repeatedly inspect the $k-1$ positions shared by neighboring windows.
Instead, maintain the vowel count for one fixed-width window and update only
the two characters that change when the window moves one position right.

First count the vowels in `s[0:k]`. This establishes both the current count and
the initial best answer. Then let `right` visit positions from `k` through
`n - 1`. The new window ends at `right`, while the old window's leftmost
character is at `right - k`.

**Update the exact count for the shifted window**

For each shift, add one if `s[right]` is a vowel and subtract one if
`s[right - k]` is a vowel. Before the update, the count describes
`s[right-k:right]`; afterward, it describes
`s[right-k+1:right+1]`. No other character changes membership, so retaining
all shared characters' contribution is both sufficient and exact.

Compare the updated count with the best count seen so far. The best can never
exceed $k$, because a length-$k$ substring has only $k$ characters. Therefore,
if it reaches $k$, return immediately: no later window can improve it.

**Why the maximum cannot be missed**

The initial count is correct by direct inspection of the first length-$k$
substring. Each shift removes precisely the character that leaves and adds
precisely the character that enters, so by induction the maintained count is
correct for every subsequent length-$k$ substring. Updating the best after
each such count means it equals the maximum over every window processed so
far. Once the final window is processed, that set is all legal substrings, so
the returned best is the required global maximum.

#### Complexity detail

Let $n$ be the length of `s`. Initializing the first window takes $O(k)$, and
the remaining $n-k$ shifts each take constant time, for $O(n)$ total time.
The algorithm stores only two counts, an index, and a constant-size vowel set,
so its auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Recount every window:** Scanning each length-$k$ substring independently
  is correct but takes $O((n-k+1)k)$ time, which becomes quadratic when $k$ is
  proportional to $n$.
- **Prefix sums:** Store at every boundary the number of vowels seen so far;
  each window count is then a difference of two prefix values. This also takes
  $O(n)$ time but uses $O(n)$ auxiliary space when only the maximum is needed.
- **One-character windows:** When $k=1$, return `1` if any character is a vowel
  and `0` otherwise; the same sliding-window logic handles this directly.
- **Whole-string window:** When $k=n$, there is exactly one candidate, so the
  initialization is already the answer.
- **All consonants:** Every window count is zero, and the answer remains `0`.
- **All vowels:** The first window reaches the upper bound $k$, allowing an
  immediate return.
- **Repeated maxima:** The problem asks only for the count, so the location or
  number of tied windows does not affect the result.
- **Exactly five lowercase vowels:** Treat only `a`, `e`, `i`, `o`, and `u` as
  vowels; the source guarantees lowercase English input.

</details>
