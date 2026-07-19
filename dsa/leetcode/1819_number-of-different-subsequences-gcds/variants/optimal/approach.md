## General
**Characterize which subsequences could have a candidate GCD**

If a subsequence has GCD $g$, every selected value must be divisible by $g$. Conversely, take all values present in `nums` that are multiples of $g$. If their collective GCD is exactly $g$, those values themselves form a valid subsequence with GCD $g$. If their collective GCD is larger than $g$, every subset of them also has GCD divisible by that larger common divisor, so $g$ is unattainable.

**Enumerate candidates through their multiples**

Record value presence in a Boolean array through $M$. For each candidate $g$ from 1 through $M$, visit `g`, `2*g`, `3*g`, and so on. Fold only the present multiples into a running GCD. As soon as it becomes $g$, count the candidate and stop: adding more multiples cannot make the GCD cease to divide $g$, and it cannot fall below $g$ because every visited value is a multiple of $g$.

**Why the test is both necessary and sufficient**

Any subsequence producing $g$ is contained within the present multiples of $g$. The GCD of the complete set of those multiples divides the GCD of every subset, including that subsequence, while it is itself divisible by $g$; hence it must equal $g$. In the other direction, when the complete set's GCD is $g$, selecting one occurrence of each participating value is a legal non-empty subsequence whose GCD is $g$. The multiple scan therefore counts exactly the attainable values.

## Complexity detail
Building presence takes $O(n)$ time. Candidate $g$ visits at most $\lfloor M/g\rfloor$ multiples, so the total number of visits is

$$
\sum_{g=1}^{M}\left\lfloor\frac{M}{g}\right\rfloor = O(M\log M).
$$

Early exits can reduce this work but are not required for the bound. The Boolean presence table uses $O(M)$ space; scalar GCD state adds $O(1)$.

## Alternatives and edge cases
- **Enumerate all subsequences:** It directly follows the definition but considers $2^n-1$ choices and is infeasible.
- **Incrementally store every seen subsequence GCD:** Combining each new number with all previously attainable GCDs is correct, but the set can contain $\Theta(M)$ values and lead to $O(nM)$ work.
- **Duplicate input values:** Presence is sufficient because repeated equal values cannot create a new GCD value.
- **Value 1 present:** GCD 1 is immediately attainable, although other values must still be tested.
- **Single element:** Exactly that element is attainable, so the answer is one.
- **Candidate absent from `nums`:** It may still be attainable as the GCD of several larger multiples.
- **No present multiple:** The running GCD stays zero, so the candidate is not counted.
- **Maximum value:** Its only possible present multiple within the domain is itself; it is attainable exactly when present.
