## General

For a fixed choice of `k`, every array value has a fixed contribution sign:

$$
a_i(k)=
\begin{cases}
\texttt{nums}[i], & k\mid\texttt{nums}[i],\\
-\texttt{nums}[i], & k\nmid\texttt{nums}[i].
\end{cases}
$$

For a chosen range `[l,r]`, Alice's score minus Bob's score is exactly:

$$
\sum_{i=l}^{r}a_i(k).
$$

Thus, after `k` is fixed, the best range is the maximum-sum nonempty subarray of this signed sequence. Kadane's algorithm finds that value in linear time.

The remaining challenge is that `k` may be any integer greater than one. The source proves implicitly through its candidate construction that only prime factors occurring in the input, plus `2`, need to be tested.

**Why a composite `k` never wins the smallest-value tie-break**

Suppose composite `k` divides at least one array value. Let `p` be any prime factor of `k`. Then:

$$
k\mid x\implies p\mid x.
$$

Moving from `k` to `p` has this pointwise effect on the signed sequence:

- every value positive under `k` remains positive under `p`;
- some values negative under `k` may become positive under `p`;
- no positive contribution becomes negative.

Since all `nums[i]` are positive:

$$
a_i(p)\ge a_i(k)
$$

for every index. Therefore every fixed subarray has score at least as large under `p` as under `k`, and so:

$$
\operatorname{bestDifference}(p)
\ge
\operatorname{bestDifference}(k).
$$

If the inequality is strict, composite `k` does not achieve the global maximum. If it is an equality, `p<k` gives the same maximum with a smaller choice, so `k` loses the tie-break.

Consequently, the smallest maximizing `k` can be prime whenever it divides some input value.

**Why candidate `2` covers divisors of no value**

An integer `k` that divides none of the input values makes every signed contribution negative. Its best range is the single or multi-element negative subarray with greatest sum, normally the least-magnitude individual value because all magnitudes are positive.

The smallest permitted integer is two. If two also divides no value, it produces exactly this all-negative behavior and is the smallest representative. If two divides some values, changing their signs to positive can only improve the maximum subarray score.

Therefore no absent divisor can beat candidate two, and `2` must be included even when it is not a prime factor of any input value.

**Extracting distinct prime factors**

The source starts:

```python
candidates = {2}
```

It factors each distinct input value. Processing `set(nums)` avoids factoring duplicate values repeatedly.

For current `value`, trial factor `factor` begins at two. When it divides:

1. add `factor` to the candidate set;
2. divide out every copy of that factor.

Removing all copies ensures that later trial divisors operate on the remaining cofactor and that each prime factor is added only once per number.

The loop continues while `factor * factor <= value`. If a residual `value>1` remains afterward, that residual is prime and is also added.

Although `factor` increments through composite integers too, a composite cannot first divide the reduced value after all its smaller prime factors have been removed. Every added factor is therefore prime.

The outer candidate set automatically removes factors shared by several array values.

**Kadane's algorithm for one candidate**

For a selected `k`, the first value initializes both:

- `current`: maximum signed sum of a nonempty subarray ending at the current index;
- `maximum`: maximum signed sum over all subarrays seen so far.

For each later input `value`, the source forms its positive or negative `signed` contribution. A best subarray ending here either:

- begins at the current value, giving `signed`;
- extends the previous ending subarray, giving `current+signed`.

Therefore:

```python
current = max(signed, current + signed)
maximum = max(maximum, current)
```

Initialization from the first signed value, rather than zero, enforces a nonempty chosen range. If every contribution is negative, Kadane returns the least negative legal subarray instead of an invalid empty range of score zero.

**Choosing the smallest `k` among ties**

The source iterates:

```python
for k in sorted(candidates):
```

and replaces the global choice only when:

```python
maximum > best_difference
```

Candidates arrive from smallest to largest. On an equal score, no update occurs, so the earlier and smaller `k` remains selected.

This implements the tie-break without a separate equality comparison.

**Negative best differences**

The maximum difference can be negative because Alice must choose a nonempty range. The source retains that negative value and multiplies it by `best_k` before applying modulo:

```python
best_difference * best_k % 1_000_000_007
```

Python's modulo operation returns the standard nonnegative residue. For example, `-2\bmod(10^9+7)=10^9+5`.

**Why every relevant `k` is covered**

Take the smallest `k` attaining the global best difference.

- If it divides some input value and is composite, a smaller prime factor does at least as well, contradicting either optimality or smallestness.
- If it divides some input value and is prime, it appears in that value's factorization.
- If it divides no input value, candidate two does at least as well and is no larger.

Hence the candidate set contains the required choice.

## Complexity detail

Let:

- `n` be the array length;
- `U` be the number of distinct input values;
- `M=\max(nums)`;
- `P` be the number of distinct candidate primes, including forced candidate two.

Trial division takes `O(\sqrt M)` iterations per distinct value in the worst case, giving `O(U\sqrt M)` factorization time. Creating `set(nums)` costs expected `O(n)` time.

Sorting candidates costs `O(P\log P)`. Kadane scans all `n` values for each candidate, costing `O(nP)`. Total time is:

$$
O\left(n+U\sqrt M+P\log P+nP\right),
$$

usually written as the manifest's:

$$
O\left(U\sqrt M+P\log P+nP\right),
$$

because `P\ge1` makes `nP` cover `n`.

The candidate set and sorted candidate list use `O(P)` storage. However, the exact expression `set(nums)` also materializes up to `U` distinct values during factorization. A source-literal peak auxiliary-space bound is:

$$
O(U+P),
$$

not merely the manifest's `O(P)` unless `U` is treated as bounded by or folded into that measure. Kadane itself uses constant additional state.

The source does not modify `nums`.

## Alternatives and edge cases

- **Try every `k` through `M`:** This can require up to `10^6` Kadane scans. Prime-factor dominance reduces the candidates drastically.

- **Try every divisor, including composites:** Composite candidates cannot beat their prime factors and cannot win an equal-score smallest-`k` tie.

- **Use total signed sum instead of Kadane:** Alice chooses any nonempty subarray, not necessarily the whole array. Negative regions may need to be excluded.

- **Allow an empty range:** A zero score would incorrectly beat all-negative legal ranges. Kadane is initialized from the first element to enforce nonemptiness.

- **Factor every duplicate separately:** Duplicate values have identical prime factors. `set(nums)` avoids repeated factorization, at the cost of `O(U)` temporary storage.

- **Forget candidate two:** If no input value supplies factor two—or if no divisor behavior is beneficial—the smallest permitted absent divisor still needs representation.

- **Prime candidate divides no input:** Such a candidate produces the all-negative sequence. Candidate two is never worse and is smaller.

- **All values divisible by two:** The full array has all-positive signed contributions for `k=2`, so its sum is a strong candidate and often optimal.

- **One input value:** For any prime factor of the value, the difference is positive `nums[0]`; the smallest such factor wins. If the value is one, every `k` gives `-1` and two wins.

- **Repeated prime factors:** A value such as `12=2^2\cdot3` adds candidates two and three only once.

- **Residual prime factor:** After smaller factors are removed, a remaining value above one must be included; otherwise large prime factors would be missed.

- **Score ties:** Sorted iteration plus strict improvement preserves the smallest candidate.

- **Negative modulo:** Python converts a negative product to its nonnegative residue automatically.

- **Space-manifest qualification:** The candidate set is `O(P)`, but the exact temporary `set(nums)` may contain `U` values and must be counted in a faithful peak-space analysis.
