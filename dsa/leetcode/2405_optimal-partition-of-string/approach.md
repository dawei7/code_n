## General

**Extend the current part as far as validity allows**

Each substring in the partition must contain unique characters. The greedy rule is:

- keep appending while the next character has not appeared in the current substring;
- when it repeats, end the current substring immediately before that character and start a new substring with it.

The exact code represents letters already in the current part with a 26-bit mask.

**Map lowercase letters to mask bits**

`ord(c) - ord("a")` maps each lowercase character to an index `0` through `25`. Bit `x` is one when that letter has already appeared in the current substring.

The membership test:

```python
mask >> x & 1
```

extracts that bit. Adding the letter uses `mask |= 1 << x`.

The fixed lowercase alphabet means this state is one integer rather than a growing set.

**Start with one substring**

The input is guaranteed nonempty, so at least one substring is required. `ans` begins at one and `mask` begins empty.

For each character, if its bit is already set, the current substring cannot legally include it. The code increments `ans` and resets `mask = 0`. It then executes the common insertion line, adding the current character as the first member of the new substring.

Forgetting that final insertion would allow an immediate duplicate to slip into the new part.

**Why a repeated letter forces some cut**

Suppose current substring began at index `l` and the new character `s[r]` already appeared at index `p` within `[l,r-1]`. Any valid partition must place a boundary somewhere after `p` and no later than `r`; otherwise, both equal characters occupy one substring.

The greedy method puts the boundary immediately before `r`, which is the latest possible location. It preserves the longest possible current part and leaves no extra earlier characters for future substrings.

Cutting earlier cannot avoid the need for this boundary region and cannot reduce the number of parts needed for the suffix. It only shortens a valid part unnecessarily.

**Trace `"abacaba"`**

The first `a` and `b` set distinct bits. The next `a` repeats, so the first part ends as `"ab"` and a new part begins with `a`.

That part can extend through `c`, but the next `a` repeats and forces another cut. Continuing similarly yields four parts. The exact character grouping may be `"ab" | "ac" | "ab" | "a"`, and only the count is returned.

For `"ssssss"`, every `s` after the first repeats the current one-character part, so each forces a new substring and the answer is six.

**Exchange argument for greedy optimality**

Consider the first position where greedy cuts. The current character duplicates one earlier in the current prefix, so every valid partition needs a cut between those occurrences. Move the first cut of any optimal partition in that interval rightward to the greedy boundary, immediately before the duplicate.

This move cannot create a duplicate in the first part because greedy's prefix was valid up to that point. It also removes characters from the next part rather than adding earlier duplicates to it, so it does not increase the number of parts needed.

After making the same first cut, the remaining suffix is the identical smaller problem. Repeating the exchange proves a partition with greedy boundaries is optimal.

**Maintain the scan invariant**

Before each character, `mask` contains exactly the letters in the current unfinished substring, all unique, and `ans` counts that substring plus all completed ones.

A new letter preserves uniqueness and is added. A repeated letter closes the valid current part, increments the count, clears its bits, and begins a new valid part with the current letter. Thus, the invariant holds through the whole string, and `ans` is the number of greedy-optimal parts.

## Complexity detail

Let $n$ be the string length. The lazy `map` and loop process each character exactly once. Every iteration performs constant-time code-point arithmetic and bit operations. Total time is $O(n)$.

The mask holds 26 bits regardless of $n$, and other variables are scalar. Auxiliary space is $O(1)$.

The function returns only a count and does not allocate substring copies.

## Alternatives and edge cases

- **Set for the current part:** A set provides clearer membership semantics and remains $O(1)$ space for 26 letters, but the bitmask has lower overhead.
- **Dynamic programming over cut positions:** It can find a minimum but is unnecessary because the latest-valid-cut greedy choice is provably optimal.
- **One character:** Initialization returns one part.
- **All characters unique:** No reset occurs, so the entire string is one substring.
- **All characters equal:** Every character after the first forces a new part.
- **Repeated character after a cut:** The reset removes prior-part bits, so characters may repeat across different substrings.
- **Current character insertion:** It must be added after reset as the first letter of its new part.
- **Lowercase-only contract:** It makes a 26-bit integer sufficient.
- **Nonempty input:** It justifies initializing `ans` to one rather than zero.
