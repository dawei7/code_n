## General
**Simulate the unique legal transition**

Initialize a step counter to zero. While `num` is positive, inspect its least significant bit. An even number has a zero bit there and must be replaced by `num // 2`; an odd number has a one bit and must be replaced by `num - 1`. Increment the counter after each replacement.

Every iteration exactly follows the operation specified for the current value, so the produced sequence is the only legal sequence. Each transition makes the value smaller, and every odd step creates an even value unless it reaches zero, ensuring termination. The counter therefore equals the requested number of operations.

## Complexity detail
Each division removes one binary digit, and each subtraction clears a low one bit before a division. The number of iterations is $O(\log \texttt{num})$ for positive input; zero takes constant time. The algorithm stores only the current integer and counter, using $O(1)$ space.

## Alternatives and edge cases
- **Bit-count formula:** For positive `num`, the answer is its bit length minus one divisions plus one subtraction for every set bit; this also takes $O(\log \texttt{num})$ time.
- **Dynamic programming through every integer:** Computing the recurrence for all values from 0 through `num` is correct but takes $O(\texttt{num})$ time and space.
- **Zero:** Return 0 without entering the loop.
- **One:** One subtraction reaches zero.
- **Power of two:** Repeated division reaches 1, followed by one final subtraction.
- **Odd value:** Subtraction occurs before any subsequent division.
