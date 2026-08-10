## General

**Ask for the longest valid substring ending at each position**

The longest answer can end anywhere, so the selected implementation computes a dynamic-programming value for every processed prefix. It creates `f` with `n + 1` entries and uses one-based DP positions:

> `f[i]` is the length of the longest valid parentheses substring ending at original character `s[i - 1]`.

`f[0] = 0` describes the empty prefix. The extra leading entry makes expressions such as `f[i - 2]` safe when a pair begins at the start of the string.

Only a `')'` character can end a non-empty valid parentheses string. Therefore entries corresponding to `'('` remain zero, and the loop performs transition logic only when `c == ')'`.

**Case one: the current closer follows an opener**

If `s[i - 2] == '('`, the final two characters are `"()"`. They contribute two characters and may attach directly after any valid substring ending before that opener:

```python
f[i] = f[i - 2] + 2
```

For `"()()"`, the last pair at positions three and four attaches to the valid length two ending at position two, producing four. The condition `i > 1` protects the `s[i - 2]` access when the current character is the first input character.

**Case two: the current closer follows an existing valid block**

When the previous character is not `'('`, a new longer valid suffix may have the shape

```text
( previous-valid-block )
```

Let `f[i - 1]` be the length of the valid block ending immediately before the current closer. The source calculates

```python
j = i - f[i - 1] - 1
```

Here `j` is the one-based position of the character immediately before that previous valid block. Its corresponding zero-based string index is `j - 1`.

If `j` is zero, there is no character before the block and no opener available for the current closer. The condition

```python
if j and s[j - 1] == "(":
```

requires both existence and the correct character type. Python treats zero as false, so it avoids indexing `s[-1]` as though the final string character were before the beginning.

**Join the wrapped block to an earlier adjacent valid block**

When `s[j - 1]` is `'('`, it pairs with the current `')'`. The wrapped portion has length `f[i - 1] + 2`. There may also be a valid substring immediately before that matching opener, whose length is `f[j - 1]`. The transition is

```python
f[i] = f[i - 1] + 2 + f[j - 1]
```

The final term is essential for concatenated structures. In `"()(())"`, the last closer wraps the inner `"()"`, but the earlier leading `"()"` is adjacent and belongs to the same valid substring. Without `f[j - 1]`, the method would report only four instead of six.

**Why the two cases are complete**

Every valid substring ending at a closer has a matching opener. If that opener is immediately before the closer, case one applies. Otherwise, at least one valid parenthesized block lies between them and ends at the previous character; case two jumps across the longest such block and tests the character before it. There is no third structural possibility.

If the test in case two fails, the current closer cannot extend a valid suffix ending at `i - 1`, and `f[i]` correctly stays at its initialized zero.

**Trace `"()(())"` with one-based DP positions**

- At `i = 2`, the characters are `"()"`, so `f[2] = f[0] + 2 = 2`.
- At `i = 3` and `i = 4`, the current characters are both `'('`, so `f[3]` and `f[4]` remain zero.
- At `i = 5`, the current `')'` immediately follows `'('`, so `f[5] = f[3] + 2 = 2`. This entry describes the inner pair at zero-based indices three and four.
- At `i = 6`, the previous valid block has length two. `j = 6 - 2 - 1 = 3`, and `s[2]` is the opener before that block. Wrapping adds four, while `f[2] = 2` adds the adjacent leading pair. Thus `f[6] = 6`.

This careful indexing is why `f` has one more element than `s`.

**Take the maximum over all ending positions**

`f[i]` concerns only a valid substring ending at one specific character. The globally longest substring may finish before the input ends, so the method returns `max(f)`. For an empty string, `f` is `[0]`, and `max(f)` safely returns zero.

**Why the recurrence is correct**

Assume earlier `f` entries correctly describe their longest valid suffixes. Case one appends a guaranteed pair to the best adjacent valid suffix. Case two uses the known valid suffix ending at `i - 1`, verifies the exact opener required before it, wraps that block, and adds the best valid suffix immediately before the opener. Each constructed interval is contiguous and well formed. Conversely, decomposing any valid suffix by the opener matched with its final closer leads to exactly one of these transitions, so no candidate is missed.

## Complexity detail

Let $n=\lvert s\rvert$.

- **Time complexity: $O(n)$.** The loop visits each character once, each transition uses constant-time indexing and arithmetic, and `max(f)` performs one additional linear scan.
- **Auxiliary space of the exact selected source: $O(n)$.** The list `f` has `n + 1` integer entries. This contradicts the variant manifest's $O(1)$ claim; constant space belongs to the two-direction counter method, not this dynamic-programming implementation.

The input string is immutable and the output is one integer.

## Alternatives and edge cases

- **Two directional counter scans:** Count openers and closers left-to-right and right-to-left. This achieves $O(n)$ time and $O(1)$ space and is the Competitive variant.
- **Index stack:** Store unmatched opener indices and invalid boundaries. It is linear time but may use $O(n)$ memory.
- **Brute-force substrings:** Validating every even-length candidate costs up to $O(n^3)$.
- **Empty string:** `max([0])` returns zero.
- **Only opening parentheses:** No DP transition runs, so the answer is zero.
- **Only closing parentheses:** Every candidate opener check fails, so the answer is zero.
- **Adjacent valid blocks:** The `f[j - 1]` term joins them into one longer substring.
- **Nested blocks:** Case two jumps over the previous valid interior to find its matching opener.
- **Invalid prefix or suffix:** DP values are local to ending positions, so invalid surrounding characters do not erase an interior maximum.
- **One-based versus zero-based indexing:** `i` is a DP prefix length, while `s[i - 1]` is the current character; mixing those systems causes off-by-one errors.
