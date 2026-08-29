## General

**Simulate each shrinking row without allocating it**

The definition repeatedly transforms an array of length `m` into an array of length `m - 1`. New position `i` is

`(old[i] + old[i + 1]) % 10`.

A direct simulation could allocate a new list on every round. The exact solution computes the same rows inside the prefix of `nums`. Once a row of length `k + 1` has been reduced, only positions zero through `k - 1` are needed for the next row. The rest of the original list can remain as stale storage because later loops ignore it.

The outer loop is

`for k in range(len(nums) - 1, 0, -1)`.

Its first value is `n - 1`, the number of entries in the first reduced row. Each later value is one smaller, ending at one. During the iteration for `k`, the current meaningful row occupies `nums[0]` through `nums[k]` and has length `k + 1`. The inner loop writes the next row of length `k` into `nums[0]` through `nums[k - 1]`.

**Why left-to-right overwriting is safe**

For each `i` in `range(k)`, the assignment is

`nums[i] = (nums[i] + nums[i + 1]) % 10`.

At first, modifying a list while still reading it can look dangerous. Direction makes it safe. Before position `i` is written:

- `nums[i]` still contains the old row's value at `i`, because that position has not yet been written during this iteration;
- `nums[i + 1]` also still contains the old row's value, because the loop moves left to right and has not reached that position.

Positions below `i` may already contain new-row values, but the formula never reads them again in the same round. Therefore, every assignment uses exactly the two adjacent entries from the old row that the definition requires.

If the loop ran right to left, it would overwrite `nums[i + 1]` before the calculation for `i` and incorrectly combine an old value with a new-row value. Left-to-right order is an essential part of the implementation.

**One round preserves the defined transformation**

Assume the prefix `nums[0:k+1]` equals some current row of the triangular process. For each `i` from zero to `k - 1`, the inner loop computes the sum of current-row entries `i` and `i + 1` modulo ten and stores it at `nums[i]`. By the safe-overwrite observation, neither operand has been altered before it is read.

After all `k` assignments, prefix `nums[0:k]` exactly equals the next row defined by the problem. Entry `nums[k]` and all positions to its right no longer matter. This is the inductive step that lets the same list serve as storage for every shrinking row.

Before the first round, the meaningful prefix is the entire input, which is the initial row by definition. Applying the step for outer-loop values `n - 1, n - 2, ..., 1` leaves a meaningful prefix of length one. Its sole value is the triangular sum, so returning `nums[0]` is correct.

**Trace the mutation on a small array**

Begin with `nums = [1, 2, 3, 4]`. The first outer value is `k = 3`.

- At `i = 0`, write `(1 + 2) % 10 = 3`, giving a meaningful beginning `[3, 2, 3, 4]`.
- At `i = 1`, both operands are still old-row values `2` and `3`, so write `5`.
- At `i = 2`, use old values `3` and `4` to write `7`.

The meaningful prefix is now `[3, 5, 7]`. On the next round, it becomes `[8, 2]` because `3 + 5 = 8` and `5 + 7 = 12`, whose last digit is two. The last round computes `(8 + 2) % 10 = 0`. The returned value is zero.

The values beyond the current prefix may look inconsistent during this trace, but they are deliberately ignored. In-place algorithms often reuse a larger buffer while tracking which region remains meaningful.

**Modulo can be applied at every step**

The definition itself takes modulo ten after each adjacent sum, and the solution follows it exactly. Modular addition also satisfies

$$
(a + b) \bmod 10
= ((a \bmod 10) + (b \bmod 10)) \bmod 10.
$$

Since every stored entry remains a digit from zero through nine, intermediate values never grow. The maximum pre-modulo sum is eighteen.

**The method intentionally mutates the input**

Because `nums` is the work buffer, the original row is overwritten. When the function returns, `nums[0]` contains the answer, while later entries contain stale values from different stages. This is acceptable for the solution contract, which asks only for the triangular sum, but callers should not expect the input list to retain its original contents.

No copy is created. This mutation is what reduces auxiliary storage from the `O(n)` needed by a fresh-row simulation to `O(1)`.

**Length one is already finished**

If `len(nums) == 1`, the outer range is empty. No assignment occurs, and the method returns the existing `nums[0]`. That matches the stopping rule directly.

## Complexity detail

For an input of length `n`, the inner loop runs `n - 1` times in the first round, then `n - 2`, continuing down to one. The total number of updates is

$$
(n-1) + (n-2) + \cdots + 1
= \frac{n(n-1)}{2},
$$

so time complexity is `O(n^2)`. Every update performs constant-time addition, modulo, indexing, and assignment.

The method reuses `nums` and stores only loop variables. It allocates no second row, so auxiliary space complexity is `O(1)`. This bound excludes the caller-owned input list, even though the method modifies it.

The quadratic simulation is practical for `n <= 1000`. The exact number of updates is below half a million at the maximum length.

## Alternatives and edge cases

- **Allocate a new row each round:** This follows the statement literally and is easy to visualize. It has the same `O(n^2)` time but requires `O(n)` peak extra space and repeated allocations.
- **Binomial-coefficient formula:** The final value is a weighted sum using row `n - 1` of Pascal's triangle modulo ten. Computing coefficients safely modulo the composite number ten requires additional number theory, such as separate moduli two and five plus reconstruction; it is more complex than needed for `n <= 1000`.
- **Naively compute full binomial coefficients:** Python can hold them, but they become very large and add unnecessary big-integer work. Fixed-width languages can overflow.
- **Right-to-left in-place update:** This is incorrect because `nums[i + 1]` would already contain a new-row value when computing `nums[i]`. The exact left-to-right direction preserves both old operands.
- **Single digit:** No reduction occurs, and that digit is returned unchanged.
- **Two digits:** Exactly one update computes their sum modulo ten, and `nums[0]` is returned.
- **All zeros:** Every generated row is all zeros, so the answer is zero.
- **Values summing above nine:** Modulo ten is applied on each assignment; for example, nine plus eight becomes seven.
- **Maximum length:** The nested loops perform `n(n-1)/2` updates, which remains within the intended constraint scale.
- **Input mutation:** The caller's list is destroyed as an original-data record. If preservation were required, a copy would add `O(n)` space before running the same algorithm.
- **Stale suffix entries:** They are harmless because outer value `k` strictly decreases and subsequent loops access only the meaningful prefix through index `k`.
- **Digits-only guarantee:** Every input begins between zero and nine, and modulo keeps every written value in that range. No normalization branch is needed.
