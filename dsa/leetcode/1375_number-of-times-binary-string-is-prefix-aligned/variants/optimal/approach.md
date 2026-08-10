## General

**Avoid constructing the binary string**

After step $i$, exactly $i$ distinct positions have been flipped to one because `flips` is a permutation and no position repeats. Prefix alignment at that moment means those one-bits are exactly positions one through $i$. All positions after $i$ must still be zero.

The exact solution does not store the bits. It tracks only `mx`, the largest position flipped so far. This single value is enough to decide whether any flipped one lies outside the required prefix.

`enumerate(flips, 1)` produces the step number `i` beginning at one and the position `x` flipped at that step. The one-based enumeration is important because both bit positions and problem steps are one-indexed. After `mx = max(mx, x)`, `mx` is the maximum among the first $i$ flip positions.

**Why `mx == i` exactly characterizes alignment**

If `mx > i`, some position beyond the prefix `[1, i]` has already been flipped to one. The string cannot be prefix-aligned, regardless of which earlier positions are on.

Now suppose `mx == i`. The first $i$ flips are $i$ distinct positive integers, and all are at most $i$. There are only $i$ possible positions in that range: one through $i$. Therefore the flipped set must contain every one of them exactly once. Positions beyond $i$ have not been flipped because their indices would make the maximum larger. The string is consequently one on the entire prefix and zero afterward.

The reverse direction is immediate: if the string is prefix-aligned after step $i$, position $i$ is one and no larger position is one, so the maximum flipped position is exactly $i$.

This proof relies on the permutation guarantee. If repeated flips were allowed, knowing only the maximum and step count would not prove that all earlier positions had been covered.

**How the counter is updated**

`ans += mx == i` uses Python's Boolean-as-integer behavior. The comparison produces `True` for an aligned step and `False` otherwise. In arithmetic, these act as one and zero, so the statement increments `ans` exactly when alignment holds.

Writing an explicit `if mx == i: ans += 1` would behave identically. The compact form does not change the invariant: after processing $i$ flips, `ans` equals the number of aligned moments among steps one through $i$.

For `[3, 2, 4, 1, 5]`, the running maxima are 3, 3, 4, 4, and 5. Comparing with step numbers 1, 2, 3, 4, and 5 succeeds only at steps four and five. At step four, the four distinct values seen are 3, 2, 4, and 1, necessarily the complete prefix. At step five, the entire string is on.

**Why no sum or set is needed**

Another common solution tracks the sum of flipped positions and compares it with $1+2+\cdots+i$. The maximum invariant is simpler. Once $i$ distinct positions all lie within `[1, i]`, completeness follows automatically. A set is also unnecessary because uniqueness is guaranteed by the input.

**Why the algorithm is correct**

Maintain the invariant that after iteration $i$, `mx` is the greatest of the first $i$ flips and `ans` counts all earlier aligned steps. Updating with `max` preserves the first part. By the permutation argument, `mx == i` is true exactly when the currently flipped positions equal `[1, i]`, which is exactly the prefix-aligned condition. Adding that Boolean therefore preserves the second part. After all $n$ iterations, `ans` counts every and only prefix-aligned moment, so returning it is correct.

The final step always counts. Once all $n$ permutation values have appeared, every position one through $n$ is one, the maximum is $n$, and the entire binary string is a complete prefix.

## Complexity detail

Let $n$ be `len(flips)`. The method makes one pass and performs constant work per position: one maximum, one comparison, and one addition. Time is $O(n)$.

Only `ans`, `mx`, the loop index, and current value are stored, so auxiliary space is $O(1)$. The input is read without modification, and no representation of the binary string or set of flipped positions is allocated. These bounds match the manifest.

## Alternatives and edge cases

- **Running sum:** Compare the sum of seen flip positions with $i(i+1)/2$. Under distinctness, equality also proves the seen set is `[1, i]`, but the maximum method uses simpler arithmetic.
- **Explicit bit array:** Apply every flip and scan the prefix. It mirrors the story but can cost $O(n^2)$ if rescanned after each step and uses $O(n)$ space.
- **Set of flipped positions:** Check whether all positions one through $i$ are present. It works but stores information the permutation and maximum invariant make unnecessary.
- **First flip is one:** Then `mx == i == 1`, so the first moment is aligned.
- **First flip is larger than one:** The maximum exceeds the step number, so alignment correctly fails.
- **Final step:** It is always aligned because every permutation position has been flipped.
- **Large early position:** Once `mx` jumps ahead, alignment cannot return until the step count catches up to that maximum and all intervening positions have appeared.
- **Permutation requirement:** Distinctness is essential to the pigeonhole argument. Duplicate or toggle operations would require additional state.
- **One-element input:** `[1]` produces one aligned moment.
- **One-based indexing:** Starting `enumerate` at one avoids off-by-one errors between Python iteration and problem positions.
- **Boolean addition:** `True` contributes one and `False` zero in Python; an explicit conditional is a readability-equivalent alternative.
- **Input mutation:** The method never changes `flips`.
