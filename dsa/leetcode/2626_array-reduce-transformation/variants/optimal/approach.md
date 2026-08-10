## General

**Carry one accumulated value from left to right**

A reduction converts an array into one final value. The value after processing one element becomes the input state for processing the next element.

The exact recurrence is:

$$
\begin{aligned}
A_0&=\texttt{init},\\
A_{i+1}&=\texttt{fn}(A_i,\texttt{nums[i]}).
\end{aligned}
$$

After all $n$ elements, the required answer is $A_n$.

The implementation mirrors this definition directly. Variable `result` stores the current accumulator and starts as `init`. For every source `value` in order, the assignment

`result = fn(result, value)`

replaces the accumulator with the next recurrence value.

**Why the initial value is not an array element**

`init` is supplied separately and is the accumulator before any element is processed. It is not automatically added, multiplied, or otherwise combined except through the callback.

For a sum callback with zero initialization, it acts like an additive identity. For a sum-of-squares callback with initialization 100, the first call is `fn(100, nums[0])`, so 100 remains part of the computation.

The reduction helper must not guess what `init` means. Only `fn` defines how accumulator and current element combine.

**Evaluation order is part of the contract**

The array is processed from index zero upward. In general:

$$
\texttt{fn}(\texttt{fn}(\texttt{init},a),b)
$$

need not equal:

$$
\texttt{fn}(\texttt{fn}(\texttt{init},b),a).
$$

A reducer can subtract, concatenate digits, build a string, or make any order-sensitive calculation. Therefore, reversing the array, grouping calls, or processing elements concurrently could change the result.

`for (const value of nums)` follows array iteration order and gives exactly the sequential left fold required by the statement.

**The invariant behind the loop**

Before processing element at index $i$, maintain:

> `result` equals the reduction of the prefix `nums[0]` through `nums[i - 1]`, starting from `init`.

Before the first iteration, the processed prefix is empty, and `result = init`, so the invariant holds.

During iteration $i$, the code evaluates `fn(result, nums[i])`. By the invariant, the first argument is exactly the required result from the preceding element. Assigning the callback's return value establishes the same statement for the prefix ending at $i$.

After the loop, the processed prefix is the whole array, so returning `result` yields the required final reduction.

This proof does not assume anything about addition, associativity, or commutativity. It works for every callback satisfying the interface.

**Trace the sum example**

For `nums = [1,2,3,4]`, sum callback, and `init = 0`:

- start: `result = 0`;
- after one: `result = fn(0,1) = 1`;
- after two: `result = fn(1,2) = 3`;
- after three: `result = fn(3,3) = 6`;
- after four: `result = fn(6,4) = 10`.

The returned result is ten.

For the sum-of-squares callback and `init = 100`, the values added are one, four, nine, and sixteen. The accumulator progresses through 101, 105, 114, and 130.

**Why the empty array returns `init`**

If `nums` is empty, the loop has zero iterations. No callback is invoked, and `result` retains its initialization.

Returning `init` is not a special accidental behavior; it is the mathematically correct reduction of an empty sequence when an explicit initial accumulator is supplied.

This also means callbacks with side effects are not called for empty input.

**No intermediate history is needed**

Once $A_{i+1}$ has been computed, earlier accumulator values are irrelevant to all later steps. The current state completely summarizes the processed prefix.

The solution therefore stores one accumulator rather than an array of prefix results. This is both simpler and asymptotically space-optimal for the requested final value.

**Callback return values drive the type and value**

The documentation annotates numbers, and the challenge callbacks return numeric results. The control flow itself does not perform arithmetic; it simply passes values through `fn`.

The code must assign the return value back to `result`. Calling `fn(result, value)` without assignment would discard the transition and repeatedly use `init`.

Likewise, the source elements are read only. Reduction changes the local accumulator, not `nums`.

**Why the built-in method is unnecessary**

`Array.prototype.reduce` implements this same fold, but the problem forbids it to test whether the iteration semantics are understood.

The explicit loop makes initialization, order, and state replacement visible. It also avoids subtleties of the built-in overload where an initial value can be omitted; this contract always supplies `init`.

**Handling callback cost**

The algorithm invokes `fn` exactly once per element. If callback evaluation is considered constant time, the reduction is linear. If callbacks take varying time $C_i$, the precise total is the sum of those callback costs plus loop overhead.

No implementation can generally avoid these $n$ calls because an arbitrary callback may make every element affect the final result.

## Complexity detail

Let $n=\texttt{nums.length}$. The loop visits every element once and performs one callback invocation per element. Assuming each callback call is $O(1)$, total time is $O(n)$.

The implementation stores only `result` and the current iteration value, so auxiliary space is $O(1)$. The call stack used internally by `fn`, if any, belongs to the supplied callback rather than the reduction loop.

The returned scalar does not require output storage proportional to $n$.

## Alternatives and edge cases

- **Built-in `Array.reduce`:** It expresses the operation directly but is explicitly forbidden.
- **Indexed `for` loop:** Equivalent and makes the index available, though this callback contract needs only accumulator and value.
- **Recursion:** Can express the recurrence but adds $O(n)$ call-stack space and risks stack overflow.
- **Empty array:** The loop makes no callback calls and returns `init`.
- **Nonzero initial value:** It is the first callback's accumulator, not an extra array element.
- **Non-associative reducer:** Left-to-right order must be preserved.
- **Callback returning zero:** Zero must replace the accumulator normally; truthiness is irrelevant.
- **Single element:** The answer is exactly `fn(init, nums[0])`.
- **Input preservation:** The source array is never modified.
- **Side-effecting callback:** It is invoked exactly once per element in source order.
