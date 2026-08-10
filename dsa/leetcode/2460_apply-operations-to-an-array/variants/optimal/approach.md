## General

**Simulate in the required left-to-right order**

The adjacent operations are sequential. An operation can change a value that a later index will inspect, so all comparisons cannot be made from the original array at once.

The first loop visits `i=0` through `n-2`. When `nums[i] == nums[i+1]`, it doubles the left value using `nums[i] <<= 1` and sets the right value to zero. Left shift by one bit multiplies a non-negative integer by two.

Because the array is modified immediately, iteration `i+1` sees the result of iteration `i`. For example, if an operation zeros `nums[i+1]`, the next comparison uses that zero. This matches the statement's sequential semantics.

Equal zeros also satisfy the equality condition. Doubling zero and setting the next value to zero leaves both unchanged, so the code may execute the branch without affecting the result.

A doubled value is written at index `i` after that index's comparison has begun, so it is never compared again as the left member of a later operation. The zero written at `i+1` is compared in the next iteration. For a run such as `[2,2,2]`, the first operation makes `[4,0,2]`; the second compares 0 with 2 and does nothing. It would be incorrect to combine the last two original twos after the first pair has already changed the shared middle position.

**Separate combination from zero shifting**

After all adjacent operations, the problem asks for a stable compaction: nonzero values keep their relative order, and enough zeros fill the remaining suffix.

The exact source allocates `ans = [0] * n`. Pointer `i` identifies the next output position for a nonzero value. Scanning the mutated `nums` from left to right:

- If `x` is zero, it is skipped.
- If `x` is nonzero, it is written to `ans[i]` and `i` increments.

Since `ans` started entirely zero, every position not overwritten remains zero. Nonzero values are written in encounter order, so compaction is stable.

For `[1,2,2,1,1,0]`, sequential operations produce `[1,4,0,2,0,0]`. The second pass writes 1, 4, and 2 into the first three answer positions, leaving the last three zeros.

For `[0,1]`, no equality operation changes the array. Compaction skips the leading zero, writes 1 at answer index zero, and returns `[1,0]`.

**Why every operation is simulated exactly once**

The first loop's index corresponds one-to-one with the $n-1$ prescribed operations. At each index it checks the current adjacent values, applies exactly the specified update when equal, and does nothing otherwise. Induction over the loop proves the mutated `nums` equals the statement's array after the same number of operations.

The compaction pass then produces the unique sequence consisting of all nonzero values from that final intermediate array followed by all its zeros. It neither invents nor loses a value: each nonzero is copied once, while the preallocated length preserves the correct total number of positions.

**The exact storage differs from the manifest wording**

The summary says nonzero values are compacted in place with $O(1)$ space. The protected code creates a new length-$n$ list `ans` and returns it. It does not shift zeros inside `nums`.

If returned-output storage is excluded by convention, one might describe working state beyond the output as constant. Operationally, however, the method allocates $O(n)$ new storage, while also mutating `nums` during the first phase. A caller sees the intermediate operated array in `nums`, not the final compacted answer.

## Complexity detail

The operation loop examines $n-1$ adjacent pairs. The compaction loop examines $n$ values. Every iteration does constant work, so total time is $O(n)$.

The returned list has $n$ entries and is newly allocated, giving $O(n)$ additional storage in the exact implementation. Apart from that output list, only dimension and pointer scalars use $O(1)$ space.

The maximum doubled value is at most 2000 because each original position is processed once as a left operand and newly doubled values are never moved left during the operation phase. Python arithmetic is safe regardless.

Compaction performs no arithmetic on the values. It changes only their positions in the newly allocated answer, so the multiset of nonzero results from the operation phase is preserved exactly.

## Alternatives and edge cases

- **In-place stable compaction:** Use a write pointer to move nonzero values forward in `nums` after operations, then fill the suffix with zeros. This matches the manifest's $O(1)$ auxiliary-space claim.
- **Combine operation and compaction carefully:** A one-pass method is possible but must respect that a newly produced zero participates in the next prescribed comparison. Separating phases is easier to verify.
- **Apply all comparisons simultaneously:** This is incorrect because later operations must observe earlier mutations.
- **Adjacent equal zeros:** The branch executes but changes nothing.
- **No equal adjacent values:** Only the compaction phase changes the arrangement.
- **All zeros:** Every operation is harmless and the returned array remains all zeros.
- **All nonzero after operations:** Every value is copied to the same relative position and no trailing zero is added.
- **Stable order:** Nonzero values must not be sorted; the write pointer preserves encounter order.
- **Input mutation:** The first phase changes `nums` even though the final shifted result is stored separately.
- **Exact array length:** Preallocating $n$ positions guarantees that the count of removed interior zeros reappears at the end.
