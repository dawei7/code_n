## General

**Separate movable values from fixed positions**

Negative values are barriers only in the layout: they must remain at their exact indices, but they do not divide the non-negative values into independent rotation groups. Reading all non-negative values from left to right produces one logical sequence that rotates as a whole.

The source extracts that sequence with

`t = [x for x in nums if x >= 0]`.

Zero is included because “non-negative” means greater than or equal to zero. Every negative number is excluded from `t` but remains in `nums` for later preservation.

Let $M=\lvert\texttt{t}\rvert$. The relative positions available for reinsertion are exactly the $M$ indices that originally contained non-negative values. Rotating `t` and writing it back to those positions completely describes the requested transformation.

**Map each source position to its left-rotated destination**

A left rotation by one moves the element at logical index 0 to index $M-1$, index 1 to 0, index 2 to 1, and so on. More generally, the element originally at logical index `i` moves to

$$
(i-k)\bmod M.
$$

The source allocates `d = [0] * m` for the rotated sequence and performs

`d[((i - k) % m + m) % m] = x`

for every `(i, x)` in `t`. This writes each original non-negative value directly into its destination.

Modulo makes rotation cyclic. If `i - k` is negative, wrapping sends it to the end of `d`. If `k >= M`, only `k % M` affects the destination, so the code automatically normalizes arbitrarily large allowed rotations.

In Python, `(i - k) % m` is already nonnegative when `m > 0`, so the added `+ m` and second modulo are redundant. They express the common language-independent normalization

$$
((i-k)\bmod M+M)\bmod M,
$$

which is needed in languages whose remainder for a negative dividend may remain negative.

**The destination mapping is a permutation**

For fixed `k` and positive `M`, two different logical indices cannot map to the same destination modulo $M$. If

$$
(i_1-k)\bmod M=(i_2-k)\bmod M,
$$

then $i_1\equiv i_2\pmod M$. Both indices lie between 0 and $M-1$, so they must be equal. Every destination receives exactly one value.

This ensures the zero placeholders in `d` are all overwritten before reinsertion. They are only allocation placeholders; they are not confused with real zero values.

The mapping also preserves the cyclic order. The value from source index `k % M` lands at destination 0, the next source value lands at destination 1, and so on, which is precisely a left rotation.

**Reinsert without moving negative entries**

After `d` is complete, `j` starts at 0. The second loop visits every physical index of `nums` in order. If the current value `x` is non-negative, that index is one of the movable slots, so the source writes `d[j]` there and increments `j`. If `x` is negative, the loop does nothing, leaving both its value and position unchanged.

The test uses the original classification of the current slot. Although `nums` is mutated during this pass, each loop iteration reads its current index before writing that same index, and earlier writes never alter a future index. Thus the sign test for each not-yet-visited position still observes the original value.

Writing `d` from left to right into the non-negative slots preserves the rotated sequence's logical order while skipping every fixed negative location.

For `nums = [5,4,-9,6]` and `k = 2`, extraction gives `t = [5,4,6]`. The destination mapping places 5 at index 1, 4 at index 2, and 6 at index 0, producing `d = [6,5,4]`. Reinsertion writes 6 and 5 into physical indices 0 and 1, skips -9 at index 2, and writes 4 at index 3. The result is `[6,5,-9,4]`.

**All-negative input avoids modulo by zero**

If no non-negative value exists, `m = 0` and `d` is empty. The first `for` loop has no iterations because `t` is empty, so its modulo expression is never evaluated; there is no division-by-zero error. The reinsertion loop finds no `x >= 0` positions, leaves every negative value untouched, and returns the original array.

A single movable element is similarly safe. Every destination is `0 % 1 = 0` regardless of `k`, so the one value remains in place.

**Mutation behavior of the exact source**

The source modifies `nums` in place during reinsertion and returns that same list object. The contract asks for the resulting array and does not forbid mutation, so this behavior is valid. A caller that needs the original list separately would have to pass a copy or use a non-mutating variant.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and $M$ be the number of non-negative elements. Extraction scans $N$ values and stores $M$ of them. Building `d` performs $M$ constant-time modular assignments. Reinsertion scans all $N$ positions. Total time is $O(N+M)=O(N)$.

The arrays `t` and `d` each contain $M$ integers, so auxiliary space is $O(M)$, which is $O(N)$ in the worst case. The output reuses `nums` rather than allocating another full result, but the two extracted/rotated buffers still determine the linear space bound.

## Alternatives and edge cases

- **Slice-based rotation:** After extraction, compute `r = k % M` and use `t[r:] + t[:r]`. This is shorter but must branch when $M=0$ before taking the modulo; it has the same $O(N)$ time and $O(M)$ space.
- **Queue of movable values:** A deque can rotate the extracted sequence and then feed values back into movable slots. It expresses the cyclic operation directly but still needs $O(M)$ storage.
- **In-place cycle decomposition:** Store the movable indices and permute their values by rotation cycles. This can avoid the second value array but requires careful visited or gcd-cycle handling and still stores indices unless they are repeatedly rediscovered.
- **All values negative:** No element is movable, both logical rotation loops do no effective work, and the input remains unchanged.
- **Zero values:** Zero belongs to the rotating sequence because the predicate is `x >= 0`, not `x > 0`.
- **Rotation by zero:** Every source index maps to itself, and reinsertion reconstructs the original array.
- **Rotation by a multiple of $M$:** Modulo maps every value back to its original logical slot, so the result is unchanged.
- **One non-negative value:** Any cyclic rotation of a length-one sequence is identical.
- **Negative barriers:** They retain both value and physical index, but non-negative values on opposite sides still participate in one shared cyclic sequence.
- **Large k:** The formula normalizes `k` implicitly at every destination; performing the rotation one step at a time would waste $O(kM)$ work.
- **Returned object identity:** The exact implementation mutates and returns `nums`. A non-mutating interface would first copy the array, increasing output allocation but not changing asymptotic complexity.
