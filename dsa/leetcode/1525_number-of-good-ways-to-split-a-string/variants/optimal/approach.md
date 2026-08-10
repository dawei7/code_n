## General

**Representing the two sides while moving the boundary**

A split after a character is good when the nonempty left prefix and remaining right suffix contain the same number of distinct letters.

The stored solution begins with `cnt = Counter(s)`, so `cnt` represents character frequencies on the right before any character has moved. `vis` is an initially empty set of letters seen on the left.

The loop moves one character `c` at a time from right to left:

1. `vis.add(c)` records that its letter is present on the left.
2. `cnt[c] -= 1` removes this occurrence from the right.
3. If its remaining frequency is zero, `cnt.pop(c)` removes the key entirely.
4. Comparing `len(vis)` with `len(cnt)` tests distinct counts.

Removing zero-count keys is essential because `len(cnt)` counts keys, not positive values automatically. Leaving a zero entry would falsely claim that character still occurs on the right.

**The invariant after each move**

After processing index `i`, `vis` is exactly the set of letters in `s[0:i+1]`, and `cnt` contains exactly the positive frequencies in `s[i+1:]`.

This holds initially for an empty left side and complete right side. Moving `c` adds precisely the next left character and subtracts precisely that occurrence from the right. Popping at zero maintains exact positive-key membership.

Therefore, the equality comparison is true exactly for split boundary `i+1` when both sides have equal distinct-letter counts.

**Why the final loop iteration is harmless**

There are only $n-1$ legal split positions because both strings must be nonempty, yet the exact loop processes all $n$ characters.

After the final character moves left, `vis` contains at least one letter because the input is nonempty, while `cnt` is empty and has length zero. Their lengths cannot be equal. Thus the final, illegal empty-right boundary contributes zero without needing a special loop limit.

For a one-character string, this is the only iteration, and the method correctly returns zero.

**A trace on aacaba**

Initially, the right counter contains all frequencies and the left set is empty.

After moving the first `a`, the left has one distinct letter while the right still has three. After moving the second `a`, the counts remain one versus three. Moving `c` gives left letters `a,c` and right letters `a,b`, so both sides have two and the answer increases.

Moving the next `a` leaves the same two distinct letters on each side, producing the second good split. Later, left gains `b` while right contains only `a`, so equality fails.

**Why every good split is counted once**

Each legal boundary occurs after one unique loop iteration. The invariant gives the exact two distinct counts for that boundary. The source adds one if and only if they match.

No substring construction or repeated set building is needed. Counts update incrementally as the boundary moves right.

**Fixed alphabet and space**

Although `Counter` and `set` are dynamic containers, `s` contains only lowercase English letters. Each can hold at most 26 keys, so their algorithmic storage is constant relative to string length.

**How the two distinct counts evolve**

As the boundary moves right, `len(vis)` can only stay the same or increase: once a letter appears on the left, it never disappears. In contrast, `len(cnt)` can only stay the same or decrease: a right-side letter disappears exactly when its final remaining occurrence is moved left.

The counts may become equal at several consecutive or separated boundaries, and every equality is a separate valid split. The algorithm deliberately checks after each single-character transfer rather than stopping at the first equality. This monotonic perspective also explains why incremental maintenance is natural: only the moved character can change either distinct count at one step.

## Complexity detail

Building `Counter(s)` scans $N$ characters. The loop scans them once more. Set insertion, counter update, deletion, and length are expected constant time, giving expected $O(N)$ total time.

Both containers hold at most 26 letters, so auxiliary space is $O(26)=O(1)$ under the fixed alphabet, matching the manifest. In a generalized unbounded alphabet, space would be $O(U)$ for $U$ distinct symbols.

The answer is at most $N-1$. No substrings are copied.

## Alternatives and edge cases

- **Prefix and suffix distinct arrays:** Precompute counts at every index and compare them. It is simple but uses $O(N)$ extra space.
- **Two fixed 26-entry frequency arrays:** Maintain explicit left and right counts plus distinct totals. It avoids hashing while preserving constant space.
- **Rebuild sets per split:** Constructing both sides repeatedly costs $O(N^2)$ time and copies substrings.
- **One-character string:** No legal split exists, and the final empty-right comparison fails.
- **All one letter:** Every legal split has one distinct letter on each side, so all $N-1$ splits are good.
- **All letters distinct:** A split is good only when both side lengths, and therefore distinct counts, match.
- **Zero-count counter key:** It must be popped so right distinctness decreases at the correct moment.
- **Final character:** Processing it does not count an illegal split because right distinct count becomes zero.
- **Nonempty guarantee:** It ensures the final left distinct count is positive.
- **Required import:** `Counter` must be available from `collections`.
