## General

The design must make `flip` constant time while keeping `fix`, `unfix`, `all`, `one`, and `count` constant time. The exact implementation stores two full character arrays:

- `a` is the currently visible bitset;
- `b` is the bitwise complement of `a`.

Swapping these arrays flips every logical bit instantly.

**Establish the core invariant**

At every index, exactly one of `a[idx]` and `b[idx]` is `'1'`. Initially, `a` contains all zeros and `b` all ones, so the invariant holds.

`cnt` stores the number of ones in the currently visible array `a`. It begins at zero.

**Fix one bit**

If `a[idx] == '0'`, `fix` changes it to one and increments `cnt`. If it was already one, neither action occurs, preserving idempotence.

The assignment `b[idx] = '0'` is performed in either case. After the method, the visible bit is one and its complement is zero, so the two-array invariant holds.

**Unfix one bit**

`unfix` is symmetric. If the visible bit is one, it becomes zero and `cnt` decreases. If already zero, the count remains unchanged. Setting `b[idx] = '1'` restores the complementary value.

**Flip without scanning**

`self.a, self.b = self.b, self.a` swaps the two list references. The former complement becomes visible, so every bit is logically inverted in $O(1)$ time.

If the old visible array contained `cnt` ones among `size` bits, its complement contains `size - cnt` ones. The assignment `self.cnt = len(self.a) - self.cnt` updates the aggregate consistently.

No character is rewritten during a flip.

**Answer aggregate queries**

`all` returns whether `cnt == len(a)`. `one` returns whether `cnt > 0`. `count` returns `cnt` directly. Because every mutation maintains the count invariant, none of these methods scans the bitset.

`toString` is the one operation that must inspect every bit because it returns all $n$ characters. `''.join(self.a)` constructs the visible representation in index order.

**Why later fixes still work after flips**

After a swap, `a` and `b` still contain opposite values at every index; only their roles changed. `fix` and `unfix` always operate on whichever list is currently named `a` and write the opposite value into current `b`. They therefore need no separate inversion flag or conditional interpretation.

This detail matters because the names `a` and `b` describe roles, not permanent physical meanings. A list that began as the all-zero visible list may become the hidden complement after one flip and become visible again after the next. The methods never need to remember that history. They only need the present rule: read and update `a` as the visible list, and keep `b` opposite at the same index.

**Why every returned answer describes the requested bitset**

Initialization establishes complementarity and the correct one count. Fix and unfix update both the affected pair and count exactly when the logical value changes. Flip swaps complements and algebraically complements the count. Therefore, after every operation, `a` contains precisely the logical character at every position and `cnt` equals the number of `'1'` characters in `a`.

Each query then reads the smallest sufficient piece of this maintained state. `all` does not need to inspect the positions because a length-$n$ bitset contains only ones exactly when its one count is $n$. `one` is true exactly when that count is positive. `count` returns the count itself. `toString` is different: the caller asks for the actual ordered characters, so the method joins `a` rather than trying to reconstruct a string from only `cnt`. The invariant just proved makes all four answers exact.

For a concrete miniature trace, start from size three: `a = ['0', '0', '0']`, `b = ['1', '1', '1']`, and `cnt = 0`. After fixing index one, the arrays are `010` and `101` and the count is one. Flipping merely swaps those arrays, making `101` visible and changing the count to two. Unfixing index zero then writes zero to the visible array, one to its complement, and decreases the count to one. The final visible value is `001`, exactly as the logical operations require.

## Complexity detail

Construction allocates and fills two length-$n$ lists, taking $O(n)$ time and space. `fix`, `unfix`, `flip`, `all`, `one`, and `count` each use $O(1)$ time. `toString` takes $O(n)$ time and creates an $O(n)$ output string.

Across $Q$ operations and at most five string conversions, total time is $O(Q+n)$ under the problem's fixed conversion limit. More explicitly, the non-string operations contribute $O(Q)$, while at most five calls each contribute $O(n)$; the constant five disappears from asymptotic notation. If an unrestricted interface allowed `toString` to be called $T$ times, the more general bound would be $O(Q+Tn)$. The two arrays use $O(n)$ persistent space, and the returned string from `toString` additionally occupies $O(n)$ output space.

The manifest describes a physical array plus lazy inversion flag, but the exact source instead pays for two complementary arrays. Both support constant-time flips, but this document follows the stored implementation.

## Alternatives and edge cases

- **One array plus inversion flag:** Interpret each stored bit through a global flipped boolean. This uses one array rather than two but makes fix and unfix compare physical and logical values carefully.
- **Flip by scanning:** Rewriting all bits makes one flip $O(n)$ and can be too slow across $10^5$ calls.
- **Recount on every query:** Maintaining `cnt` avoids repeated $O(n)$ scans.
- **Fix an existing one:** The count must not increase twice; the conditional prevents it.
- **Unfix an existing zero:** The count likewise remains unchanged.
- **Repeated flips:** Two swaps restore the original arrays and two count complements restore the original count.
- **Size one:** All operations and aggregate predicates follow the same invariants.
- **All bits fixed:** `cnt == size` makes `all` true; flipping makes the count zero.
- **No bits fixed:** `one` is false until a fix or suitable flip creates a one.
- **String output:** Joining `a` uses current logical order and does not expose `b`.
- **Character storage:** Bits are strings because `toString` can join them directly.
- **Index validity:** The contract guarantees every `idx` is inside the allocated lists.
- **Output allocation:** Even with constant-time updates, returning an $n$-character string necessarily costs $O(n)$.
