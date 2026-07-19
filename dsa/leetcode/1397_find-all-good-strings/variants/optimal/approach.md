## General
**Remember only the forbidden-prefix suffix.** Build the KMP prefix function for `evil`, then precompute how each matched-prefix length changes after appending each lowercase letter. Reaching matched length $m$ means the forbidden substring has just appeared, so that transition is discarded.

**Track both lexicographic boundaries.** Define a memoized state by the next position, the current KMP matched length, and two flags saying whether the constructed prefix still equals the lower and upper bounds. Those flags determine the smallest and largest letter allowed at the position. Appending a letter updates each flag and the KMP state.

At position $n$, every surviving construction has remained inside both bounds and has never completed `evil`, so it contributes one. Conversely, every good string in the interval follows exactly one sequence of allowed transitions. The state records everything future choices depend on, allowing equivalent prefixes to share their remaining count. Sum transitions modulo $10^9 + 7$.

## Complexity detail
There are at most $4nm$ digit-DP states, and each tries 26 letters, giving $O(26nm)$ time. KMP transition preprocessing fits the same bound because $m \le n$. Memoization and the transition table use $O(nm)$ space, with recursion depth $O(n)$.

## Alternatives and edge cases
- **Enumerate the interval:** Generate every string from `s1` through `s2` and test substring membership. It is correct but can require exponential time in $n$.
- **Automaton without boundary flags:** Counting all strings that avoid `evil` does not enforce the inclusive `s1` and `s2` interval.
- **Overlapping matches:** KMP fallbacks preserve suffixes such as those in `"aaaa"`; resetting the match length to zero can miscount.
- **Forbidden prefix:** If every bounded string begins with `evil`, the answer is zero.
- **Single-string interval:** Return either one or zero according to whether that exact string contains `evil`.
- **Inclusive endpoints:** Both `s1` and `s2` contribute when they avoid the forbidden substring.
- **Modulo arithmetic:** Reduce accumulated state counts, not the lexicographic comparisons or KMP lengths.
