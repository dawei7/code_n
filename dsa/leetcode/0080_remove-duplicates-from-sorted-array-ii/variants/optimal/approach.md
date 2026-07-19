## General
**The write pointer owns the complete valid prefix**

Read every value in order. While `write < 2`, every value is permitted. Thereafter, retain a value only when it differs from `nums[write - 2]`; if retained, write it at `nums[write]` and advance the boundary.

**Looking two retained positions back detects exactly a third copy**

Because equal values are contiguous, `value = nums[write - 2]` means at least two copies of that value already occupy the retained suffix, so the current value would be a forbidden third-or-later copy. If it differs, the retained prefix contains at most one copy of the current value at its end, so appending it remains legal.

**In-place writes cannot destroy unread values**

Before each read, `nums[:write]` is the correct at-most-two compression of the processed original prefix. Accepting appends a permitted occurrence; rejecting removes only a third-or-later duplicate. Since `write` never passes the read position, an assignment cannot overwrite an unread input value.

**Trace the two-position comparison**

For `[1,1,1,2,2,3]`, retain the first two 1s and reject the third because it matches two write positions back. Both 2s and the 3 are then retained, producing `[1,1,2,2,3]`.

**Looking two positions back enforces the exact cap**

In sorted order, a third retained copy of the current value would have to equal the value two positions before the write boundary. Rejecting in exactly that case prevents any run from growing beyond two.

If the current value differs from that position, fewer than two equal copies can occupy the retained suffix, so accepting it cannot violate the cap. The first two values are always safe. Processing all input values this way preserves up to two copies of every run and rejects only excess copies.

## Complexity detail
One pass reads each element once, giving $O(n)$ time. Read and write indices use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Delete excess items with list removal:** repeated shifting can take $O(n^2)$ time.
- **Build a new array:** is simple but violates the constant-space in-place requirement.
- **Count each duplicate run first:** remains linear but needs more branching than the two-position rule.
- Arrays of length one or two are retained unchanged. A run of any greater length contributes exactly its first two copies.
- Values beyond the returned prefix are unspecified by the native judge and need not be cleared.
