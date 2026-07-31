## General

**Express the triple around its middle**

Any three consecutive integers can be written as $x-1$, $x$, and $x+1$.
Their sum is

$$
(x-1)+x+(x+1)=3x.
$$

Therefore a representation exists exactly when `num` is divisible by three.
When it exists, the middle value is uniquely fixed as `num // 3`, so returning
its two neighbors gives the only valid sorted triple.

**Reject the other residues**

If `num % 3` is nonzero, no integer can serve as the middle value because
$3x$ is always divisible by three. Returning an empty array is therefore both
necessary and sufficient. For `num = 0`, the same formula correctly returns
`[-1, 0, 1]`; the output integers are not required to be nonnegative.

## Complexity detail

The method performs a fixed number of arithmetic operations and returns at
most three integers. It takes $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Search outward from zero:** Testing candidate triples eventually finds a
  representation but wastes work proportional to the answer's magnitude.
- **Solve from the first integer:** Deriving `3 * first + 3 = num` is
  equivalent, but centering the triple makes divisibility and uniqueness more
  immediate.
- `num = 0` has the valid triple `[-1, 0, 1]`.
- Inputs with residue one or two modulo three return an empty array.
- Use exact integer arithmetic for values near $10^{15}$; floating-point
  division is unnecessary.
