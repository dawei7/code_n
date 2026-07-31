## General

Maintain two bitmasks, `seen_once` and `seen_twice`, as a finite-state counter for every bit position in parallel. For one incoming value, the updates

`seen_once = (seen_once ^ value) & ~seen_twice`

and then

`seen_twice = (seen_twice ^ value) & ~seen_once`

cycle each bit through counts $0 \rightarrow 1 \rightarrow 2 \rightarrow 0$ modulo $3$. Consequently, all values appearing three times vanish after the first pass.

Let the exceptional values be $a$ (once) and $b$ (twice). At any bit, their residual contribution modulo $3$ is:

| Bit of $a$ | Bit of $b$ | Residue | Final mask |
|---:|---:|---:|---|
| 0 | 0 | 0 | neither |
| 1 | 0 | 1 | `seen_once` |
| 0 | 1 | 2 | `seen_twice` |
| 1 | 1 | 0 | neither |

Thus `seen_once | seen_twice` equals $a \mathbin{\mathrm{XOR}} b$. The two exceptional values are distinct, so its lowest set bit is a valid distinguishing bit.

Partition the array by that bit and run an independent pair of ternary counters for each partition. Every triplicate stays wholly inside one partition. One partition contains $a$ once, so its final `once` mask is $a$; the other contains $b$ twice, so its final `twice` mask is $b$. Whether the distinguishing bit lies in the global `seen_once` or `seen_twice` mask identifies which partition supplies each output position.

Python's bitwise integers behave as unbounded two's-complement values for these operations, so the same transitions recover negative signed inputs without a separate 32-bit mask.

## Complexity detail

Let $n$ be the length of `nums`. The algorithm makes two complete passes and performs a constant number of bitwise operations per value, giving $O(n)$ time.

It stores only six integer masks and the distinguishing bit. Their count does not depend on $n$, so auxiliary space is $O(1)$, satisfying the explicit contract.

## Alternatives and edge cases

- **Frequency hash table:** Counting values directly is simple and runs in $O(n)$ expected time, but uses $O(n)$ space and violates the required bound.
- **Sorting:** Adjacent runs reveal both frequencies, but sorting costs $O(n\log n)$ time and may mutate the input.
- **Per-bit arrays:** Counting all 32 bit positions also gives linear time, but allocating result/count arrays is unnecessary; parallel masks encode the same states directly.
- **Plain XOR:** Values appearing three times do not cancel under XOR, so the familiar two-singletons technique does not apply.
- **Shared set bits:** Bits present in both exceptional values disappear modulo three, which is why the second partitioning pass is necessary.
- **Zero:** A zero exceptional value produces an all-zero recovered mask but is still located correctly by the other value's distinguishing bit.
- **Negative values:** Sign extension must remain consistent across XOR, complement, and partition tests; fixed-width languages should use their native 32-bit unsigned bit pattern.
