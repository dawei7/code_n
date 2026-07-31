## General

**Maximize lexicographically before taking the modulus**

Every ordering contains exactly $L$ bits. Among equal-length binary strings, the larger integer is precisely the lexicographically larger string, so the task is to make the earliest differing bit a `1`. The modulo operation cannot be used when choosing the order; it is applied only while evaluating the already-maximal string.

Write a segment as $1^a0^b$. A pairwise exchange identifies the order that no optimal concatenation can violate:

- If $b=0$, the segment is made entirely of ones. It must precede every segment that contains a zero: moving those uninterrupted ones earlier delays the first possible zero.
- If $a=0$, the segment is made entirely of zeros. It must follow every segment containing a one, because placing it earlier introduces a zero before that other segment's leading one.
- For two mixed segments $X=1^a0^b$ and $Y=1^c0^d$, compare `XY` with `YX`. When $a\ne c$, the segment with the longer leading-one run must come first; after the shorter run ends, that order still has a `1` where the other has reached a `0`. When $a=c$, both concatenations first differ after the shorter zero run, so the segment with fewer trailing zeros comes first.

These rules produce a direct sort key: pure-one segments, then mixed segments ordered by decreasing $a$ and increasing $b$, then pure-zero segments. Every adjacent inversion would become lexicographically larger if swapped according to this rule. Removing all such inversions therefore yields a globally maximal concatenation.

**Evaluate runs without constructing the binary string**

Maintain the processed prefix value modulo $P=10^9+7$. For each of a segment's `ones` positions, shift the prefix left and append one with `value = (value * 2 + 1) % P`. For each of its `zeros` positions, shift and append zero with `value = value * 2 % P`. This scans the chosen bit sequence directly without allocating the segment text or the potentially enormous full integer.

## Complexity detail

Let $N$ be the number of segments and $L$ their total bit count as defined in the Function Contract. Constructing and sorting the segment pairs costs $O(N\log N)$ time, and evaluating their runs scans all $L$ bits. The total is $O(N\log N+L)$ time. The ordered segment list and the language runtime's sort workspace use $O(N)$ auxiliary space.

The benchmark defines size as $N$ and keeps the average segment length bounded, making $L=\Theta(N)$. The required method therefore scales as $O(N\log N)$. A correct repeated-selection control performs $\Theta(N^2)$ segment comparisons before the same linear evaluation pass.

## Alternatives and edge cases

- **Generic concatenation comparator:** Sorting explicit strings by whether `x + y` exceeds `y + x` is logically valid, but materializing both concatenations in every comparison repeats work proportional to segment lengths and is unnecessary for this restricted run structure.
- **Repeatedly select the next segment:** Choosing the best remaining segment by a full scan preserves correctness but requires $\Theta(N^2)$ comparisons.
- **Modular powers per run:** Appending $a$ ones as `value * 2**a + (2**a - 1)` and then shifting by $b$ zeros gives the same result with modular exponentiation; the direct scan more closely mirrors the chosen bit sequence.
- **Pure-one segments:** Even a short all-one segment precedes every mixed segment, because it contributes no zero that could interrupt the combined leading-one prefix.
- **Pure-zero segments:** These belong at the end; their relative order does not affect the final string.
- **Equal leading-one counts:** For mixed segments with the same number of leading ones, the shorter zero run comes first so the next segment's `1` appears earlier.
- **Tied segments:** Identical `(ones, zeros)` pairs, all-one pairs, and all-zero pairs may be permuted within their tied group without changing the concatenation.
- **Modulo timing:** Comparing residues could select a smaller actual binary value. Determine the maximal order first and reduce only during numeric accumulation.
- **Parallel arrays:** Counts at the same index form one indivisible segment; sorting either input array independently would destroy the contract.
