## General

The array may contain up to $10^{15}$ elements, so reading every position is impossible. The special guarantee makes sublinear access possible: every distinct value occupies one maximal contiguous block and never appears again after that block ends.

The algorithm stands at the first index `i` of a block, counts that block once, then jumps directly to the first index of the next block. It uses the read-only `BigArray.at` interface and never materializes the array.

**Start of each loop is a block boundary**

Initially `i = 0`, which is the first block's start. At every iteration:

1. Increment `ans` because one new maximal equal-value block has been reached.
2. Read its value `x = nums.at(i)`.
3. Find the smallest index at or after `i` whose value differs from $x$.
4. Set `i` to that index.

If no different value exists, the new index becomes $n$ and the outer loop ends.

Because equal values occur in only one adjacent run, the predicate

`nums.at(j) != x`

is monotone over indices $j=i,\ldots,n-1$: it is false throughout the current block and true everywhere after the block. A binary search can locate the first true position.

**Fast path for a one-element block**

If `i + 1 < n` and `nums.at(i + 1) != x`, the current block has length one. The source advances by one without binary search.

This is a constant-call optimization. It is not needed for correctness, but it prevents paying logarithmic access cost for singleton blocks, which may be common.

**How the `bisect_left` call finds the boundary**

For a block containing at least its first two positions, the source searches:

`bisect_left(range(i, n), True, key=lambda j: nums.at(j) != x)`.

Python applies the key to candidate indices in the range. The resulting conceptual sequence is

`False, False, ..., False, True, True, ...`.

`bisect_left` returns the insertion position of `True`—the number of indices from `i` through the final occurrence of $x$. Importantly, this return value is an offset within `range(i,n)`, not the absolute array index. Therefore the source uses `i += offset`.

If the first different value is at absolute index $q$, the offset is $q-i$, so `i` becomes $q$. If the block reaches the end, every predicate value is false and the insertion position is `n-i`, making `i=n`.

**Why no block is skipped or counted twice**

The loop invariant says `i` is the first position of the next uncounted block. After counting it, the monotone search returns exactly the first position outside it. That is either the next block's start or the end of the array. Induction proves every maximal block is visited once.

For `[1,1,1,3,9,9,9,2,10,10]`, the starts visited are $0,3,4,7,8$, followed by $10$. Those five visits match the five maximal blocks without scanning all internal positions.

## Complexity detail

Let $b$ be the number of blocks and $n$ the virtual array length. A singleton block is handled with $O(1)$ accesses. A longer block boundary uses $O(\log(n-i))$, at most $O(\log n)$, random accesses. Worst-case time and `BigArray.at` call complexity are $O(b\log n)$.

`range(i,n)` is a lazy constant-space object even when $n$ is enormous. The method stores only indices, counters, and a value, while binary search is iterative inside the library. Auxiliary space is $O(1)$.

The bound is expressed in terms of blocks because an answer of $b$ inherently requires recognizing $b$ different runs through the interface.

## Alternatives and edge cases

- **Linear scan:** Comparing adjacent elements takes $O(n)$ remote accesses and is infeasible for $n$ up to $10^{15}$.
- **Pure binary search for every block:** Correct with the same asymptotic bound; the explicit adjacent check improves singleton-block constants.
- **Exponential bracketing:** It can first double a probe distance and then binary-search the boundary. The exact source instead searches the complete remaining index range directly.
- **One block:** Binary search finds no true predicate, advances directly to $n$, and returns one.
- **All singleton blocks:** Every adjacent check differs, producing $O(n)$ accesses; here $b=n$, so output-sensitive work cannot avoid recognizing all blocks.
- **Final singleton:** There is no `i+1` access. The binary search over one false entry returns offset one safely.
- **Repeated value in a later block:** The monotone predicate would fail, but the contract explicitly forbids separated occurrences of the same value.
- **Huge virtual size:** No list of indices is allocated because `range` remains lazy.
- **Optional annotation:** Although the parameter type is optional in the signature, judged calls provide a valid `BigArray`; the source does not handle `None`.
- **Why searching the whole suffix is safe:** The first value different from $x$ begins a block whose value can never equal $x$ later. The predicate stays true after that boundary, satisfying binary search's sorted-key requirement.
- **Access count versus arithmetic size:** Index addition and the lazy range are constant-space operations even when indices need 50 bits; the expensive resource is the number of `at` calls, which remains logarithmic per nonsingleton block.
