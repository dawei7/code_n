# String Compression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 443 |
| Difficulty | Medium |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/string-compression/) |

## Problem Description
### Goal
Given a mutable character array, divide it into maximal consecutive runs of equal characters. Encode each run by writing its character once, followed by the decimal digits of its length only when that length is greater than one.

Write the encoding into the beginning of the same array using constant extra space, and return the compressed prefix length. Counts of ten or more occupy several character positions, one per decimal digit. Only the first returned-length positions define the result; leftover array contents beyond them are irrelevant. Runs are based on adjacency, so separated occurrences of the same character are encoded independently.

### Function Contract
**Inputs**

- `chars`: a mutable list of single-character strings

**Return value**

- The native method returns the compressed length and leaves the compressed characters in the first positions of `chars`. The app-local `solve` returns `{"length": k, "prefix": chars[:k]}` so both parts of that outcome are verifiable.

### Examples
**Example 1**

- Input: `chars = ["a", "a", "b", "b", "c", "c", "c"]`
- Output: `{"length": 6, "prefix": ["a", "2", "b", "2", "c", "3"]}`

**Example 2**

- Input: `chars = ["a"]`
- Output: `{"length": 1, "prefix": ["a"]}`

**Example 3**

- Input: `chars = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]`
- Output: `{"length": 3, "prefix": ["a", "1", "2"]}`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate the unread run from the write position**

Use `read` to locate the first character of the next run and advance `end` until the character changes. The run length is `end - read`. Independently maintain `write`, the first array position not yet occupied by compressed output.

**Write one character and only necessary count digits**

Write the run's character at `chars[write]`. A run of length one needs no count. For a longer run, convert the count to decimal and write each digit separately, so length twelve becomes characters `"1"` and `"2"`, not one multi-character element.

**Why unread input is never overwritten**

Every compressed run uses at most as many positions as its original run: one position for a singleton, or one character plus at most the number of run elements needed to represent the count. Thus `write` never advances beyond the processed boundary `end`, so writes cannot destroy characters belonging to a future run.

**Why the returned prefix is complete**

Each maximal run is discovered exactly once and emits its required encoding in original order. After assigning `read = end`, the next iteration begins at the next run. When `read` reaches `n`, `write` is exactly the compressed length and all meaningful output lies in `chars[:write]`.

#### Complexity detail

The read boundary visits each input character once, and the total number of written characters is at most `n`, giving $O(n)$ time. Apart from the app's returned verification copy, the compression itself uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Build a separate compressed list:** is straightforward and linear but uses $O(n)$ additional space.
- **Repeatedly append by copying the accumulated output:** remains correct but can take $O(n^2)$ time when many singleton runs are emitted.
- **Single-character run:** write no count digit.
- **Multi-digit count:** write every decimal digit individually.
- **Alternating characters:** compression length equals the original length.
- **Entire array one run:** output one character followed by the run length's digits.

</details>
