## General

**Every rotation is a length-$n$ window in a conceptual doubled string.** Moving the first character to the end repeatedly generates all cyclic rotations. If one imagines `s + s`, rotation by `r` positions is the window of length `n` starting at doubled index `r`. The source simulates the mismatch count for these windows without actually allocating the doubled string.

**Only two alternating targets exist.** One target begins with zero and follows `0101...`; the other begins with one and follows `1010...`. String `target = "01"` represents the first pattern, and `target[i & 1]` selects its expected character at global index `i`. At every position, a binary character matches exactly one of the two complementary patterns. Therefore, if `cnt` characters mismatch `0101...` in a window of length `n`, exactly `n - cnt` mismatch `1010...`. Tracking one count is enough for both targets.

**Initialize the unrotated window.** The expression

`sum(c != target[i & 1] for i, c in enumerate(s))`

counts how many positions of the original string differ from `0101...`. In Python, each Boolean comparison contributes one for true and zero for false. `ans = min(cnt, n - cnt)` records the smaller flip count for either alternating pattern before using any type-1 operation.

**Slide one character from the front to the back.** On iteration `i`, character `s[i]` leaves its old conceptual doubled position `i` and re-enters at position `i + n`. The update first removes its old mismatch contribution:

`cnt -= s[i] != target[i & 1]`.

It then adds the mismatch at the new global position:

`cnt += s[i] != target[(i + n) & 1]`.

All other characters keep the same doubled indices in the sliding window, so their mismatch contributions remain valid. After this pair of updates, `cnt` describes the rotation whose window begins at `i + 1`.

**Why global parity describes the rotated target.** An alternating window can begin with either digit, so comparing window positions to the global `0101...` pattern is sufficient: the complementary count covers the other start. The window beginning at doubled index `r` occupies global positions `r` through `r + n - 1`. Matching its characters against parity at those global positions is an alternating pattern across the window. If `r` is odd, its first expected bit is one instead of zero, but the two tracked complementary choices still cover both possibilities.

**Even and odd lengths behave differently automatically.** If `n` is even, positions `i` and `i + n` have the same parity. Removing and re-adding the moved character uses the same expected bit, so `cnt` does not change. A cyclic rotation of an even-length alternating pattern merely swaps which of the two complementary patterns is visible; rotation cannot improve the minimum beyond the initial comparison.

If `n` is odd, `i + n` has the opposite parity from `i`. Moving one character changes which expected bit it faces, so different cuts can have different flip costs. The update examines all of them in linear time. No parity-specific branch is necessary.

**Take the minimum after every rotation.** `ans = min(ans, cnt, n - cnt)` compares the best answer so far with both alternating targets for the newly simulated window. The loop performs `n` updates, including the final move that returns to the original cyclic arrangement. Rechecking that duplicate orientation is harmless and keeps the loop structure simple.

**Trace a short odd string.** For `s = "111"`, the initial mismatch count against `010` is two, and the complementary cost is one. Moving the first `1` from global index zero to index three changes its expected target from `0` to `1`, reducing `cnt` by one. The rotated text is still `111`, but its alignment against the global pattern changes; the complementary minimum remains one. The algorithm returns one, correctly flipping the middle character to form `101`.

**Why every legal strategy is represented.** Type-1 operations only choose a cyclic rotation; applying more than `n - 1` of them repeats an earlier rotation. For any chosen rotation, the minimum type-2 operations is simply the Hamming distance to one of the two alternating strings, because each mismatching position must be flipped and flipping exactly those positions suffices. The rolling count evaluates both distances for every rotation, so its global minimum is exactly the optimal number of flips.

## Complexity detail

Let $n$ be the string length. Initial mismatch counting visits all characters once. The rotation loop has $n$ iterations and performs constant work in each. Total time is $O(n)$.

The source stores only `n`, the two-character target, the current mismatch count, the answer, and a loop index. It does not create `s + s`, a prefix array, or copies of rotations. Auxiliary space is $O(1)$, matching the manifest. The generator used by `sum` is lazy.

The count always stays between zero and $n$. Boolean arithmetic is exact, and all string indexing operations are constant time in Python. The maximum stated $n=10^5$ presents no numeric concern.

## Alternatives and edge cases

- **Explicitly build `s + s`:** A conventional sliding window over the doubled string is easy to visualize and remains $O(n)$ time, but consumes $O(n)$ extra space. The exact source obtains the same entering character from `s[i]`.
- **Prefix and suffix mismatch arrays:** Combining a suffix with a prefix for every cut also works, but uses linear storage and more state than the rolling contribution update.
- **Generate and compare every rotation:** Constructing $n$ strings and scanning each costs $O(n^2)$ and is unnecessary.
- **Length one:** A single character is already alternating. One pattern has zero mismatches, so the method returns zero.
- **Already alternating:** Initial `ans` is zero, which can never be improved, though the source still completes its simple linear scan.
- **Odd length:** Rotations can genuinely change the answer because the moved character switches target parity. The `(i + n) & 1` expression captures exactly that switch.
- **Even length:** Old and new parities are equal, so rotation does not change `cnt`. The method still remains correct without a special-case return.
- **Repeated rotations:** The final loop iteration returns to the starting arrangement. Including it duplicates one candidate but cannot alter the minimum.
- **Binary alphabet dependence:** `n - cnt` is the complementary pattern's mismatch count only because every character is either zero or one. The contract guarantees this.
