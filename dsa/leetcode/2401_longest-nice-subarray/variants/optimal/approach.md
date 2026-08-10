## General

**Translate pairwise AND into bit ownership**

Two positive integers have bitwise AND zero exactly when they share no set bit. A subarray is nice when every bit position is set in at most one of its elements.

The algorithm maintains `mask` as the bitwise OR of the current window. Under the nice-window invariant, each set bit in `mask` belongs to exactly one active number.

When a new value `x` arrives, `mask & x` is nonzero precisely when `x` shares a bit with some number already in the window. That is the only reason adding `x` could violate niceness.

**Expand right, shrink left on conflict**

The right pointer scans every element. Before inserting `x`, the loop removes leftmost values while:

```python
mask & x
```

is nonzero. Once the intersection is zero, `x` shares no bit with the entire remaining aggregate. It can be added with `mask |= x`, and the new window is nice.

The algorithm records `r - l + 1` as the longest nice window ending at `r` after shrinking.

**Why XOR removes a departing number**

Removal uses:

```python
mask ^= nums[l]
```

Normally, XOR is not a general way to remove a value from an OR aggregate. Here it is safe because the maintained nice window guarantees no two active numbers share a set bit. Every bit set in `nums[l]` appears exactly once in `mask`. XOR toggles those one bits to zero, while bits belonging to other numbers remain unchanged.

If duplicate bit ownership were allowed, removing one number with XOR could clear a bit still needed by another. The niceness invariant is what makes this compact operation correct.

**Why aggregate disjointness implies all pairwise checks**

If `mask & x == 0`, no set bit of `x` occurs in the OR of existing values. Therefore, it occurs in none of those individual values, so `x & y == 0` for every existing `y`.

Conversely, if `x` shares a bit with any existing number, that bit is set in their OR, making `mask & x` nonzero. The one aggregate test is exactly equivalent to all pairwise tests involving the new element.

Existing pairs were already valid by the window invariant, so no other comparison is needed.

**Trace the example window**

For values `3, 8, 48`:

```text
3  = 000011
8  = 001000
48 = 110000
```

Their set bits are disjoint, so the mask is their OR and the window length is three. When a later value contains a bit already in the mask, the left pointer removes numbers until the conflicting owner leaves.

Some left removals may not clear the relevant conflict immediately because the shared bit belongs to a later window element. The while loop continues until all overlapping bits are gone.

**Why the remaining window is the longest feasible one ending at `r`**

Before adding `x`, the algorithm advances `l` only while a conflict exists. Every removed earlier start still includes the conflicting bit owner and therefore cannot form a nice window ending at `r`.

The first start where the conflict disappears yields a valid window. Starting later would only shorten it. Thus, after the while loop, `[l,r]` is the longest nice subarray with right endpoint `r`.

Taking the maximum across all right endpoints covers every possible optimal subarray.

**Maintain the invariant formally**

Initially, the empty window is nice and `mask = 0`. Removing left values preserves niceness among the survivors and updates their OR exactly by unique-bit XOR. When the conflict test becomes zero, adding `x` gives it disjoint bits from all survivors, so the enlarged window is nice and OR assignment is exact.

Induction across right endpoints proves the mask and window claims throughout the algorithm.

## Complexity detail

The right pointer advances $n$ times. The left pointer also advances at most $n$ times over the entire run; it never moves backward. Each element enters the mask once and leaves at most once. Total time is $O(n)$.

Only the integer `mask`, two pointers, the answer, and current value are stored. Since input values have at most about 30 relevant bits, auxiliary space is $O(1)$.

Bitwise operations are treated as constant time for the bounded integer domain.

## Alternatives and edge cases

- **Bit-frequency array:** Track how many active values use each of 30 bits and decrement on removal. It is more general and explicit but adds a constant factor.
- **Brute-force all subarrays:** Extending every start until a conflict can take $O(n^2)$ time.
- **XOR without the invariant:** It would be unsafe if active numbers shared bits; correctness depends on shrinking before insertion.
- **One element:** Every singleton is nice, so the answer is at least one.
- **All values pairwise conflicting:** Every valid window has length one.
- **Powers of two with distinct bits:** They can coexist in one long nice window.
- **Conflict owned by the leftmost value:** One removal clears it immediately.
- **Conflict owned later:** Several left values may be removed before the owner exits.
- **Positive inputs:** Zero is absent by contract, though adding zero would never create a bit conflict.
