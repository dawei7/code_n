# Replace All Digits with Characters

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/replace-all-digits-with-characters/) |
| Frontend ID | 1844 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The input `s` alternates by index: every even position contains a lowercase English letter, and every odd position contains a decimal digit. Define `shift(c, x)` as the letter found $x$ alphabet positions after letter `c`; a shift of zero returns `c` itself.

Replace each digit at odd index $i$ with `shift(s[i - 1], s[i])`, using the immediately preceding original letter. All requested shifts are guaranteed to stay at or before `'z'`. Return the resulting all-letter string without changing its length or its even-indexed characters.

### Function Contract

**Inputs**

- `s`: a string containing lowercase English letters at even indices and digits at odd indices.
- $1 \le \lvert\texttt{s}\rvert \le 100$.
- Every requested alphabet shift stays within `'a'` through `'z'`.
- Let $n=\lvert\texttt{s}\rvert$.

**Return value**

- Preserve every even-indexed letter.
- At each odd index $i$, replace digit `s[i]` with the character whose code is `ord(s[i - 1]) + int(s[i])`.
- Return the transformed string of length $n$.

### Examples

**Example 1**

- Input: `s = "a1c1e1"`
- Output: `"abcdef"`

The three shifts are `'a' + 1 = 'b'`, `'c' + 1 = 'd'`, and `'e' + 1 = 'f'`.

**Example 2**

- Input: `s = "a1b2c3d4e"`
- Output: `"abbdcfdhe"`

Each digit uses the letter directly to its left; the final `'e'` has no following digit and stays unchanged.

**Example 3**

- Input: `s = "x0"`
- Output: `"xx"`

A zero shift reproduces the preceding letter.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Convert the string to a mutable character list. Visit only indices `1, 3, 5, ...`, which are exactly the digit positions guaranteed by the contract. For each one, convert its digit character to an integer, add that offset to the character code of the preceding even-indexed letter, and convert the sum back to a character.

Earlier replacements never affect later shifts because every odd index refers to `i - 1`, an even index that is never modified. Each replacement therefore implements its own `shift` independently and exactly once. Even-indexed positions remain untouched, so joining the list yields precisely the required all-letter string.

#### Complexity detail

The loop processes half of the $n$ positions and the final join processes all $n$, giving $O(n)$ time. The mutable list and returned string use $O(n)$ space; beyond the output representation, the algorithm uses $O(1)$ auxiliary state.

#### Alternatives and edge cases

- **Repeated immutable concatenation:** Appending one character at a time can copy an ever-growing prefix and take $O(n^2)$ time in languages without optimized builders.
- **Mapping every index:** Branching on every character is correct but does unnecessary digit-versus-letter checks when index parity already identifies the role.
- **Zero shift:** Digit `'0'` becomes the same letter as its predecessor.
- **Largest valid shift:** The guarantee permits a result of exactly `'z'` but never beyond it.
- **Odd string length:** The last even-indexed letter has no digit after it and remains unchanged.
- **Single character:** There are no odd indices, so return the original letter.
- **Local dependency:** Each digit uses the immediately preceding even-indexed input letter, not a previously generated odd-index character.

</details>
