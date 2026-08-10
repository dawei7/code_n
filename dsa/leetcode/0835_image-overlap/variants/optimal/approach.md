## General

**A translation is completely determined by one matched pair of one-cells**

Suppose `img1[i][j] == 1` and `img2[h][k] == 1`. To place these two one-cells on the same final position, `img1` must be translated by the row and column displacement that takes `(i,j)` to `(h,k)`.

The exact source records this displacement as

`(i - h, j - k)`.

Using the opposite sign would describe moving the other image instead, but consistency is all that matters: every pair aligned by one physical translation must produce the same key.

**Turn the problem into voting for a displacement**

The solution examines every one-cell in `img1` and every one-cell in `img2`. Their coordinate difference votes for the translation that would align them:

`cnt[(i - h, j - k)] += 1`.

Fix one displacement `d`. Every counted pair with key `d` represents one cell of `img1` and one cell of `img2` that coincide under that translation. Conversely, every overlapping pair of one-cells under `d` produces exactly that key.

Therefore, `cnt[d]` is exactly the overlap achieved by displacement `d`.

The maximum counter value is consequently the largest possible overlap.

**Why it is enough to consider differences between one-cells**

Any translation with positive overlap aligns at least one one-cell from `img1` with one one-cell from `img2`. Its displacement therefore appears as the coordinate difference of that pair and receives votes in the counter.

A translation with zero overlap cannot improve on any positive one. If every possible translation has zero overlap—because at least one image has no one-cells—the counter stays empty and the correct answer is zero.

There is no need to enumerate an arbitrary unbounded range of shifts. Only shifts capable of aligning at least one relevant pair can matter, and the pair differences enumerate all of them.

**Bits outside the border require no special handling**

The problem says translated one-bits outside the matrix are erased. The voting method never tries to construct the translated image. It counts only pairs where both endpoints are actual in-bounds one-cells in the two original matrices.

If a translated one from `img1` lands outside `img2`, it has no in-bounds `img2` coordinate to pair with and contributes no vote. Thus, clipping at the border is handled implicitly.

**No rotations enter the calculation**

The coordinate difference preserves each image's row and column orientation. It only adds a fixed offset. No coordinate swap, sign-changing rotation, or reflection is attempted, matching the translation-only contract.

**Trace a simple case**

Suppose `img1` has one-cells at `(0,0)` and `(0,1)`, while `img2` has one-cells at `(1,1)` and `(1,2)`.

Pairing corresponding positions produces the same key:

$$
(0-1,0-1)=(-1,-1),
$$

$$
(0-1,1-2)=(-1,-1).
$$

That displacement receives two votes, meaning one translation aligns both cells. Cross-pairings produce other displacement keys with only one vote. The maximum counter value is therefore two.

**Why each overlap is counted once**

For a fixed translation, each overlapping final position comes from one unique original coordinate in `img1` and one unique coordinate in `img2`. That coordinate pair contributes one vote. Different overlapping positions form different coordinate pairs but share the same displacement key.

Non-overlapping one-cells may vote for other translations, but they do not inflate this key. Hence, the counter frequency is neither missing overlap cells nor double-counting them.

**Return zero for an empty counter**

`max(cnt.values())` is valid only if at least one one-cell pair was encountered. The conditional expression returns zero when `cnt` is empty. This covers an all-zero first image, an all-zero second image, or both.

## Complexity detail

Let `a` be the number of one-cells in `img1` and `b` the number in `img2`. The loops inspect every matrix cell to find one-cells and, for each one in the first image, scan the second matrix for its ones. The exact number of successful pair votes is `a b`, while the loop structure performs up to `O(n^2 + a n^2)` cell checks.

In an all-ones case, all four loops run fully, giving `O(n^4)` time. More precisely, coordinate-pair voting is `O(ab)` if the one-cell coordinates are first extracted into lists; the protected source finds the second set inside the nested loops and has the same `O(n^4)` dense worst case.

Possible row differences range from `-(n-1)` through `n-1`, and the same is true for column differences. The counter can therefore contain `O(n^2)` distinct displacement keys.

The manifest's listed `O(n^3)` time and `O(n)` space are not the precise worst-case bounds of this exact Counter implementation. Tighter bounds require a different representation or technique, such as bitset row comparisons for each shift. The code explained here is the coordinate-difference voting algorithm actually present in the optimal source.

## Alternatives and edge cases

- **Shift and compare every matrix cell:** There are `O(n^2)` shifts and `O(n^2)` cells per shift, also giving `O(n^4)` time in a direct implementation.

- **Extract one-cell coordinate lists first:** This makes the work visibly `O(ab)` and avoids repeatedly testing zero-cells, while retaining the same voting proof.

- **Bitset rows:** Encode rows as integers, shift bits, and use bit counts. This can reduce practical and asymptotic factors and more closely support the manifest's tighter target.

- **Convolution:** Cross-correlation computes overlap for every translation together, but FFT-based machinery is much more complex for `n <= 30`.

- **One image all zeroes:** No pair votes exist, so the result is zero.

- **Both images one-by-one ones:** Their only pair gives one vote and answer one.

- **Large translation:** Cells falling outside simply form no in-bounds matching pairs.

- **Several pairs share a displacement:** Their votes accumulate and represent multiple overlapping positions.

- **Different displacement signs:** Either convention works if applied uniformly; this source uses first-coordinate minus second-coordinate.

- **No rotation:** Coordinate differences model translation only.

- **Duplicate coordinates:** A binary matrix has one value per coordinate, so each one-cell appears once and pair votes are unambiguous.

- **Input immutability:** Both matrices are read without changing any cell.
