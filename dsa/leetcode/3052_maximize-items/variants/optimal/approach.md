## General

**Treat each item type as a complete repeatable batch.** The intended warehouse model stocks whole copies of every item in a category together. For `prime_eligible`, one complete batch has total footprint

$$
S_p=\sum \texttt{square\_footage}
$$

over prime rows and contains $C_p$ items. The CTE `T` computes `s = S_p`.

The number of whole prime batches fitting in 500,000 square feet is

$$
q_p=\left\lfloor\frac{500000}{S_p}\right\rfloor.
$$

The first branch returns `COUNT(1) * FLOOR(500000 / s)`, which is $C_pq_p$ prime items.

**Use only the remainder for non-prime batches.** After filling prime batches, remaining area is

$$
500000\bmod S_p.
$$

For non-prime rows, the query computes their complete-batch footprint $S_n$ with `SUM(square_footage)` and item count $C_n$ with `COUNT(1)`. It then returns

$$
C_n\left\lfloor\frac{500000\bmod S_p}{S_n}\right\rfloor.
$$

This respects the priority rule: maximize complete prime batches first, then spend only the exact leftover capacity on complete non-prime batches.

**Understand the singleton CTE join.** `T` contains one aggregate row. Combining `Inventory` with `T` makes its `s` value available to each aggregate branch. Each `WHERE` clause selects one item type, and aggregate functions collapse that type into one output row.

**Why multiplication gives item count.** A complete category batch contains one of every row for that item type. Repeating it $q$ times stores $q$ copies of each of $C$ distinct rows, hence $Cq$ total items.

**The zero-result wrapper.** In the non-prime branch, `COALESCE(..., 0)` turns a null aggregate calculation into zero, as required when no non-prime batch fits or its aggregate is absent. It does not round a fractional batch up; `FLOOR` ensures only whole batches count.

**Behavioral assumptions and defects.** The exact source assumes a usable prime total. If there are no prime rows, `SUM` returns `NULL`, not zero. `IF(s = 0, 500000, 500000 % s)` does not treat null as zero, so the remaining-area expression stays null and the query can report null prime count and zero non-prime count rather than using the full warehouse for non-prime items. The local description does not state that both categories must exist.

The query also contains no final `ORDER BY`, despite the contract requiring item count descending. `UNION ALL` does not guarantee that the first branch will be returned first. Even if prime count is usually larger, SQL result order is undefined without an explicit order clause.

These are genuine limitations of the protected SQL, not properties of the batch arithmetic.

**Why `IF(s = 0, ...)` is present.** It tries to avoid remainder by zero by treating zero prime footprint as leaving all 500,000 square feet. With ordinary positive square footage and at least one prime row, `s` is positive and the remainder branch is used. It does not cover `NULL`.

## Complexity detail

Logically, the CTE scans prime rows once, and the two aggregate branches scan the table by item type. This is $O(R)$ work for $R$ inventory rows, up to constant repeated scans. Each branch produces one row, so aggregate state is $O(1)$ because there are only two fixed categories.

Actual MySQL complexity depends on indexes, CTE materialization or merging, decimal arithmetic, and optimizer choices. The two-row result itself is constant-sized.

No source table is modified.

## Alternatives and edge cases

- **Conditional aggregation in one CTE:** Compute counts and footprints for both types together, then derive both outputs. This can avoid repeated scans and handle missing categories explicitly.
- **Add final ordering:** Wrapping the union and ordering by `item_count DESC` is necessary for a guaranteed contract-compliant row order.
- **No prime rows:** The correct logic should allocate the full warehouse to non-prime batches; the exact source mishandles null `s`.
- **No non-prime rows:** `COALESCE` produces zero for that category, although denominator-null behavior should be handled deliberately.
- **Prime batch larger than warehouse:** Zero prime batches fit, and the mathematical remainder should be the full 500,000 because `500000 % s = 500000` when `s>500000`.
- **Exact prime fit:** Remainder is zero, so non-prime item count is zero.
- **Fractional batch:** `FLOOR` rejects partial sets, satisfying the whole-item-batch rule.
- **Zero footprint:** The source has a guard for `s=0`, but non-prime zero totals could still cause division issues; ordinary square footage is expected positive.
- **Required result order:** The protected query omits `ORDER BY`, so its output order is not guaranteed.
- **Priority:** Non-prime capacity is calculated only after maximum prime batches, not by comparing individual item efficiencies.
- **`UNION ALL` is semantically appropriate:** The two branches deliberately produce different fixed `item_type` labels, so duplicate elimination is unnecessary. Its lack of ordering, however, still requires a final `ORDER BY` for the contract.
- **Decimal remainder behavior:** MySQL's remainder and floor operations act on the aggregate decimal footprint. Exact whole-batch arithmetic depends on consistent numeric precision; binary floating-point conversion should be avoided.
- **Count versus category count:** `COUNT(1)` counts inventory rows in one batch, then multiplication counts stocked item copies. It does not count distinct `item_category` values, which could differ if categories repeat.
