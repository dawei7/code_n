## General

Build both addends from their least significant digits upward so ordinary addition carries flow in the processing direction. The decimal digits of `n` are likewise read from right to left.

**Represent shorter addends without internal zeroes.** A state records the incoming carry and whether each addend is still active. At the units position, both chosen digits must lie in `1..9`, which makes both numbers positive. At every later position, an active number may choose another digit from `1..9`, or choose `0` to end its representation. Once ended, it must choose `0` at every more significant position. Thus zero acts only as absent leading space above the number; it can never occur between two represented digits.

**Apply column addition.** For target digit $t$, chosen digits $x$ and $y$, and incoming carry $c$, retain the transition exactly when

$$
(x+y+c)\bmod 10=t.
$$

The outgoing carry is $\lfloor(x+y+c)/10\rfloor$. The active flags remain set precisely when their chosen digits are non-zero. State counts accumulate because each digit choice extends every lower-digit construction represented by that state.

Append one zero target column above the most significant digit of `n`. This forces both still-active numbers to end and rejects any leftover carry. The final state `(carry = 0, a ended, b ended)` therefore corresponds bijectively to complete positive no-zero pairs summing to `n`. Digit choices for `a` and `b` are distinct coordinates in every transition, so ordered pairs are counted separately.

## Complexity detail

Let $D=\lfloor\log_{10}n\rfloor+1$. There are only two carry values and two active flags for each addend, while each transition tries at most $10^2$ digit pairs. The time complexity is therefore $O(D)=O(\log n)$. The reversed target-digit list uses $O(D)$ space; the dynamic-programming maps contain only a constant number of states.

## Alternatives and edge cases

- **Enumerate one addend:** Trying every `a` from `1` through `n - 1` and checking both decimal representations takes $O(n\log n)$ time, which is impossible at $n=10^{15}$.
- **Most-significant-digit DP:** Addition carries travel from right to left, so an MSD-first formulation needs more complicated deferred-carry reasoning.
- **Leading absence versus digit zero:** Choosing zero after an addend ends is padding, not part of its decimal representation; choosing zero and later restarting is forbidden.
- **Ordered pairs:** Swapping unequal addends produces a separate valid pair and must not be divided out.
- **Smallest target:** At `n = 2`, both positive addends must equal `1`.
- **Final carry:** The extra target column ensures that constructions summing above `n` are rejected.
