## General

**Use the extreme remaining value to satisfy each sign immediately**

The result must be a permutation of every integer from `0` through `n`. At each position, the current character says only whether the next permutation value must be larger or smaller. It does not prescribe an exact difference.

The solution maintains the interval of values not yet used:

- `low` is the smallest unused value;
- `high` is the largest unused value.

Initially every required value is available, so `low = 0` and `high = n`.

When the current sign is `I`, the algorithm places `low`. Every value that remains afterward is larger, so whichever value is chosen next will satisfy the required increase.

When the current sign is `D`, it places `high`. Every remaining value is smaller, so the next choice will satisfy the required decrease.

This extreme-choice rule turns a condition involving the unknown next value into a guarantee against all possible next values.

**Processing an `I`**

For character `I`, the code appends the current `low` and increments `low`.

Before the update, unused values form the inclusive interval `[low, high]`. After using the smallest one, the future unused interval is `[low + 1, high]`. Every member of that interval exceeds the appended value.

Therefore, the next appended value is guaranteed to be larger, regardless of whether the next character asks the algorithm to choose its new low endpoint or high endpoint.

**Processing a `D`**

For character `D`, the code appends `high` and decrements `high`.

After the largest value is removed, every future unused value is at most the old `high - 1` and is therefore smaller than the appended value. The descent is guaranteed before the algorithm even knows which remaining value will be selected next.

**Why no lookahead is needed**

A tempting approach is to choose values based on runs such as `III` or `DDD`. The interval invariant makes that unnecessary.

After processing any prefix of the sign string:

- all values already appended are distinct;
- every unused value is exactly one integer in the current interval `[low, high]`;
- the comparison requested by the most recently processed sign will be satisfied by any next choice from that interval.

For an `I`, the appended old low endpoint lies below the entire new interval. For a `D`, the appended old high endpoint lies above it. This invariant makes future signs irrelevant to the correctness of the comparison just created.

**Why the last value is `low`**

The string has length `n`, so the loop processes `n` signs and appends `n` values. A valid permutation needs `n + 1` values, leaving exactly one unused number.

Each iteration removes one endpoint from the interval. After `n` removals from the original `n + 1` values, `low == high`. Appending `low` adds that unique remaining number. Appending `high` would be identical at this point.

The final value also satisfies the last sign because the previous iteration selected an extreme that guaranteed its relationship with every remaining value, including this last one.

**A trace for `IDID`**

Start with unused interval `[0, 4]`.

- The first sign is `I`, so append zero and move `low` to one. Every remaining value is greater than zero.
- The next sign is `D`, so append four and move `high` to three. Every remaining value is less than four.
- The next `I` appends one and moves `low` to two.
- The final `D` appends three and moves `high` to two.
- Only two remains, so append it.

The result is `[0, 4, 1, 3, 2]`. Its comparisons are increase, decrease, increase, decrease, exactly matching the string.

**Why the output is a permutation**

The algorithm never reuses a value. It appends an endpoint and then moves that endpoint inward, permanently removing the chosen number from the unused interval.

It appends exactly `n + 1` numbers drawn from a range containing exactly `n + 1` numbers. Since all appended values are distinct and remain within `0` through `n`, they form a permutation of the entire range.

**Why every requested comparison is correct**

Consider the value appended for sign position `i`. If the sign is `I`, that value was the smallest unused number, and the next value is selected later from the strictly larger remaining interval. If the sign is `D`, it was the largest unused number, and the next value comes from the strictly smaller remaining interval. This holds for every sign, so the finished permutation matches the complete pattern.

## Complexity detail

Let `n` be the length of `s`.

The loop examines each character once and performs constant work per character. Appending the final remaining number is constant time, so total time is `O(n)`.

The returned list contains `n + 1` integers and therefore uses `O(n)` output space. Aside from that required output, the algorithm stores only `low`, `high`, the loop character, and a few references, so auxiliary working space is `O(1)`. The manifest counts the returned list and states `O(n)` space.

## Alternatives and edge cases

- **Construct from runs of `D`:** Start with increasing values and reverse segments corresponding to consecutive decreases. This also yields `O(n)` time, but the low/high invariant is more direct.
- **Backtracking over permutations:** It may find an answer but explores an enormous search space even though an extreme choice always guarantees progress.
- **Sort values after assigning inequalities:** Postponing exact values creates an unnecessary constraint-solving problem. The endpoint method assigns a valid unused value immediately.
- **All `I` characters:** The algorithm repeatedly takes the low endpoint and returns `[0, 1, ..., n]`.
- **All `D` characters:** It repeatedly takes the high endpoint and returns `[n, n - 1, ..., 0]`.
- **Alternating signs:** Low and high endpoints alternate, producing a zigzag such as `[0, n, 1, n - 1, ...]` while preserving uniqueness.
- **String length one:** One endpoint is selected for the single sign and the other is appended, giving either `[0, 1]` or `[1, 0]`.
- **Multiple valid permutations:** The problem permits any valid answer. This method deterministically returns one particular extreme-based permutation.
- **Strict comparisons:** Values never repeat, and the next unused interval lies strictly above an old low or strictly below an old high, so equality cannot occur.
- **Final endpoint equality:** After processing all signs, `low` and `high` must coincide. If they did not, the endpoint-removal invariant or loop count would have been violated.
- **Output-space convention:** Some analyses call the working space `O(1)` by excluding the answer list. Including the returned permutation gives `O(n)` total additional storage, which matches this package's manifest.
