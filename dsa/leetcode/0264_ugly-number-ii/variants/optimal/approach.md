## General

Every ugly number has the form

$$
2^a3^b5^c
$$

for nonnegative exponents $a$, $b$, and $c$. Therefore, multiplying any known ugly number by `2`, `3`, or `5` produces another ugly number. The exact solution uses this closure property to generate candidates instead of testing ordinary integers one by one.

The candidates are kept in a min-heap `h`. A min-heap always removes the smallest stored value, so repeated pops enumerate generated ugly numbers in increasing order. The set `vis` records every value that has already been inserted, preventing the same number from entering the heap along multiple multiplication paths.

**Begin with one**

`1` is the first ugly number because it has no prime factors outside the allowed set; equivalently, it is $2^0 3^0 5^0$. The heap and set both begin with `1`.

On each of exactly `n` iterations:

1. pop the smallest candidate into `ans`;
2. generate `ans * 2`, `ans * 3`, and `ans * 5`;
3. insert each product only if it is not already in `vis`.

After the first iteration, `ans` is the first ugly number. After the second, it is the second, and so on. The value popped on iteration `n` is returned.

**Why duplicate suppression is necessary**

Many ugly numbers have more than one generating path. For example,

$$
6=2\cdot3=3\cdot2,
$$

and

$$
30=5\cdot6=3\cdot10=2\cdot15.
$$

Without `vis`, all of these paths could push the same value. The heap would then pop duplicates, and counting pops would no longer correspond to one-based positions in the distinct ugly-number sequence.

The source adds `nxt` to `vis` at the same time it pushes it, not when it is later popped. This early marking ensures a second generating path cannot insert another copy while the first copy is still waiting in the heap.

**Trace of the beginning of the sequence**

Start with heap `[1]` and seen set `{1}`.

- Pop `1`; push `2`, `3`, and `5`.
- Pop `2`; generate `4`, `6`, and `10`, all new.
- Pop `3`; generate `6`, `9`, and `15`. `6` is already seen, so only `9` and `15` are pushed.
- Pop `4`; generate `8`, `12`, and `20`.
- Pop `5`; products include `10` and `15`, already seen, plus new `25`.
- Pop `6`; continue similarly.

The first ten popped values are

```text
1, 2, 3, 4, 5, 6, 8, 9, 10, 12
```

so the tenth returned value is `12`.

For `n = 1`, the loop runs once, pops `1`, generates future candidates, and returns the popped `1`. The extra candidates are harmless even though the method will not use them.

**Why every popped value is ugly**

The initial value `1` is ugly. Every later inserted value is a previously popped ugly number multiplied by one of the only allowed primes. Multiplication adds one to the exponent of `2`, `3`, or `5` and cannot introduce any forbidden prime. By induction, every heap entry and every popped result is ugly.

**Why no ugly number is missed**

Take any ugly number $u>1$. At least one of its exponents is positive, so it is divisible by one of `2`, `3`, or `5`. Dividing by that prime gives a smaller ugly number $v$. Because $v<u$, best-first generation pops $v$ before it could need to pop $u$. When $v$ is popped, the algorithm generates $u=v\cdot p$ and inserts it unless another path already inserted it. Thus every ugly number eventually appears in the heap.

**Why heap order gives the exact sequence**

Immediately before a pop, the heap contains generated but not yet processed ugly numbers. Suppose there were a smaller unpopped ugly number missing from the heap. Its smaller ugly predecessor would already have been popped, which would have generated it, contradicting its absence. Therefore, the heap minimum is the smallest ugly number not yet returned. Removing one unique minimum per iteration enumerates the sequence in strictly increasing order.

The set is needed only for uniqueness, while the heap is needed only for ordering. Together they implement a best-first traversal of the infinite multiplication graph without exploring non-ugly integers.

## Complexity detail

After each pop, at most three new distinct values are inserted. After `n` iterations, `vis` therefore contains at most `1 + 3n` values, and the heap contains $O(n)$ pending values after subtracting the `n` popped ones.

Each heap pop or push costs $O(\log n)$ at this size. There are `n` pops and at most `3n` pushes, so total time is $O(n\log n)$. Expected set membership and insertion are $O(1)$ each and do not dominate.

The heap and seen set each hold $O(n)$ integers, giving $O(n)$ auxiliary space.

These are the bounds of the exact protected source. The manifest describes the different three-pointer dynamic-programming merge, which achieves $O(n)$ time and $O(n)$ space. The heap implementation remains correct but should not be credited with the manifest's linear running time.

## Alternatives and edge cases

- **Three-pointer dynamic programming:** Store generated ugly numbers and maintain the next unused multiples of `2`, `3`, and `5`. Advancing every pointer tied for the minimum avoids duplicates and produces $O(n)$ time. This is the algorithm summarized by the manifest, not the exact source.
- **Ordered set:** Repeatedly remove the minimum and insert its three products. It expresses the same best-first search, but Python's ordinary set cannot remove the minimum efficiently; the heap-plus-set combination separates those responsibilities.
- **Test every positive integer:** Repeatedly classify integers until `n` ugly values are found. It spends most work on numbers that are not ugly and scales poorly.
- **Duplicate product:** `vis` prevents values such as `6` from being inserted once from `2` and again from `3`.
- **`n = 1`:** The first pop is `1`, correctly treating the empty prime factorization as ugly.
- **Ties among generated products:** The set collapses them before heap insertion, so the heap contains one copy and the sequence stays distinct.
- **Large products:** Python integers grow as needed, so multiplication does not overflow. The constrained requested index remains manageable.
- **Heap never becomes empty:** Popping any ugly number generates larger ugly products. At least one is new, so candidates remain available for the next iteration.
- **Return order:** Only one integer is returned. Internal generation order among multipliers does not affect the min-heap's sorted pop order.
- **Nonpositive `n`:** The contract guarantees `n >= 1`. A zero iteration count would leave `ans` at its initial value, but that case has no defined one-based answer and should be rejected by a broader API.
