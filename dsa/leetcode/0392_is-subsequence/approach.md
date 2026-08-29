## General

**What must be preserved**

A subsequence may delete any characters from `t`, but it may not reorder the characters that remain. Therefore the task is not to ask whether every character of `s` occurs somewhere in `t`; it is to ask whether those occurrences can be chosen at strictly increasing positions.

The exact solution uses two indices:

- `i` is the index of the next character of `s` that still needs a match;
- `j` is the current position being inspected in `t`.

Both begin at zero. The algorithm scans `t` only from left to right. When `t[j]` matches `s[i]`, it accepts that occurrence and increments `i`. Whether it matches or not, it increments `j`, because the current source position has now been fully considered and can never be useful again.

**Why the pointer into `t` always moves**

If `s[i] != t[j]`, the current `t` character cannot satisfy the next required character. It may be deleted from the prospective subsequence, so moving `j` forward loses nothing.

If `s[i] == t[j]`, the algorithm uses this occurrence. It advances `i` to the next requirement and advances `j` because one physical position in `t` cannot be reused for two positions of `s`. This preserves the strictly increasing order of selected indices.

Thus every iteration consumes exactly one character from `t` and consumes either zero or one character from `s`.

**The greedy choice: accept the earliest available match**

When characters match, another strategy might skip this occurrence and hope to use a later equal character. The algorithm never does that; it greedily accepts the earliest possible occurrence.

This choice is safe because an earlier match leaves at least as much of `t` available for the remaining characters as any later match would. Suppose some valid embedding matches `s[i]` at a later index `q`, while the algorithm finds the same character at earlier index `j < q`. Replacing `q` with `j` preserves order with all already chosen positions, and every position used for later characters remains after `j`. The rest of the valid embedding still works.

Therefore accepting an early match cannot destroy a solution. It can only leave a longer suffix in which to find the remaining characters.

**The loop invariant**

At the beginning of each iteration:

- the prefix `s[0:i]` has been matched in order within `t[0:j]`;
- among all ways to match that many characters, the greedy choices use positions no later than necessary;
- `s[i]`, when `i < len(s)`, is the next unmatched requirement.

The invariant is initially true because both prefixes are empty. A mismatch advances only `j`, preserving the existing match. A match appends position `j` to the chosen increasing sequence and advances both conceptual prefixes. The greedy exchange argument shows the new matched prefix remains as early as possible.

When the loop ends, this invariant turns the pointer state into the answer.

**Why the final condition is sufficient**

The loop continues only while both `i < len(s)` and `j < len(t)`.

If `i == len(s)`, every character of `s` has been matched at increasing positions in `t`. The method returns `True` even if unexamined characters remain in `t`, because they can simply be deleted.

If `j == len(t)` while `i < len(s)`, the source string has been exhausted but some required characters remain unmatched. No later position exists, so completion is impossible and the method returns `False`.

The expression `return i == len(s)` captures both cases without a separate branch.

**Tracing a successful example**

For `s = "abc"` and `t = "ahbgdc"`:

| `j` | `t[j]` | Next required character | Action | New `i` |
|---:|:---:|:---:|---|---:|
| `0` | `a` | `a` | match | `1` |
| `1` | `h` | `b` | skip `h` | `1` |
| `2` | `b` | `b` | match | `2` |
| `3` | `g` | `c` | skip `g` | `2` |
| `4` | `d` | `c` | skip `d` | `2` |
| `5` | `c` | `c` | match | `3` |

Now `i == len(s)`, so the answer is `True`. The selected positions are `0`, `2`, and `5`, which are strictly increasing.

For `s = "axc"` and the same `t`, `a` matches, but no `x` appears in the remaining source string. The `j` pointer reaches the end while `i` still points to `x`, so the method returns `False`.

**Why matching by character counts would be insufficient**

The strings `s = "aec"` and `t = "abcde"` contain all three required characters, each with enough frequency. But after matching `a` and then `e`, there is no `c` to the right of `e`. A frequency table loses this positional constraint. The two-pointer scan retains it by never moving `j` backward.

**A direct correctness argument**

If the method returns `True`, every increment of `i` was caused by an equal character at the current, strictly increasing `j` position. Those selected positions spell all of `s` in order, so `s` is a subsequence.

If the method returns `False`, the scan exhausted all of `t` without matching all of `s`. The greedy exchange argument establishes that after every source prefix, the algorithm’s last chosen position is no later than that of any other possible matching of the same prefix. If even this earliest-position strategy cannot find the next requirement, no alternative that matched earlier characters later can succeed. Thus `s` is not a subsequence.

## Complexity detail

Let $S = \lvert s \rvert$ and $T = \lvert t \rvert$.

The pointer `j` starts at zero and increases once per iteration, never decreasing. It advances at most $T$ times. All work inside an iteration is constant, so worst-case time is $O(T)$. The method may stop earlier after matching all $S$ characters, but this does not change the worst-case bound.

Only two integer indices are stored, so auxiliary space is $O(1)$. The input strings are read-only, and the method creates neither substrings nor a match list.

The linear worst case is optimal for one query: an algorithm may need to inspect the final character of `t` to determine whether the last required match exists.

## Alternatives and edge cases

- **Recursive greedy scan:** Apply the same match-or-skip rule recursively. It is correct and linear but uses up to $O(T)$ call-stack space in Python, while the iterative form is constant space.

- **Dynamic programming:** A table over prefixes of `s` and `t` can determine subsequence membership in $O(ST)$ time and space. It solves a more general alignment problem than necessary; the greedy property makes the table wasteful here.

- **Character counts:** Frequencies can reject some impossible inputs but cannot prove subsequence order. Strings may have enough copies of every character in the wrong order.

- **Preprocessed positions for many queries:** For the follow-up, store the sorted indices of each character in fixed `t`. For each character of an incoming `s`, binary-search for the first index greater than the previous match. Preprocessing costs $O(T)$ time and space, and a query costs $O(S\log T)$, avoiding a full rescan of `t` for billions of queries.

- **Next-occurrence table for many queries:** With a fixed 26-letter alphabet, precompute for every position and character the next matching index. This uses $O(26T)$ space and permits each query in $O(S)$ time.

- **Empty `s`:** `i == len(s)` initially, so the loop is skipped and `True` is returned. The empty string is a subsequence of every string, including another empty string.

- **Empty `t` with nonempty `s`:** The loop is skipped because `j == len(t)`, while `i != len(s)`, so the answer is `False`.

- **`s` longer than `t`:** There cannot be enough distinct positions to match every source character. The scan naturally exhausts `t` and returns `False`; no length precheck is required.

- **Equal strings:** Every comparison matches, both pointers advance together, and the method returns `True`.

- **Repeated characters:** Each required occurrence needs a different later position. Advancing `j` after every match enforces that rule automatically.

- **A match at the final source position:** If it completes `s`, the next loop condition fails because `i == len(s)`, and the method returns `True` without reading beyond either string.

- **Greedy tie choice:** Always taking the first usable equal character is essential to the simple proof; deliberately delaying a match cannot help and may leave too little suffix for later requirements.
