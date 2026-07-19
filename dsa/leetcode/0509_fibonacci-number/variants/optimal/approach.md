## General
**Keep only the two values needed by the recurrence**

At the start of an iteration, let `previous = F(i)` and `current = F(i + 1)`. The simultaneous update `(previous, current) = (current, previous + current)` advances this relationship to the next index without storing the whole sequence.

**Advance exactly n times**

Initialize the pair as $(F(0), F(1)) = (0, 1)$. After `n` updates, the maintained relationship gives `previous = F(n)`, so return `previous`. This also handles $n = 0$: no update occurs and the initial zero is returned.

**Why simultaneous assignment matters**

The new second value must use both old values. Computing the pair together preserves them until their sum is formed; overwriting `previous` first in languages without simultaneous assignment requires a temporary variable.

## Complexity detail
The loop performs one constant-time update for each of `n` indices, giving $O(n)$ time. Two running integers and the loop counter use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Memoized recursion:** evaluates each index once in $O(n)$ time but uses $O(n)$ cache and call-stack space.
- **Bottom-up array:** makes every intermediate value available later but uses $O(n)$ space unnecessarily.
- **Naive recursion:** mirrors the recurrence directly but repeats subproblems and takes exponential time.
- **Fast doubling or matrix exponentiation:** computes the value in $O(\log n)$ arithmetic steps and is useful for much larger indices, but is more machinery than these constraints require.
- **Zero:** returns the first base value without entering the loop.
- **One:** one update moves `previous` to the second base value.
