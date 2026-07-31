## General

Maintain the GCD of the current part while scanning from left to right. Incorporating the next value can only keep or decrease that GCD. If the extended GCD remains greater than 1, retaining the value in the current part makes the part as long as possible without invalidating it.

If the extended GCD becomes 1, no later value can repair that part: the GCD of a sequence that already has GCD 1 remains 1 after more values are included. A boundary is therefore mandatory at or before the current value. Cutting immediately before it is optimal because the preceding part is valid and is the longest valid prefix available. Start the new part with the current value and continue.

Repeating this forced-boundary rule yields the fewest parts. Every produced part is valid because each input value is at least 2, and every cut occurs before the current GCD would become 1.

## Complexity detail

The scan performs one Euclidean GCD computation per value. With $V=\max(\texttt{nums})$, this costs $O(n\log V)$ time in the standard integer model. The running GCD and part count use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Partition dynamic programming:** Trying every final subarray produces a correct $O(n^2\log V)$ method but repeats many GCD computations.
- **Prime-factor sets:** Tracking common factors can express the same boundary rule but is more expensive than direct GCD updates.
- **Single value:** It forms one valid part because every value is at least 2.
- **Whole-array GCD above one:** The answer is 1.
- **Pairwise coprime neighbors:** Each value may be forced into its own part.
- **GCD cannot recover:** Once a candidate part reaches GCD 1, extending it can never make it valid again.
- **Large values:** Euclid's algorithm handles values up to $10^9$ without factorization.
