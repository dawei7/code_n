## General

The array may contain up to $10^5$ elements, but every value is between one and 100. The exact solution exploits that small value domain:

1. count how many times each distinct value occurs;
2. enumerate every ordered triple of distinct-value keys, allowing keys themselves to repeat;
3. test whether the value sum is divisible by exactly one of the three positions;
4. convert the value pattern into the number of ordered triples of distinct indices.

The loops enumerate ordered value triples, not sorted value triples as the manifest summary says. This directly matches the problem examples, which count all six index permutations of three distinct positions.

**Compress positions into multiplicities**

`cnt = Counter(nums)` maps value `a` to occurrence count `x`.

Once a value triple `(a, b, c)` is chosen, the exact identities of indices matter only through how many choices exist for each position. The Counter avoids iterating over the much larger index array three times.

Let $U$ be the number of distinct values. Under the constraint, $U\le100$ even when $n$ is very large.

**Enumerate ordered value assignments**

The three nested loops independently iterate over `cnt.items()`. They choose:

- first-position value `a` with count `x`;
- second-position value `b` with count `y`;
- third-position value `c` with count `z`.

Because the loops are independent, `(4,3,2)` and `(3,4,2)` are separate iterations. They represent different ordered assignments to `(i,j,k)`.

Keys may also be equal. A value triple `(2,2,1)` represents two distinct array indices holding two and a third index holding one.

**Count how many of the three values divide the sum**

The candidate sum is `s = a + b + c`.

For each positional value `v` in `(a, b, c)`, predicate `s % v == 0` says whether that member divides the sum. Python booleans sum as ones and zeros.

The condition

`sum(s % v == 0 for v in (a, b, c)) == 1`

therefore accepts exactly when one positional member divides the sum.

Positional wording matters when values repeat. If `a == b` and that value divides the sum, both first and second members count as divisors, producing at least two and failing the single-divisor condition. This agrees with the definition, which refers to the three selected array entries.

**Convert all-distinct values into index choices**

If `a`, `b`, and `c` are all different, any occurrence of `a` can serve as `i`, any occurrence of `b` as `j`, and any occurrence of `c` as `k`.

The number of ordered distinct-index triples for this exact value assignment is

$$
xyz.
$$

Distinct values guarantee the selected indices are automatically distinct.

**Handle one repeated value**

If `a == b`, the first index has `x` choices and the second has only `x - 1` remaining choices of that value. The third value differs in any accepted repeated case and has `z` choices. Contribution is `x(x-1)z`.

The `a == c` case similarly contributes `x(x-1)y`, and `b == c` contributes `xy(y-1)`.

The conditional branches are ordered, so an all-equal triple enters the first equality branch. However, such a triple can never pass the divisor test: its sum is `3a` and all three positional values divide it, giving divisor count three rather than one. No missing `x - 2` factor can affect an accepted candidate.

**Why no factor of six is added**

For three different values, the nested loops separately visit all six value orders. Each order counts indices assigned to those exact ordered positions.

Multiplying an all-distinct contribution by six would count every ordered index triple six times. The enumeration already provides the permutations requested by the examples.

**Why the result is exact**

Take any ordered triple of distinct indices. Its three values determine exactly one iteration of the nested loops. If it is a single divisor triplet, that iteration passes the test, and the appropriate multiplicity formula includes this exact index choice.

Conversely, every counted multiplicity selects distinct indices with the loop's values, and the divisibility predicate has verified exactly one divisor. Each ordered index triple belongs to one value assignment and is counted once.

For values `[4,3,2]`, sum nine is divisible only by three. Every one of the six ordered arrangements appears in a different loop order and contributes the corresponding index choices.

## Complexity detail

Building the Counter takes $O(n)$ time. The three nested loops examine $U^3$ ordered value triples, and each performs constant work over three values. Total time is $O(n+U^3)$.

The Counter stores $O(U)$ entries. Loop variables and the generator over three values use $O(1)$ additional space. Thus auxiliary space is $O(U)$.

Since $U\le100$, the cubic domain enumeration is bounded independently of $n$. The manifest complexity matches, though its “sorted value triples” wording does not match the exact ordered loops.

## Alternatives and edge cases

- **Enumerate index triples:** Directly trying $n^3$ ordered indices is impossible for $n=10^5$.
- **Enumerate sorted value triples:** One can visit each multiset once and multiply by positional permutations carefully. It reduces constant work but makes repeated-value permutation factors more complex.
- **Precompute divisibility for values:** With only 100 values, candidate-sum divisibility could be tabled, though the constant three modulus checks are already small.
- **All three values equal:** The sum is divisible by all three positional entries, so the triple never qualifies.
- **Exactly two equal values:** If their common value divides the sum, it counts twice and cannot be the sole divisor; qualification may occur only through the distinct value.
- **Value one:** One always divides the sum, but another selected value might also divide it, so the triplet is not automatically valid.
- **Insufficient multiplicity:** Factors such as `x * (x - 1)` become zero when two distinct indices of that value do not exist.
- **Ordered output count:** Permutations of the same three indices count separately, as demonstrated by the examples.
- **Positive values:** Modulo never uses zero as a divisor.
- **Bounded domain:** At most 100 Counter keys keep $U^3$ practical.
- **Input preservation:** The source array is only read.
- **Manifest wording:** The exact source enumerates ordered key triples and therefore needs no later permutation multiplier.
