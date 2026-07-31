## General

**Operations preserve a remainder class.** Adding or subtracting `value` never changes an integer's remainder modulo `value`. Conversely, any two integers in the same remainder class differ by a multiple of `value`, so one can be transformed into the other with allowed operations. Each array element is therefore a single reusable supply item for its normalized remainder.

**Build the MEX greedily.** To make the final array contain every integer from zero upward, candidate `x` must consume one element whose remainder is `x % value`. Count all remainder supplies, start `mex` at zero, and spend one matching item while it exists. Stop at the first candidate whose class is exhausted.

Every consumed item can be transformed into its assigned candidate, so all smaller integers are simultaneously achievable. At the stopping point, every original element in the required remainder class has already been assigned to a smaller candidate of that class. No operation can move an element from another class into it, making this MEX both achievable and maximal.

## Complexity detail

Let $n$ be the length of `nums`. Counting remainders takes $O(n)$ time. The greedy loop consumes at most one element per iteration, so it also performs at most $n$ iterations. Total time is $O(n)$. At most $\min(n, \texttt{value})$ remainder counts are stored, which is $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Scan unused elements for every candidate:** Greedily finding a matching unused element is correct but can rescan the array and take $O(n^2)$ time.
- **Sort normalized remainders:** Sorting can also organize supplies, but it raises the time to $O(n \log n)$ without improving the greedy decision.
- **Negative inputs:** Remainders must be normalized to the range from zero through `value - 1`; Python's positive-modulus result already has this form.
- **`value = 1`:** Every element can represent the next candidate, so the maximum MEX equals the array length.
- **Missing residue zero:** If no element has remainder zero, the loop stops immediately and the maximum MEX is zero.
