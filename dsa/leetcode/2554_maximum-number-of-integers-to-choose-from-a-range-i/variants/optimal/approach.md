## General

For any fixed number of picks, the smallest available integers have the least possible sum. Therefore, if some valid selection of $k$ values fits the budget, the first $k$ allowed values in ascending order also fit. This exchange argument turns the maximum-count objective into a direct greedy scan.

Put every value from `banned` in a set so duplicates collapse and membership checks take expected constant time. Visit the integers from $1$ through $n$. Skip a value when it is forbidden; otherwise, add it when it still fits and increase the count.

When the next allowed value would exceed `maxSum`, stop. Every later candidate is at least as large, so none can fit the remaining budget either. The values already selected are the cheapest possible selection of that size, and no larger valid selection can exist.

## Complexity detail

Let $m$ be the length of `banned`. Building the set takes expected $O(m)$ time, and scanning at most $n$ candidates takes expected $O(n)$ time, for $O(n+m)$ overall. The forbidden-value set uses $O(m)$ space. Duplicate and out-of-range banned values may reduce its actual size but do not worsen the bound.

## Alternatives and edge cases

- **Linear search in `banned`:** Checking membership directly in the list preserves correctness but can take $O(nm)$ time when each scan traverses most of the list.
- **Sort and coordinate the bans:** Sorting unique forbidden values can support a coordinated scan, but it costs $O(m \log m)$ time and is unnecessary for this bounded range.
- **Duplicate banned values:** Converting the list to a set ensures repeated restrictions do not change behavior or lookup cost.
- **Out-of-range bans:** A forbidden value greater than $n$ never matches a candidate and may safely remain in the set.
- **Immediate budget exhaustion:** If the smallest allowed value exceeds `maxSum`, the correct count is zero.
