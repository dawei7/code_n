## General

A direct solution chooses one index from each of four arrays, creating $n^4$ tuples. The zero-sum equation can be split into two independent halves:

$$
\texttt{nums1}[i]+\texttt{nums2}[j]
=
-(\texttt{nums3}[k]+\texttt{nums4}[l]).
$$

Instead of remembering three indices while searching for the fourth, the exact solution precomputes how often every sum from the first two arrays occurs. It then enumerates sums from the final two arrays and looks up the required opposite. This is a meet-in-the-middle strategy: combine two choices on each side, then match the two summaries.

**Count first-half sums, not merely distinct sums**

The generator `a + b for a in nums1 for b in nums2` produces one sum for every index pair from the first two arrays. `Counter(...)` maps each numerical sum to the number of pairs that create it.

Frequency is essential. If three different `(i, j)` pairs all produce sum `5`, and one `(k, l)` pair produces `-5`, those are three different valid index tuples, not one. A plain set would remember only that `5` exists and would undercount duplicates.

Even equal values at different indices count separately. The nested generator iterates occurrences, so two identical elements in one array participate as distinct choices and correctly increase the counter.

**Match each second-half pair with its complement**

For every `c` from `nums3` and every `d` from `nums4`, the second-half sum is `c + d`. To make the total zero, the first-half sum must be `-(c + d)`. The lookup `cnt[-(c + d)]` returns exactly how many first-half index pairs have that required sum.

The outer `sum(...)` adds this count for all $n^2$ second-half pairs. Python's `Counter` returns zero for a missing key, so a pair with no complement contributes nothing and needs no conditional branch.

**Trace the first example**

For `nums1 = [1,2]` and `nums2 = [-2,-1]`, the four first-half index pairs produce:

- `1 + (-2) = -1`
- `1 + (-1) = 0`
- `2 + (-2) = 0`
- `2 + (-1) = 1`

Thus the counter is `{-1: 1, 0: 2, 1: 1}`.

For `nums3 = [-1,2]` and `nums4 = [0,2]`, the second-half sums are `-1`, `1`, `2`, and `4`. Their required complements are `1`, `-1`, `-2`, and `-4`. The first two complements occur once each, while the latter two do not occur. The total is $1+1+0+0=2$.

These two matches correspond exactly to the two index tuples listed in the example.

**Why every valid tuple is counted once**

Take any valid tuple `(i, j, k, l)`. Its first pair has some sum `p`, and its second pair has sum `q`. Since the four values total zero, $p=-q$. When the counter is built, pair `(i, j)` contributes one occurrence to key `p`. Later, when the exact second pair `(k, l)` is enumerated, the complement lookup selects key `-q = p`, so that first pair contributes one to the answer.

No other second-pair iteration represents the same `(k, l)`, and no other counter occurrence represents the same `(i, j)`. Therefore the tuple is counted exactly once.

Conversely, every unit counted by a lookup consists of a concrete first pair whose sum is `-(c + d)` and the current concrete second pair. Their combined sum is zero, so every contribution corresponds to a valid tuple. This proves both completeness and absence of overcounting.

**Why splitting two arrays and two arrays is balanced**

Each half has $n^2$ combinations. Storing one half and scanning the other therefore costs quadratic time and space. An unbalanced split—for example, precomputing one array and enumerating the other three—would use less memory but require $n^3$ time. Dividing four arrays evenly minimizes the larger enumeration exponent.

The method does not need to sort, deduplicate, or return actual tuples. It counts index combinations directly, which avoids the additional uniqueness concerns found in the ordinary single-array 4Sum problem.

## Complexity detail

Each of the first two arrays has length $n$, so the first generator produces $n^2$ pair sums. Building the counter takes expected $O(n^2)$ time under expected constant-time hash-table operations.

The second generator also enumerates $n^2$ pairs. Each performs one addition, negation, counter lookup, and contribution to the total, for another expected $O(n^2)$ time. Overall expected time is $O(n^2)$.

In the worst case, all first-half pair sums are distinct, so the counter stores $n^2$ keys. Auxiliary space is therefore $O(n^2)$. The generators are lazy and do not create separate $n^2$ lists, but the counter itself can still reach that size.

If many pairs share sums, actual counter space may be smaller, yet the worst-case manifest bound remains $O(n^2)$. Python integer arithmetic prevents overflow of sums and the accumulated answer; fixed-width implementations should use types wide enough for pair sums and counts.

## Alternatives and edge cases

- **Four nested loops:** It is conceptually direct but takes $O(n^4)$ time, which is unnecessary for the separable sum equation.
- **Three loops plus a frequency map for one array:** This reduces lookup cost but still requires $O(n^3)$ time. Pairing the arrays evenly gains another factor of $n$.
- **Sort both pair-sum lists:** Build all sums for each half, sort them, and use two pointers to count opposite values. It also uses $O(n^2)$ space but costs $O(n^2\log n)$ time because of sorting.
- **Store a set of sums:** A set loses multiplicities and is incorrect whenever different index pairs produce the same sum.
- **Counter both halves:** One can multiply `left[s] * right[-s]` for each distinct sum. It is correct but may store two quadratic maps; the exact solution stores only one and scans the other lazily.
- **All zeros:** Every one of the $n^4$ index tuples sums to zero. The first counter stores key zero with frequency $n^2$, and each of the $n^2$ second pairs adds that frequency, producing $n^4$.
- **Repeated values:** Frequencies in the counter preserve every distinct index choice, even when numerical values are identical.
- **No complement:** `Counter` returns zero for a missing key, so such a second-half pair adds nothing.
- **Negative and positive values:** Negation handles both symmetrically; no ordering assumptions are used.
- **Input arrays remain unchanged:** The algorithm only iterates over them and stores derived sums.
