## General

**Isolate the portion in each bracket**

Track `previous_upper`, initially zero. At `[upper, percent]`, at most
`min(income, upper) - previous_upper` dollars belong to the current bracket.
If that quantity is positive, multiply it by `percent` and add it to an
integer total measured in percent-dollars.

Once `upper` reaches or exceeds `income`, no later bracket contains earned
income, so the traversal can stop. Otherwise, set `previous_upper = upper` and
continue.

**Accumulate before converting the percentage**

Dividing each term by 100 is mathematically valid, but summing the integer
products first avoids unnecessary floating-point operations. Divide the final
total by 100 once.

The increasing boundaries partition `[0, income]` into nonoverlapping pieces.
For each visited bracket, the formula takes exactly its intersection with that
interval and applies exactly its listed rate. The pieces cover all income up
to the stopping boundary, so their tax sum is precisely the progressive tax
owed.

## Complexity detail

Let $b=\lvert\texttt{brackets}\rvert$. Each relevant bracket is visited at
most once, giving $O(b)$ time in the worst case. The boundaries and running
tax use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Classify every earned dollar:** Searching the bracket for each individual dollar is correct for integer income but can take $O(b\cdot\texttt{income})$ time.
- **Mutate remaining income:** Subtracting each taxed slice from a remaining balance also works, but careful boundary tracking is still required.
- **Zero income:** No bracket contributes, so the result is zero.
- **Zero-percent bracket:** Its income slice is consumed even though it adds no tax.
- **Partial final bracket:** Only the amount through `income`, not the bracket's full width, is taxed.
- **Exact upper bound:** Income equal to a bracket boundary fills that bracket and never enters the next one.
- **One-time percentages:** A later rate applies only to the interval above the prior upper bound, not to all income earned so far.
- **Numerical accuracy:** Integer percent-dollar accumulation followed by one division represents every possible cent exactly enough for the accepted tolerance.
