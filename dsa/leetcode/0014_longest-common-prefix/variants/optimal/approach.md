## General

**A common prefix must agree one complete column at a time**

Choose `strs[0]` as the reference string. If all strings share a prefix of length `k`, then for every index `i < k`, every string must contain index `i` and must have the same character there as `strs[0][i]`.

This leads to **vertical scanning**: validate character index `0` across all strings, then index `1`, and so on. The first failed column determines the answer immediately. No later character can belong to a common prefix once an earlier position is missing or different, because prefixes must start at index zero and remain contiguous.

The outer loop

```python
for i in range(len(strs[0])):
```

tries every possible prefix position supplied by the reference. A common prefix cannot be longer than `strs[0]`, so there is no need to inspect a larger index.

**Every other string must pass two checks**

For the current position `i`, the inner loop examines each remaining string `s`. The condition is

```python
if len(s) <= i or s[i] != strs[0][i]:
```

The two parts represent different ways the common prefix can end:

- `len(s) <= i`: `s` is too short to contain a character at index `i`;
- `s[i] != strs[0][i]`: the character exists but differs from the reference.

The length check comes first. Python evaluates `or` from left to right and stops when the first part is true, so `s[i]` is never read out of bounds for a shorter string.

If neither condition is true for any string, the complete column matches and the algorithm advances to `i + 1`.

**Why returning `s[:i]` is correct even when `s` caused the failure**

On failure, the method returns

```python
s[:i]
```

rather than `strs[0][:i]`. These slices are equal. Reaching column `i` means every earlier column `0` through `i - 1` passed for every string already checked, including the current `s`. Therefore

$$
s[:i] = \texttt{strs[0][:i]}.
$$

If the failure occurs at `i = 0`, `s[:0]` is the empty string, correctly indicating that no non-empty prefix is shared.

If `s` is shorter and has length exactly `i`, then `s[:i]` is the whole string. That is also correct: all of its characters matched, but a common prefix cannot extend beyond the shortest participant.

**Trace `flower`, `flow`, and `flight`**

| Index `i` | Reference character | `flow` | `flight` | Result |
|---:|:---:|:---:|:---:|---|
| `0` | `f` | `f` | `f` | full column matches |
| `1` | `l` | `l` | `l` | full column matches |
| `2` | `o` | `o` | `i` | mismatch; return prefix of length `2` |

The result is `"fl"`. Characters after index `2` are irrelevant because a prefix cannot skip the mismatch and restart later.

For `["dog", "racecar", "car"]`, the first comparison at index zero finds `d != r` and returns `""` immediately.

**Why returning the whole first string is safe**

If the outer loop completes, every position in `strs[0]` matched every other string. Thus `strs[0]` is a prefix of every input string.

No common prefix can be longer than `strs[0]` itself, so it is not merely common—it is the longest possible common prefix. Returning `strs[0]` is therefore exact.

This also handles a one-string array. The inner loop has no elements, every reference column vacuously matches, and the sole string is its own longest common prefix.

**Empty strings are handled by loop structure**

The input array is guaranteed non-empty, but an individual string may be empty. If `strs[0] == ""`, the outer range is empty and the method returns `""`. If a later string is empty, the first column's `len(s) <= 0` check returns `""`. No separate empty-string branch is necessary.

**Why the first failure gives the global answer**

Before column `i`, all strings have been proved equal on exactly the prefix of length `i`. A failure at `i` proves that no prefix of length `i + 1` can be common. Any longer prefix would contain that same failed position, so it is impossible as well. The verified length-`i` prefix is therefore the longest one.

If no failure occurs, all reference positions are verified and the reference length is the maximum possible. These two termination cases cover every execution.

## Complexity detail

Let $q$ be the number of strings, let $k$ be the length of the returned common prefix, and let

$$
S = \sum_{s \in \texttt{strs}} \lvert s \rvert.
$$

- **Character-comparison time: $O(qk)$, bounded by $O(S)$.** At most `k + 1` columns are considered, and each checks up to `q - 1` strings. In the full-match case, the first string may be the shortest bound. No character position beyond the first mismatch is examined. The standard worst-case statement is $O(S)$.
- **Auxiliary space of this exact Python source: $O(q)$.** The expression `strs[1:]` creates a new list of up to `q - 1` references for each outer iteration. Only one such temporary slice exists at a time, so peak extra space is $O(q)$, not $O(1)$. The returned string slice uses $O(k)$ output space when a mismatch occurs.

The conceptual vertical-scan algorithm can meet the manifest's $O(1)$ auxiliary-space target by iterating indices `1` through `q - 1` instead of slicing the list. The current source's string and character logic is linear, but its Python list slice is a real allocation.

## Alternatives and edge cases

- **Index the original list instead of `strs[1:]`:** `for j in range(1, len(strs))` preserves the same comparisons and removes the $O(q)$ temporary list, achieving constant auxiliary space excluding output.
- **Horizontal scanning:** Start with the first string as a candidate and repeatedly shorten it against each later string. It is also $O(S)$ but may revisit prefix characters through slicing or prefix searches.
- **Sort and compare extremes:** After lexicographic sorting, only the first and last strings determine the common prefix. Sorting costs $O(q\log q)$ comparisons and mutates or copies ordering, which is unnecessary for one query.
- **Trie:** Useful when the same string set serves many prefix queries, but building it costs $O(S)$ extra space and is excessive for one result.
- **First string empty:** The outer loop is skipped and `""` is returned.
- **Later string empty:** The first length check returns `""` without indexing the empty string.
- **One input string:** It is returned unchanged.
- **Mismatch at index zero:** `s[:0]` returns the required empty prefix.
- **Shortest string is a full prefix:** Failure occurs when the next reference column is beyond that string, returning the complete shorter string.
- **All strings identical:** Every column passes and the shared complete string is returned.
- **Duplicates mixed with longer strings:** Duplicate entries do not change the proof; every column still must pass for every entry.
- **Lowercase contract:** Comparisons are exact and case normalization is neither needed nor performed.
- **Input preservation:** Strings are immutable and the list is not reordered; only a temporary reference slice is created.
