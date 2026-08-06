## General

**Separate optimization from reconstruction**

For each interval `s[left:right + 1]`, store its minimum encoded length in `encoded_length[left][right]` and the
decision that attains that length in `decision[left][right]`. Process widths from one through $n$, so every proper
subinterval needed by a transition is already optimal. The literal interval, whose cost equals its width, is the
initial choice.

Storing only a length and a compact decision is important in Python. Concatenating candidate strings during all
$O(n^3)$ split transitions would copy their characters repeatedly. Deferring text construction avoids that extra
factor.

**Test every possible outermost form**

For each split position `split`, the interval can be represented by the optimal encoding of
`s[left:split + 1]` followed by that of `s[split + 1:right + 1]`. Their stored lengths make this candidate an $O(1)$
calculation.

The interval may instead be repetitions of one shorter unit. For its text `t`, the first occurrence of `t` within
`t + t` after position zero gives the shortest period. If that position is smaller than the interval width and
divides the width, the repetition candidate consists of the decimal repeat count, two brackets, and the already
optimal encoding of the period-length prefix.

Only a strictly shorter candidate replaces the current choice. This matches the source contract and preserves the
implementation's deterministic order among tied minimum encodings: literal first, then earlier split decisions,
then repetition.

**Why these decisions produce a shortest encoding**

Induct on interval width. A one-character interval must remain literal. For a longer interval, any valid shortest
representation is either literal, has an outermost concatenation boundary, or has one outermost repetition wrapper.
The transitions inspect the literal form, every boundary, and the interval's shortest repeating unit. By the
induction hypothesis, every referenced subinterval already has minimum encoded length, including the unit inside a
repetition. The selected decision therefore has minimum length for the interval.

After the table is complete, recursively follow the decision for the whole string. Literal decisions append one
slice, split decisions emit both children, and repetition decisions emit the count and brackets around the unit.
Collecting pieces and joining once constructs exactly the encoding represented by the optimal decisions without
reintroducing repeated concatenation costs.

## Complexity detail

Let $n = \lvert \texttt{s} \rvert$. There are $O(n^2)$ intervals. Across them, all split positions take $O(n^3)$
time. Creating each interval slice and finding its shortest period are linear in the interval width, contributing
another $O(n^3)$ total. Reconstruction visits the selected decision tree and emits an $O(n)$-length result, so the
overall time complexity is $O(n^3)$.

The two interval tables contain $O(n^2)$ entries. The recursion stack and emitted result use $O(n)$ additional
space, for $O(n^2)$ auxiliary space overall.

## Alternatives and edge cases

- **Eager encoded-string table:** the protected and immutable Accepted implementations use the same recurrence but
  concatenate strings inside every split transition. In Python that copying raises actual time to $O(n^4)$ and
  total stored characters to $O(n^3)$ in the worst case.
- **Top-down memoization:** can evaluate the same interval states recursively, but all intervals are reachable from
  the full recurrence and recursion adds control overhead without improving the asymptotic bounds.
- **Manual period enumeration:** checking every possible unit length character by character is correct, but can add
  another linear factor on near-uniform intervals.
- **Greedy repetition selection:** choosing a locally attractive repeated block can miss a shorter concatenation or
  a repetition whose unit is itself encoded.
- **Short repetition:** leave a region literal whenever the count and brackets do not make it strictly shorter.
- **Nested encoding:** the repetition cost and reconstruction use the optimal decision for the repeated unit, not
  its raw text.
- **Partial repeated prefix:** split transitions allow a compressible prefix or middle region to coexist with an
  unmatched suffix or surrounding literals.
- **Tied answers:** any minimum-length representation is valid; strict comparisons retain a stable choice without
  affecting optimality.
