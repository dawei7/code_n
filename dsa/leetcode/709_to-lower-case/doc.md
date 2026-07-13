# To Lower Case

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 709 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/to-lower-case/) |

## Problem Description
### Goal
Given a printable ASCII string `s`, replace every uppercase English letter with the corresponding lowercase letter.

Return the resulting string. Characters that are already lowercase remain unchanged, as do digits, punctuation, spaces, and other printable characters. The transformation changes letter case only; it does not remove characters, alter their order or positions, or apply language-specific case rules beyond the English alphabet.

### Function Contract
**Inputs**

- `s`: a nonempty string of printable ASCII characters

**Return value**

- The lowercased string

### Examples
**Example 1**

- Input: `s = "Hello"`
- Output: `"hello"`

**Example 2**

- Input: `s = "here"`
- Output: `"here"`

**Example 3**

- Input: `s = "LOVELY"`
- Output: `"lovely"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Recognize only uppercase English letters**

Scan each character and test whether it lies between `'A'` and `'Z'`. Digits, punctuation, spaces, and already lowercase letters do not satisfy this range and must be copied unchanged.

**Apply the ASCII case offset**

For an uppercase character, lowercase is exactly 32 code points later. Convert it with `chr(ord(character) + 32)` and append the result to an output buffer.

**Build once from buffered characters**

Collect transformed characters in a list and join them after the scan. This avoids repeatedly rebuilding an immutable string prefix.

**Why every output position is correct**

Each input position is handled independently. The range test selects exactly the uppercase ASCII letters, and the fixed offset maps each to its corresponding lowercase letter. Every unselected character is copied, so the joined sequence satisfies the contract at every position and preserves length and order.

#### Complexity detail

The algorithm performs constant work for each of the `n` characters, taking $O(n)$ time. The returned string and temporary character buffer contain `n` characters, using $O(n)$ space.

#### Alternatives and edge cases

- **Built-in lowercase conversion:** `s.lower()` is concise and linear for this ASCII contract, though it hides the character mapping.
- **Immutable-string concatenation:** appending one character to a growing string can repeatedly copy the prefix and degrade to $O(n^2)$ in implementations without concatenation optimization.
- **Repeated positional rescans:** find each next character by scanning from the beginning; it is correct but explicitly takes $O(n^2)$ time.
- An already lowercase string is returned unchanged in content.
- Digits, punctuation, and spaces are preserved.
- Mixed-case words transform each uppercase position independently.

</details>
