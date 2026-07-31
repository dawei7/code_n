## General

**Separate the array by value**

An operation can contain only equal values, so deleting one value never changes what is possible for another. Count the occurrences of every distinct value and solve each frequency independently. The total minimum is the sum of those independent minima.

**Decompose each frequency into groups of two and three**

For a frequency $f$, every operation removes at most three elements. Therefore at least $\lceil f / 3 \rceil$ operations are necessary. A frequency of one is the only impossible case: neither allowed group fits.

For every $f \ge 2$, the lower bound is attainable:

- if $f \bmod 3 = 0$, use only triples;
- if $f \bmod 3 = 1$, reserve four elements for two pairs and delete the rest as triples;
- if $f \bmod 3 = 2$, reserve one pair and delete the rest as triples.

Thus each valid frequency contributes $\lceil f / 3 \rceil$, computed with integer arithmetic as `(f + 2) // 3`. If any frequency equals one, return `-1`; otherwise sum these contributions. The construction proves feasibility, while the three-elements-per-operation limit proves minimality.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and let $u$ be the number of distinct values. Building the frequency table takes expected $O(n)$ time, and processing its $u$ entries takes $O(u)$ time, so the total is expected $O(n)$. The table stores $u$ counters and uses $O(u)$ auxiliary space.

The benchmark uses $n$ as `size` and supplies two occurrences of each distinct value at sizes 48, 192, and 768. This forces the frequency table to grow linearly with the input. The hash-counting method scales linearly, while a correct implementation that searches a growing list of distinct values for every element completes all tiers but exhibits quadratic scaling.

## Alternatives and edge cases

- **Sorting and run lengths:** Sorting groups equal values and then applies the same frequency formula in $O(n \log n)$ time with language-dependent auxiliary space.
- **Repeated linear searches:** A list of value-count pairs avoids hashing but can require $O(nu)$ time, which becomes quadratic when most groups are distinct.
- **Dynamic programming per frequency:** A recurrence using groups of two and three is correct, but the closed-form remainder analysis makes an $O(f)$ table unnecessary.
- **Singleton frequency:** Even one value occurring exactly once makes the entire array impossible to empty.
- **Frequency four:** Taking a triple would leave one element, so four copies must be deleted as two pairs.
- **Frequency five:** One triple and one pair achieve the two-operation lower bound.
- **Independent values:** Operations cannot mix values, so a surplus occurrence of one value cannot compensate for a singleton of another.
