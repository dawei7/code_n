# Guided Example: Pass the Pillow

## 1. The instance and the seconds it passes through

People numbered `1` through `n` stand in a line, the pillow starts with person `1`, and every second its holder hands it to the neighbouring person in the current direction. At either end the direction reverses. The instance traced here is the first official input, $n = 4$ and $time = 5$, whose required answer is `2`; the statement describes the same walk as `1 -> 2 -> 3 -> 4 -> 3 -> 2`.

| Second $t$ | Holder after $t$ seconds | Hand-off performed during second $t$ | Direction afterwards |
|---|---|---|---|
| 0 | `1` | none, this is the initial state | toward person `4` |
| 1 | `2` | `1` to `2` | toward person `4` |
| 2 | `3` | `2` to `3` | toward person `4` |
| 3 | `4` | `3` to `4` | reverses, now toward person `1` |
| 4 | `3` | `4` to `3` | toward person `1` |
| 5 | `2` | `3` to `2` | toward person `1` |

Note where the reversal happens: the hand-off into person `4` is completed at second `3`, and only then does the direction flip. The endpoint is therefore visited once per pass, not twice, and the class of "holders" is exactly the sequence of positions the walk occupies.

## 2. The configuration is a position plus a direction, and it forms one cycle

A position alone does not determine the future, because person `3` of four may be reached while travelling right or while travelling left. The state is the pair (position, direction). Only $2n - 2$ states of the full $2n$ combinations are reachable: the two endpoints force their direction, person `1` can only be entered while travelling rightward and person `n` only while travelling leftward, so the reachable states are the $2(n-2)$ interior combinations plus the two endpoint states. For $n = 4$ that is six states, and they form a single closed cycle.

| Index $t \bmod 6$ | Position | Direction of the next hand-off | Following index |
|---|---|---|---|
| 0 | `1` | rightward | 1 |
| 1 | `2` | rightward | 2 |
| 2 | `3` | rightward | 3 |
| 3 | `4` | leftward | 4 |
| 4 | `3` | leftward | 5 |
| 5 | `2` | leftward | 0 |

```mermaid
flowchart LR
    accTitle: Reachable configuration cycle for four people
    accDescr: The six reachable states of position and direction form one cycle, so the configuration after six seconds is identical to the initial configuration.
    S0["t=0 person 1 moving right"] --> S1["t=1 person 2 moving right"]
    S1 --> S2["t=2 person 3 moving right"]
    S2 --> S3["t=3 person 4 moving left"]
    S3 --> S4["t=4 person 3 moving left"]
    S4 --> S5["t=5 person 2 moving left"]
    S5 --> S0
```

Because the transition is deterministic and each reachable state has exactly one predecessor, the walk cannot branch or merge, and the cycle is the whole reachable state space. The answer for any `time` is therefore read straight off the cycle: reduce `time` modulo its length and report the position stored there.

## 3. Why the cycle length is exactly 2(n-1)

The configuration after $2(n-1)$ seconds is the initial one, so the period divides $2(n-1)$.

- The outbound traversal advances the position by one for $n-1$ seconds, ending at person $n$ with the direction reversed.
- The return traversal advances by one in the negative direction for another $n-1$ seconds, ending at person `1` with the direction reversed again.

After those $2(n-1)$ hand-offs the holder is back at person `1` and the direction points toward person $n$ once more, which is exactly the starting state, so the sequence of states repeats from there. The period cannot be smaller: the walk spends $n-1$ seconds on each leg, the two legs carry opposite directions, and the direction is part of the state, so no proper prefix of the cycle returns to (person `1`, rightward). This is the invariant that makes the closed form exact rather than approximate:

> the holder after $time$ seconds is the position component of the state reached by advancing $time$ steps around a cycle of length $2(n-1)$ from (person `1`, rightward).

## 4. Unfolding the reflection into a triangle wave

Reflection is easier to compute if it is replaced by something straight. Imagine infinitely many copies of the line laid end to end and a walker who keeps moving rightward on that infinite line, one unit per second, starting at coordinate $0$. Folding the copies back onto the original line maps the walker's coordinate to a real position, and the fold is the triangle wave

$$
f(u) = 1 + \min\bigl(u \bmod 2(n-1),\ 2(n-1) - (u \bmod 2(n-1))\bigr).
$$

Setting $u = time$ reproduces the walk with reflections, because each time the unfolded walker crosses into the next copy the folded coordinate turns around at an endpoint. The correctness of the formula is the correctness of this folding: the two legs of the folded triangle are the outbound and return traversals, and the endpoints of the triangle are the two ends of the line. Writing $x = time \bmod 2(n-1)$ turns the triangle into two plain branches.

| Residue $x$ | Traversal it belongs to | Position | Check at $n = 4$ |
|---|---|---|---|
| $0 \le x \le n-1$ | outbound, from person `1` toward person $n$ | $1 + x$ | $x = 2$ gives `3` |
| $n-1 < x < 2(n-1)$ | return, from person $n$ back toward person `1` | $2n - 1 - x$ | $x = 5$ gives `2` |

