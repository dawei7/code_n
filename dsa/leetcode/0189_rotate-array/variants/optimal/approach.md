## General

**Reduce large rotations to one equivalent shift**

Rotating an array of length $n$ right by $n$ positions returns every element to
its original index. Therefore only the remainder `k % n` matters. The statement
guarantees that `nums` is nonempty, so `k %= n` cannot divide by zero.

This normalization handles both very large values and exact multiples of the
length. If the remainder is zero, the desired result is the original array;
the later reversals still produce that result without a special branch.

**Describe the desired block movement**

After normalization, split the original array conceptually into two blocks:

- `A`, the first $n-k$ elements.
- `B`, the final $k$ elements.

A right rotation changes `A B` into `B A`. The challenge is to perform that
block swap in place without allocating another length-$n$ array. Three
reversals accomplish it because reversing a concatenation reverses both the
block order and the character order inside each block.

**Use an inclusive reversal helper**

The nested `reverse(i, j)` treats both indices as included. While `i < j`, it
swaps the two endpoint values and moves the pointers inward. An odd-length
interval leaves its middle element untouched after all surrounding pairs have
been swapped. Empty or one-element intervals perform no swaps.

Only a constant number of indices and temporary references are used. Python's
parallel assignment exchanges list elements in the existing list rather than
constructing a replacement array.

**First reversal: reverse the complete array**

`reverse(0, n - 1)` transforms the conceptual sequence `A B` into:

`reverse(B) reverse(A)`

This already moves the original suffix in front of the original prefix, which
is the correct block order. However, the elements inside both blocks are
backward and must be repaired.

**Second reversal: restore the new prefix**

The first $k$ positions now contain `reverse(B)`. Calling
`reverse(0, k - 1)` reverses those positions again, restoring `B` to its
original internal order.

When `k = 0`, this call receives the interval `(0, -1)`. The condition
`0 < -1` is false, so it safely does nothing. No negative index is accessed.

**Third reversal: restore the new suffix**

The positions from `k` through `n - 1` contain `reverse(A)`. Calling
`reverse(k, n - 1)` restores that block. The array is now exactly `B A`, which
is the desired right rotation.

When `k = n - 1`, the suffix contains one element and needs no swap. When the
normalized `k` is zero, this third call reverses the whole array a second time,
cancelling the first global reversal and restoring the input.

**Trace the seven-element example**

For `[1,2,3,4,5,6,7]` and `k = 3`, conceptual blocks are
`A = [1,2,3,4]` and `B = [5,6,7]`.

- Reverse everything: `[7,6,5,4,3,2,1]`.
- Reverse the first three: `[5,6,7,4,3,2,1]`.
- Reverse positions three through six: `[5,6,7,1,2,3,4]`.

All values are the original objects; only their positions change.

**Why every element reaches the correct index**

An original element in suffix `B` must move to the front while retaining its
relative order among suffix elements. The global reversal moves it into the
first $k$ positions but reverses that relative order; the prefix reversal
reverses the order again and restores it.

An original element in prefix `A` similarly moves into the last $n-k$
positions, is reversed globally, and is restored by the suffix reversal. The
two blocks cover every index and do not overlap after the first phase, so every
element is handled exactly as required.

Equivalently, the target index of original position $i$ is $(i+k) \bmod n$.
The block argument shows the same mapping without moving elements one at a
time.

**Honor mutation and return semantics**

The method has no explicit return statement, so it returns `None`. The caller
observes the answer through the same `nums` list object. Rebinding a local name
to a new list would not meet that interface; these swaps mutate the supplied
object directly.

The exact source uses the annotation `List[int]` without importing `List` in
the file. A LeetCode-style harness may supply it, but standalone execution
normally needs `from typing import List` or the built-in `list[int]` form.

## Complexity detail

Let $n$ be the array length. The three reversal lengths are $n$, $k$, and
$n-k$. Their total is $2n$, so the number of swaps and pointer updates is
$O(n)$. Normalizing `k` takes constant time.

The helper uses only two indices and constant-size swap temporaries. No slice
or auxiliary array is created, so extra space is $O(1)$. The input list does
not count as auxiliary storage.

## Alternatives and edge cases

- **Cyclic replacement:** Follow target indices `(i + k) % n` and use one temporary value; also $O(n)$ time and $O(1)$ space, but multiple index cycles require careful counting.
- **Extra array:** Write each value directly to its target index, then copy back; straightforward $O(n)$ time but $O(n)$ extra space.
- **Repeated one-step rotation:** Constant space but $O(nk)$ time after normalization.
- **Left/right block interpretation:** Right rotation by `k` is also left rotation by `n - k`; the reversal boundaries must match the chosen direction.
- **`k = 0`:** The first and third full reversals cancel while the empty prefix reversal does nothing.
- **`k` multiple of `n`:** Normalizes to zero and leaves the array unchanged.
- **One element:** Every reversal is empty or length one, so the sole value remains.
- **Negative and duplicate values:** Movement depends only on indices, not value comparisons.
- **Nonempty guarantee:** Required for `k %= n`; a generalized API should guard an empty list.
- **Missing typing import:** Supply `List` outside a harness that already defines it.
