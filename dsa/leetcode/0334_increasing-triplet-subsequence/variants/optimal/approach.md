## General

**Keep the best possible tails, not the subsequence itself.**

The task asks only whether some strictly increasing subsequence of length three exists. It does not ask for the indices or values of that subsequence. This allows the scan to summarize all useful earlier choices with two numbers:

- `mi`: the smallest value seen so far, which is the best possible tail of a length-one increasing subsequence;
- `mid`: the smallest possible second value of any increasing pair seen so far, which is the best possible tail of a length-two increasing subsequence.

A smaller tail is always at least as useful as a larger one. If a future number can extend a pair ending at a larger `mid`, it can also extend a pair ending at a smaller `mid`. Therefore the algorithm does not need to remember every candidate pair.

Both variables begin at positive infinity. Before any input is processed, no real length-one or length-two candidate exists. Any allowed integer can replace `mi`, and no ordinary integer can incorrectly exceed a real pair tail before one has been created.

**Test whether the current value completes a triplet.**

The first condition in the exact source is `if num > mid`. A finite `mid` certifies that two earlier indices form a strictly increasing pair ending at value `mid`. Because the scan moves left to right, the current `num` occurs at a later index. If it is strictly greater than `mid`, those two earlier elements followed by `num` form the required triplet, so the method can immediately return `True`.

Checking this condition first is safe. When `mid` is still infinity, no finite input can be larger, so the method cannot report a triplet before an increasing pair exists.

Strict `>` is essential. If `num == mid`, appending it would create equal second and third values, not a strictly increasing subsequence.

**Update the best length-one tail.**

If the current number does not complete a triplet, the source next checks `num <= mi`. In that case, it assigns `mi = num`.

This keeps `mi` equal to the smallest value encountered in the processed prefix. Replacing it with an equal value is harmless, and the `<=` condition ensures that equal values are not mistakenly used as a strictly increasing pair. For example, scanning `[2,2]` repeatedly updates `mi` but never creates a finite `mid`, which is correct.

A newly smaller `mi` makes future pair formation easier. Any later number above it can become a candidate second value.

**Otherwise, improve the best pair tail.**

If execution reaches the final `else`, two facts are known:

- `num > mi`, because `num <= mi` was false;
- `num <= mid`, because `num > mid` was false.

Thus `mi` followed by `num` is a strict increasing pair in index order, and `num` is no larger than the previous pair tail. Assigning `mid = num` records a valid pair and keeps the smallest available second value.

The source does not write an explicit `num <= mid` condition because the earlier triplet check already establishes it. The order of the branches is part of the logic.

**Why a later update of `mi` does not invalidate `mid`.**

This is the most subtle point. Suppose the scan sees `[1,2,0,3]`:

- `1` sets `mi = 1`;
- `2` forms a pair and sets `mid = 2`;
- `0` lowers `mi` to `0`;
- `3 > mid`, so the method returns `True`.

At the final step, the currently stored values `mi = 0` and `mid = 2` are not in index order: the `0` appeared after the `2`. But `mid = 2` still carries an existence certificate from the moment it was assigned. At that earlier moment, there was some value—namely `1`—before it and strictly smaller than it. Updating `mi` later does not erase that earlier pair.

The algorithm is not claiming that the current variables themselves always spell out the answer. Its invariant is existential: whenever `mid` is finite, there exists an earlier increasing pair whose second value is `mid`. That is sufficient because a later `num > mid` extends that witnessed pair.

**Walk through `[2,1,5,0,4,6]`.**

- `2` lowers `mi` from infinity to `2`.
- `1` lowers `mi` again to `1`.
- `5` is above `mi` but not above infinite `mid`, so it creates the pair tail `mid = 5`.
- `0` lowers `mi` to `0`. The earlier pair ending at `5` still exists.
- `4` is above `mi` and no greater than `mid`, so it improves the pair tail to `4`. This assignment has the direct witness `0 < 4`.
- `6` is greater than `mid = 4`, so `0,4,6` is a strictly increasing triplet in index order.

The method returns as soon as existence is proven; later values cannot change a true answer.

**Why returning false is also correct.**

After each processed prefix, `mi` is its smallest single-element tail, and `mid` is the smallest tail among all increasing pairs in that prefix. The update rules preserve these statements: a new minimum improves `mi`; a value above `mi` creates or improves `mid`; a value above `mid` would have returned true.

Suppose a triplet with third value `num` existed but the method failed to recognize it. Its first two values form an earlier increasing pair. Since `mid` is the smallest tail of any such pair, `mid` is no greater than that triplet's second value. The third value is strictly greater than the second, hence also greater than `mid`, so the first branch would return `True`—a contradiction.

Therefore, if the loop ends without that branch firing, no increasing triplet exists.

## Complexity detail

Let $n$ be `len(nums)`. The method scans every element once and performs a constant number of comparisons or assignments per element. Its time complexity is $O(n)$.

Only `mi`, `mid`, the loop variable, and normal control state are used. No array, stack, set, or recursion is required, so auxiliary space is $O(1)$. This meets both follow-up targets.

## Alternatives and edge cases

- **Enumerate triples:** Testing all index triples directly takes $O(n^3)$ time and is impossible for up to $5\cdot10^5$ elements.

- **For every middle index, search both sides:** Precomputed prefix minima and suffix maxima can detect a triplet in $O(n)$ time, but require $O(n)$ extra arrays. The two-tail scan compresses the same useful information into constants.

- **Longest-increasing-subsequence tails array:** Standard binary-search LIS tracking can detect whether length reaches three in $O(n\log 3)=O(n)$ time and $O(1)$ bounded storage. The explicit two variables are simpler for the fixed target length.

- **Use `<` instead of `<=` when updating `mi`:** Equal values must not form a strict pair. The source's `<=` sends duplicates into the minimum update rather than the pair update.

- **Length below three:** The loop cannot establish a finite pair and then see a later larger value with fewer than three elements, so it naturally returns `False`.

- **Strictly decreasing input:** Every new value lowers `mi`; `mid` remains infinity, and the result is false.

- **Strictly increasing input:** The first value sets `mi`, the second sets `mid`, and the third immediately returns true.

- **Repeated values:** Duplicates can replace equal tails but never satisfy the strict comparisons needed to increase subsequence length.

- **Extreme integer values:** Infinity sentinels are outside all finite inputs, and Python compares them safely with the full signed 32-bit range.

- **Existence versus reconstruction:** The variables may not identify the actual triplet after `mi` changes. That is acceptable only because the contract asks for a Boolean. Returning indices would require storing witness positions or predecessor information.
