## General

Label the `n` final pieces of value one. Whenever a current piece of value `x` is split into parts `a` and `b`, exactly $a b$ unordered pairs of final unit pieces are separated: choose one unit that will descend from the `a` side and one that will descend from the `b` side. This is exactly the operation's cost.

Every unordered pair of final unit pieces stays together until one unique split sends its two members to different children. After that moment the pair can never be reunited. Consequently, every one of the $\binom{n}{2}$ pairs contributes exactly once to the total cost, regardless of the chosen split sizes or order.

The same invariant appears algebraically in the hinted recurrence. If the two children are solved optimally, then

$$
a b + \frac{a(a-1)}{2} + \frac{b(b-1)}{2}
= \frac{(a+b)(a+b-1)}{2}.
$$

Because `a + b = n`, every complete split process has total cost $n(n-1)/2$. Returning that value is therefore both feasible and minimal.

## Complexity detail

The result uses a constant number of arithmetic operations, so the running time is $O(1)$ and the auxiliary space is $O(1)$. The maximum result is approximately $1.25 \cdot 10^{15}$, so implementations with fixed-width integers need a 64-bit type.

## Alternatives and edge cases

- **Recursive split DP:** Trying every first split and recursively solving both parts repeats equivalent states and obscures the fact that all split trees have the same cost.
- **Greedy balanced or one-off splits:** Both strategies are valid, but neither is uniquely optimal; the pair-count invariant proves that every complete strategy has the identical total.
- **Single unit:** When `n = 1`, no operation is needed and the formula returns zero.
- **Wide result:** At the upper bound, the answer is `1249999975000000`, which does not fit in a signed 32-bit integer.
