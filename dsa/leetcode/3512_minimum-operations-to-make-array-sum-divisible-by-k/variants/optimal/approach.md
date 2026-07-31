## General

Let the initial array sum be $S$. Every permitted operation decreases exactly one element by one, so it also decreases the total by exactly one. The distribution of those decrements among the indices is irrelevant to divisibility.

Write $S=qk+r$, where $0 \le r<k$. After exactly $r$ operations, the new sum is

$$
S-r=qk,
$$

which is divisible by $k$. Thus $r$ operations are sufficient.

They are also necessary. After any smaller number $t<r$ of operations, the sum is $S-t=qk+(r-t)$, whose remainder is still positive. No result with fewer than $r$ operations can be divisible by $k$. Therefore the answer is precisely `sum(nums) % k`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Summing the array takes $O(n)$ time, and the remainder calculation is constant time. A correct algorithm must inspect every input value in the worst case because changing any uninspected value can change the total remainder. The $O(n)$ scan therefore matches an $\Omega(n)$ lower bound.

Only the running total is needed, so auxiliary space is $O(1)$. Complexity is verified by an asymptotic-optimality certificate: even literal decrement simulation performs fewer than $k \le 100$ decrements after the initial scan and remains linear in the legal workload, so there is no genuine principal slower class for an honest scaling comparison.

## Alternatives and edge cases

- **Simulate individual decrements:** Repeatedly reducing a value until the sum is divisible is correct, but it obscures the direct remainder formula and needlessly mutates data.
- **Remove elements or subarrays:** The operation changes one value by exactly one; it never removes an element, so subset or prefix-map methods solve a different problem.
- **Choose a particular index:** Any distribution of the required decrements produces the same total, so no index-selection strategy is needed.
- **Already divisible:** A zero remainder immediately gives zero operations.
- **`k = 1`:** Every integer sum is divisible by one, so the remainder and answer are zero.
- **Remainder `k - 1`:** Decreasing the sum is the only allowed direction, so the answer may be as large as `k - 1`; increasing by one is not permitted.
- **Input preservation:** The method calculates a count without modifying `nums`.
