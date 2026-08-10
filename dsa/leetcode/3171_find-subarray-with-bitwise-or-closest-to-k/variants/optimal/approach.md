## General

**Use monotonic behavior of OR in a window**

When a value is added to a window, bitwise OR can only gain 1-bits, so its numeric value never decreases. When a value is removed, OR can only lose bits, so it never increases.

This monotonicity supports two pointers around target $k$. The current window is `nums[i..j]` and `s` is its OR.

For each new right endpoint, `s |= x` extends the window and the difference `abs(s-k)` is checked.

If `s > k`, shrinking from the left may lower it toward $k$. The code repeatedly removes left values while the window has more than one element and remains above $k$, checking the result after every removal.

Once `s <= k`, further shrinking can only make `s` smaller or equal, increasing or preserving $k-s$. No later start for this same right endpoint can improve the difference, so shrinking stops.

**How to remove a value from an OR**

OR has no simple inverse. If a removed value contains a 1-bit, that bit must remain in `s` if another window element also contains it.

Array `cnt[h]` stores how many current window values contain bit $h$. When adding `x`, every set bit increments its count. When removing `y`, its set-bit counts decrement. If one reaches zero, no remaining element supplies that bit, so `s ^= 1 << h` clears it.

The bit width `m = max(nums).bit_length()` covers every possible input bit.

**Why discarded starts never become useful later**

When left index advances, the removed wider window had OR greater than $k$. Extending that old window with future right endpoints could only keep or increase its OR, so its difference above $k$ could never improve beyond the value already checked. It is safe never to revisit that start.

For a fixed right endpoint, all starts examined while shrinking have their OR checked. Starts after the first point where OR becomes at most $k$ can only produce smaller OR and no better difference. Thus every potentially optimal window is either evaluated or dominated by an evaluated window.

**Nonempty requirement**

Condition `i < j` prevents removal of the only element. Every checked `s` therefore belongs to a nonempty window. A singleton greater than $k$ is evaluated but not shrunk into an empty OR.

For `nums = [1,2,4]` and $k=3$, extending through 1 then 2 produces OR 3 and difference zero. Bit counts are one for bit 0 and one for bit 1. If a later value forced shrinking, removing 1 would reduce bit 0's count to zero and clear only that bit, leaving every bit still supplied by another element intact.


For every right endpoint, the algorithm checks the sequence of window OR values while starts advance until crossing from above $k$ to at most $k$, or reaching a singleton. Because these values are nonincreasing as the start advances, the closest value to $k$ occurs at the crossing boundary: the last value above and first value below/equal. Both are checked.

Starts removed in earlier iterations remain permanently above-$k$ dominated under future extensions. Therefore, taking the minimum over all checked candidates gives the global minimum.

**Relation to the manifest**

The manifest describes carrying distinct OR values of all subarrays ending at each position, another standard $O(n\log M)$ solution. The exact source instead maintains one monotone sliding window with per-bit counts. Its bounds match, but its invariant and data flow are different.

## Complexity detail

Let $n$ be array length and $B=\lfloor\log_2 M\rfloor+1$, where $M=\max(nums)$.

Each right addition scans all $B$ bits. Each left index is removed at most once and also scans $B$ bits. Time is $O(nB)=O(n\log M)$.

The bit-count array has $B$ entries, so auxiliary space is $O(B)=O(\log M)$. Scalars use constant additional space.

The input is not modified and output is one integer.

Under the $10^9$ bound, $B\le30$.

## Alternatives and edge cases

- **Distinct ending-OR sets:** Form `{x | old_or | x}` for each position and deduplicate. This matches the manifest and also has only $O(\log M)$ distinct values per endpoint.
- **Enumerate all subarrays:** It costs $O(n^2)$ even with rolling OR.
- **Sparse set-bit iteration:** Iterate only set bits of added and removed values, potentially faster but more intricate.
- **Exact match:** Difference zero is globally optimal; the source could return early but continues safely.
- **Single element:** It is evaluated and never removed into an empty window.
- **Current OR below k:** Expanding may improve it, so the left boundary is retained.
- **Current OR above k:** Shrinking is the only current-right operation that may improve it.
- **Repeated bits:** A bit is cleared only when its count reaches zero.
- **All values identical:** Counts preserve the shared OR until the final copy would be removed.
- **Large k:** Windows may remain below $k$ and left pointer may stay zero; all right extensions are still checked.
- **Manifest mismatch:** Do not explain this source as a distinct-set DP; it uses two pointers and reversible counts.
- **Positive inputs:** `m` is at least one and the bit array is nonempty.
