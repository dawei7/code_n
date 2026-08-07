## Function Contract

**Inputs**

- `value`: A nonempty list whose entry `value[i]` is the first gain available from index `i`.
- `decay`: A list of the same length; `decay[i]` is the fixed amount subtracted after each selection of index `i`.
- `m`: The maximum total number of selections allowed across all indices.

Let $n = \lvert\texttt{value}\rvert = \lvert\texttt{decay}\rvert$ and let $A = \max(\texttt{value})$. Each index can be selected any number of times, and selections at one index do not change the progression belonging to another index.

**Return value**

Return the greatest total obtainable with at most `m` selections, reduced modulo $10^9 + 7$. Maximization is performed on the actual gains before applying the modulus.
