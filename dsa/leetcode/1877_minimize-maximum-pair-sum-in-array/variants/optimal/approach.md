## General
**Balance the two extremes**

Sort the numbers into non-decreasing order. Pair the smallest value with the largest, the second smallest with the second largest, and continue inward. Compute each of these $N/2$ sums and return their maximum.

**Why the outermost pair can be fixed**

Let $a$ be the smallest remaining value and $b$ the largest. Consider any pairing in which $b$ is paired with some $x$ instead of $a$, while $a$ is paired with $y$. Replacing those two pairs by $(a,b)$ and $(x,y)$ cannot increase their worst sum: $a+b \le x+b$, and $x+y \le x+b$ because $y \le b$. Thus an optimal pairing exists that joins the two extremes.

**Repeat the exchange**

After fixing $(a,b)$, remove both values. The same argument applies to the smallest and largest values still unpaired. Repeating it constructs every opposite-rank pair without worsening an optimum, so the maximum sum produced by the two-pointer scan is globally minimal. Equal values cause no difficulty because exchanges involving them may simply leave the sums unchanged.

## Complexity detail
Sorting the $N$ values takes $O(N\log N)$ time, and examining the $N/2$ opposite-rank pairs takes $O(N)$ time. The app-local implementation creates a sorted copy, requiring $O(N)$ space. Its two indices and running maximum use only constant additional storage.

## Alternatives and edge cases
- **Frequency counting:** Since every value is at most $10^5$, a frequency array and two opposing value pointers can form the same pairs in $O(N+10^5)$ time and $O(10^5)$ space.
- **Quadratic selection sort:** It produces the needed ordering but takes $O(N^2)$ time.
- **Enumerate all pairings:** Exhaustive pairing can confirm tiny examples, but its combinatorial running time is unsuitable for the input bound.
- **Two elements:** They form the only possible pair, so return their sum.
- **Duplicate values:** Treat duplicates as separate occurrences; their relative order after sorting is irrelevant.
- **Already sorted input:** The same outer-to-inner pairing applies without changing the reasoning.
- **Large values:** A pair sum can reach $2\cdot 10^5$, which fits ordinary integer ranges.
