## General

**Reduce rearrangement to frequencies**

Rearranging letters changes their order but not how many occurrences of each
letter exist. Count every letter in `s` as the available supply and every
letter in `target` as the demand for one copy.

**Find the limiting letter**

For a letter $c$ required by `target`, the source can support

$$
\left\lfloor
\frac{\operatorname{count}_{\texttt{s}}(c)}
     {\operatorname{count}_{\texttt{target}}(c)}
\right\rfloor
$$

copies with respect to that letter. A valid collection of copies must satisfy
the supply constraint for every required letter, so its size cannot exceed the
smallest of these quotients.

Conversely, let $k$ be that minimum. For every required letter $c$, the source
contains at least $k$ times the per-copy demand for $c$. Those occurrences can
therefore be partitioned among $k$ copies, and arbitrary rearrangement places
them in the target order. Thus $k$ copies are achievable as well as maximal.

## Complexity detail

Let $S = \lvert\texttt{s}\rvert$ and
$T = \lvert\texttt{target}\rvert$. Building both frequency tables takes
$O(S + T)$ time. Inspecting the fixed 26-letter alphabet does not change that
bound. The two fixed-size tables use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Repeated full-string counting:** Recounting both strings separately for every position or distinct target letter is correct, but can take $O(T(S + T))$ time.
- **Repeatedly build one copy:** Removing the letters for one target copy at a time works, but performs avoidable repeated searches and mutations.
- **Missing required letter:** Its available-to-required quotient is zero, so the answer is zero.
- **Repeated target letter:** Divide by its full multiplicity in one copy, not merely by one.
- **Irrelevant source letters:** Letters absent from `target` do not constrain the result.
- **Unused leftovers:** Surplus occurrences may remain after the maximum complete copies are formed.
- **Nonempty target:** The contract guarantees at least one required letter, so the minimum quotient is always defined.
