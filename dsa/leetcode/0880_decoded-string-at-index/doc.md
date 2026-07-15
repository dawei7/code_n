# Decoded String at Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 880 |
| Difficulty | Medium |
| Topics | String, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/decoded-string-at-index/) |

## Problem Description
### Goal
Read the encoded string `s` from left to right to form a tape. A lowercase letter is appended to the current tape. A digit `d` writes the entire current tape another `d - 1` times, so the tape becomes `d` consecutive copies of what it was before the digit.

Given a one-based position `k`, return the letter occupying that position in the fully decoded tape. The decoded string may be enormously larger than the encoding and should not need to be constructed.

### Function Contract
**Inputs**

- `s`: an encoded string of length $q$, where $2 \leq q \leq 100$. It begins with a lowercase English letter, and every other character is a lowercase letter or a digit from `2` through `9`.
- `k`: a one-based decoded position, where $1 \leq \texttt{k} \leq 10^9$ and the decoded tape has at least `k` letters.
- The complete decoded length is guaranteed to be less than $2^{63}$.

**Return value**

Return the single lowercase letter at one-based position `k` in the decoded tape.

### Examples
**Example 1**

- Input: `s = "leet2code3", k = 10`
- Output: `"o"`

The tape is `"leetleetcodeleetleetcodeleetleetcode"`.

**Example 2**

- Input: `s = "ha22", k = 5`
- Output: `"h"`

The tape is `"hahahaha"`.

**Example 3**

- Input: `s = "a2345678999999999999999", k = 1`
- Output: `"a"`

The tape contains only repetitions of `"a"`, even though its total length is enormous.

### Required Complexity
- **Time:** $O(q)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Measure the tape without constructing it**

Scan the encoding forward while maintaining `decoded_length`. A letter adds one; a digit `d` multiplies the length by `d`. Stop at the first encoding position whose decoded prefix reaches or passes `k`, since later characters cannot affect the requested position.

**Undo the encoding from right to left**

Walk backward through that relevant prefix. When the current character is a digit `d`, the current tape consists of `d` identical copies of the previous tape. First execute `decoded_length //= d`, then map the one-based position into one copy with `k = (k - 1) % decoded_length + 1`.

When the current character is a letter, it was appended at position `decoded_length`. If `k == decoded_length`, that letter is the answer; otherwise, remove its contribution with `decoded_length -= 1` and continue.

The forward pass records the exact length produced by every relevant prefix. Each reverse step maps the requested position to the equivalent position before the last encoding operation. This preserves the identity of the target character until the responsible appended letter is reached, proving the returned character is correct.

#### Complexity detail

The algorithm scans at most $q$ characters forward and the same prefix backward, so it takes $O(q)$ time. It stores only indices, lengths, and the target position, requiring $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Build the decoded tape:** Explicit expansion is simple but can require time and memory proportional to a decoded length near $2^{63}$.
- **Recursive expansion:** Recursively forming repeated prefixes has the same prohibitive output-size cost and may also add call-stack depth.
- **Store every prefix length:** A length array supports the reverse pass but uses $O(q)$ space; the stopping index and one running length are sufficient.
- **Position at a repetition boundary:** The one-based mapping `(k - 1) % decoded_length + 1` correctly maps the final position of a copy to the previous tape's final position.
- **No digits before the answer:** Reverse processing simply removes later letters until it reaches the requested appended character.
- **Repeated digits:** Each digit is undone separately, even when the conceptual tape is already extremely large.
- **Single distinct letter:** Every valid position returns that letter regardless of the repetition factors.
- **Wide length arithmetic:** Fixed-width implementations should use a 64-bit type for `decoded_length`, matching the stated decoded-length guarantee.

</details>
