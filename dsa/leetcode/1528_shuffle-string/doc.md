# Shuffle String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1528 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/shuffle-string/) |

## Problem Description
### Goal

Given a lowercase string `s` and an integer array `indices` of the same length, shuffle the string by moving the character originally at position `i` to position `indices[i]` in the result.

Every value in `indices` is unique and lies within the string's index range, so `indices` is a permutation of all result positions. Return the string obtained after every character has been moved to its specified destination.

### Function Contract
**Inputs**

- `s`: A string of $n$ lowercase English letters, where $1 \leq n \leq 100$.
- `indices`: A length-$n$ integer array containing unique values from 0 through $n-1$.

**Return value**

Return the length-$n$ string whose character at position `indices[i]` equals `s[i]` for every original index `i`.

### Examples
**Example 1**

- Input: `s = "codeleet", indices = [4, 5, 6, 7, 0, 2, 1, 3]`
- Output: `"leetcode"`
- Explanation: Each source character is written to its paired destination position.

**Example 2**

- Input: `s = "abc", indices = [0, 1, 2]`
- Output: `"abc"`
- Explanation: The identity permutation leaves every character in place.

**Example 3**

- Input: `s = "aiohn", indices = [3, 1, 4, 2, 0]`
- Output: `"nihao"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Read `indices` as destinations**

The array does not describe which source character should be read at each result position. Instead, `indices[i]` is the destination of `s[i]`. Allocate a length-$n$ character array and, for every paired `(character, destination)`, perform `shuffled[destination] = character`.

The uniqueness guarantee is what makes direct placement complete. No two source characters compete for one destination. Because there are $n$ distinct destination values and every value lies from 0 through $n-1$, every result slot is written exactly once; no fallback or collision handling is needed.

**Join after all positions are filled**

Strings are immutable in Python, so repeatedly rebuilding a partial string would add unnecessary work. A mutable list supports constant-time indexed placement, and one final `"".join(shuffled)` constructs the required string.

For every original index `i`, the algorithm writes exactly `s[i]` into `indices[i]`, which is the transformation required by the contract. Since every output position receives one such write, the joined list is both complete and uniquely determined.

#### Complexity detail

The placement loop processes each of the $n$ characters once, and joining the result also processes $n$ characters, giving $O(n)$ time. The destination list contains $n$ characters, so auxiliary space is $O(n)$.

The input permutation is not modified. Although some languages can encode the permutation in place, the returned immutable string still requires storage for its characters.

#### Alternatives and edge cases

- **Sort `(destination, character)` pairs:** sorting reconstructs the correct order but costs $O(n\log n)$ time instead of using the permutation directly.
- **Search for each destination:** repeatedly calling `indices.index(destination)` is correct but performs up to $n$ searches of length $n$, giving $O(n^2)$ time.
- **Cycle-based in-place permutation:** cycles can rearrange a mutable character array, but they complicate the implementation and still require constructing the returned string.
- **Identity permutation:** each write targets its existing position, so the original string is returned unchanged.
- **Single character:** the only legal destination is 0, and that character remains in place.
- **Repeated characters:** characters need not be unique; placement follows their source positions, not their values.
- **One long cycle:** direct destination writes handle it exactly like any other permutation without explicit cycle detection.

</details>
