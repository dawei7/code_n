## General

**A valid substring is determined by endpoint occurrences.** Let character $c$ appear $q$ times in `s`. A substring starting and ending with $c$ can use:

- the same occurrence as both endpoints, producing a length-one substring;
- two distinct occurrences, with the earlier one as start and later one as end.

Every choice of endpoints determines exactly one substring, including all characters between them.

**Count single-occurrence endpoints.** There are $q$ length-one valid substrings, one for each occurrence of $c$.

**Count distinct endpoint pairs.** Choosing any two of the $q$ positions gives one ordered-by-index start/end pair. Their natural order is fixed, so the count is:

$$
\binom q2=\frac{q(q-1)}2.
$$

Total is:

$$
q+\binom q2
=\frac{q(q+1)}2.
$$

The source computes the unsimplified form:

`cnt + cnt * (cnt - 1) // 2`.

**A trace.** In `"abada"`, $c='a'$ appears at three indices. Three single-character substrings qualify. The three pairs of distinct occurrences create `"aba"`, `"ada"`, and `"abada"`. Total is six.

For `"zzz"`, $q=3$ and every one of the $3\cdot4/2=6$ substrings qualifies.

**Why interior characters do not matter.** The condition restricts only first and last characters. Once two $c$ positions are selected, any letters between them are allowed, so no substring scanning or prefix information is needed.

**Why distinct positions give distinct substrings as occurrences.** Even if two chosen ranges have identical text, substrings are counted by their positions in `s`. Different endpoint pairs represent different occurrences and must each contribute.
Map every valid substring to its endpoint occurrence set: size one for a length-one range and size two otherwise. This mapping is one-to-one and covers all one- or two-element choices among the $q$ positions. The formula counts exactly those choices.

**The count can be quadratic even though computation is linear.** A length-$N$ all-$c$ string has $N(N+1)/2$ valid substrings. The method returns that large number without enumerating them, which is the central optimization.

## Complexity detail

`s.count(c)` scans the length-$N$ string once, taking $O(N)$ time. The arithmetic afterward is constant work. Total time is $O(N)$.

Only `cnt` and the returned integer are stored, so auxiliary space is $O(1)$. No substring objects or occurrence-index list is created.

Python integers handle the maximum result for $N\le10^5$ without overflow.

## Alternatives and edge cases

- **Store every occurrence index:** It also yields $q$, but wastes $O(q)$ space because exact positions are unnecessary.
- **Enumerate all substrings:** There are $O(N^2)$ and checking endpoints repeats work.
- **Streaming count:** As each $c$ appears, add the number of occurrences seen so far; this also derives the triangular total in $O(N)$ time and $O(1)$ space.
- **No occurrence of $c$:** $q=0$ and the formula returns zero.
- **One occurrence:** Only its length-one substring counts, returning one.
- **Every character equals $c$:** Every substring qualifies and the formula returns total substring count.
- **Interior copies of $c$:** They create additional endpoint choices but do not invalidate larger ranges.
- **Identical substring text at different positions:** Both occurrences count through distinct endpoints.
- **Integer division:** $q(q-1)$ is always even, so `//2` is exact.
- **Character length:** The contract supplies one lowercase character `c`; longer strings would change the meaning of `s.count`.
- **Endpoint order is automatic:** For two selected occurrences, the smaller index must be the start and larger index the end, so each unordered pair yields exactly one substring rather than two.
- **Length-one ranges use one occurrence:** They are not included in $\binom q2$, which is why the separate $q$ term is necessary.
- **Closed-form alternative:** The expression can simplify to `cnt * (cnt + 1) // 2`. The source's form mirrors the two endpoint cases more explicitly.
- **Overlapping substrings:** They are independent endpoint choices and all count; no disjointness requirement exists.
- **Whole string:** It qualifies whenever both the first and final characters equal `c`, corresponding to that endpoint pair.
- **Middle characters unrestricted:** They may include any number of additional `c` occurrences, and the larger substring still counts once for its chosen outer endpoints.
- **Counting built-in:** `str.count` with a one-character argument counts every occurrence, including adjacent ones.
- **Maximum result:** With $q=N=10^5$, the answer is $5{,}000{,}050{,}000$, demonstrating why a 64-bit or arbitrary-precision result is needed.
- **No answer reconstruction:** Only the total is requested, so storing endpoint positions would be unnecessary.
- **Combinatorial partition is exhaustive:** Every valid range has either equal endpoint indices or distinct endpoint indices; the $q$ and combination terms cover these disjoint cases.
- **No double counting between cases:** Length-one substrings cannot arise from choosing two occurrences, while every longer valid substring has two distinct endpoint occurrences.
- **Linear lower bound:** Any solution must at least inspect the string to know how many target characters occur, so the $O(N)$ scan is asymptotically optimal.
- **Character not present:** The arithmetic remains well-defined because both terms vanish when `cnt=0`.
