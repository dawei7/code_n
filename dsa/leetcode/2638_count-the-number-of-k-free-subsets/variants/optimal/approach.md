## General

Two values can conflict only when their difference is exactly `k`. Such values have the same remainder modulo `k`, so partitioning `nums` by `value % k` separates the conflict graph into independent groups. Choices made in different groups never invalidate one another, which means their valid-subset counts can be multiplied.

**Each remainder group is a collection of paths**

Sort the values inside one remainder group. A value can conflict only with the immediately preceding sorted value, and only when their difference is `k`. If the gap is larger than `k`, no value before that gap can conflict with the current value or with any later value. Thus each group consists of one or more path components separated by larger gaps.

**Count selections with two states**

While scanning a sorted group, maintain `skip`, the number of valid selections that omit the previous value, and `take`, the number that include it. Initially the empty prefix has `skip = 1` and `take = 0`.

If the current value differs from the previous value by `k`, including it is possible only after a selection counted by the old `skip`. Omitting it allows either old state. The transition is therefore `new_take = skip` and `new_skip = skip + take`.

For a larger gap, the current value conflicts with nothing already processed. Every prior selection can either include or omit it, so both new states equal `skip + take`. These transitions count every valid selection exactly once according to whether it contains the current value, and they never admit a forbidden adjacent pair. The group contributes `skip + take` after its final value. Multiplying all group totals is valid because the groups have no cross-conflicts; the product also includes the globally empty subset.

## Complexity detail

Let $n$ be the length of `nums`. Building the remainder groups takes $O(n)$ time. Sorting all groups takes at most $O(n \log n)$ time in total, and the dynamic-programming scans take $O(n)$ time. The groups store all $n$ values, so space is $O(n)$.

## Alternatives and edge cases

- **Backtracking over every subset:** It directly tests or prevents forbidden pairs, but it can explore $2^n$ selections and is infeasible for $n = 50$.
- **Global sort plus a value map:** A dynamic program can track predecessor values through hash maps, but remainder groups make the independent path structure and multiplicative counting explicit.
- **Bounded-value counting array:** Because values are at most $1000$, scanning a presence array can avoid comparison sorting; it trades the clean $n$-based bound for dependence on the numeric universe.
- **Empty subset:** It is represented by the initial `skip = 1` state and must remain in the final count.
- **No conflicts:** Every value independently doubles the count, producing $2^n$ valid subsets.
- **Consecutive chain:** For values spaced exactly `k` apart, the transitions count independent sets of a path and follow the Fibonacci recurrence.
- **Gap larger than `k`:** It starts an independent component even when both values share the same remainder.
- **Distinct values:** The contract excludes duplicates, so no multiplicity factor is needed for equal values.
