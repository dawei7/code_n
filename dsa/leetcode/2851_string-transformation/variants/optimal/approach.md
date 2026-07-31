## General

**View every operation as a rotation-offset transition.** Moving a nonempty proper suffix to the front is a nonzero cyclic rotation. Label the $n$ possible offsets from $0$ through $n-1$, with offset $0$ representing the original `s`. From any current offset, the $n-1$ legal suffix lengths lead once each to every other offset and never remain at the current offset.

Several offsets may spell the same visible string when `s` is periodic. They must remain separate states because different suffix choices are different ways. The target contribution is therefore determined by how many of the $n$ rotations of `s` equal `t`, not merely by whether one match exists.

**Find all matching offsets in linear time.** Every length-$n$ rotation appears exactly once as a length-$n$ substring beginning in `s + s[:-1]`. Build the KMP prefix function for `t + "#" + s + s[:-1]`, where the separator cannot occur in either lowercase input. Each prefix value equal to $n$ identifies one target rotation, including offset $0$ when `s == t`.

**Collapse the complete transition graph to two counts.** By symmetry, after any number of operations every fixed nonzero offset has the same number of paths from offset $0$. Let $A_j$ count paths that return to offset $0$ after $j$ operations, and let $B_j$ count paths that end at one particular nonzero offset. Then

$$
A_{j+1}=(n-1)B_j,
\qquad
B_{j+1}=A_j+(n-2)B_j,
$$

with $A_0=1$ and $B_0=0$. Diagonalizing this two-state recurrence gives

$$
A_k=\frac{(n-1)^k+(n-1)(-1)^k}{n},
\qquad
B_k=\frac{(n-1)^k-(-1)^k}{n}.
$$

Because $n < 10^9+7$, division by $n$ is multiplication by its modular inverse. Fast modular exponentiation evaluates both powers safely for $k$ as large as $10^{15}$.

If $c$ rotations match `t`, each contributes $B_k$, except that offset $0$ contributes $A_k$ when `s == t`. Thus the answer is $cB_k$ plus $A_k-B_k$ exactly in that equal-string case. This counts every matching offset and every exact-length operation sequence once.

## Complexity detail

Building the KMP prefix function for a combined string of length $O(n)$ takes $O(n)$ time and space. Modular exponentiation takes $O(\log k)$ time; the inverse exponent uses the fixed modulus and does not depend on the input magnitudes. Total time is $O(n+\log k)$ and auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Compare every explicit rotation:** Constructing or comparing all $n$ rotated strings takes $O(n^2)$ total character work and cannot handle the maximum length.
- **Two-by-two matrix exponentiation:** Raising the recurrence matrix to the $k$th power also takes $O(\log k)$ time and avoids modular division, but the closed form is smaller once its two eigenvalues are derived.
- **Dynamic programming for every operation count:** Iterating the recurrence $k$ times is $O(k)$ and is infeasible when $k$ reaches $10^{15}$.
- **Target is not a rotation:** KMP finds zero matching offsets, so the answer is `0` for every positive `k`.
- **Equal strings:** Offset $0$ must use $A_k$, while any additional periodic offsets still use $B_k$; treating all matches identically gives the wrong result.
- **Length two:** There is only one legal suffix choice, so the string alternates deterministically between its two offsets and exposes parity mistakes.
- **Uniform strings:** All $n$ offsets spell the same target, but there are still $(n-1)^k$ distinct sequences of suffix choices.
