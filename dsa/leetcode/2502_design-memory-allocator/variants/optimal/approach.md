## General

**Represent every memory unit by its current owner**

The allocator stores `self.m`, an array of length `n`. Entry zero means the unit is free, while a positive entry is the `mID` that owns it.

This encoding is unambiguous because the constraints require `mID>=1`. It also naturally supports the same identifier owning several separated blocks: every owned unit independently stores that identifier.

At construction, `[0]*n` marks all units free.

**Find the leftmost free run during allocation**

`allocate(size,mID)` scans the memory array from index zero upward. Variable `cnt` is the length of the consecutive free run ending at the current index.

- If `v` is nonzero, the current unit is occupied and no free run can cross it, so `cnt` resets to zero.
- If `v` is zero, the current free run extends by one and `cnt` increments.

When `cnt==size` at index `i`, the run begins at

`i-size+1`

and ends at `i`.

The slice

`self.m[i-size+1:i+1] = [mID]*size`

assigns every unit in that block to the requested identifier. The method immediately returns the start index.

**Why the first found run is the leftmost**

The scan examines end indices in increasing order. A block of fixed length `size` has start `end-size+1`, which also increases with its end.

The first time a free-run counter reaches `size` is therefore the smallest possible end and smallest possible start of any fitting block. Returning immediately implements the leftmost requirement.

A longer free region causes allocation at its first `size` positions. The scan does not wait to see whether an even larger free run exists because size, not maximum capacity, determines the request.

**Why resetting `cnt` is essential**

Consecutive means there can be no occupied unit between selected positions. When the scan reaches an owned entry, all earlier free cells become unusable for a block ending later. Resetting discards that interrupted run.

For state `[0,0,3,0,0,0]` and `size=3`, the first two zeroes do not combine with the final three because value 3 separates them. The reset makes the accepted block begin at index 3.

**Allocation failure preserves memory**

The array is modified only inside the branch where a full run has been found. If the loop finishes without `cnt==size`, no slice assignment occurs and the method returns `-1`.

Thus a failed allocation has no side effects.

**Free every unit with the requested identifier**

`freeMemory(mID)` scans the complete memory array. Whenever `v==mID`, it writes zero and increments `ans`.

The method deliberately does not stop after one contiguous block. The same identifier may own multiple blocks created by separate calls, and the contract requires all of them to be freed.

At the end, `ans` equals the number of changed entries and therefore the exact number of released memory units. If the identifier owns nothing, no entry changes and zero is returned.

**State invariants across operations**

After construction and after every method call:

- each array entry is either zero or one allocated identifier;
- an allocation writes only currently free consecutive entries;
- freeing one identifier cannot disturb units owned by another;
- the array indices remain the memory addresses from zero through `n-1`.

Allocation preserves the invariant because its run consists entirely of zeroes before the slice write. Freeing preserves it by replacing matching positive entries with the free sentinel.

**Walk through reuse**

If units 0, 1, and 2 are separately owned and unit 1 is freed, a later size-one allocation finds index 1 before any free unit to its right. For a larger request, that single hole is too short, `cnt` resets at the next occupied unit, and scanning continues.

This behavior matches fragmentation in the example: total free capacity can be large while no sufficiently long consecutive block exists.

**The class persists state**

`self.m` belongs to the allocator object, so every call sees modifications made by earlier calls. Local variables `cnt` and `ans` are recreated per call because they describe only the current scan.

## Complexity detail

Let $n$ be the memory-array size and $q$ the total number of method calls.

One allocation scans at most $n$ entries. Its successful slice assignment writes `size<=n` entries, so the whole call is $O(n)$. One free call always scans $n$ entries and is also $O(n)$. Across all calls, worst-case time is $O(qn)$.

The persistent memory array uses $O(n)$ space. A successful allocation creates the temporary list `[mID]*size`, which can use $O(n)$ additional space before slice assignment. Thus peak auxiliary storage in the exact Python implementation is $O(n)$.

## Alternatives and edge cases

- **Free-interval tree:** Track free ranges for faster allocation, but merging after frees becomes more complex.
- **Segment tree:** Store maximum free prefix, suffix, and run lengths to find blocks faster when constraints are much larger.
- **Size one:** The first zero entry is allocated immediately.
- **Request fills all memory:** It succeeds only when the full array is free.
- **Enough total free units but fragmented:** Allocation correctly returns `-1` if no consecutive run is long enough.
- **Repeated `mID` allocations:** They may form separate blocks; freeing scans and releases all of them.
- **Unknown `mID` on free:** Return zero without changing state.
- **Leftmost rule:** Immediate return at the first completed run is essential.
- **Sentinel zero:** It is safe only because valid identifiers are positive.
- **Failed allocation:** It performs no partial write.
