# Shifting Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 848 |
| Difficulty | Medium |
| Topics | Array, String, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/shifting-letters/) |

## Problem Description
### Goal
A shift replaces a lowercase English letter with the next letter of the alphabet, with `z` wrapping around to `a`. Repeating that operation advances the letter cyclically; for example, one shift changes `a` to `b`, while 26 shifts return any letter to itself.

You are given a lowercase string `s` and an equally long integer array `shifts`. For every index `i`, apply `shifts[i]` shifts to the first `i + 1` characters of the string. Return the final string after all prefix operations have been applied.

### Function Contract
**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \leq n \leq 10^5$.
- `shifts`: an integer array of length $n$, where $0 \leq \texttt{shifts[i]} \leq 10^9$.

**Return value**

Return the lowercase string produced by applying each indexed shift count to its corresponding prefix.

### Examples
**Example 1**

- Input: `s = "abc", shifts = [3,5,9]`
- Output: `"rpl"`

The successive prefix results are `"dbc"`, `"igc"`, and `"rpl"`.

**Example 2**

- Input: `s = "aaa", shifts = [1,2,3]`
- Output: `"gfd"`

**Example 3**

- Input: `s = "z", shifts = [1]`
- Output: `"a"`

The alphabet wraps after `z`.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Each position receives a suffix of the operations**

The operation at index `j` affects positions $0$ through $j$. Therefore the character at position `i` receives exactly the shifts whose indices satisfy $j \geq i$. Its total advance is

$$
T_i = \sum_{j=i}^{n-1} \texttt{shifts[j]}.
$$

Computing every $T_i$ independently would repeat work. Instead, scan from right to left while maintaining `total_shift`. Add `shifts[i]` before converting `s[i]`; the accumulator now equals $T_i$.

**Reduce the accumulated shift around the alphabet**

Only the remainder modulo 26 affects a lowercase letter. Keep `total_shift = (total_shift + shifts[i]) % 26` so even the largest input values stay small. Convert `s[i]` to its zero-based alphabet index, add the remainder modulo 26, and convert the result back to a character.

At each index, the maintained remainder equals $T_i \bmod 26$, so the produced letter is exactly the result of every prefix operation that covers that position. Since the scan fills all positions, joining the transformed characters yields the required final string.

#### Complexity detail

The reverse scan processes each of the $n$ positions once, taking $O(n)$ time. The mutable character list used to construct the returned immutable string contains $n$ characters, so the implementation uses $O(n)$ space.

#### Alternatives and edge cases

- **Simulate every prefix:** Applying each operation directly is straightforward and correct, but performs $Theta(n^2)$ character updates in the worst case.
- **Store all suffix sums:** A separate suffix-sum array also gives $O(n)$ time, but uses an additional $O(n)$ integers beyond the output buffer.
- **Difference-array view:** Prefix range additions can be encoded by endpoint differences and accumulated once; it is linear but less direct here than the right-to-left suffix total.
- **Zero shifts:** A zero contributes nothing, and an all-zero array returns `s` unchanged.
- **Large shift counts:** Reducing modulo 26 preserves the result and avoids carrying unnecessary large totals.
- **Wraparound:** Any transformed alphabet index at least 26 wraps back to the beginning.
- **Single character:** The sole value in `shifts` applies to that one character.
- **Repeated coverage:** Earlier characters receive at least as many indexed operations as later characters, but the operation magnitudes can still make their final remainders arbitrary.

</details>
