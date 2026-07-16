# Number of Good Ways to Split a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1525 |
| Difficulty | Medium |
| Topics | Hash Table, String, Dynamic Programming, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/) |

## Problem Description
### Goal

Split a lowercase string at one boundary between adjacent characters, producing a nonempty left part and a nonempty right part whose concatenation is the original string. A split is good when the two parts contain the same number of distinct letters.

Count how many of the $n-1$ possible boundaries are good and return that count. Letter frequencies do not need to match across the pieces; only the number of different letters present on each side matters.

### Function Contract
**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \leq n \leq 10^5$.

**Return value**

Return the number of indices $i$ with $1 \leq i < n$ for which `s[:i]` and `s[i:]` contain equal numbers of distinct letters.

### Examples
**Example 1**

- Input: `s = "aacaba"`
- Output: `2`
- Explanation: Splits `("aac", "aba")` and `("aaca", "ba")` each have two distinct letters on both sides.

**Example 2**

- Input: `s = "abcd"`
- Output: `1`
- Explanation: Only `("ab", "cd")` balances two distinct letters on each side.

**Example 3**

- Input: `s = "aaaa"`
- Output: `3`
- Explanation: Every nonempty piece contains only the letter `a`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Initialize the unsplit suffix**

Store the frequency of every letter in the entire string as the initial right side, and start the left side as an empty set. The number of keys with positive frequency is exactly the number of distinct right-side letters.

Move the split boundary one character at a time, stopping before the final character so the right piece never becomes empty. Add the moved character to the left set and decrement its right frequency. When that frequency reaches zero, remove the key because the letter is no longer present on the right.

**Compare the maintained distinct counts**

After each move, the left set contains precisely the letters in the current prefix, while the right map contains precisely the letters in the remaining suffix. Their sizes therefore equal the required distinct-letter counts. Increment the answer whenever those sizes match.

Each boundary is examined exactly once, and the maintained structures evolve rather than being rebuilt. This covers all legal splits and counts each good split once.

#### Complexity detail

Building the right frequencies and scanning the split boundaries each take $O(n)$ time. Set and frequency updates are constant time, so total time is $O(n)$.

At most 26 lowercase letters can occupy either structure. The alphabet is fixed, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix and suffix arrays:** record the distinct count at every position from both directions, then compare adjacent entries. This is linear but uses $O(n)$ space.
- **Rebuild sets per split:** `set(s[:i])` and `set(s[i:])` are direct and correct but take $O(n^2)$ total time.
- **Bit masks:** two 26-bit masks can represent distinct letters, though right-side removals still require frequencies.
- **Length one:** no boundary produces two nonempty pieces, so the answer is zero.
- **All one letter:** every boundary is good because both sides have one distinct letter.
- **All distinct letters:** only a central boundary can balance the counts, and only when the length is even.
- **Frequency imbalance:** repeated counts do not matter once a letter remains present on both sides.
- **Final boundary:** process through index `n - 2`; moving the last character would create an invalid empty suffix.

</details>
