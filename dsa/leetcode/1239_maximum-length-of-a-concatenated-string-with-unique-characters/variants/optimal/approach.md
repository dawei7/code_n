## General

**Represent a set of lowercase letters with 26 bits**

Each lowercase letter maps to one bit: `a` to bit zero, `b` to bit one, through `z` to bit 25. A mask stores one at a letter’s bit exactly when that letter is present.

For a string `t`, the code maps each character to `b = ord(c) - 97`. It tests `x >> b & 1` to see whether bit `b` is already set. If so, `t` itself contains a duplicate character and can never participate in a valid concatenation, so `x` is reset to zero and processing that string stops.

Otherwise, `x |= 1 << b` adds the character. Because input strings are nonempty, a valid string produces a positive mask; zero is reserved for invalid strings and the empty concatenation.

**Maintain every valid combination mask**

The list `s` begins as `[0]`, representing the choice to select no strings. After processing some prefix of `arr`, `s` contains a mask for every valid concatenation obtainable as a subsequence of that prefix.

For a valid current string mask `x`, it can be appended to an existing combination `y` exactly when they share no letter. Bitwise AND detects overlap:

`(x & y) == 0`.

When disjoint, `x | y` is the union mask for the extended concatenation. The source adds all such unions with:

`s.extend((x | y) for y in s if (x & y) == 0)`.

Existing masks remain in `s`, representing the choice to skip the current string. Newly appended masks represent taking it.

**Why extending while iterating the same list is safe here**

Python’s list iterator can observe elements appended during iteration. That deserves attention because the generator loops over `s` while `extend` adds to `s`.

Every newly added mask has the form `x | y` and therefore contains every bit of the nonzero `x`. When the iterator later reaches that new mask, `x & (x | y)` is nonzero, so the condition fails and no second copy of the same input string is appended.

Thus the operation terminates and has the intended effect. Taking a snapshot of the old list would be clearer, but the overlap condition makes the exact source correct.

**Why invalid individual strings are discarded**

If a string repeats a character internally, every concatenation containing it also repeats that character. No choice of other strings can repair a duplicate, because concatenation only adds characters. Skipping such a string entirely loses no valid solution.

**Subsequence order is respected**

Strings are processed in original array order. A new state combines the current string only with states formed from earlier strings, so every represented choice follows subsequence order. The current problem’s objective depends only on the selected character set, not the textual order, but the construction still satisfies the formal subsequence requirement.

**A trace for `["un","iq","ue"]`**

The initial state is zero.

- `"un"` creates the mask for letters `u,n`, so `s` represents empty and `"un"`.
- `"iq"` is disjoint from `"un"`. It adds the mask for `"iq"` and the union for `"uniq"`.
- `"ue"` can combine with the empty mask and with `"iq"`, producing `"ue"` and `"ique"`. It overlaps `"un"` and `"uniq"` on `u`, so those combinations are rejected.

The largest mask has four set bits.

**Obtain length with `bit_count`**

A valid mask has one set bit per distinct character in its concatenation. `x.bit_count()` therefore equals the concatenated length. The final generator evaluates every stored state, and `max` returns the greatest length.

The initial zero ensures `s` is never empty, even if every input string is internally invalid. In that case, the answer is zero.


Assume `s` represents exactly all valid selections from the already processed strings. For the next string, an internally invalid mask cannot belong to any valid selection. For a valid mask `x`, every solution either skips it, already represented by an old state, or takes it alongside a prior selection whose mask is disjoint, represented by one appended union.

The AND test accepts exactly the compatible prior selections. Hence the invariant holds after each string. At the end, every valid subsequence has a state, every state is valid, and maximum bit count returns the requested optimum.

**Duplicate masks**

`s` is a list rather than a set, so different subsequences that use the same character set may create duplicate integer masks. This does not change correctness because they have the same compatibility and length. It can increase practical work, but there are still at most \(2^n\) subsequences across \(n\) strings.

## Complexity detail

Let \(n=\lvert\texttt{arr}\rvert\) and let \(S\) be the sum of all string lengths. Building individual masks costs \(O(S)\). Across processing, at most one state exists per selected subsequence occurrence, so the total state-generation and scanning work is \(O(2^n)\) in the worst case. Final bit counting is also \(O(2^n)\). Total time is \(O(S+2^n)\).

The state list can contain \(O(2^n)\) masks, and the generator itself is lazy. Auxiliary space is \(O(2^n)\), which also covers transient growth during `extend`.

## Alternatives and edge cases

- **Snapshot before extending:** Iterate over `s[:]` or its original length. This makes “use the current string at most once” explicit, at the cost of a temporary list.
- **Set of masks:** Deduplicate equivalent character sets and often reduce work. Hashing adds overhead but preserves the same worst-case exponential bound.
- **Backtracking with one mask:** Explore take/skip choices recursively using only \(O(n)\) stack space, though time remains exponential.
- **String with internal duplicates:** It is discarded because no valid concatenation can include it.
- **Overlap between two valid strings:** Bitwise AND rejects their combination immediately.
- **All strings mutually disjoint:** Every subset is valid, so the state list reaches \(2^n\) entries and the answer is the sum of all lengths, at most 26.
- **All choices invalid:** The initial zero state remains and `max` returns zero.
- **Different subsequences with the same mask:** The list may store duplicates, which affects constants but not the result.
- **Alphabet bound:** Only 26 bits are needed because every character is lowercase English.
- **Required Python version:** `int.bit_count` must be available; older versions can count set bits with another method.
