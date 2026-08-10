## General

**A partition cannot end before the last occurrence of any letter it contains**

If the current part contains character `c`, every occurrence of `c` must remain in that same part. Therefore its right boundary must reach at least `last[c]`, the character’s final position in the whole string.

The solution first builds a dictionary of final positions. The comprehension overwrites earlier indices, leaving the last index for each lowercase letter.

**Grow the smallest valid current boundary**

Variable `j` is the current part’s start. Variable `mx` is the farthest last occurrence required by every character seen since `j`.

While scanning index `i` and character `c`, the update

`mx = max(mx, last[c])`

extends the required boundary if this character appears farther right.

Characters encountered inside that extension may themselves have later occurrences, so the scan continues and keeps expanding `mx` until all dependencies are contained.

**Close exactly when the scan reaches the boundary**

When `i == mx`, every character seen in the current part has its last occurrence at or before `i`. No such character appears later, so cutting after `i` is valid.

The length is `i - j + 1`. The next part begins at `i + 1`.

**Why closing immediately maximizes the number of parts**

At `i == mx`, the current part is valid. Extending it farther would only merge characters that could have belonged to later parts and could never increase the number of pieces.

Before that moment, a cut is impossible because some character already in the part appears after the proposed boundary. Thus the first valid boundary is both forced as the earliest cut and optimal for maximizing partition count.

**Trace the first partition**

In `"ababcbacadefegdehijhklij"`, the first character `a` last appears at index eight, so `mx` becomes eight. Characters `b` and `c` encountered before then have last occurrences no later than eight. The scan reaches eight without extending farther and closes a part of length nine.

The next character `d` begins a new dependency range that eventually ends at index fifteen, producing length seven. The final range has length eight.

**Why repeated characters do not cross boundaries**

A part closes only after the last occurrence of every character it has encountered. Consequently no character inside that part can appear in a later part.

Conversely, a character first encountered after a cut obviously did not appear in the closed part, or its last occurrence would have forced the boundary past the cut.

**Occurrence intervals explain the greedy merge**

Each character defines an interval from its first occurrence to its last. Valid partitions cannot split any such interval. Scanning the string and extending `mx` is equivalent to merging all character intervals that overlap the current component.

When the scan reaches the merged component’s right endpoint, no character interval crosses farther, so a partition boundary is possible. This interval viewpoint explains why dependencies can chain: one character extends the boundary, and a new character encountered inside that extension may extend it again.

**Why `mx` need not be reset explicitly**

After a cut, `j` advances to the next index. On that next iteration, `last[c]` is at least the current index and therefore replaces or exceeds the old `mx`, which equaled the previous index. The maximum update naturally starts the new component without a separate assignment.

**The loop invariant**

Before each equality check, `mx` equals the maximum last occurrence among characters from current start `j` through current index `i`. This is true at the first character and is preserved by the maximum update.

The equality condition therefore means precisely that all obligations introduced by the part have been fulfilled.


Every emitted boundary is valid by the invariant: all characters in the part end there or earlier. No earlier boundary could be valid because `mx > i` would identify a character crossing it.

Choosing each earliest possible boundary leaves the longest possible suffix for additional partitions. Induction over the remaining suffix proves the greedy scan produces the maximum number of valid parts, and the recorded sizes reconstruct the original string in order.

## Complexity detail

Let `n` be the string length. Building last occurrences takes `O(n)` time, and the greedy scan takes another `O(n)`. Total time is `O(n)`.

The dictionary contains at most 26 lowercase letters, so its space is `O(1)` relative to input length. The output list may contain `O(n)` sizes and is required result storage.

## Alternatives and edge cases

- **Expand each partition with repeated searches:** Repeatedly finding last positions can become quadratic. Precompute them once.

- **Cut after a character’s first occurrence:** Later copies would cross the boundary and invalidate the partition.

- **Delay a valid cut:** This remains valid but reduces or preserves, never increases, the number of parts.

- **All characters unique:** Every last occurrence is the current index, so every character forms a length-one part.

- **One character repeated throughout:** Its last occurrence forces a single part containing the whole string.

- **Nested occurrence ranges:** Taking the maximum automatically absorbs every dependency encountered before the boundary.

- **Output sizes:** `i - j + 1` includes both endpoints and the lengths sum to `n`.
