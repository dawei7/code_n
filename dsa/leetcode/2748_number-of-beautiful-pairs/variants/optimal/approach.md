## General

Process `nums` from left to right and treat the current position as the later index $j$. Only the first digits of earlier values matter for pairs ending at $j$, and there are just nine possible nonzero first digits. Maintain how many earlier values have each first digit from $1$ through $9$.

For the current value, obtain its last digit. For each possible earlier first digit $d$, add that bucket's frequency when $\gcd(d,\text{last digit})=1$. These additions count exactly the beautiful pairs whose later index is the current position. Afterward, extract the current value's first digit and increment its bucket so it can participate only as the earlier member of future pairs.

Every index pair is examined implicitly once, when its later endpoint is processed. Its earlier value contributes to precisely one first-digit bucket, and the greatest-common-divisor test includes that bucket exactly when the pair is beautiful. Thus no valid pair is missed or counted twice.

## Complexity detail

Let $n$ be the number of values. Each value checks nine fixed digit buckets and extracts a decimal first digit from a number bounded by $9999$, so the total time is $O(n)$. The ten-entry frequency array uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Check every index pair:** Testing all $i<j$ pairs directly follows the definition but takes $O(n^2)$ time.
- **Convert numbers to strings:** Indexing the first and last characters is correct, but integer division and remainder avoid temporary strings.
- **Precompute compatible digits:** A fixed $9\times9$ coprimality table can replace repeated GCD calls without changing the asymptotic bounds.
- The array contains at least two values, but it may still have zero beautiful pairs.
- A digit of $1$ is coprime with every possible digit, including another $1$.
- The relevant digits are directional: first digit from the earlier number and last digit from the later number.
- Repeated values represent different indices and can form a pair when their relevant digits are coprime.
- Last digits are guaranteed nonzero, while first digits are nonzero because every value is positive.
