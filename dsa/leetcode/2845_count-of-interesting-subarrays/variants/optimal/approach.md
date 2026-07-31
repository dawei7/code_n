## General

**Replace values with a qualifying indicator.** For each array position, only whether `nums[i] % modulo == k` matters. Treat that condition as `1` and every other value as `0`. Then the number `cnt` for a subarray is the sum of this binary sequence over the same interval.

Let $P_j$ be the number of qualifying positions among the first $j$ elements, with $P_0=0$. For a subarray beginning at $l$ and ending at $r$, its qualifying count is $P_{r+1}-P_l$. The interesting condition becomes

$$
(P_{r+1}-P_l)\bmod\texttt{modulo}=k.
$$

Rearranging the congruence shows that an ending prefix with remainder $P_{r+1}\bmod\texttt{modulo}$ is compatible with every earlier prefix remainder equal to

$$
(P_{r+1}-k)\bmod\texttt{modulo}.
$$

**Count earlier compatible prefixes.** Maintain a frequency map of prefix-count remainders already seen. Initialize remainder `0` with frequency one for the empty prefix. After processing each value, update the qualifying prefix count, add the frequency of the required earlier remainder to the answer, and only then record the current remainder.

Every added map entry corresponds to one earlier boundary and therefore one non-empty subarray ending at the current position. The congruence proves that each counted subarray is interesting, while every interesting subarray has exactly one pair of prefix boundaries and is included when its ending boundary is processed.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each element causes a constant number of expected-time hash-map operations, so the total expected time is $O(n)$.

The map contains at most one entry for each observed prefix remainder: at most $n+1$ entries and never more than `modulo`. Thus the tighter auxiliary bound is $O(\min(n,\texttt{modulo}))$, which is within the required $O(n)$ space bound.

## Alternatives and edge cases

- **Enumerate all subarrays:** Extending every starting position while maintaining its qualifying count is correct but takes $O(n^2)$ time.
- **Store the complete prefix array:** Prefix sums make each individual subarray test constant-time, but testing all boundary pairs is still quadratic; only remainder frequencies remove that second loop.
- **Target remainder zero:** When `k = 0`, a subarray with no qualifying elements can be interesting because zero is divisible by `modulo`.
- **Query before insertion:** Recording the current prefix before querying would count an empty subarray when `k = 0`; only earlier boundaries are valid starts.
- **Large modulus:** The map need not allocate an array of length `modulo`, which may be as large as $10^9$.
- **Large answer:** Up to $n(n+1)/2$ subarrays can qualify, so the result may exceed 32-bit integer range.
- **Element test versus count test:** `nums[i] % modulo == k` selects individual elements, whereas `cnt % modulo == k` decides whether the whole subarray is interesting; neither condition requires every element to qualify.
