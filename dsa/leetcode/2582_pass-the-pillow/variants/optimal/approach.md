## General

The pillow repeats a back-and-forth motion. Moving from person `1` to person `n` takes $n-1$ seconds; the next traversal of the same length moves back from person `n` to person `1`.

Divide `time` by $n-1$. The quotient counts complete endpoint-to-endpoint traversals, and the remainder `offset` is the distance traveled within the current traversal.

- After an even number of complete traversals, the current direction is from left to right, so the holder is `offset + 1`.
- After an odd number, the direction is from right to left, so the holder is `n - offset`.

The quotient's parity therefore identifies both the starting endpoint and direction of the unfinished traversal. Adding or subtracting the remainder gives exactly the holder after all elapsed seconds, including the endpoint cases where the remainder is zero.

## Complexity detail

The calculation uses a fixed number of integer arithmetic operations, so it takes $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Second-by-second simulation:** Updating the holder and direction once per second is straightforward and correct, but takes $O(\texttt{time})$ time when the periodic motion can be folded arithmetically.
- **Full-period reduction:** Reducing `time` modulo $2(n-1)$ and reflecting positions beyond `n` is another constant-time formulation of the same cycle.
- **Endpoint remainder:** A remainder of zero means the pillow is exactly at an endpoint; the traversal quotient's parity selects the correct endpoint.
- **Two people:** When `n = 2`, every traversal lasts one second and the quotient parity alternates directly between people `1` and `2`.
