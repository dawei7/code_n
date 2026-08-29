## General

**Focus on the final block of each prefix**

Every valid partition of the first `i` elements ends with one contiguous block whose length is between one and `k`. If that final block starts at position `j - 1` and ends at `i - 1`, everything before it is an independent optimal partition of the first `j - 1` elements.

This gives a one-dimensional dynamic program. Let `f[i]` be the maximum transformed sum obtainable from prefix `arr[0:i]`. The answer is `f[n]`.

The base value `f[0] = 0` represents an empty prefix. It contributes nothing before a first block that begins at array index zero.

**Enumerate every legal final-block length**

For a fixed prefix end `i`, the inner loop starts with `j = i`. This makes the last block `arr[i - 1:i]`, containing one element.

Each decrement of `j` extends that block one position to the left. The loop stops before `j` would make the length exceed `k` or before it would pass the start of the array.

The expression

`range(i, max(0, i - k), -1)`

therefore visits exactly the one-based starts for block lengths one through `min(k, i)`.

For a chosen `j`:

- The preceding prefix is `arr[0:j - 1]` and has best score `f[j - 1]`.
- The final block is `arr[j - 1:i]`.
- Its length is `i - j + 1`.

**Maintain the block maximum incrementally**

After partitioning, every value in a block becomes the maximum original value from that block. If the current final block has maximum `mx` and length `L`, its transformed contribution is `mx * L`.

As `j` moves left, only one new element `arr[j - 1]` enters the block. The update

`mx = max(mx, arr[j - 1])`

computes the new maximum in constant time. Recomputing `max(arr[j - 1:i])` from scratch for every candidate would add another factor of `k`.

The candidate total is

`f[j - 1] + mx * (i - j + 1)`.

The assignment to `f[i]` takes the maximum over all legal final-block starts.

**Why the table is filled left to right**

Every candidate for `f[i]` depends on `f[j - 1]` where `j - 1 < i`. Since the outer loop processes `i = 1, 2, ..., n`, all preceding-prefix values are already final.

No recursion or future information is needed. Once `f[i]` is computed, it can serve as the optimal preceding prefix for later blocks.

**Trace the main example**

For `arr = [1,15,7,9,2,5,10]` and `k = 3`, one optimal partition is:

- `[1,15,7]`, whose maximum is 15 and transformed contribution is `15 * 3 = 45`.
- `[9]`, contributing nine.
- `[2,5,10]`, whose maximum is 10 and contribution is 30.

The total is `45 + 9 + 30 = 84`.

The DP discovers this through prefixes. At `i = 3`, the inner loop considers a length-three final block and records 45. At `i = 4`, choosing a one-element final block adds nine to `f[3]`, producing 54. At `i = 7`, choosing a length-three final block with maximum ten adds 30 to `f[4]`, producing 84.

Other last-block lengths are evaluated at every stage, so the method does not assume this partition in advance.

**Why multiplying by the maximum is correct**

The transformation replaces every element of a chosen block with that block's maximum. It does not add the maximum once or preserve other values.

A block of length `L` therefore becomes `L` identical values, each equal to `mx`. Its sum is exactly `L \cdot mx`.

The original array is not actually modified because only the final total is requested. Computing the contribution is sufficient.

**Why a greedy partition can fail**

Choosing the block with the largest immediate transformed sum may consume a large value that would benefit more elements in a neighboring block. Choosing the longest block around every large value can also prevent another large value from improving its own group.

The effect of a boundary is coupled to both adjacent blocks. Dynamic programming evaluates each possible last boundary together with the already optimal preceding prefix, retaining all globally relevant choices.


Take an optimal partition of prefix `arr[0:i]`. Its last block begins at some `j - 1` and has a legal length at most `k`. The inner loop considers that exact `j`.

The portion before the block cannot be better than `f[j - 1]` by definition, and the loop computes the final block's exact maximum and transformed contribution. Therefore, the candidate considered by the DP is at least the score of the chosen optimal partition.

Conversely, every DP candidate combines a valid optimal partition of a shorter prefix with one contiguous block of legal length. It is a valid partition of the first `i` elements, so the DP cannot exceed what is achievable.

Both inequalities show that `f[i]` is exact. Induction from `f[0] = 0` proves `f[n]` is the maximum total for the full array.

**Why zero initialization is safe**

The source guarantees all array values are nonnegative. Every block contribution and every valid total is therefore nonnegative, so initializing `f` and `mx` to zero cannot hide a negative-but-required choice.

If negative values were allowed, `f[i]` would need a negative-infinity sentinel and `mx` would need to begin from the first included element. That is outside this contract.

## Complexity detail

Let `N = len(arr)` and let `K = k`. There are `N` prefix states. Each state tries at most `K` final-block lengths, doing constant work per length because `mx` is updated incrementally. Time complexity is `O(NK)`, matching the manifest.

The `f` array contains `N + 1` integers and uses `O(N)` space. All loop variables and `mx` use constant extra storage. Total auxiliary space is `O(N)`, matching the manifest.

Only the most recent `K` prefix values are theoretically needed, so circular storage can reduce the table to `O(K)`, but the exact solution keeps all prefixes for simpler indexing.

## Alternatives and edge cases

- **Top-down memoization:** Define the best score from a starting index and try the next one through `K` block lengths. It has the same `O(NK)` time and `O(N)` memo plus recursion stack.
- **Circular `K`-sized DP:** Because transitions look back at most `K` positions, prefix states can be stored modulo `K + 1`. This reduces auxiliary space but makes indexing easier to get wrong.
- **Enumerate every partition:** There are exponentially many boundary choices. Dynamic programming merges partitions sharing the same prefix endpoint.
- **Greedy around the largest value:** A locally attractive block can steal positions from another beneficial maximum and is not globally reliable.
- **`k = 1`:** Every block has one element, so no value changes and the answer is the original array sum.
- **Single-element array:** The only state considers a one-element block and returns that value.
- **`k >= N`:** The DP considers the whole array as one block as well as all smaller partitions; it chooses whichever has the greatest total.
- **All zeroes:** Every candidate is zero, and the initialized table already represents the correct result.
- **Repeated maximum inside a block:** The contribution depends only on its value, not how many times it originally appeared; after transformation every position becomes that maximum.
- **Final short suffix:** The inner loop naturally tries every length available near the start or end and never requires a full `K` elements.
- **Contiguous requirement:** `arr[j - 1:i]` is one uninterrupted interval. The recurrence cannot skip elements inside a block.
- **Every element used exactly once:** The preceding prefix ends where the final block starts, so candidates have neither gaps nor overlaps.
- **Large element values:** Products and sums can be large, but the source guarantees the final answer fits in 32 bits and Python integers handle the arithmetic directly.
- **Input preservation:** The algorithm reads `arr` and stores only scores; it does not apply the conceptual replacement to the array itself.
