## General

Let `ways[length]` be the number of valid binary strings of exactly that length, and set `ways[0] = 1` for the empty construction. A valid nonempty string ends in either `1` or `0`. If it ends in `1`, remove exactly `oneGroup` trailing ones; the remainder is another valid construction of length `length - oneGroup`. Removing `zeroGroup` trailing zeros gives the analogous predecessor for a string ending in `0`.

These predecessors are unique. Even when the final block is several group units long, removing one fixed-size unit leaves exactly one shorter representation of the same block; there is no alternative split that produces the same final string. The two final-bit cases are disjoint, so

$$
\textit{ways}[\ell]
=
[\ell\ge\texttt{oneGroup}]\,\textit{ways}[\ell-\texttt{oneGroup}]
+
[\ell\ge\texttt{zeroGroup}]\,\textit{ways}[\ell-\texttt{zeroGroup}].
$$

Compute lengths in increasing order, reduce every state modulo $10^9+7$, and add states from `minLength` through `maxLength` to the answer. The recurrence generates exactly the strings whose maximal block sizes are multiples of their required group sizes.

## Complexity detail

Let $L=\texttt{maxLength}$. Each of the $L$ states uses at most two constant-time transitions, so the algorithm takes $O(L)$ time. The dynamic-programming array contains $L+1$ values and uses $O(L)$ space.

## Alternatives and edge cases

- **Track the last bit and enumerate block multiples:** Summing every possible final block length is correct but can require $O(L^2)$ time when a group size is one.
- **Generate strings:** Enumerating binary strings is exponential and becomes impossible long before $L=10^5$.
- **Equal group sizes:** The two transitions still represent different final bits and must both be counted.
- **Unreachable lengths:** Their state remains zero and contributes nothing to the requested range.
- **All-one and all-zero strings:** They arise by repeatedly extending the same final block in fixed-size units.
- **Modulo reduction:** Apply it during every transition and range accumulation to keep counts bounded.
