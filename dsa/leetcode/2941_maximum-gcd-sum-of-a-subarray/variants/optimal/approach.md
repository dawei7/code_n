## General

For a fixed right endpoint $i$, many subarrays end there, but their GCD values repeat. As the left endpoint moves left, the GCD can only stay the same or decrease to a divisor. The number of distinct suffix GCDs is therefore small.

The source maintains `f` as pairs `(j, x)` describing relevant subarrays ending at the previous position: start index $j$ and GCD $x$. It compresses equal GCD outcomes while extending them by the current value.

**Prefix sums supply each subarray sum**

`s = accumulate(nums, initial=0)` creates

$$
\texttt{s}[q]=\sum_{p=0}^{q-1}\texttt{nums}[p].
$$

The sum of inclusive subarray `nums[j..i]` is `s[i + 1] - s[j]`. This makes score evaluation constant time once start and GCD are known.

**Extend all previous suffixes**

For current value `v = nums[i]`, every previous suffix `nums[j..i-1]` with GCD $x$ becomes `nums[j..i]` with GCD

`y = gcd(x, v)`.

The source builds a new list `g`. If the most recently appended pair already has GCD $y$, it does not append another.

Previous pairs are ordered by increasing start index. When several starts collapse to the same new GCD, keeping the first retains the earliest start.

**Why the earliest start dominates for equal GCD**

All input numbers are positive. For the same right endpoint and same GCD $y$, an earlier start gives:

- a sum at least as large because it includes additional positive values;
- a length at least as large, so it satisfies the minimum-$k$ condition whenever a later start does.

Its product of sum and $y$ is therefore no smaller. Later starts with the same GCD can never be the best current candidate or a better basis for future extension. Discarding them is safe.

After processing extensions, the source sets `f = g` and appends singleton pair `(i, v)`. If that singleton happens to duplicate the preceding GCD, the current list may temporarily contain a redundant pair. It is harmless during answer evaluation, and the next extension's compression merges equal outcomes.

**Evaluate every relevant current suffix**

For each `(j, x)` in `f`, the length is `i - j + 1`. If it is at least $k$, the candidate score is

`(s[i + 1] - s[j]) * x`.

`ans` keeps the maximum across all right endpoints and compressed suffix states.

Every subarray has some right endpoint. Its GCD state is either retained directly or dominated by an earlier start with the same GCD, whose positive sum and eligibility are no worse. Hence compression cannot remove the global optimum.

**Why the state list stays small**

Distinct positive GCD values form a decreasing divisor chain as suffixes expand. Whenever a GCD changes to a smaller proper divisor, it is at most half the previous value. Thus there are $O(\log V)$ distinct values for maximum input value $V$, plus at most the temporary singleton redundancy.

This is what avoids enumerating all $O(n^2)$ subarrays.

## Complexity detail

For each of $N$ elements, the source processes $O(\log V)$ GCD states. Euclid's algorithm costs $O(\log V)$ per GCD in the usual bound, giving $O(N\log^2 V)$ time. Scanning states for candidates adds $O(N\log V)$ and is dominated.

The compressed state lists use $O(\log V)$ space, but the exact source also stores the length-$(N+1)$ prefix-sum list `s`. Actual auxiliary space is therefore $O(N)$, not the manifest's $O(\log V)$ claim.

## Alternatives and edge cases

- **Enumerate all subarrays:** Maintain a running GCD and sum for every start in $O(N^2\log V)$ time.
- **Sparse table for GCD:** It answers range GCD quickly, but maximizing over all ranges still needs additional boundary grouping.
- **Segment tree plus GCD jumps:** Can locate ranges of equal GCD, though the rolling suffix compression is simpler.
- **$k=1$:** Singletons are legal and have score `nums[i] * nums[i]`.
- **All values equal:** Only one dominant long suffix GCD is needed per endpoint; the full positive sum is favored.
- **GCD becomes one:** Extending farther cannot lower it again, so only the earliest start with GCD one matters.
- **Positive values:** Earliest-start dominance relies on added elements never decreasing the sum.
- **Temporary duplicate singleton:** It affects only a constant and does not change correctness.
- **Space mismatch:** Prefix sums make the checked-in implementation $O(N)$ space even though its rolling GCD state alone is logarithmic.
- **Why GCD groups appear consecutively:** As starts move right in their stored order, suffix relationships are nested. Extending all with the same $v$ preserves the order in which equal resulting GCDs collapse, so comparing only `g[-1]` is sufficient.
- **Length threshold:** An earlier representative is especially valuable because it may satisfy `k` while a later equal-GCD suffix does not. Keeping the later one instead could lose a valid candidate.
- **Answer initialization:** All numbers and GCDs are positive, and $k\le n$, so some legal subarray exists and eventually raises `ans` above zero.
