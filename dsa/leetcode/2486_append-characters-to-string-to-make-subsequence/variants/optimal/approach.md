## General

**Only a prefix of the target can be matched before appending**

Characters may be appended only after the existing string `s`. Suppose some prefix of `t` can already be selected as a subsequence of `s`. Any remaining target characters can then be appended in their original order, producing a complete subsequence equal to `t`.

The key is to make that matched prefix as long as possible. If the longest prefix of `t` that fits inside `s` has length `j`, then exactly the suffix `t[j:]` remains. Its length is `len(t)-j`, which is the returned answer.

It would not help to match a target segment that skips an earlier target character. A subsequence equal to `t` must produce target characters from left to right. Before target position `j` can be matched, every earlier target position must already have been matched.

**Greedily match the next required character**

The variable `j` is the index of the next unmatched character in `t`. It begins at zero, meaning no target characters are matched.

The loop reads each character `c` of `s` from left to right. If `j<n` and `c==t[j]`, that source character is used to match the next required target character and `j` advances. Otherwise, `c` is skipped.

The guard `j<n` is important. Once all of `t` has been matched, `j` equals `n`, and indexing `t[j]` would be outside the string. The loop can safely keep scanning `s` because the guard prevents that access and `j` remains `n`.

For `s="coaching"` and `t="coding"`, the scan matches `c` and then `o`. The next required target character is `d`, which does not appear later in `s`, so `j=2` at the end. The unmatched suffix is `"ding"`, whose length is four.

**Why taking the earliest match is optimal**

When the current source character equals the next required target character, using it can never make a later match harder. Choosing the earliest possible position for a target character leaves every later source position available for subsequent target characters.

This can be formalized inductively. After scanning any prefix of `s`, `j` equals the greatest number of initial target characters that can be formed from that source prefix. Initially both lengths are zero. When a new source character arrives, any subsequence either ignores it or uses it as the next character after a previously achievable target prefix. If it equals `t[j]`, extending the current longest prefix increases the optimum by one. If it does not, no longer target prefix can use it as its next required character, so the optimum stays unchanged.

Therefore, after the complete scan, no method can match a longer prefix of `t` inside the original `s`.

**Why the unmatched suffix is both sufficient and necessary**

It is sufficient to append `t[j:]` verbatim. The first `j` target characters have already been matched at increasing positions in the original `s`. Every appended character occurs after all original positions, so selecting the newly appended suffix after those matches yields all of `t` in order.

It is also necessary to append at least `n-j` characters. The original `s` cannot realize target prefix length `j+1` by the maximality proved above. In particular, the next required target character and everything following it cannot all be supplied in order by original positions. Each appended position contributes at most one character to a subsequence, and `n-j` target positions remain. Fewer appended characters cannot fill all of them.

Meeting the lower bound with the direct construction proves that `n-j` is the minimum, not merely one possible append count.

**Subsequence is different from substring**

Matched source characters do not need to be adjacent. The scan may skip any number of unrelated characters in `s` while preserving order. In the example, characters between the matched `c` and `o` or after them do not invalidate the match.

On the other hand, order cannot change. A useful character that appeared earlier in `s` cannot be revisited after `j` advances. The one-directional loop models this rule exactly.

**What the method returns**

The problem requests only the minimum number, not the appended string. The remaining string would be `t[j:]`, but constructing that slice would allocate unnecessary memory. Returning the length difference gives the requested result directly.

## Complexity detail

Let $p=\lvert s\rvert$ and $q=\lvert t\rvert$. The loop visits every character of `s` once and performs constant work. Reading `len(t)` and computing the difference are constant-time operations in Python. The exact runtime is therefore $O(p)$, which is also within the manifest's looser $O(p+q)$ bound because $O(p)\subseteq O(p+q)$.

The algorithm stores the two integers `n` and `j` plus one loop character. It creates no array, stack, substring, or recursion state, so auxiliary space is $O(1)$.

The returned integer is at most $q\le10^5$.

## Alternatives and edge cases

- **Explicit two-pointer loop:** Maintain indices into both strings with a `while` loop. It has the same greedy invariant and complexity but requires manually advancing the source index.
- **Next-occurrence lookup:** Preprocess positions of letters and binary-search successive matches. That is useful for many target queries against one fixed `s`, but unnecessary for one query.
- **Dynamic programming:** A general subsequence DP uses far more time or space than needed because only the longest matched target prefix matters.
- **`t` already a subsequence:** `j` reaches `n` and the answer is zero.
- **No first-character match:** `j` remains zero, so all of `t` must be appended.
- **Repeated letters:** Each source position can be used once; advancing only one target position per match handles duplicates correctly.
- **Noncontiguous match:** Skipped source characters are allowed because the requirement is subsequence, not substring.
- **Order mismatch:** Having all target letters in `s` is insufficient if they do not occur in target order.
- **Completed target early:** The `j<n` guard prevents an out-of-range target access during the rest of the source scan.
- **Append-only restriction:** New characters cannot be inserted between existing positions, which is why the unmatched portion must be a suffix of `t`.
