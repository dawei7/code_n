## General

The competitive implementation uses dynamic programming over source prefixes while compressing a two-dimensional table into one row. It first ensures that `s1` is the shorter source. Consequently the Boolean list has length `min(len(s1), len(s2)) + 1`, which achieves the manifest's requested memory bound.

If the sources are in the opposite size order, the method recursively calls itself with `s1` and `s2` swapped. Interleaving is symmetric in the two sources: exchanging their names does not change whether their order-preserving characters can form `s3`. After one swap, the condition is false, so this does not recurse repeatedly.

**Underlying two-dimensional state**

Conceptually, let $D[i][j]$ mean that the first $i$ characters of `s1` and first $j$ characters of `s2` can interleave to form exactly the first $i+j$ characters of `s3`.

The empty prefixes form the empty target, so $D[0][0]$ is true. For positive indices, the final target character at position `i + j - 1` must have come from one of two places:

$$
D[i][j]
=
\bigl(D[i-1][j]\land s1[i-1]=s3[i+j-1]\bigr)
\lor
\bigl(D[i][j-1]\land s2[j-1]=s3[i+j-1]\bigr).
$$

The first term consumes the newest `s1` character; the second consumes the newest `s2` character.

**What `match[i]` means during the loops**

The one-dimensional list stores the current DP row over `s2` prefix length `j`, with `i` representing how many characters are taken from the shorter `s1`.

Before any `s2` character is used, initialization computes $D[i][0]$. `match[0] = True` is the empty case. Each next entry remains true only if the preceding entry was reachable and the next `s1` character matches the corresponding target character. Thus initialization checks whether each `s1` prefix alone equals the same-length `s3` prefix.

For each outer-loop value `j`, `match[0]` is updated to $D[0][j]$, similarly checking the `s2`-only prefix.

**Why left-to-right in-place updates are correct**

At the start of an inner iteration for `i`:

- `match[i]` still contains $D[i][j-1]$, the state from the previous outer row; and
- `match[i - 1]` has already been updated to $D[i-1][j]$, the current row's left neighbor.

Those are exactly the two predecessor states in the recurrence. The assignment replaces `match[i]` with $D[i][j]$. Iterating `i` from low to high is therefore essential. Reversing the direction would read an old value for `match[i - 1]` and combine two previous-row states incorrectly.

The first OR term uses updated `match[i - 1]` and tests `s1[i - 1]`. The second uses old `match[i]` and tests `s2[j - 1]`. Both compare against target position `i + j - 1`, because together the chosen prefixes contain exactly `i + j` characters.

**Length rejection**

The method returns false when source lengths do not sum to the target length. Interleaving neither drops nor duplicates characters, so equality is mandatory. This check also makes every later `s3` index valid.

**Why the DP is correct**

Any interleaving forming the prefix represented by $D[i][j]$ ends with either `s1[i - 1]` or `s2[j - 1]`. Removing that last character leaves the corresponding predecessor prefix, and the removed character must equal the final target character. Therefore every valid interleaving satisfies at least one recurrence term.

Conversely, if either term is true, append its matching source character to an interleaving witnessed by its predecessor. This constructs the desired target prefix without disturbing order. Induction from $D[0][0]$ proves all entries, including the returned `match[-1]`.

## Complexity detail

Let original source lengths be $m$ and $n$. The two nested loops fill $(m+1)(n+1)$ logical states, so time is $O(mn)$. The one possible argument-swapping call performs only constant work before the real loops.

After swapping if needed, `match` has $\min(m,n)+1$ Booleans. Loop variables use constant extra storage, giving $O(\min(m,n))$ auxiliary space, matching the manifest. The source's header comment says $O(m+n)$, which is a valid but loose upper bound; the actual list is sized to the shorter source.

## Alternatives and edge cases

- **Memoized recursion:** Cache suffix states `(i, j)`. It is intuitive but uses $O(mn)$ cache space and a call stack.
- **Full DP table:** Retain every prefix state for easier tracing or path reconstruction, at $O(mn)$ space.
- **Greedy selection:** Taking a matching character from one preferred source can fail when both match now but only one permits the remaining suffix. DP preserves both possibilities.
- **Do not update right-to-left:** This recurrence needs the current row's left neighbor and previous row's same column; ascending `i` supplies exactly those versions.
- **Both sources empty:** `match` remains `[True]`, so an empty target returns true.
- **One source empty:** Initialization or repeated `match[0]` updates compare the nonempty source directly with `s3`.
- **Repeated characters:** OR combines both predecessor paths without counting or duplicating states.
- **Source swap:** Only the storage orientation changes. The characters retain their internal order, and validity is symmetric.
- **Length mismatch:** Return false before allocating the DP row or indexing `s3`.
