## General

Rearrange the required product equality as a ratio equality:

$$
\frac{\texttt{nums[p]}}{\texttt{nums[q]}}
=
\frac{\texttt{nums[s]}}{\texttt{nums[r]}}.
$$

Floating-point values are unnecessary and unsafe. Reduce each positive pair $(a,b)$ by $\gcd(a,b)$ and use the integer tuple $(a/g,b/g)$ as its canonical ratio key. Two positive fractions are equal exactly when these reduced tuples match.

Sweep the third index $r$ from left to right. Before counting choices of $s$ for this $r$, let $q=r-2$ and insert every pair $(p,q)$ with $p\le q-2$ into a frequency map keyed by `nums[p] / nums[q]`. The map persists across iterations. Consequently, after this insertion it contains exactly all left pairs whose second index satisfies $q\le r-2$, which is precisely the required middle gap.

For every $s\ge r+2$, reduce the ratio `nums[s] / nums[r]` and add the matching left-pair frequency. The lower bound on $s$ enforces the final gap. Each contribution therefore supplies indices $p<q<r<s$ with all three separations and the required product equality.

Conversely, consider any valid quadruple. When the sweep reaches its unique third index $r$, its pair $(p,q)$ has already been inserted because $q\le r-2$, and its $s$ is visited because $s\ge r+2$. The two reduced ratios match, so the quadruple is counted once. It cannot be counted at another sweep position because its third index is fixed.

## Complexity detail

Let $n$ be the array length and let $V=\max(\texttt{nums})$. Every eligible left pair is inserted once, and every eligible right pair $(r,s)$ is queried once, for $O(n^2)$ pair operations. Reducing a ratio takes $O(\log V)$ time for the greatest common divisor, so the total time is $O(n^2\log V)$. With expected $O(1)$ hash-table access, the ratio map stores at most $O(n^2)$ distinct keys and uses $O(n^2)$ space.

The benchmark defines `size` as $n$ and uses legal 10-, 20-, and 40-element all-one arrays, spanning 4x. Every eligible quadruple matches. The accepted sweep adds each left pair only when it first becomes eligible and remains quadratic. A correct slower baseline rebuilds all eligible left-pair frequencies from scratch for every $r$, taking $O(n^3\log V)$ time and failing only the scaling verdict.

## Alternatives and edge cases

- **Enumerate all quadruples:** Four nested index loops directly test the definition but require $O(n^4)$ time.
- **Rebuild the left map for each `r`:** This preserves correctness and improves on four loops, but repeats earlier pair work and takes cubic time.
- **Use floating-point ratios:** Rounding can make mathematically equal fractions compare differently, or distinct fractions compare alike; reduced integer pairs are exact.
- **Use products as keys:** A product alone does not represent a pair ratio, and different right denominators would be mixed incorrectly.
- **Forget a gap:** Ordinary subsequence order is insufficient; each of the three adjacent selected-index differences must exceed 1.
- **Duplicate values:** Equal value quadruples formed from different indices are distinct and are captured by frequency counts.
- **Minimum length:** At $n=7$, only indices $(0,2,4,6)$ satisfy all three spacing constraints.
