## General

**What must be prevented**

A beautiful array is a permutation of the integers from `1` through `n` in which no three positions `i < k < j` satisfy `2 * nums[k] = nums[i] + nums[j]`. In other words, the value at a position strictly between two other positions must never be the arithmetic mean of the two endpoint values.

Trying to place the numbers one at a time and testing every earlier pair creates a difficult global search. A choice that appears harmless now can form a forbidden triple after more values are appended. The optimal construction avoids backtracking by exploiting two facts:

- the beautiful property survives a suitable linear transformation of every value;
- an odd number plus an even number can never equal twice an integer.

Those facts let the solution construct the answer recursively from two smaller beautiful arrays.

**Why transforming a beautiful array preserves beauty**

Suppose an array `a` is already beautiful. Transform each value with `b[x] = p * a[x] + q` for some positive integer `p` and constant `q`. Imagine that three transformed entries at positions `i < k < j` violated the rule:

`2 * b[k] = b[i] + b[j]`.

Substituting the transformation gives `2 * (p * a[k] + q) = (p * a[i] + q) + (p * a[j] + q)`. The two copies of `q` cancel, and dividing by positive `p` leaves `2 * a[k] = a[i] + a[j]`. That would already be a forbidden triple in `a`, contradicting that `a` was beautiful.

The code uses exactly two such transformations:

- `2 * x - 1` turns the integers `1, 2, ..., ceil(n / 2)` into every odd integer from `1` through `n`;
- `2 * x` turns the integers `1, 2, ..., floor(n / 2)` into every even integer from `1` through `n`.

Therefore, if the recursive arrays are beautiful before the transformation, the odd group and the even group remain beautiful internally afterward.

**Why odd values and even values are separated**

The result places all transformed odd values first and all transformed even values second. Consider any possible forbidden triple in the concatenated result.

If both endpoints lie in the odd group, then the middle position also lies inside that earlier group because its index is between them. The transformed odd array is already beautiful, so this case is impossible. The same reasoning applies when both endpoints lie in the even group.

The remaining possibility has the left endpoint in the odd group and the right endpoint in the even group. Their values have different parity, so their sum is odd. However, `2 * nums[k]` is always even for every integer `nums[k]`. An even number cannot equal an odd number, so a triple crossing the boundary is also impossible. This parity argument works regardless of whether the middle position belongs to the odd group or the even group.

Separating by parity is therefore more than an ordering preference: it makes every cross-group endpoint pair automatically safe.

**How the recursive sizes cover exactly the required values**

There are `ceil(n / 2)` odd numbers in `1` through `n` and `floor(n / 2)` even numbers. In integer arithmetic, the code obtains those counts as:

- `(n + 1) >> 1` for the odd count;
- `n >> 1` for the even count.

Right-shifting a nonnegative integer by one bit performs integer division by two. Adding one before the shift produces the ceiling for the odd side.

The recursive call for the left side returns a permutation from `1` through the odd count. Mapping `x` to `2 * x - 1` produces `1, 3, 5, ...` up to the largest odd value not exceeding `n`. The recursive right side maps `x` to `2 * x` and produces `2, 4, 6, ...` up to the largest even value not exceeding `n`. The groups have no overlap, and together they contain every integer from `1` through `n` exactly once. Their concatenation is consequently a permutation, not merely a sequence that happens to satisfy the arithmetic condition.

**Base case and termination**

When `n = 1`, `[1]` is the only possible permutation and cannot contain a triple, so it is beautiful. For every larger `n`, both recursive sizes are smaller than `n` and at least one. The calls must eventually reach `n = 1`.

For example, with `n = 5`, the solution recursively constructs a beautiful array of size `3` for the odd positions and one of size `2` for the even positions. If those recursive results are `[1, 3, 2]` and `[1, 2]`, their mappings become `[1, 5, 3]` and `[2, 4]`. The returned array is `[1, 5, 3, 2, 4]`. It contains every value from `1` through `5`, its same-parity portions inherit beauty, and no cross-parity endpoints can satisfy the forbidden equality.

**Why the construction is correct**

The proof follows the recursion. The size-one result is beautiful and is the correct permutation. Assume the recursive results for the smaller odd and even counts are beautiful permutations. Their affine mappings preserve beauty within each group. The odd mapping covers all required odd values once, and the even mapping covers all required even values once, so concatenation covers `1` through `n` once. Any candidate forbidden triple either remains within one group, where beauty excludes it, or has endpoints in different groups, where parity excludes it. The returned array is therefore a beautiful permutation for `n`.

## Complexity detail

At a call of size `n`, the two recursive subproblems have total size `n`. After they return, the two list comprehensions transform `n` values in total, and concatenating the lists copies `n` references into a new result. Thus the recurrence is `T(n) = T(ceil(n / 2)) + T(floor(n / 2)) + O(n)`. There are `O(log n)` levels, and each level processes `O(n)` total values, giving `O(n log n)` time for this exact implementation.

The returned array itself requires `O(n)` space. Peak live auxiliary storage is also `O(n)`: recursive results and newly transformed lists coexist temporarily, but their sizes form bounded geometric portions of the root problem, while the recursion stack has depth `O(log n)`. The implementation does perform `O(n log n)` total list-element allocations over its entire run because each level rebuilds arrays, but most lower-level temporary lists become unreachable before the algorithm finishes. Complexity discussions should distinguish total allocation work from peak simultaneously live memory.

## Alternatives and edge cases

- **Memoizing results by size:** Repeated subproblem sizes can occur, so caching may avoid reconstructing identical beautiful arrays. It uses additional retained memory and is unnecessary for the given direct construction, but it can reduce repeated recursive work if the same helper is reused across calls.
- **Iterative doubling construction:** Start with `[1]` and repeatedly form valid odd and even transformations, filtering out values greater than `n`. This uses the same mathematical idea without recursion and can reach `O(n)` generated output work with careful implementation.
- **Backtracking over permutations:** It can test the definition directly, but the search space grows factorially and ignores the parity structure that makes a deterministic construction possible.
- **Random shuffling:** A random permutation might be beautiful, but repeated guessing provides no useful worst-case guarantee and still requires expensive validation.
- **Keeping natural sorted order:** `[1, 2, ..., n]` fails once `n >= 3` because consecutive values form arithmetic progressions; for example, the middle of `1, 2, 3` is exactly their average.
- **The cases `n = 1` and `n = 2`:** No three indices exist, so every permutation is automatically beautiful. The recursion returns valid arrays without special handling for `n = 2`.
- **Odd `n`:** The odd group contains one more value than the even group. Using `(n + 1) >> 1` is what preserves the largest odd value instead of accidentally omitting it.
- **Ordering the two groups:** Placing evens before odds would also support the same parity proof if both transformed groups remained internally beautiful. The code consistently returns odds first.
- **Do not confuse positions with values:** The restriction requires `i < k < j` for positions, then compares the values stored there. The construction controls position ranges by concatenating groups and controls value equality through affine preservation and parity.
