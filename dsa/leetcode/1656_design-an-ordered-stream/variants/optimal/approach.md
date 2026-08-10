## General

**Separate arrival order from output order**

Pairs arrive in arbitrary order, but values must leave the stream in increasing `idKey` order. The central difficulty is not sorting all pairs after they arrive; each call must immediately return the largest consecutive chunk that has just become available. A value with a large ID may arrive early and wait, while inserting one missing smaller ID may suddenly unlock several stored values.

The implementation uses two pieces of persistent object state:

- `data` stores each value at the array index equal to its ID;
- `ptr` identifies the smallest ID whose value has not yet been returned.

The constructor sets `ptr = 1` because valid IDs start at one. It allocates `n + 1` entries so that index and ID can match directly. Index zero is deliberately unused. This one extra slot avoids repeatedly converting between a one-based problem ID and a zero-based Python index.

Every slot begins as `None`, which means that the corresponding pair has not arrived. The contract says every insertion has a unique ID, so an existing value never needs to be overwritten as part of normal operation.

**The pointer invariant**

Immediately before and after every call, `ptr` satisfies a precise invariant:

> Every ID smaller than `ptr` has already been returned exactly once, while `ptr` is the first ID that has not yet been returned.

An ID at or above `ptr` might already be stored, but it cannot be emitted while a smaller required ID is missing. This invariant explains why there is no need to search the whole array for the next result. The next possible output must begin exactly at `ptr`.

When `insert(idKey, value)` is called, the assignment `self.data[idKey] = value` records the arrival in constant time. The method then creates an empty call-specific result list `ans`. If the insertion did not fill the current `ptr` slot, that slot is still empty and the loop does nothing. Returning an empty list is correct because the required next ID is missing; no later stored ID may leap over that gap.

If the current pointer slot is filled, the method enters the loop. It appends `data[ptr]`, increments `ptr`, and immediately tests the next slot. This continues while IDs are consecutive and already present. The condition `self.ptr < len(self.data)` prevents reading beyond the allocated array after ID `n` has been emitted.

The second condition, `self.data[self.ptr]`, uses the stored value’s truthiness to distinguish a filled slot from `None`. This is safe under the contract because every value has length five and is therefore nonempty. If empty strings were permitted, an explicit `is not None` check would be needed.

**Why the returned chunk is the largest possible one**

Suppose `ptr` has value `p` when a call starts its scan. By the invariant, IDs below `p` have already been returned and must never appear again. Therefore any new valid chunk must start with ID `p`.

If slot `p` is empty, no valid nonempty chunk exists, so the empty answer is maximal. If it is filled, the loop emits it and checks `p + 1`. At each subsequent step, the next value is appended exactly when its slot is filled. The loop stops only for one of two reasons: it reaches the end after emitting ID `n`, or it reaches the first not-yet-inserted ID. In the latter case, including any higher ID would violate increasing consecutive order. Thus the accumulated list cannot be extended and is the largest possible chunk.

After appending an item, `ptr` moves past it. Consequently every ID smaller than the new pointer has been emitted. The stopping slot has not been emitted, and no greater slot has been emitted out of turn, so the pointer invariant is restored for the next call.

**A trace showing delayed values**

Take `n = 5` and insert ID `3` first. It is stored in `data[3]`, but `ptr` remains `1` because ID `1` is absent. The returned chunk is empty. Inserting ID `1` next fills the pointer slot, so the loop returns only its value and moves `ptr` to `2`; ID `3` is still blocked by missing ID `2`.

When ID `2` arrives, the loop first appends the value at ID `2` and advances. ID `3` was saved earlier, so it is immediately appended in the same call. The pointer then stops at missing ID `4`. This demonstrates why stored future values need no special queue or sorting step: the array preserves them until the advancing frontier reaches them.

**Why the complete output is correct**

The invariant proves that no value is returned twice: once its slot is emitted, `ptr` permanently moves beyond it. It also proves that no value is returned out of order: a chunk begins at the smallest unreturned ID and advances only one ID at a time. Exactly `n` unique calls occur, so every slot from `1` through `n` is eventually filled. Once all calls finish, the loop will have crossed every slot, which means every value has been returned.

Therefore concatenating the chunks yields each inserted value exactly once and in increasing ID order, as required.

## Complexity detail

Constructing an `OrderedStream` allocates and initializes `n + 1` slots, taking $O(n)$ time and $O(n)$ persistent space.

For one `insert` call, storing the value takes $O(1)$ time. If that call unlocks a chunk of length `c`, the loop performs `c` appends and pointer increments, so the call takes $O(c + 1)$ time. A single call can therefore take $O(n)$ in the worst case when it fills the final gap before many previously stored values.

Across the complete sequence of exactly `n` insertions, however, each value is appended and each pointer position is crossed only once. The total loop work is $O(n)$, and the total work of all insertion assignments is also $O(n)$. Thus all operations together take $O(n)$ time, or $O(1)$ amortized administrative work per insertion plus the unavoidable size of the returned chunk.

The persistent `data` array uses $O(n)$ space. The list returned by one call uses $O(c)$ space, and all returned chunks contain $O(n)$ elements in total. `ptr` itself is constant space.

## Alternatives and edge cases

- **Sort all received pairs after every insertion:** This can recover ID order but repeatedly performs unnecessary work and still needs logic to know which prefix has already been emitted. Direct indexing plus the frontier pointer is simpler and gives linear total work.
- **Min-heap of arrived IDs:** A heap can reveal the smallest stored ID, but IDs are already bounded and unique, and output must wait for one exact next ID. Heap operations add $O(\log n)$ overhead without improving the decision.
- **Hash map instead of an array:** A dictionary keyed by ID also works and may suit sparse unbounded IDs, but here every ID from `1` to `n` arrives exactly once, so the direct array is smaller conceptually and has predictable indexing.
- **Insertion before the current gap:** Under the unique-ID contract, this cannot happen because every ID below `ptr` was already inserted and emitted. Without uniqueness, the class would need a policy for duplicate IDs.
- **Insertion after the current gap:** The value is stored but the returned list stays empty; it will be emitted later when all preceding IDs have arrived.
- **One insertion unlocks many values:** The while loop intentionally returns the entire consecutive run, including values stored during much earlier calls.
- **First ID arrives last:** All other values remain safely stored. Inserting ID `1` on the final call returns all `n` values in one chunk.
- **`n == 1`:** The array has indices zero and one. The only insertion fills `data[1]`, returns its value, and advances `ptr` to the array length.
- **End-of-stream boundary:** After ID `n` is emitted, `ptr == len(data)`. The left side of the short-circuit condition fails, so the code never indexes beyond the array.
- **Empty values outside the contract:** The truthiness test would mistake `""` for a missing slot. The stated fixed length of five makes the implementation correct; a generalized class should test `is not None`.
