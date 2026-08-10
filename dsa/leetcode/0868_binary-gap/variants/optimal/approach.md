## General

The binary gap concerns consecutive set bits, not every possible pair of set bits. A set bit is a binary digit equal to `1`. Two such bits are adjacent for this problem when no other `1` lies between them, even though any number of `0` digits may lie between them. Therefore, while scanning the binary representation, the only history needed for a newly encountered `1` is the position of the previous `1`.

The solution reads bits from right to left, beginning with the least significant bit. The variable `cur` is the position of the bit currently being examined: position zero for the rightmost bit, position one for the next bit, and so on. The test `n & 1` is nonzero exactly when the current least significant bit is `1`. After processing that bit, `n >>= 1` discards it and shifts the next bit into the least significant position. Incrementing `cur` keeps the position synchronized with that shift.

**The two pieces of state.** The variable `pre` stores the original position of the most recently encountered `1`. The variable `ans` stores the largest distance between consecutive `1` bits found so far. When the current bit is `1`, the distance from the preceding set bit is `cur - pre`. The update

```text
ans = max(ans, cur - pre)
pre = cur
```

first considers that new adjacent pair, then makes the current position the predecessor for the next set bit.

The order is essential. If `pre` were changed before calculating the distance, the subtraction would always use the current position twice and produce zero. If `pre` were not changed afterward, a later set bit could be compared with an older, non-adjacent `1` and could produce an invalid gap.

**How the first set bit is handled without a branch.** Before any `1` has been seen, there is no valid previous position. The implementation initializes `pre` to positive infinity. At the first set bit, `cur - pre` is negative infinity, so `max(ans, cur - pre)` leaves the initial answer zero unchanged. The current position is then stored in `pre`. Every later set bit has a finite predecessor and yields a genuine candidate distance.

This sentinel is a compact substitute for a boolean such as “have we seen a one?” It is safe because valid distances are positive, while the sentinel calculation is smaller than the initial answer. It also explains why a number with exactly one set bit returns zero: the only attempted comparison is the harmless sentinel comparison.

**Why checking only the previous set bit is sufficient.** Suppose the set-bit positions, in the order encountered, are $p_0 < p_1 < \dots < p_k$. The adjacent pairs defined by the problem are exactly $(p_0,p_1)$, $(p_1,p_2)$, and so forth. When the scan reaches $p_i$, `pre` equals $p_{i-1}$ because it was replaced at the preceding set bit and remained unchanged across any intervening zeros. Thus the solution considers $p_i-p_{i-1}$ exactly once. It never considers a nonconsecutive pair because `pre` never skips over the latest set bit.

For `n = 22`, the binary representation is `10110`. Scanning from the right sees positions zero through four:

- Position zero is `0`, so no state changes except `cur`.
- Position one is `1`. It becomes the first recorded set bit.
- Position two is `1`. The candidate distance is $2-1=1$.
- Position three is `0`. The previous set-bit position remains two.
- Position four is `1`. The candidate distance is $4-2=2$, which becomes the answer.

Although the scan direction is opposite the usual written direction, distances are absolute differences between positions, and the set-bit positions are still visited in increasing numerical order. Therefore right-to-left scanning changes neither which pairs are adjacent nor their distances.

The loop ends when repeated shifts reduce `n` to zero. At that moment every bit up to and including the most significant `1` has been processed. Leading zeros are not part of a positive integer's binary representation and cannot form a pair, so no further work is needed.

## Complexity detail

Let $b = \lfloor\log_2 n\rfloor+1$ be the number of bits in the positive integer `n`. Each loop iteration examines one bit, performs constant-time arithmetic and bit operations, and shifts the number once.

- **Time complexity:** $O(b)$, equivalently $O(\log n)$.
- **Space complexity:** $O(1)$. Only `ans`, `pre`, `cur`, and the progressively shifted integer are stored, regardless of the number of bits.

The solution mutates its local parameter `n` by shifting it, but this does not alter any caller-owned mutable object because Python integers are immutable. No binary string or list of set-bit indices is created.

## Alternatives and edge cases

- **Store all set-bit positions:** First collect every position containing `1`, then compare neighboring positions in the list. This is correct and still takes $O(\log n)$ time, but it uses $O(\log n)$ space that the one-pass state makes unnecessary.
- **Convert to a binary string:** Scanning `bin(n)` can be visually intuitive. It also takes $O(\log n)$ time, but creates an $O(\log n)$ string and requires careful treatment of indices or counts between ones.
- **Count zeros between ones:** One can reset a counter whenever a `1` appears and translate a run of zeros into a distance by adding one. This is equivalent, but tracking absolute bit positions makes the definition of distance more direct.
- **Compare every pair of ones:** This does extra work and, more importantly, includes pairs that are not adjacent because another `1` may separate them. Only consecutive set bits are valid candidates.
- **Exactly one set bit:** Powers of two such as `8 = 1000` contain no pair. The infinity sentinel ensures the answer remains zero.
- **Adjacent literal ones:** A suffix such as `11` gives a distance of one. No separating zero is required for two set bits to be adjacent under the definition.
- **Long zero run:** For `100001`, the two ones are still adjacent because there is no intervening one, and their positional difference is five.
- **Three or more ones:** Only neighboring ones in positional order are compared. For `10101`, the outer ones are not a valid pair because the middle one separates them.
- **Least significant bit set:** If the rightmost bit is `1`, it is simply recorded at position zero; no special indexing adjustment is needed.
- **Maximum allowed value:** The constraint $n \le 10^9$ means at most 30 relevant bits, but the loop is written generically and naturally stops after the actual most significant set bit.
