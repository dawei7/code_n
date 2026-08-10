## General

**The API both answers and changes the hidden state.** The initial hidden number uses exactly 30 relevant bit positions, numbered 0 through 29. A call `commonBits(num)` first counts positions where the current hidden number and `num` agree, then replaces the hidden number by its XOR with `num`. The required return value is the number before any calls, so the algorithm must learn bits while controlling those mutations.

**Ask the same one-bit question twice.** For a legal bit position $i$, let:

$$
q=1\ll i.
$$

This query has a one only at position $i$ and zeros in every other one of the 30 positions. The exact source calls `commonBits(q)` twice, storing the two results as `count1` and `count2`.

The first call toggles hidden bit $i$ because XOR with one flips that bit. All other hidden bits are unchanged because the query has zeros there. The second identical call toggles bit $i$ again, restoring it to its value before the pair:

$$
(n\mathbin{\mathrm{XOR}}q)\mathbin{\mathrm{XOR}}q=n.
$$

Therefore, every pair of valid calls is self-contained. It reveals one initial bit and leaves the hidden number ready for the next bit position.

**Why comparing the two counts reveals the bit.** Contributions from all positions other than $i$ are identical in the two calls: neither the hidden bits nor the query bits at those positions change. Only position $i$ changes its match status.

If the original hidden bit is one, it agrees with the query's one during the first count. The first call then toggles it to zero, so it disagrees during the second count. Hence `count1` is exactly one larger than `count2`.

If the original hidden bit is zero, it initially disagrees with the query's one. After the first call toggles it to one, it agrees during the second count. Then `count2` is exactly one larger.

Thus:

$$
\text{initial bit }i=1
\iff
\texttt{count1}>\texttt{count2}.
$$

When that comparison is true, the source sets the bit in its local answer with `n |= 1 << i`. When false, the answer bit remains zero.

**Reconstruction does not need the absolute common-bit count.** The two results may include many agreements caused by zeros in the query and zeros in the hidden number. Those background matches can be difficult to reason about individually, but they cancel in the comparison. Only the one toggled position differs between observations. This difference-based measurement is the central idea.

**A simple bit example.** Suppose initial bit 5 is one. Query `1 << 5` matches at bit 5 on the first call, then XOR changes the hidden bit to zero. The identical second query no longer matches there, so the first result exceeds the second. The second XOR restores bit 5 to one. If initial bit 5 were zero, the order of match and mismatch would reverse.

**A material correctness defect in the exact source.** The problem states that every legal number lies between 0 and $2^{30}-1$, and only the first 30 bits participate. It also explicitly warns that asking with a `num` outside this range produces an unreliable output. Valid query masks are therefore `1 << i` only for $0\le i<30$.

The checked-in loop is:

`for i in range(32)`.

Its iterations for $i=30$ and $i=31$ call the API with $2^{30}$ and $2^{31}$, both outside the legal range. The API contract provides no reliable meaning for those four calls. Worse, if the unreliable comparison happens to satisfy `count1 > count2`, the source sets bit 30 or bit 31 in its returned integer, producing a result larger than $2^{30}-1$ even though the answer must be a 30-bit number.

The first 30 iterations implement a sound reconstruction and restore the hidden state after each pair. The last two iterations invalidate the overall correctness guarantee. This is a genuine source defect, not merely an alternative style or complexity mismatch. A correct implementation must use `range(30)`.

**What can and cannot be claimed about the returned value.** If an environment happens to ignore high query bits and returns counts that never make those two comparisons true, the source may still return the correct initial number. But the local contract says out-of-range query results are unreliable, so correctness cannot depend on that accidental behavior. The exact implementation is not guaranteed correct for the stated interface.

## Complexity detail

The source performs 32 loop iterations and two API calls per iteration, for exactly 64 calls. All arithmetic and bit operations are constant time on these bounded integers. Its time complexity is therefore $O(1)$ and its auxiliary space is $O(1)$.

A corrected 30-bit loop would make exactly 60 calls and have the same asymptotic bounds. Saying $O(B)$ for a generalized $B$-bit interface is also informative, but here $B=30$ is fixed by the problem, so the manifest's constant bounds are accurate.

The correctness defect does not change the complexity analysis: two extra invalid iterations are still constant work. Complexity and semantic validity are separate questions.

## Alternatives and edge cases

- **Correct two-call scan:** Replace `range(32)` with `range(30)`. This preserves the intended method and obeys the API domain.
- **One call per bit without restoration:** Mutations would accumulate and make later comparisons difficult to interpret; the paired call is what isolates and restores each bit.
- **Query all zeros first:** It can reveal the current zero-bit count, but the state mutation and per-bit recovery still require carefully planned legal calls.
- **Initial number zero:** Every valid bit comparison has `count1 < count2`, so no answer bit is set.
- **Initial number $2^{30}-1$:** Every valid bit comparison has `count1 > count2`, so bits 0 through 29 are set.
- **Bit position 29:** `1 << 29` is legal and is the highest single-bit query within the 30-bit range.
- **Bit position 30:** `1 << 30` is already outside the allowed range; this is the first defective loop iteration.
- **State restoration:** Two identical XOR operations cancel exactly, so a valid pair does not contaminate the next pair.
- **Background matches:** They contribute equally to both counts and disappear when the results are compared.
- **Strict comparison:** Equality should not occur for a reliable one-bit pair because exactly one match status flips. The source treats equality as a zero bit, but equality would signal behavior outside the proved contract.
- **No need to know the changing hidden value:** The local `n` variable is an answer accumulator, not a mirror of the API's temporary state.
- **High answer bits:** Setting bit 30 or 31 violates the required result range, even if lower bits were reconstructed correctly.
- **Unreliable does not mean safely ignored:** Once the contract disclaims an output, no proof may assume how the API handles it.
- **Fixed call budget:** The corrected method uses two calls per each of 30 bits and requires no adaptive search.
- **Source/manifest relationship:** The manifest's broad “toggle each legal position” summary describes the intended 30-bit algorithm, while the exact source actually toggles two illegal positions as well.
