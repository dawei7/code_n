## General

**Describe a candidate by its two equal boundary characters**

If equal characters occur at indices $L$ and $R$, with $L<R$, the substring strictly between them begins at $L+1$ and ends at $R-1$. Its length is

$$
R-L-1.
$$

The subtraction by one is easy to get wrong. The inclusive span from $L$ through $R$ has length $R-L+1$, but both boundary characters must be excluded, so two positions are removed: $(R-L+1)-2=R-L-1$.

The task is therefore to find two equal characters whose indices are as far apart as possible. It is not necessary to construct or slice the substring itself; only its length is requested.

**Scan once while remembering the earliest occurrence**

The dictionary `d` maps each character already seen to its first index. The answer `ans` starts at `-1`, which is the required result when no character appears twice.

The loop `for i, c in enumerate(s)` reads the string from left to right. At every index there are two cases.

If `c` is absent from `d`, this is the first occurrence of that character, so the source records `d[c] = i`.

If `c` is already present, then `d[c]` is the earliest possible left boundary for a substring ending at `i`. The candidate interior length is `i - d[c] - 1`. The source compares it with the best length found so far and retains the larger one.

Crucially, the dictionary entry is not updated after a repeated occurrence. Suppose a character occurs at indices 2, 5, and 9. When index 9 is the right boundary, pairing it with index 2 produces length $9-2-1=6$, while pairing it with index 5 produces only $9-5-1=3$. For a fixed right boundary, the smallest left index always creates the greatest distance. Replacing 2 with 5 would discard the only occurrence that can produce the best future answer for that character.

**Why skipped pairs cannot improve the answer**

There can be many pairs of equal occurrences, but the source examines only pairs made from each occurrence and the character's first occurrence. This pruning is safe.

Fix any right endpoint $R$ containing character $c$. Let $F$ be the first index at which $c$ appears. Any other eligible left endpoint $L$ satisfies $F\le L<R$. Therefore,

$$
R-F-1 \ge R-L-1.
$$

The pair $(F,R)$ is at least as long as every pair $(L,R)$ ending at the same position. Thus, none of the omitted later-left-boundary pairs can be the unique optimum. As the scan eventually treats every occurrence as a possible right endpoint, it considers a candidate at least as good as every valid pair in the string.

Another equivalent perspective is to focus on one character. Its longest possible interior is always between its first and last occurrences. The dictionary permanently retains the first, while the scan eventually reaches the last, so that maximum is considered. Taking `max` across all repeated characters then yields the global maximum.

**A concrete trace**

For `s = "abca"`, the scan proceeds as follows:

- At index 0, `a` is new, so store `a -> 0`.
- At index 1, `b` is new, so store `b -> 1`.
- At index 2, `c` is new, so store `c -> 2`.
- At index 3, `a` is already mapped to 0. The interior length is `3 - 0 - 1 = 2`, so `ans` becomes 2.

Those two positions enclose `"bc"`, but the algorithm never needs to allocate that string.

For `s = "aa"`, the second `a` gives `1 - 0 - 1 = 0`. An empty interior is valid, so zero correctly replaces the initial `-1`. For a string such as `"cbzxy"`, no dictionary lookup ever finds a repeated character, so `ans` remains `-1`.

**Why the final answer is correct**

The dictionary invariant is: immediately before processing index $i$, `d[c]` is the earliest index below $i$ containing $c$, for every stored character. The first encounter establishes that fact, and refusing to overwrite an entry preserves it.

Whenever the current character has appeared before, the algorithm evaluates the longest valid substring whose right boundary is the current index. The inequality above proves that choosing any later occurrence as the left boundary cannot do better. Since every index is processed, the best pair for every repeated character is considered. `ans` is updated only with valid equal-boundary lengths and always stores their maximum. Therefore it is exactly the requested longest length, or remains `-1` precisely when no valid pair exists.

## Complexity detail

Let $n$ be the length of `s`. The loop visits every character once. Dictionary membership, lookup, and insertion take expected $O(1)$ time, so the total expected time complexity is $O(n)$.

At most one dictionary entry is stored per distinct character. Because the input alphabet contains only 26 lowercase English letters, the dictionary holds at most 26 entries. Its auxiliary space is therefore $O(1)$ under the stated constraints. If the alphabet were unbounded, the more general bound would be $O(\min(n,\Sigma))$, where $\Sigma$ is the alphabet size, and hence $O(n)$ in the worst case.

The source calculates only integer index differences. It creates no substrings, so there is no hidden per-candidate slicing cost. `enumerate` supplies indices during the single traversal without allocating an index list.

## Alternatives and edge cases

- **Brute-force all index pairs:** Test every $L<R$ and update the answer when `s[L] == s[R]`. This is direct and correct, but it performs $O(n^2)$ comparisons instead of using the earliest-occurrence observation.
- **First and last occurrence arrays:** With 26 lowercase letters, two fixed arrays can record each letter's first and last indices. A second pass computes every distance. This is also $O(n)$ time and $O(1)$ space, but the one-pass dictionary updates the answer immediately.
- **Use `str.find` and `str.rfind` for each letter:** Calling both for every one of 26 fixed letters is still $O(n)$ under the fixed alphabet. It is concise but scans the same string repeatedly and is less adaptable to a larger alphabet.
- **Store every occurrence index:** This uses unnecessary $O(n)$ space. Only the first occurrence is needed because it dominates all later left boundaries for every future right endpoint.
- **Adjacent equal characters:** Their interior length is zero. The formula produces zero, which is a valid answer rather than `-1`.
- **No repeated character:** No candidate is evaluated and the sentinel `-1` is returned.
- **A character appears many times:** The first dictionary index must remain unchanged. Updating it would make later candidates shorter and could lose the optimum.
- **A one-character string:** It contains no pair, so the initialized `-1` is correct.
- **Do not include the boundary characters:** Using `i - d[c] + 1` would measure the whole bounded substring; using `i - d[c]` would still be one too large. The required interior is `i - d[c] - 1`.
- **Lexicographic concerns are irrelevant here:** The result asks only for maximum length. If several pairs have the same length, there is no need to retain their positions or choose among their contents.
