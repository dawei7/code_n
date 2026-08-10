## General

**What the CTE actually ranks.** The window function partitions rows by `state`, so each state's ranking starts independently. Within a state, it orders `fraud_score DESC`, assigning the highest score rank 1.

`RANK` gives tied scores the same rank and leaves gaps afterward. For example, scores 100, 100, and 90 receive ranks 1, 1, and 3.

**What the outer filter actually returns.** `WHERE rk = 1` keeps only policies tied for the maximum fraud score in their state. If the maximum is unique, exactly one policy is returned for that state. If several policies share the maximum, all are returned.

The final order is correct for the rows that survive:

- `ORDER BY 2` sorts `state` ascending;
- `3 DESC` sorts `fraud_score` descending within state;
- `1` sorts `policy_id` ascending for equal scores.

**This does not generally solve the stated top-five-percent task.** A top 5% selection depends on the number of claims in each state. The exact query never computes a state count, percentile rank, or five-percent cutoff. In a state with 100 distinct fraud scores, the requested top 5% contains five policies, while `rk = 1` returns only one.

The query agrees with the examples only because each state has very few policies, making the ceiling of 5% equal to one. It also returns all maximum-score ties, but it would not include lower scores that still fall inside a larger state's top-five-percent boundary.

This is a genuine correctness defect in the protected Optimal source. The local manifest describes ranking plus state population and a ceiling-five-percent boundary, but no population calculation appears in the SQL.

**What a complete ranking criterion needs.** Let $C_s$ be the number of policies in a state. A count-based top-five-percent cutoff normally keeps the first

$$
\left\lceil0.05C_s\right\rceil
$$

positions. To include score ties at the boundary, one can compute `RANK()` and `COUNT(*) OVER (PARTITION BY state)`, then keep rows whose rank is at most that ceiling. This is the mechanism described by the manifest, not the exact source.

An alternative is `PERCENT_RANK` with an appropriate boundary, but one must define small-partition and tie semantics carefully. The count-and-rank formula makes the intended ceiling explicit.

**Why `RANK` is appropriate for ties but insufficient alone.** Ranking by score is the right first component because equal scores should be treated together if boundary ties are included. However, `rk = 1` hardcodes the boundary at the maximum rather than deriving it from partition size. The missing piece is not tie behavior; it is the percentile cutoff.

**A counterexample.** Imagine one state with policy scores 100 down through 81 for 20 distinct policies. Five percent of 20 is one, so only score 100 belongs and the source happens to be correct. Add one more policy with score 80. The ceiling of 1.05 is two, so scores 100 and 99 should be returned. The source still returns only score 100.

**No mutation occurs.** The CTE and outer query are read-only. The issue is semantic selection, not side effects or ordering.

## Complexity detail

For $R$ fraud rows, the window engine partitions and orders rows by state and descending score. A typical bound is $O(R\log R)$ time, with $O(R)$ temporary space for sorting and window state. Final ordering of the selected rows is within the same asymptotic bound.

If a suitable composite index supports the partition and ordering, the optimizer may reduce sorting work, but physical behavior is database-dependent.

Adding a partition count for the correct cutoff would remain $O(R\log R)$ time and $O(R)$ space; the defect cannot be justified as an asymptotic optimization.

## Alternatives and edge cases

- **Rank plus partition count:** Compute `RANK` and `COUNT(*) OVER (PARTITION BY state)`, then filter rank at or below `CEIL(count * 0.05)`. This matches the manifest's intended boundary and includes score ties.
- **`PERCENT_RANK`:** Filtering at or below 0.05 can express percentile position, but its denominator and small-group behavior should be checked against the exact ceiling definition.
- **`NTILE(20)`:** Selecting tile one is tempting, but tile sizing and ties may not match the required top-five-percent semantics.
- **One policy in a state:** The source returns it, and the ceiling top 5% also contains it.
- **Twenty or fewer distinct policies:** The ceiling cutoff is one, so maximum-only is correct unless tie rules expand the boundary.
- **More than twenty policies:** Lower-ranked policies can belong to the top 5%, exposing the source defect.
- **Several maximum-score ties:** `RANK=1` returns all of them. Depending on tie semantics, this may exceed the numeric 5% count but is consistent with including boundary ties.
- **Tie at a lower cutoff:** The exact query never reaches that cutoff and misses all such rows.
- **Output ordering:** The final three ordinal keys correctly implement state ascending, score descending, and policy ID ascending.
- **Manifest mismatch:** The source does not compute state population or a five-percent threshold, so its advertised summary is inaccurate.
