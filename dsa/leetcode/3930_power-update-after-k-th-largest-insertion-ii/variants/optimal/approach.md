## General

Each query changes two pieces of state:

1. The inserted value permanently joins the current multiset of numbers.
2. The current `p` is replaced by a modular power and remains the base for the next query.

Queries must therefore be processed from left to right. Neither the collection of values nor `p` can be reset between queries.

The central data-structure operation is an order statistic: after insertion, find the one-based `k`th largest value while counting duplicate occurrences separately. The source intends to maintain all current values in a `SortedList` so that insertion keeps them ordered and indexing retrieves the requested rank.

**Important defect and manifest mismatch**

The exact `solution.py` references `SortedList` but neither imports it nor defines it. In a normal Python execution environment, the method raises `NameError: name 'SortedList' is not defined` at `sl = SortedList(nums)`. A typical intended dependency would be `SortedList` from the third-party `sortedcontainers` package, but that import is absent from the checked source.

The Optimal manifest also says that the implementation coordinate-compresses values and uses a Fenwick tree. The source does neither: it directly constructs a `SortedList` and uses `add` plus negative indexing. This document follows the exact source algorithm, not the inaccurate Fenwick-tree summary. The runtime discussion below states the intended ordered-list costs conditionally; the current file cannot execute until `SortedList` is supplied.

**Why a sorted multiset represents the query state**

An ordinary set would be wrong because equal values occupy separate rank positions. For example, if the current values are `[7, 7, 5]`, the first and second largest elements are both `7`. A sorted-list structure retains both occurrences:

`[5, 7, 7]`.

The source initializes the structure from `nums`. This gives it a sorted copy of the initial multiset without changing the order or contents of the caller's list.

For each pair `[val, k]`, `sl.add(val)` inserts one new occurrence at its sorted location. Earlier insertions remain present, so the structure exactly represents the multiset required after the current query.

**Convert a largest rank to an ascending-list index**

A `SortedList` is indexed in ascending order. Positive index zero is the smallest element, but the query asks for a rank from the largest end. Python negative indices make the conversion direct:

- `sl[-1]` is the largest value;
- `sl[-2]` is the second largest value;
- in general, `sl[-k]` is the `k`th largest value.

The contract guarantees that `k` is between one and the current multiset size, so `-k` is always a valid index. No subtraction involving the current length is required.

Duplicates behave correctly because they occupy distinct list positions. Inserting another copy may shift indices, but `sl[-k]` always refers to the rank in the fully updated collection.

**Update the evolving modular state**

Let `x = sl[-k]`. The required transition is

$$
p\leftarrow p^x\bmod M,
\qquad M=10^9+7.
$$

The source performs it with Python's three-argument `pow(p, x, mod)`. This form uses modular exponentiation: it repeatedly squares and reduces intermediate values modulo $M$ instead of first constructing the enormous integer $p^x$. It is both faster and far more memory-efficient than `p ** x % mod` for exponents as large as $10^9$.

The assignment is made back to `p` before appending. Therefore `ans[i]` is the state after query $i$, and the next query raises that updated residue—not the original input value—to its newly selected exponent.

For example, suppose the first query selects exponent $3$. The state becomes $p^3\bmod M$. If the second query selects exponent $2$, the next state is

$$
\left(p^3\bmod M\right)^2\bmod M,
$$

not the unrelated value $p^2\bmod M$ based on the original `p`.

**Why the chosen exponent is exact**

Immediately before each selection, the source has inserted the query value. Initially the ordered structure contains every entry of `nums`. By induction, after processing the first $i$ insertions it contains the initial values plus exactly those $i$ inserted occurrences. Maintaining ascending order means negative index `-k` selects precisely the requested position in descending order.

Python's modular `pow` then computes the specified update exactly, and the result is appended in query order. These two facts maintain both required states after every iteration.

No value is removed from the collection. The method's behavior correctly models cumulative insertion rather than answering each query against only the original array plus its own `val`.

## Complexity detail

Let $N$ be the initial number of values, $Q$ the number of queries, and $V$ the largest possible selected exponent. Assuming `SortedList` denotes an ordered-multiset implementation with the commonly intended logarithmic insertion and indexed-access interface, construction costs $O(N\log N)$, and each query uses $O(\log(N+Q))$ ordered-structure work.

Three-argument modular exponentiation uses $O(\log x)$ modular multiplication steps for exponent $x$, bounded by $O(\log V)$. Across all queries, the intended total is

$$
O\left(N\log N+
Q\log(N+Q)+Q\log V\right),
$$

which can be written as the manifest's broader `O((N + Q) log (N + Q) + Q log V)` bound.

The ordered multiset holds $N+Q$ occurrences, including duplicates, and the answer holds $Q$ residues. Intended additional space is $O(N+Q)$.

The exact constants and even the precise insertion guarantee depend on which `SortedList` implementation is supplied. For example, the commonly named third-party class uses a blocked sorted-list representation and documents approximate/amortized operation bounds. Since the source contains no import, its actual current behavior is an immediate `NameError` rather than the advertised complexity.

## Alternatives and edge cases

- **Required source dependency:** `SortedList` must be imported or otherwise supplied. The current Optimal source is not self-contained, and this documentation does not silently edit it.
- **Fenwick tree with coordinate compression:** This is the algorithm claimed by the manifest and can support frequency updates plus order-statistic search in $O(\log(N+Q))$. It is not the algorithm present in `solution.py`.
- **Sort the entire collection after every insertion:** This is simple but costs up to $O((N+Q)\log(N+Q))$ per query and repeats nearly all sorting work.
- **Use a plain set:** A set discards duplicates, changing rank positions and producing incorrect `k`th-largest values.
- **Maintain only one heap:** A heap exposes only one extreme efficiently. Queries may request different arbitrary ranks, so a single min-heap or max-heap is insufficient without rebuilding or additional structures.
- **Compute `p ** x` before reducing:** The intermediate integer can have an enormous number of digits. Three-argument `pow` reduces throughout exponentiation.
- **Rank `k = 1`:** Negative index `-1` selects the current maximum after insertion.
- **Rank equal to the multiset size:** `-k` selects index zero, the current minimum.
- **Duplicate selected values:** Equal occurrences occupy separate ranks, but they yield the same exponent; the sorted multiset preserves both positions.
- **Inserted value becomes the answer immediately:** Insertion happens before `sl[-k]`, so the new value participates in its own query as required.
- **Repeated queries with the same pair:** Each still inserts another occurrence and raises the already-updated `p` again, so outputs need not repeat.
- **State becomes zero:** If modular exponentiation produces zero, every later positive exponent keeps it zero. The code naturally preserves that state.
- **Initial `p` near the modulus:** Three-argument `pow` handles reduction correctly; no manual pre-reduction is necessary.
- **Input list ownership:** Constructing the intended sorted structure from `nums` does not append query values to the original list itself.
