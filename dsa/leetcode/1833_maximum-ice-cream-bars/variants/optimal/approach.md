## General
**Count prices instead of comparison-sorting them**

Create a frequency array indexed by price. Scanning `costs` once records how many bars are available at each value from 1 through $M$. Iterating those indices in increasing order then exposes the bars in counting-sort order without rearranging the original list.

**Buy as much as possible from each cheapest bucket**

At price $p$ with frequency $f$, the current budget can afford at most `coins // p` bars. Buy

$$
\min\left(f,\left\lfloor\frac{\texttt{coins}}{p}\right\rfloor\right)
$$

of them, add that quantity to the answer, and subtract their total cost. If fewer than $f$ bars were affordable, no later price can be affordable either, so the scan may stop.

**Why choosing the cheapest bars maximizes the count**

Consider any feasible selection of $k$ bars. If it contains a bar more expensive than an unselected bar, replacing the selected bar with the cheaper one does not increase total cost and preserves the count. Repeating this exchange transforms the selection into the $k$ cheapest bars. Therefore, if the greedy cheapest-first prefix of length $k+1$ exceeds the budget, every possible set of $k+1$ bars does as well; the greedy count is maximal.

Processing an entire equal-price bucket at once is equivalent to visiting its bars individually. The integer division determines exactly how much of the bucket fits and leaves no missed cheaper choice.

## Complexity detail
Building the frequency array takes $O(n)$ time, and scanning all price indices through $M$ takes $O(M)$ time, for $O(n+M)$ total. The frequency array has $M+1$ entries and uses $O(M)$ space.

## Alternatives and edge cases
- **Comparison sort:** Sorting `costs` and buying its prefix gives the same greedy result in $O(n\log n)$ time, but it does not satisfy the counting-sort requirement.
- **Min-heap:** Repeatedly extracting the cheapest price is correct but adds $O(\log n)$ work per purchase and extra heap storage.
- **Insertion sort:** It also exposes prices in order but can take $O(n^2)$ time on reverse-sorted costs.
- **Nothing affordable:** If the first nonempty price bucket exceeds the budget, return zero.
- **Exact budget:** A bar or bucket whose total cost equals the remaining coins is affordable.
- **Partial bucket:** Buy only the number of equal-price bars covered by integer division.
- **All bars affordable:** Exhaust every frequency bucket and return $n$, even if coins remain.
- **Repeated prices:** Their frequency must count separate purchasable bars.
- **Input order:** The original ordering has no effect because purchases may occur in any order.
- **Large unused prices:** The $O(M)$ scan includes empty price buckets, which is why $M$ appears explicitly in the complexity.
