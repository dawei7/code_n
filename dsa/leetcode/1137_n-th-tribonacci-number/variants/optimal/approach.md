## General

**Reduce the recurrence to the only state the next term needs**

The sequence begins with `T_0 = 0`, `T_1 = 1`, and `T_2 = 1`. Every later value is the sum of the preceding three values. A direct recursive translation would ask for the same smaller terms many times. A full dynamic-programming table avoids that repetition, but it stores values that will never be needed again. Once the algorithm is ready to compute the next term, only the latest three consecutive Tribonacci values can affect it.

The optimal solution captures those three values in `a`, `b`, and `c`. Initially,

`a = T_0`, `b = T_1`, and `c = T_2`.

One update advances this three-value window by one position:

`a, b, c = b, c, a + b + c`.

The new first value is the old second value, the new second value is the old third value, and the new third value is the next Tribonacci term. No earlier term can influence any future computation except through these three accumulated values, so discarding it loses no information.

**Understand Python's simultaneous assignment**

The right-hand side of the assignment is evaluated completely before any variable on the left is replaced. Therefore, `a + b + c` uses all three old values. This detail matters. If the variables were updated through three ordinary assignments in the wrong order, the sum could accidentally mix old and new values and would no longer implement the recurrence. Tuple assignment makes the intended state transition both short and safe.

**Why the loop runs exactly `n` times and returns `a`**

Many bottom-up implementations handle `n < 3` separately, perform `n - 2` updates, and return the third variable. This exact solution uses an equally correct but slightly more uniform alignment: it performs `n` updates and returns the first variable.

The loop invariant explains the alignment precisely. After `t` completed iterations,

`a = T_t`, `b = T_{t+1}`, and `c = T_{t+2}`.

Before any iteration, `t = 0` and the initialization gives exactly `T_0`, `T_1`, and `T_2`, so the invariant is true. Assume it is true after `t` updates. The next simultaneous assignment produces

`a = T_{t+1}`,

`b = T_{t+2}`, and

`c = T_t + T_{t+1} + T_{t+2} = T_{t+3}`.

Those are exactly the three consecutive values required after `t + 1` updates, so the invariant remains true. After the loop has run `n` times, the invariant gives `a = T_n`. Returning `a` is therefore correct for every legal input.

This alignment also handles every base case without a branch. If `n = 0`, `range(0)` is empty, `a` remains zero, and the method returns `T_0`. If `n = 1`, one shift makes `a` equal to the original `b`, which is `T_1 = 1`. If `n = 2`, two shifts make `a` equal to `T_2 = 1`. For `n = 3`, the third shift returns `2`, the sum of the three base values.

**A small trace**

Starting from the state `(0, 1, 1)`:

- after one update, the state is `(1, 1, 2)`;
- after two updates, the state is `(1, 2, 4)`;
- after three updates, the state is `(2, 4, 7)`;
- after four updates, the state is `(4, 7, 13)`.

For input `n = 4`, the method returns the first value of the final state, namely `4`. Notice that `b` and `c` have deliberately advanced beyond the requested term. They are maintained because they are necessary to shift the window uniformly; only `a` is aligned with the requested index after `n` iterations.

**Why this is dynamic programming even without an array**

Dynamic programming builds larger subproblem answers from already solved smaller subproblems. Here, each new value is built from the preceding three answers. The algorithm is often called space-optimized bottom-up dynamic programming or a rolling-state recurrence. Removing the array changes only how much history is retained; it does not change the dependency order or the fact that every required subproblem is computed once.

The input is restricted to `0` through `37`, so every legal execution is small and the result fits in a 32-bit signed integer according to the contract. Python integers also grow automatically, so the addition itself cannot overflow. The bounded input domain does not alter the algorithmic explanation: relative to the numeric input `n`, the method performs one constant-time transition per index.

## Complexity detail

The loop executes exactly `n` iterations. Each iteration performs a constant number of integer additions, variable reads, and assignments, so the time complexity is `O(n)`.

Only `a`, `b`, `c`, the loop counter, and the input are retained. The method does not allocate an array, map, or recursion stack whose size grows with `n`. Its auxiliary space complexity is `O(1)`.

Strictly speaking, the stated constraints cap `n` at `37`, making the legal domain finite. Under a purely fixed-domain machine-analysis viewpoint, even the maximum work is bounded by a constant. The conventional complexity statement still uses `O(n)` because it describes how the chosen algorithm scales with the sequence index and distinguishes it from repeated recursion. The repository's required bound is therefore accurately reported as `O(n)` time and `O(1)` auxiliary space.

The output integer is not counted as auxiliary storage. In languages with fixed-width integers, the contract's guarantee ensures the answer fits in 32 bits; in Python, integer storage at these bounded values is also constant for this domain.

## Alternatives and edge cases

- **Naive recursion:** Directly evaluating the three recursive branches matches the mathematical definition, but it recomputes the same terms many times and grows exponentially. It is unnecessary even for a small legal domain and obscures the simple forward dependency.
- **Top-down memoization:** Caching each recursive result reduces the time to `O(n)`, but the cache and recursion stack require `O(n)` space. It is useful for teaching overlapping subproblems, not optimal for this recurrence.
- **Bottom-up array:** Storing every value from `T_0` through `T_n` also takes `O(n)` time and makes previous terms easy to inspect or reuse. For a single requested value, however, the array's `O(n)` space is avoidable because only three consecutive terms are needed.
- **Matrix exponentiation:** A fixed transition matrix can compute `T_n` in `O(log n)` arithmetic steps. That asymptotic improvement matters for enormous indices, but it introduces matrix machinery for a contract capped at `37` and is not the chosen canonical solution.
- **Precomputed constant table:** Because the legal domain has only 38 possible inputs, a hard-coded table could answer in `O(1)` lookup time. It uses domain-specific stored data and teaches less about the recurrence; the rolling solution remains direct, tiny, and fully sufficient.
- **Input `n = 0`:** The loop performs no update, and returning the initialized `a` correctly yields zero.
- **Inputs `n = 1` and `n = 2`:** The uniform shift-and-return alignment produces the two remaining base cases without special conditional logic.
- **Largest legal input:** Exactly 37 updates are performed. The answer is within the guaranteed integer range, and constant auxiliary state is maintained throughout.
- **Sequential assignment trap:** Replacing tuple assignment with statements that overwrite `a` or `b` before calculating the sum can corrupt the recurrence. A temporary variable or simultaneous assignment is necessary if the update is written imperatively.
