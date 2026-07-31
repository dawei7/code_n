## General

A generator suspends its execution at each `yield` and resumes with all local variables intact. Store two values: `previous`, the Fibonacci number to yield now, and `current`, the following Fibonacci number. Initialize them to $0$ and $1$.

Inside an infinite loop, first yield `previous`. When the caller requests another value, execution resumes immediately after that yield. Replace the state pair with `(current, previous + current)`, then repeat.

Before the $i$th yield, the two variables equal $(F_i,F_{i+1})$. The generator returns $F_i$, and the simultaneous update produces $(F_{i+1},F_i+F_{i+1})=(F_{i+1},F_{i+2})`. This establishes the same invariant for the next advance and proves that every yielded value is the required Fibonacci number.

The loop is intentionally infinite: laziness means it runs only until the next `yield` on each call to `next()`, so creating the generator or stopping calls does not perform unbounded work.

## Complexity detail

Creating the generator and each call to `next()` use $O(1)$ time. The suspended generator retains two numbers and fixed control state, so its auxiliary space is $O(1)$. A harness that requests and stores $k$ values necessarily uses $O(k)$ total time and $O(k)$ output space, but the required generator operation remains constant per yield.

## Alternatives and edge cases

- **Precomputed array:** Building a fixed prefix cannot represent the required infinite lazy sequence and performs work before values are requested.
- **Recursive Fibonacci evaluation:** Recomputing each term recursively repeats subproblems and loses the constant-time incremental update.
- **Ordinary function returning an array:** This changes the required generator interface; callers must receive an object supporting repeated `next()` calls.
- With zero calls, the generator body has not started and no value is observed.
- The first two yields must be `0` and `1`; updating before yielding would shift the sequence.
- Simultaneous reassignment must use the old two values so the next pair is not corrupted by update order.
