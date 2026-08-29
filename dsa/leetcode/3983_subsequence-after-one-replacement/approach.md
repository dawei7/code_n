## General

A usual subsequence check keeps one pointer into `s` and scans `t` from left to right. A matching character advances the pointer; a nonmatching character is skipped.

Here one character of `s` may be replaced, so the scan must preserve two kinds of progress:

- `i0`: the longest prefix of `s` that can be matched exactly, using no replacement;
- `i1`: the longest prefix of `s` that can be matched using at most one replacement.

Both values are prefix lengths, so `i0=3` means `s[0:3]` has been matched. The next required character is `s[i0]`.

The source scans `t` with index `j`. After every processed character, it retains only the greatest reachable prefix length in each category.

**Why the longest prefix is enough**

Suppose two exact states have matched prefix lengths `a<b` after consuming the same portion of `t`. State `b` dominates `a`: it has matched every character that `a` has and more, while using the same zero replacements. Any future characters capable of finishing from `a` can be considered from the more advanced position `b` without needing to recover skipped target characters.

The same reasoning applies among states that may already have used the one replacement. Thus one maximum length per replacement budget is sufficient.

However, `i0` cannot be discarded in favor of `i1`. The longer `i1` route may have spent its replacement, while the exact route still has the replacement available for a future mismatch. The two budgets must remain separate.

**Extending the at-most-one-replacement state exactly**

For current target character `t[j]`, if it matches the next character needed by `i1`, that state can advance without spending any additional replacement:

```python
if s[i1] == t[j]:
    i1 += 1
```

If the path represented by `i1` already used a replacement, this is an ordinary exact continuation. If it has not, it still remains legal under “at most one.”

**Spending the replacement now**

Before processing `t[j]`, the exact state has matched `i0` characters of `s`. The current `t[j]` can always match the next `s[i0]` by replacing that source character with `t[j]`.

That creates a one-replacement prefix of length `i0+1`. The best one-replacement progress after considering both possibilities is:

```python
i1 = max(i1, i0 + 1)
```

This transition is allowed regardless of whether `s[i0]` originally equals `t[j]`. If they are equal, no replacement is actually needed and the state is still valid under an at-most-one allowance. If they differ, one replacement makes them equal.

**Why update order is essential**

Only after the replacement transition does the source advance the exact pointer:

```python
if s[i0] == t[j]:
    i0 += 1
```

The order prevents one character `t[j]` from being consumed twice.

If `i0` were advanced first and `i1=max(i1,i0+1)` were then calculated, the algorithm could use `t[j]` once to match `s[i0]` exactly and a second time to replace and match the following character. A subsequence position may be selected only once.

Using the old exact `i0` for the replacement transition means both alternatives consume the current target character exactly once:

- match it exactly and advance `i0`;
- replace the next source character and advance a one-replacement route.

They are alternative histories, not consecutive actions.

The exact-extension of `i1` also occurs before the `max`, so it uses the current target character once from its own previous state. Taking a maximum merges alternative outcomes after all have consumed the same character.

**Loop condition and safe indexing**

The loop continues while:

```python
i1 < len(s) and j < len(t)
```

If `i1==len(s)`, the complete source string has already been matched and the answer is known to be true. If `j==len(t)` first, no target characters remain.

Throughout the loop, `i0\le i1<len(s)`. Therefore both `s[i1]` and `s[i0]` are safe to access.

The relation `i0\le i1` holds initially because both are zero. Exact progress is always also feasible with at most one replacement, and the `max(i1,i0+1)` transition keeps `i1` at least as advanced.

**Why the final test is complete**

After the scan, `i1` is the maximum prefix length of `s` realizable as a subsequence of the consumed `t` using at most one replacement.

Therefore:

```python
return i1 == len(s)
```

is true exactly when every source character can be matched.

If `s` is already a subsequence of `t`, `i1` can follow exact matches and succeeds without requiring a replacement. This matches the “at most one” wording.

**A mismatch illustration**

For `s="cat"` and `t="chat"`:

- target `c` advances both exact and flexible progress to one;
- target `h` does not advance exact `i0`, but replacement turns `s[1]` into `h` and advances `i1` to two;
- later target `t` exactly advances `i1` to three.

The resulting source `"cht"` is a subsequence.

If `s` is longer than `t`, no replacement can change length. Every target character can advance a prefix by at most one, so `i1` cannot reach `len(s)` and the method returns false naturally.

## Complexity detail

Let

$$
S=\lvert s\rvert
\qquad\text{and}\qquad
T=\lvert t\rvert.
$$

The scan increments `j` once per loop and never moves it backward, so it processes at most `T` target characters. Each iteration performs constant work. Time complexity is `O(T)`.

The source locally names `m=len(s)` and `n=len(t)`, while the reference contract uses the opposite letters. Using `T` here avoids that naming ambiguity. The manifest's `O(m)` refers to the target scan under its own symbol convention.

Only three indices and the two string lengths are stored. Auxiliary space complexity is `O(1)`.

Neither string is modified; the replacement is modeled as a state transition rather than materialized.

## Alternatives and edge cases

- **Try every replacement:** For each source index and each of 26 letters, running a full subsequence check costs `O(26ST)` in the straightforward form. The two-progress scan considers all replacement moments together.

- **Dynamic programming over both strings and replacement count:** A table can solve the problem in `O(ST)` time and space, but subsequence matching needs only the farthest prefix for each budget.

- **Keep only `i1`:** This loses the less-advanced exact route that still has its replacement available for a later mismatch.

- **Advance `i0` before the replacement transition:** That can consume the same target character for two consecutive source characters and produce false positives.

- **Require exactly one replacement:** The contract permits no replacement. Exact subsequences must return true, and `i1` includes them.

- **Replace with the same character:** It is never required, but treating an exact match as an at-most-one transition is harmless because no replacement must actually be performed.

- **`s` longer than `t`:** A replacement cannot reduce length, so success is impossible. The pointer scan returns false.

- **Identical strings:** Every character advances both states, yielding true.

- **One-character source:** It succeeds whenever `t` is nonempty because that one source character can be replaced to match any chosen target character. Both strings are guaranteed nonempty.

- **Repeated characters:** The left-to-right scan chooses increasing target positions automatically; no special duplicate handling is needed.

- **Target characters skipped:** If a character does not improve either progress state, only `j` advances, which is the standard subsequence skip.

- **Early completion:** Once `i1==len(s)`, later target characters cannot change the answer, so the loop stops.

- **No input mutation:** The source never constructs the replaced string. State `i1` proves that some legal replacement exists.