The two branches agree at $x = n-1$, where both give person $n$, so the piecewise definition has no gap. Values of $x$ beyond $n-1$ are already walking back: at $x = 2(n-1) - 1$ the return is one step short of person `1`, giving position $2n - 1 - (2n - 3) = 2$.

## 5. Worked trace for `n = 4, time = 5`

| Quantity | Value | Reason |
|---|---|---|
| Period $2(n-1)$ | $2 \cdot 3 = 6$ | one outbound and one return leg of three seconds each |
| Residue $x = time \bmod 6$ | $5 \bmod 6 = 5$ | `time` is already smaller than the period |
| Branch | return, because $5 > 3$ | the residue exceeds the outbound length $n-1$ |
| Position $2n - 1 - x$ | $8 - 1 - 5 = 2$ | matches the cycle index `5`, which holds person `2` |

The official answer `2` is reproduced, and the cycle table of Section 2 agrees independently: index `5` is the state (person `2`, leftward).

## 6. Boundary behaviour of the same formula

| Input | Residue $x$ | Computed position | Authored expectation | What the row demonstrates |
|---|---|---|---|---|
| $n = 5$, $time = 4$ | 4 | $1 + 4 = 5$ | `5` | the outbound leg ends exactly at the far endpoint |
| $n = 5$, $time = 8$ | 0 | $1 + 0 = 1$ | `1` | one whole period returns the pillow to person `1` |
| $n = 5$, $time = 9$ | 1 | $1 + 1 = 2$ | `2` | the first second after a period begins a fresh outbound leg |
| $n = 5$, $time = 7$ | 7 | $10 - 1 - 7 = 2$ | `2` | the return leg is one second short of person `1` |
| $n = 2$, $time = 1$ | 1 | $1 + 1 = 2$ | `2` | smallest legal line; the period is $2$ |
| $n = 2$, $time = 2$ | 0 | $1 + 0 = 1$ | `1` | with two people a full period costs two seconds |
| $n = 1000$, $time = 999$ | 999 | $1 + 999 = 1000$ | `1000` | the journey reaches person $n$ exactly at $time = n-1$ |
| $n = 1000$, $time = 1000$ | 1000 | $2000 - 1 - 1000 = 999$ | `999` | the first second of the return leg |

The rows for $n = 5$, $time = 8$ and $n = 5$, $time = 9$ are the ones that separate a period-aware method from a simulation that only walks forward: after eight seconds the configuration is identical to the start, so the ninth second behaves exactly like the first.

## 7. Traps this instance exposes

| Trap | Failure mode | Correction |
|---|---|---|
| Using period $n-1$ | at $n = 4$, $time = 3$ gives residue $0$ and reports person `1` instead of person `4` | one pass is only half a period; the round trip costs $2(n-1)$ |
| Off-by-one between state and holder | reporting the holder at $time - 1$ seconds because the initial state is indexed $0$ | the residue is taken from `time` itself, and residue $0$ names the initial holder |
| Mixing the two branches | applying $1 + x$ on the return leg, which grows past person $n$ | the branch is chosen by comparing $x$ with $n-1$ |
| Treating the endpoints as ordinary positions | doubling them with both directions gives the wrong cycle length $2n$ | endpoint directions are forced, which is why the period is $2(n-1)$ |
| Reversing before the hand-off | flipping direction on arrival at the endpoint so the endpoint is never reported | the flip happens after the hand-off completes |
| Counting hand-offs instead of seconds | iterating the pass loop $time$ times but starting the holder at person `2` | person `1` holds the pillow at second `0`, before any hand-off |
| Applying the closed form when $n = 1$ | the period $2(n-1)$ collapses to $0$, so the modulus is undefined | the stated domain is $2 \le n \le 1000$; the authored case $n = 1, time = 5$ expects `6` and records a walk that never reaches an endpoint above it, so it is not covered by this periodic model |
| Simulating every second | $O(time)$ steps when a single remainder answers the question | the cycle derivation replaces the loop without changing the result on the legal domain |

## 8. Time and auxiliary space

Let $n$ be the line length and $time$ the number of seconds, with $2 \le n \le 1000$ and $1 \le time \le 1000$.

| Resource | Bound | Derivation |
|---|---|---|
| Time | $O(1)$ | one remainder, one comparison, and one addition or subtraction |
| Auxiliary space | $O(1)$ | the residue and the resulting position are the only stored values |

A step-by-step simulation is also correct and needs only a position, a direction, and a loop counter, so it is $O(time)$ time with $O(1)$ auxiliary space; at $time \le 1000$ it finishes instantly. The closed form is still the better lesson, because it shows the walk is not merely bounded but exactly periodic, and it removes the dependence on `time` entirely: the cost is the same whether the pillow is passed five times or a billion, and the only quantity that ever grows is the value of the remainder input.