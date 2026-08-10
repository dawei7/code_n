## General

**Turn the encoding rule into a deterministic walk**

The input is not an arbitrary stream that may be split into characters in several different ways. Its first unread bit tells us exactly how many bits the next character occupies:

- A leading `0` is a complete one-bit character, so the next unread position is one step later.
- A leading `1` starts a two-bit character. The following bit belongs to that same character, whether it is `0` or `1`, so the next unread position is two steps later.

That observation removes the need for backtracking, dynamic programming, or trying different partitions. Starting at index `0`, there is only one legal move at every character boundary. The exact solution stores the next unread position in `i`. Its update,

`i += bits[i] + 1`,

compactly represents both rules. If `bits[i]` is `0`, the added amount is `1`. If `bits[i]` is `1`, the added amount is `2`.

**Why the loop stops before the final bit**

The question is specifically whether the last bit is a one-bit character. We therefore do not need to decode that bit after reaching it. Instead, the loop processes characters only while `i < n - 1`, where `n - 1` is the final index.

There are two meaningful ways the walk can finish:

- It lands exactly on `n - 1`. Every earlier character has been consumed, and the last bit is now the first unread bit. The input is guaranteed to end in `0`, so that last bit is a valid one-bit character. The answer is `True`.
- It jumps from an earlier `1` to `n`. That jump consumed two bits, and the final bit was the second half of that two-bit character. The answer is `False`.

The return expression `i == n - 1` distinguishes exactly these cases. The pointer cannot stop at some unrelated position beyond `n` under the valid encoding contract: every move is one or two positions, and the final bit is `0`.

**The key invariant**

At the start of every loop iteration, `i` points to the first bit of the next character, never to the second bit of a two-bit character. This is true initially because index `0` begins the encoded sequence. If the current bit is `0`, advancing once skips precisely that one-bit character. If it is `1`, advancing twice skips precisely the complete two-bit character. Thus the invariant remains true after every update.

This invariant is what makes reading `bits[i]` safe and meaningful. Without it, seeing a `0` would not tell us whether it was a standalone character or the second bit of `10`. Because the walk always arrives at character boundaries, that ambiguity never occurs.

**Walk through `[1, 0, 0]`**

Here `n = 3` and the final index is `2`.

1. Start with `i = 0`. Since `bits[0] = 1`, the first character occupies indices `0` and `1`. Add `2`, giving `i = 2`.
2. The condition `i < n - 1` is now false because `i` is the final index.
3. The return test `i == n - 1` is true.

The encoding is therefore `10 | 0`, and the last bit is a one-bit character.

**Walk through `[1, 1, 1, 0]`**

Here the final index is `3`.

1. Start at `i = 0`. The leading `1` consumes indices `0` and `1`, so `i` becomes `2`.
2. Index `2` also contains `1`, so it starts another two-bit character using indices `2` and `3`. The pointer becomes `4`.
3. The pointer passed the final index rather than landing on it, so `i == n - 1` is false.

The unique encoding is `11 | 10`. The final `0` belongs to the last two-bit character.

**Why looking only at the final two bits is insufficient**

A suffix such as `10` does not by itself prove that those two bits form one character. The `1` might already be the second bit of an earlier two-bit character. Character boundaries depend on the complete prefix. The left-to-right walk reconstructs those boundaries with constant state, which is both simple and conclusive.

**Why this proves the returned answer**

The deterministic parsing rule gives the encoded array one unique sequence of character boundaries. By the invariant, the algorithm follows exactly those boundaries. When parsing all characters before the final position, it either exposes the final `0` as a new character or consumes it as part of a two-bit character. Those are exhaustive and mutually exclusive possibilities. The final equality test returns true in the first case and false in the second, so the result is correct.

## Complexity detail

Let `n` be the number of bits. Each iteration advances `i` by at least one and never moves it backward. No bit is used as the start of a character more than once, so the loop performs at most `n - 1` iterations. The time complexity is `O(n)`.

The method stores only `i` and `n`, regardless of input size. It does not allocate a decoded array, recursion stack, or dynamic-programming table. Its auxiliary space complexity is `O(1)`. The input list itself is read without modification and is not counted as auxiliary space.

Although every two-bit character lets the pointer skip an extra position, asymptotic analysis still uses the worst case. An array with many one-bit characters advances mostly one position at a time, so linear time is the tight general bound.

## Alternatives and edge cases

- **Count consecutive ones immediately before the final zero:** The last zero is standalone exactly when that run of ones has even length. This can also run in `O(n)` time and `O(1)` space, and it may scan backward only through a suffix. The forward parser is usually easier to justify because it follows the encoding definition directly and never depends on deriving a parity rule.

- **Dynamic programming over positions:** One could mark which indices are reachable character boundaries. That is unnecessary because every reachable boundary has only one legal next move; there is no branching to resolve. It would add `O(n)` storage without improving the time bound or clarity.

- **Recursive decoding:** Recursively consume one or two bits according to the leading bit. This expresses the same deterministic walk but uses up to `O(n)` call-stack space and risks recursion-depth limits on large input.

- **Inspect only the last two or three bits:** Local suffix patterns can be misleading because a nearby `1` may or may not begin a character depending on earlier boundaries. Any shortcut must account for the full consecutive run before the last zero; the direct walk avoids this trap.

- **Single bit `[0]`:** The loop never runs because `i` already equals the final index. The method returns `True`, correctly treating the only bit as a one-bit character.

- **Final zero paired as `10`:** If the pointer reaches the `1` immediately before the final bit, it advances by two to `n`. The equality test is false, correctly recognizing that the zero was consumed by a two-bit character.

- **Many leading zeroes:** Every zero advances the pointer once. The algorithm still preserves character boundaries, and the final zero is standalone when the pointer eventually lands on it.

- **The guaranteed trailing zero matters:** The return rule relies on the contract that the encoded sequence ends in `0`. Under the stated problem constraints this is always true; no extra validation for malformed input is required.
