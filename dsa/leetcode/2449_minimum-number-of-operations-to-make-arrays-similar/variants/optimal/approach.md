## General

**Parity can never change**

Every operation adds 2 to one element and subtracts 2 from another. Adding or subtracting an even number preserves parity. Therefore an odd value in `nums` can only become an odd target value, and an even value can only become an even target value.

The feasibility guarantee implies that `nums` and `target` contain the same number of odd elements and the same number of even elements. Otherwise no sequence of operations could make their multisets equal.

The sorting key `(x & 1, x)` groups even values first because their parity key is zero, odd values second because it is one, and sorts numerically inside each group. Applying the same key to both arrays aligns only parity-compatible values.

**Why sorted matching is optimal**

Within one parity group, suppose source values $a\le b$ are matched to target values $y\le x$ in crossed order, so $a$ goes to $x$ and $b$ goes to $y$. Replacing those assignments with ordered matches cannot increase total absolute distance:

$$
\lvert a-y\rvert+\lvert b-x\rvert
\le
\lvert a-x\rvert+\lvert b-y\rvert.
$$

This is the standard uncrossing property on a number line. Repeatedly removing crossed assignments yields the sorted-to-sorted pairing with minimum total absolute difference.

Because parity group sizes match, zipping the two fully parity-key-sorted arrays pairs every even source with the corresponding even target and every odd source with the corresponding odd target.

**Convert total discrepancy into operation count**

For an aligned pair `a,b`, `abs(a-b)` is even because they have the same parity. Summing all aligned absolute differences produces an $L_1$ discrepancy.

The total sums of `nums` and `target` must be equal under feasibility, because each operation increases one value by 2 and decreases another by 2, preserving the overall sum. Therefore total positive discrepancy equals total negative discrepancy in magnitude, and each is half of the absolute-difference sum.

One operation transfers two units from an element that must decrease to an element that must increase. It reduces the positive deficit by 2 and the negative surplus magnitude by 2, decreasing the total absolute discrepancy by 4. Consequently,

$$
\text{minimum operations}
=
\frac{\sum_i\lvert a_i-b_i\rvert}{4}.
$$

That is exactly the source's final `// 4`.

**Trace the first example**

For `nums=[8,12,6]` and `target=[2,14,10]`, all values are even. Sorting gives sources `[6,8,12]` and targets `[2,10,14]`. Absolute differences are 4, 2, and 2, totaling 8. Dividing by four gives two operations.

The pairing does not prescribe the exact index choices, because similarity cares only about frequencies. It establishes how much value must flow between the multiset elements. Feasibility guarantees that surplus and deficit transfers can be paired into legal distinct-index operations.

For `nums=[1,2,5]` and `target=[4,1,3]`, parity sorting gives `[2,1,5]` and `[4,1,3]`. Differences total 4, so one operation is sufficient.

**Why the result is a lower bound and achievable**

Any transformation induces a parity-compatible matching from original occurrences to target occurrences. Sorted matching minimizes the total absolute distance among all such matchings, so no solution can require less total movement.

Each operation supplies two upward units to one matched deficit and removes two units from one matched surplus. The equal-sum property means these needs balance. Repeatedly pair any remaining deficit with any remaining surplus and perform the operation; both values stay within their parity class and eventually reach their matched targets. This uses exactly one operation per four units of total absolute discrepancy.

Thus the computed quotient is both unavoidable and attainable.

**The exact source mutates both inputs**

`nums.sort(...)` and `target.sort(...)` reorder the lists in place. This does not affect correctness because the method needs only their multisets, but callers will observe the reordered arrays after the call. An implementation wishing to preserve inputs should use `sorted` to create copies.

## Complexity detail

Sorting each length-$n$ array takes $O(n\log n)$ time. The zip-and-sum expression performs one constant-time difference per pair, adding $O(n)$ work. Total time is $O(n\log n)$.

Python's list sort uses $O(n)$ temporary space in the worst case. The final generator is lazy and uses $O(1)$ additional iteration state. Thus the implementation's auxiliary space is $O(n)$, matching the manifest's safe bound.

The difference sum can be large, up to roughly $n\cdot10^6$. Python handles it; fixed-width languages should use 64-bit accumulation.

## Alternatives and edge cases

- **Separate explicit odd and even lists:** Filter each array into two groups, sort each group, and compare corresponding entries. This makes the parity invariant visible but allocates additional lists.
- **Frequency balancing over the bounded value domain:** Count occurrences and route surplus values to deficits of the same parity. It can avoid comparison sorting with a large count array but is more involved.
- **Match without parity separation:** An odd value can never reach an even target using steps of two, so arbitrary sorted pairing can be invalid.
- **Already similar arrays:** Sorted sequences are identical, the discrepancy is zero, and the method returns zero.
- **Duplicate values:** Occurrences are matched by sorted position; duplicates require no special handling.
- **One element:** Feasibility forces the same value because sum and parity are preserved, so zero operations result.
- **Equal total sum:** It is an invariant of every operation and is essential for dividing balanced absolute discrepancy by four.
- **Why not divide by two:** One operation changes two aligned discrepancies by two each, reducing the total absolute sum by four.
- **Distinct indices:** A surplus and deficit belong to different current occurrences whenever a transfer remains necessary; an element cannot simultaneously need to increase and decrease.
- **Input mutation:** In-place sorting changes caller-visible order even though similarity ignores order.
