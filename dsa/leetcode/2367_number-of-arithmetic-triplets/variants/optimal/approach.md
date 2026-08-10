## General

**Enumerate each possible index triplet exactly once**

The exact solution uses `combinations(nums, 3)`. This iterator selects every set of three distinct positions from `nums` while preserving their original order. If it yields values `a, b, c`, their source indices automatically satisfy `i < j < k`.

That ordering property is especially convenient here. The input is strictly increasing, so selecting later positions also guarantees:

$$
a<b<c.
$$

There is no need to separately store or compare indices, and no generated tuple can contain the same array position twice.

**Test both required gaps**

A selected triple is arithmetic with the required difference only if:

```python
b - a == diff and c - b == diff
```

Both comparisons are necessary. Checking only the total span `c - a == 2 * diff` would not force `b` to be the correct midpoint. For example, endpoints can have the proper span while the selected middle value lies elsewhere.

Python's `and` short-circuits: if the first gap is not `diff`, it does not need to evaluate the second comparison. If both are true, the expression evaluates to Boolean `True`; otherwise, it evaluates to `False`.

**Use Boolean values as counts**

In Python, `bool` is a numeric subtype: `True` contributes one and `False` contributes zero when passed to `sum`. Therefore:

```python
sum(condition for each triple)
```

counts exactly how many generated triples satisfy both arithmetic conditions. The generator expression is lazy, so it tests one triple at a time rather than first allocating a list of all Boolean results.

For `nums = [0, 1, 4, 6, 7, 10]` and `diff = 3`, the triple of values `(1, 4, 7)` contributes `True` because both gaps are three. The triple `(4, 7, 10)` also contributes `True`. Every other selected triple contributes false, so the sum is two.

**Why value triples correspond uniquely to index triples**

The question counts index triplets, while the iterator exposes values. Because `nums` is strictly increasing, every value occurs at exactly one index. Consequently, a chosen value triple identifies one and only one index triple. There is no risk that duplicate values make one tuple of values represent several index choices.

Strict increase also means any arithmetic triplet with positive `diff` appears in the order `x, x + diff, x + 2 * diff`. `combinations` generates that order automatically. It never generates permutations such as `(x + diff, x, x + 2 * diff)`, which would violate the index condition.

**Why exhaustive enumeration is correct**

Every valid arithmetic triplet consists of three distinct indices in increasing order. `combinations(nums, 3)` generates the values at that exact triple once, so no valid answer can be missed. When it is generated, the two required equalities are true, and its Boolean contributes one.

Conversely, any generated triple that contributes one comes from increasing indices and satisfies both gap equations. It meets every condition in the definition and is a valid arithmetic triplet. Each generated index selection appears only once, so none is double-counted.

The sum thus has a one-to-one correspondence with the set of valid triplets.

**Relationship to the faster value-membership insight**

The variant metadata describes recognizing the two required predecessors of an endpoint using value membership, which would be a linear-time strategy. The shipped solution shown here instead performs exhaustive three-combination enumeration. Its appeal is directness: the code mirrors the definition almost word for word and is safe under the small constraint `nums.length <= 200`.

This distinction matters when explaining both behavior and complexity. The current implementation does not construct a set, does not search for predecessors, and does not run in linear time as $n$ scales. Its result is correct, but the exact executed algorithm is the combinations-based method documented above.

At the maximum $n=200$, the number of triples is:

$$
\binom{200}{3}=1{,}313{,}400.
$$

That is far larger than $200$ but still moderate enough for simple constant-time arithmetic checks in Python in this problem's intended limits.

## Complexity detail

Let $n$ be the length of `nums`. The iterator produces:

$$
\binom{n}{3}=\frac{n(n-1)(n-2)}{6}
$$

triples. Each performs two subtractions, up to two comparisons, a Boolean conjunction, and an addition into the sum, all constant-time operations in the usual model. The exact time complexity is therefore $O\left(\binom{n}{3}\right)=O(n^3)$.

The generator and `itertools.combinations` iterator maintain only a constant number of indices and the current three-element tuple beyond references to the input. `sum` keeps one accumulator. Auxiliary space is $O(1)$, excluding the already provided input.

The manifest's $O(n)$ time and $O(n)$ space correspond to the hash-set membership alternative, not to the exact `combinations` implementation. For understanding or evaluating this source file, the cubic-time and constant-auxiliary-space bounds are the accurate operational bounds.

## Alternatives and edge cases

- **Hash-set membership:** Put all values in a set and, for each `x`, test whether `x + diff` and `x + 2 * diff` exist. Strict increase makes the index order automatic. This achieves expected $O(n)$ time and $O(n)$ space.
- **Boolean value table:** Since values lie between `0` and `200`, mark their presence in a fixed array and perform the same two lookups in $O(n+V)$ time.
- **Three pointers:** The sorted input can support pointer-based searches, but membership is simpler for this small exact-gap query.
- **Check only endpoint distance:** Testing `c - a == 2 * diff` is insufficient because the selected `b` may not be exactly one `diff` from both endpoints.
- **Exactly three elements:** The iterator produces one triple, which contributes either one or zero.
- **No matching values:** Every Boolean is false and `sum` returns zero.
- **Overlapping triplets:** Different valid triplets may share indices or values; each distinct three-index combination is still counted separately.
- **Strictly increasing guarantee:** It removes duplicates and ensures selected value order matches index order. A duplicate-containing array would require more careful value-to-index counting.
- **Positive `diff`:** Valid values increase from first to third. A zero difference would be impossible with the strictly increasing array, but the contract excludes it.
- **Maximum input length:** About 1.31 million triples are tested at $n=200$, explaining why exhaustive enumeration is feasible only because the constraint is small.
