## General

Encode a row as an $n$-bit mask, with a set bit wherever the row contains `1`. A single selected row is good only when every column sum is zero, so a zero mask immediately yields a valid one-row answer.

For two selected rows, $\lfloor2/2\rfloor=1$. Their subset is therefore good exactly when no column contains two ones, which is equivalent to the masks having bitwise AND zero.

The small bound $n\le5$ supplies the crucial structural lemma: whenever any good subset exists, a good subset of one or two rows also exists. Equivalently, if a collection contains no zero mask and every pair of its masks intersects, then for a universe of at most five bit positions some column occurs in more than half the rows, contradicting the good-subset bound. Thus it is sufficient to search only the two forms above.

Store one earliest row index for every mask already seen. For each new nonzero mask, compare it with at most $2^n$ stored masks. A zero intersection returns two ascending indices because the stored row occurred earlier. If the scan ends without a zero row or disjoint pair, the structural lemma proves that no good subset exists.

## Complexity detail

Building each mask takes $O(n)$ time, and comparing it with the at most $2^n$ distinct stored masks takes $O(2^n)$ time. Across $m$ rows the total is $O(m(n+2^n))$. The mask-to-index table stores at most $2^n$ entries, using $O(2^n)$ auxiliary space. Since $n\le5$, both bit-mask factors are tightly bounded.

## Alternatives and edge cases

- **Test every row pair:** Checking all $\binom m2$ pairs is correct after the size-one-or-two lemma, but costs $O(m^2n)$ time.
- **Enumerate arbitrary subsets:** Searching all row subsets is exponential in $m$ and ignores the structural reduction.
- **Store every duplicate row:** Only one index per mask is needed; duplicate nonzero masks cannot be disjoint from each other.
- A zero row must be returned alone because it already satisfies the one-row bound.
- Returned indices must be ascending; processing rows in input order provides that automatically.
- Repeated nonzero rows do not create a valid pair unless their mask is zero.
- If no zero mask and no disjoint mask pair occur, the correct result is empty.
