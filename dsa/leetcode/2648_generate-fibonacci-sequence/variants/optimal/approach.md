## General

**A generator produces values only when requested**

Calling `fibGenerator()` returns a generator object. The function body does not run to completion and does not create a finite Fibonacci array.

Each call to `gen.next()` resumes execution until the next `yield`, returns that yielded value, and suspends the generator again with its local state preserved.

This lazy behavior is ideal for an infinite sequence: callers can request any finite prefix without computing unused future values.

**Store only the two values needed by the recurrence**

The Fibonacci recurrence is:

$$
F_0=0,\qquad F_1=1,\qquad F_{r+2}=F_r+F_{r+1}.
$$

Variables `previous` and `current` hold two consecutive values. Initially:

$$
\texttt{previous}=F_0=0,\qquad
\texttt{current}=F_1=1.
$$

To produce the next sequence value, the generator yields `previous`. To advance the state, it replaces the pair with:

$$
(\texttt{current},\texttt{previous}+\texttt{current}).
$$

No earlier Fibonacci number is needed once the newest pair is known.

**Understand suspension around `yield`**

The loop body is:

1. `yield previous`;
2. update both variables.

On the first `next()` call, execution initializes the variables, enters the loop, and suspends at `yield previous` with value zero. The update has not happened yet.

On the second `next()` call, execution resumes immediately after that yield, updates the pair to $(1,1)$, loops, and yields one.

This resume-then-advance behavior continues for every call.

**Why simultaneous assignment matters**

The update is:

`[previous, current] = [current, previous + current]`.

JavaScript evaluates the right-hand values from the old state before assigning the left-hand variables. Therefore, the new `current` uses the old `previous + current`.

A careless sequential update:

`previous = current`

followed by:

`current = previous + current`

would use the already-updated `previous` and compute the wrong next value unless a temporary variable were introduced.

Destructuring provides a concise simultaneous transition.

**An invariant proves every yield**

Before the loop's yield on iteration $r$, maintain:

$$
\texttt{previous}=F_r,
\qquad
\texttt{current}=F_{r+1}.
$$

Initialization proves the invariant for $r=0$. The yield returns $F_r$, exactly the next required sequence member.

The pair update produces:

$$
(F_{r+1},F_r+F_{r+1})
=
(F_{r+1},F_{r+2}),
$$

which establishes the invariant for the next iteration. Induction proves the generator yields the Fibonacci sequence forever.

**Trace the first calls**

The stored pairs and returned values are:

- state $(0,1)$, yield zero;
- state $(1,1)$, yield one;
- state $(1,2)$, yield one;
- state $(2,3)$, yield two;
- state $(3,5)$, yield three.

The first five requested values are `[0,1,1,2,3]`.

**Why the loop is intentionally infinite**

The generator has no input specifying how many Fibonacci values to produce. The caller controls termination by deciding when to stop calling `next`.

`while (true)` ensures the generator never reaches a completed state through normal iteration. For every finite call count permitted by the problem, another value is available.

If call count is zero, the generator may be created but `next` is never invoked, so no values are yielded.

**Generator state is private and independent**

Local variables remain inside one generator object's suspended execution state. Creating two generators produces two independent pairs:

- advancing the first does not advance the second;
- each begins at zero when first requested.

The caller sees values and the standard iterator result objects, not writable access to `previous` or `current`.

**Why precomputation is unnecessary**

The maximum tested prefix is small, so an array could be precomputed. But the problem specifically teaches generator semantics, and the infinite logical sequence has no final length.

The two-variable recurrence provides each next value just in time, uses constant memory, and naturally supports arbitrary finite consumption.

**Numeric behavior**

JavaScript numbers exactly represent Fibonacci values only up to the safe-integer limit. With at most 50 calls, the largest yielded values remain within that exact range.

For much larger indices, a BigInt generator would be needed for exact integer results, but the stated constraint makes ordinary numbers correct.

## Complexity detail

Each resumed iteration performs one addition, one pair assignment, and one yield, so amortized time per produced Fibonacci value is $O(1)$.

The generator stores two numbers and fixed control state, using $O(1)$ space regardless of how many values have already been yielded.

Producing a prefix of $q$ values takes $O(q)$ total time while still using $O(1)$ generator state.

## Alternatives and edge cases

- **Precomputed array:** Simple for a fixed limit but uses $O(q)$ memory and is not naturally infinite.
- **Recursive Fibonacci:** Recomputes overlapping subproblems and can take exponential time per value.
- **Memoized recursion:** Avoids recomputation but stores all prior values, unnecessary for sequential generation.
- **Zero requested calls:** No sequence value is produced.
- **First two values:** Initialization must be zero and one in that order.
- **Simultaneous update:** It preserves both old values for the recurrence.
- **Multiple generators:** Each object retains independent state.
- **Infinite loop:** Safe because `yield` suspends on every iteration and the caller controls demand.
- **Large indices:** Ordinary Number precision eventually fails, though not within 50 calls.
- **Generator completion:** This implementation intentionally never returns `done: true` under continued requests.
