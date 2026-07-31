## General

The concatenated integer itself may be enormous, but only its remainder modulo `k` matters. If a prefix has remainder $r$ and the next value `x` has $d$ decimal digits, appending it changes the remainder to

$$
(r \cdot 10^d + \texttt{x}) \bmod k.
$$

An index mask identifies exactly which input occurrences have already been used; indices are necessary because equal values are still separate elements. Define suffix feasibility by `(mask, remainder)`: can the unused indices complete the permutation so that the final remainder is zero? There are only $2^n k$ such states. Store each computed result in a flat byte array, using separate markers for impossible and possible states, and precompute every decimal shift modulo `k`.

To obtain the lexicographically smallest answer, consider unused indices in ascending `nums[index]` order. At each position, choose the first value whose successor state is feasible. Any smaller candidate was rejected because no valid completion follows it; choosing the first feasible candidate therefore gives the smallest possible value at this position. Repeating that argument at every suffix proves the reconstructed full list is lexicographically smallest. If the initial state is infeasible, no permutation works.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. At most $k2^n$ mask-and-remainder states are evaluated, and each tries at most $n$ next indices, for $O(n \cdot k \cdot 2^n)$ time. The flat memo table uses $O(k \cdot 2^n)$ space; recursion and reconstruction add $O(n)$ space.

## Alternatives and edge cases

- **Enumerate all permutations:** Testing every ordering takes $O(n! \cdot n)$ time and repeats equivalent suffix states.
- **Store full concatenations:** The value can have up to $65$ digits; modular transitions retain all information relevant to divisibility.
- **Keep remainder sets per mask:** Bottom-up DP has the same asymptotic state space, but a feasibility predicate makes lexicographic reconstruction direct.
- **Return the first arbitrary valid order:** Iteration must follow ascending integer values; input order or string order does not guarantee the lexicographically smallest list.
- **Repeated values:** Equal occurrences use different mask bits. Their relative order is immaterial, but every occurrence must be consumed.
- **`k = 1`:** Every concatenation is divisible, so reconstruction returns `nums` sorted numerically.
- **Single element:** Return that element only if its value is divisible by `k`; otherwise return `[]`.
- **Decimal length:** Appending `100` shifts the prefix by three decimal places, even when its remainder modulo `k` is small.
