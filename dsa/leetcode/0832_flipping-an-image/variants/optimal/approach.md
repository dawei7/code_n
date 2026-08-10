## General

**Combine reversing and inverting instead of doing two full operations**

For each row, the requested result first reverses the row and then flips every binary bit. Consider a mirrored pair at indices `i` and `j = n-1-i` with original values `a = row[i]` and `b = row[j]`.

After reverse and invert, the desired new values are:

$$
\text{new left}=1-b,
$$

$$
\text{new right}=1-a.
$$

Because values are binary, this leads to a useful shortcut based on whether `a` and `b` are equal.

**Equal mirrored bits must both change**

If `a == b`, reversing the pair has no visible effect because equal values trade places. Inversion then changes both:

- `(0,0)` becomes `(1,1)`;
- `(1,1)` becomes `(0,0)`.

The code performs these changes with

`row[i] ^= 1` and `row[j] ^= 1`.

XOR with 1 toggles a binary value: `0 ^ 1 = 1` and `1 ^ 1 = 0`.

**Different mirrored bits need no change at all**

If the pair differs, it is either `(0,1)` or `(1,0)`. Reversing swaps it, and inversion flips both swapped bits:

- `(0,1) -> (1,0) -> (0,1)`;
- `(1,0) -> (0,1) -> (1,0)`.

The combined operation returns the pair to its original values. Therefore, the exact source does nothing when `row[i] != row[j]`.

This may look surprising because the task says to reverse every row, but the two requested transformations cancel on unequal mirrored pairs. The algorithm computes the final state directly rather than materializing the intermediate reversed row.

**Move inward with two pointers**

For every row, `i` starts at 0 and `j` starts at `n-1`. While `i < j`, the code handles one mirrored pair, then advances `i` and decrements `j`.

Every noncentral position belongs to exactly one such pair. When the pointers cross, all pairs are finished.

**Handle the middle cell of an odd-length row**

If `n` is odd, the pointers eventually meet at the central index. Horizontal reversal leaves this cell in the same position, but inversion must still toggle it. The condition `if i == j` applies `row[i] ^= 1` once.

If `n` is even, the pointers cross without meeting, so there is no middle cell and the branch is skipped.

**Trace one row**

Take `[1,1,0]`.

- The outer pair is `(1,0)`, which differs, so it remains unchanged. This already equals the outer values after reverse-plus-invert.
- The pointers meet at the center value 1, which is toggled to 0.

The final row is `[1,0,0]`. Explicitly reversing would give `[0,1,1]` and then inverting would also give `[1,0,0]`.

For `[1,0,0,1]`, both outer and inner mirrored pairs are equal: `(1,1)` and `(0,0)`. Toggling both pairs produces `[0,1,1,0]`, matching the combined transformation.

**Why the in-place transformation is correct**

Partition a row into mirrored pairs and, for odd length, one center. For each pair, the equal/different analysis proves that the code writes exactly the two values produced by reverse then invert. The center stays in place under reversal and is toggled once, also exactly correct.

These parts are disjoint and cover the entire row. Applying the same reasoning independently to every row proves that the returned matrix is the required flipped and inverted image.

The function returns the original `image` object after modifying its row elements; it does not allocate a second matrix.

## Complexity detail

An `n \times n` image has `n^2` cells. Each row processes about `n/2` mirrored pairs and possibly one center, so every cell participates in constant work. Total time is `O(n^2)`.

The exact implementation transforms the matrix in place and uses only two pointers plus loop variables, giving `O(1)` auxiliary working space. The manifest lists `O(n^2)` space when the returned image itself is included; no additional `n^2` copy is constructed by this source.

If callers require the original matrix to remain unchanged, copying it first would use `O(n^2)` extra space.

## Alternatives and edge cases

- **Reverse then invert explicitly:** Reverse every row and then scan again to toggle all bits. It is clear and still `O(n^2)`, but it performs two logical passes where the pair rule combines them.

- **Construct a new matrix with a comprehension:** Reading `1 - row[n-1-j]` directly is concise and nonmutating, but allocates `O(n^2)` new storage.

- **Unequal mirrored pair:** It must be left unchanged in the combined operation; swapping alone would be incorrect.

- **Equal mirrored pair:** Both positions must toggle, not swap.

- **Odd row length:** The center is inverted exactly once after pair processing.

- **Even row length:** There is no center, and the pointers cross.

- **One-by-one image:** The pointers start equal, so its only bit is toggled.

- **All zeroes:** Every equal pair toggles to ones, producing an all-one image.

- **All ones:** Every pair and center toggles to zero.

- **Symmetric row:** Reversal changes nothing, so the code effectively inverts each position through equal mirrored pairs and possibly the center.

- **Binary-value guarantee:** The cancellation rule relies on two different binary values being complements. It would not hold for arbitrary integers.

- **Input mutation:** The returned object is the same nested list supplied by the caller, with cell values changed in place.
