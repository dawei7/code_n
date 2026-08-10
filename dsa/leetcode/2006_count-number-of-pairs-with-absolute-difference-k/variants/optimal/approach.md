## General

**Enumerate every ordered-by-index pair**

The exact source uses one generator with two ranges. Outer index `i` visits zero through $N-1$. Inner index `j` begins at `i+1` and runs to the end.

Starting `j` after `i` enforces `i<j` automatically. Every unordered pair of distinct indices appears once, with its smaller index first. Self-pairs and reversed duplicates never appear.

**Test the stated equality directly**

For each pair, the generator evaluates

`abs(nums[i] - nums[j]) == k`.

Absolute value removes direction: a difference of $k$ and a difference of $-k$ both qualify. The values' order in the array therefore does not affect the numerical check, while index order still determines unique pair enumeration.

**Sum Boolean results**

In Python, `True` behaves as integer one and `False` as zero in arithmetic. `sum(...)` therefore counts exactly how many pair predicates are true.

No explicit answer variable is needed. The generator produces one Boolean at a time rather than constructing a list of all results.

**Trace duplicates correctly**

For `nums=[1,2,2,1]` and $k=1$, each first-value occurrence can pair with each second-value occurrence when their indices differ. There are two ones and two twos, yielding four index pairs.

Although values repeat, the nested index ranges keep occurrences distinct. A set of values would be wrong because it would collapse multiplicity.

For `nums=[3,2,1,5,4]` and $k=2$, the loop tests all ten index pairs. Pairs $(0,2)$, $(0,3)$, and $(1,4)$ pass because their value differences are two; the other seven predicates contribute zero. Notice that pair $(0,3)$ has values three and five in increasing order, while $(0,2)$ has three and one in decreasing order. The absolute-value test treats both directions correctly without changing their index order.

**Why the enumeration is complete and unique**

Take any valid pair $(i,j)$ with $i<j$. The outer range reaches `i`, and its inner range contains `j`, so the equality is tested and contributes one.

Every tested pair already satisfies the strict index order. The two ranges have only one iteration corresponding to a given ordered pair, so it cannot be counted twice. False predicates contribute zero. Thus the returned sum is exactly the answer.

**The exact complexity differs from the manifest**

There are

$$
\binom{N}{2}=\frac{N(N-1)}{2}
$$

index pairs. The generator checks all of them, even if an answer could be derived from frequencies.

Therefore the exact source takes $\Theta(N^2)$ time, not the manifest's $O(N)$ time. Its auxiliary space is constant, not $O(N)$, because it does not build a frequency table.

The constraint $N\le200$ makes at most 19,900 comparisons, so the exhaustive method is practical despite not meeting the labeled optimal asymptotic bound.

**How a linear method would work**

While scanning values left to right, a counter of earlier values can tell how many partners differ by $k$. For current $x$ and positive $k$, prior values $x-k$ and $x+k$ both qualify. Add their frequencies, then record $x$.

That approach counts each pair at its later index and takes expected $O(N)$ time with $O(N)$ storage. It matches the manifest but is not the exact `solution.py`.

**Why positive `k` simplifies the frequency alternative**

The constraints give $k\ge1$, so $x-k$ and $x+k$ are distinct. If zero were allowed, adding both counters would double-count equal-value pairs and would need a special case.

The brute-force source does not depend on this simplification; its absolute comparison would handle $k=0$ correctly as well.

## Complexity detail

Let $N$ be the number of values. The source evaluates $\binom{N}{2}$ predicates, giving $\Theta(N^2)$ time.

The generator is lazy and stores only loop state plus temporary arithmetic values, so auxiliary space is $O(1)$. These exact bounds differ from the manifest's frequency-based $O(N)$ time and $O(N)$ space.

## Alternatives and edge cases

- **One-pass frequency counter:** Add counts of `x-k` and `x+k` among earlier values, then record `x`; expected $O(N)$ time and $O(N)$ space.
- **Fixed-size frequency array:** Values lie in 1 through 100, enabling $O(N+V)$ time and $O(V)$ space.
- **Sort plus two pointers:** Possible but must count duplicate multiplicities and costs $O(N\log N)$.
- **Duplicate values:** Different indices remain distinct pairs and are all enumerated.
- **No matching pair:** Every Boolean is false and the sum is zero.
- **Array length one:** The inner ranges are empty and the result is zero.
- **Positive `k`:** Avoids ambiguity between the two frequency targets in an optimized method.
- **Absolute value:** Handles either larger value appearing first.
- **Strict index order:** Inner range beginning at `i+1` prevents self-pairs and double counting.
- **Maximum length:** Quadratic enumeration is still only 19,900 checks at $N=200$.
- **Manifest mismatch:** The exact generator is quadratic, not linear.
- **Input preservation:** The method reads `nums` without sorting or modifying it.
