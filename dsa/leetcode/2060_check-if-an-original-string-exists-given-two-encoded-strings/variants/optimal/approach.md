## General
**A balance represents unmatched wildcard characters**

Use a state `(first, second, balance)`, where the positions identify the unconsumed suffixes and `balance` is the wildcard length produced by `s1` minus that produced by `s2`. Parse one, two, or three digits from the current run of either string. A number from `s1` increases the balance; one from `s2` decreases it. Trying every numeric prefix naturally covers every partition of adjacent numeric substrings.

**Consuming literals only on the shorter expansion**

When `balance > 0`, `s1` has unmatched wildcard characters, so the next literal from `s2` can consume one and reduce the balance. When `balance < 0`, a literal from `s1` consumes one unit in the opposite direction. At balance zero, two literal characters must match and advance together. Success requires both encodings exhausted with balance zero.

Memoize states because different digit partitions repeatedly reach the same positions and balance. Each transition preserves the set of possible expanded prefixes represented by its state, and the three cases exhaust all ways the next original character can be accounted for. Therefore reaching the terminal zero-balance state is equivalent to a common original string existing.

## Complexity detail
There are at most $n_1n_2B$ reachable position-and-balance states. Each state tries at most three numeric prefixes per input or one literal transition, so time and memo space are $O(n_1n_2B)$. The constraints bound all three quantities, but retaining $B$ makes the dependence on numeric ambiguity explicit.

## Alternatives and edge cases
- **Uncached depth-first search:** It follows the same transitions but revisits states exponentially often as digit partitions accumulate.
- **Linear memo lookup:** Storing memoized states in a list preserves correctness but can add a linear state-search factor compared with hashing.
- A consecutive digit run is not necessarily one number; every partition into one- to three-digit lengths must be considered.
- Literal letters compare directly only when the unmatched wildcard balance is zero.
- Both inputs must be exhausted and the final balance must be zero; equal encoded lengths alone are insufficient.
