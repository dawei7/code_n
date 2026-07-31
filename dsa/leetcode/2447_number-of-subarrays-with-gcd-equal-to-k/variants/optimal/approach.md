## General

Group subarrays by their right endpoint. For the previous endpoint, keep a map from each distinct GCD to the number of subarrays ending there with that GCD. Many different starts collapse into the same state, so their multiplicities can be processed together.

When the next `value` arrives, the one-element subarray contributes GCD `value` with count 1. Extending a previous subarray changes its GCD from $g$ to $\gcd(g,\texttt{value})$. Add the previous state's entire count to that new GCD, merging states that produce the same result.

After constructing the states for the current endpoint, the multiplicity stored at `k` is exactly the number of qualifying subarrays ending there. Add it to the answer.

Every nonempty subarray ending at the current position is either the singleton or a unique extension of a subarray ending one position earlier, so the transition neither omits nor duplicates any subarray. The GCD update is the defining associative operation, making every grouped state exact.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $V=\max(\texttt{nums})$. The distinct GCDs for one endpoint form a decreasing divisor chain. Every strict decrease is by at least a factor of two, so there are $O(\log V)$ states.

Each state performs a Euclidean GCD operation costing $O(\log V)$ in the standard integer model. Total time is therefore $O(n\log^2 V)$, and the two endpoint-state maps use $O(\log V)$ space.

## Alternatives and edge cases

- **Enumerate every start and end:** Maintaining a running GCD for each start is correct but takes $O(n^2\log V)$ time in the standard integer model.
- **Recompute each subarray GCD:** Starting the GCD calculation from scratch adds another factor of $n$ and is unnecessary.
- **Divide by `k`:** Values divisible by `k` may be normalized and the task reduced to counting GCD 1; state compression still applies.
- **Value not divisible by `k`:** No qualifying subarray can cross it, although the general state transition handles that fact automatically.
- **Singleton:** A one-element subarray qualifies exactly when its value equals `k`.
- **All values equal `k`:** Every subarray qualifies, producing $n(n+1)/2$.
- **GCD appears after extension:** Values individually larger than `k` can combine to produce GCD `k`.
- **Large values:** Euclid's algorithm handles values up to $10^9$ without factorization.
