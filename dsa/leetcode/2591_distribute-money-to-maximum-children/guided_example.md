# Guided Example: Distribute Money to Maximum Children

## 1. The instance we will solve

Take the first official instance:

- `money = 20` dollars in total;
- `children = 3` children who must all be paid;
- the required outcome is `1`.

Three rules constrain every distribution: the whole amount must be handed out, every child must receive at least `1` dollar, and no child may receive exactly `4` dollars. Among all distributions satisfying the three rules, we must maximise the number of children who receive **exactly** `8` dollars. The official construction pays the children `8`, `9`, and `3`, which gives one eight-dollar child and satisfies every rule, so the reply is `1`.

The instance is the canonical trap of this problem. A purely arithmetic count of how many eights the budget can afford suggests `2`: after paying two children `8` each, `20 - 16 = 4` dollars remain, which is exactly enough for the third child's minimum of `1` dollar and even leaves slack. The counting bound is correct but not sufficient, because the residual lands on the single remaining child as precisely `4` dollars, the one amount the rules forbid. Resolving that obstruction — and only that one — is the whole difficulty.

## 2. Rewriting the rules as arithmetic

Let $x$ denote the number of children who receive exactly `8` dollars. Every feasible distribution satisfies the following.

| Rule from the statement | Arithmetic form |
|---|---|
| All money is distributed | The amounts sum to exactly `money` |
| Everyone receives at least `1` dollar | Each amount is $\ge 1$ |
| Nobody receives `4` dollars | No amount equals `4` |
| Exactly $x$ children receive `8` dollars | Exactly $x$ amounts equal `8`, and the other $\text{children} - x$ amounts differ from `8` |

Two immediate consequences pin down when a distribution exists at all. Since every child needs at least `1` dollar, the total must satisfy $\text{money} \ge \text{children}$; otherwise no distribution exists and the answer is $-1$. And since all money is spent, the total also bounds how many eights are affordable. The rest of the analysis is a search for the largest feasible $x$.

## 3. The counting bound on the number of eights

Fix $x$ children to receive exactly `8`. Those children consume $8x$ dollars, so

$$
R(x) = \text{money} - 8x
$$

dollars remain for the other $r = \text{children} - x$ children, each of whom needs at least `1` dollar. The budget requirement $R(x) \ge r$ rearranges into the central inequality:

$$
\text{money} - 8x \;\ge\; \text{children} - x
\quad\Longleftrightarrow\quad
7x \;\le\; \text{money} - \text{children}
\quad\Longleftrightarrow\quad
x \;\le\; \left\lfloor \frac{\text{money} - \text{children}}{7} \right\rfloor .
$$

The quantity $\text{money} - \text{children}$ is the money left after paying every child the mandatory dollar, and each additional eight-dollar child costs $8 - 1 = 7$ of it. That is why the divisor is $7$ and not $8$: the mandatory dollar of an eight-dollar child is already accounted for in $\text{money} - \text{children}$.

For the instance, the bound evaluates to $\lfloor (20 - 3)/7 \rfloor = \lfloor 17/7 \rfloor = 2$, so no distribution can have more than two eight-dollar children. The counting test does not yet tell us whether two is reachable, so each candidate has to be examined.

| Candidate $x$ | Money spent on eights | Residual $R(x)$ | Children left $r$ | Minimum needed $r$ | Budget test $R(x) \ge r$ | Forbidden-amount test |
|---|---|---|---|---|---|---|
| `0` | `0` | `20` | `3` | `3` | passes | can be arranged |
| `1` | `8` | `12` | `2` | `2` | passes | can be arranged |
| `2` | `16` | `4` | `1` | `1` | passes | **fails**: the only left child would receive exactly `4` |
| `3` | `24` | `-4` | `0` | `0` | fails | irrelevant, the budget is already exceeded |

The table shows precisely where the counting bound stops being decisive. At $x = 2$ the budget test passes with equality, so the arithmetic alone would accept the candidate; only the third rule rejects it. The naive reply `2` comes from reading the bound and stopping there.

## 4. Why the candidate `x = 2` collapses

Suppose two children receive `8`. They consume `16` dollars, leaving `4` for the last child. That child needs at least `1` dollar, so the `4` dollars must be given in full — there is no other place to put them, because every other child's amount is already fixed at `8`. The remaining child therefore receives exactly `4` dollars, which the rules forbid. This is not a matter of choosing a cleverer arrangement: with two eights and one remaining child, the amount that child receives is forced to be $R(2) = 4$.

The obstruction is a *forced* amount, not a shortage. Only one exotic configuration can produce a forced `4`: when a single child remains and the residual is exactly `4`, that is, when

$$
\text{money} - 8x = 4 \quad\text{with}\quad x = \text{children} - 1,
$$

which is equivalent to $\text{money} = 8 \cdot \text{children} - 4$. For `money = 20` and `children = 3` this identity holds exactly, which is why this instance is the trap.

## 5. Repairing the plan downwards by one eight

Since `2` is blocked, try `1`: one child receives `8`, and `20 - 8 = 12` dollars remain for two children, each of whom needs at least `1` dollar. The residual is now split between two children, so there is room to avoid the forbidden amount. Several splits work.

| Distribution | Amounts | Sum | Minimum satisfied? | Any amount equal to `4`? | Eights |
|---|---|---|---|---|---|
| Official | `8`, `9`, `3` | `20` | yes, all $\ge 1$ | no | `1` |
| Alternative | `8`, `11`, `1` | `20` | yes, all $\ge 1$ | no | `1` |
| Alternative | `8`, `5`, `7` | `20` | yes, all $\ge 1$ | no | `1` |
| Splitting evenly | `8`, `6`, `6` | `20` | yes, all $\ge 1$ | no | `1` |

Every candidate split avoids `4`, and the count of eight-dollar children stays at `1`, so the answer for this instance is `1`. Note that the distributions are far from unique: the problem asks only for the maximum count of eight-dollar children, never for a particular distribution, so the reasoning only has to exhibit one witness per candidate count.

## 6. The four regimes of the general answer

The instance analysis generalises into a small decision structure with four regimes. Let $b = 8 \cdot \text{children}$ be the total needed to pay every child exactly `8`, so that $\text{money} = b$ is the boundary between "enough for all eights" and "more than enough".

| Regime | Condition | Answer | Reason |
|---|---|---|---|
| Impossible | $\text{money} < \text{children}$ | `-1` | Paying every child the mandatory `1` dollar already exceeds the budget |
| Excess | $\text{money} > 8 \cdot \text{children}$ | $\text{children} - 1$ | All `children` eights would spend $b < \text{money}$, leaving money that must be given away, which lifts one child above `8`; giving all surplus to a single child costs only that one eight |
| Forced four | $\text{money} = 8 \cdot \text{children} - 4$ | $\text{children} - 2$ | The counting bound is $\text{children} - 1$, but the plan forces exactly `4` on the last child; dropping one eight leaves `12` dollars for two children, which split as `11` and `1` |
| Ordinary | $\text{children} \le \text{money} \le 8 \cdot \text{children}$ and $\text{money} \ne 8 \cdot \text{children} - 4$ | $\left\lfloor \dfrac{\text{money} - \text{children}}{7} \right\rfloor$ | The counting bound is attainable; the residual can always be spread without producing a `4` |

Reading the regimes against the authored instances confirms each one.

| `money` | `children` | Regime | Answer | Verifying arithmetic |
|---|---|---|---|---|
| `1` | `2` | impossible | `-1` | $1 < 2$ |
| `2` | `2` | ordinary | `0` | $\lfloor (2-2)/7 \rfloor = 0$, distribution `1`, `1` |
| `5` | `2` | ordinary | `0` | $\lfloor (5-2)/7 \rfloor = 0$, distribution `2`, `3` |
| `8` | `2` | ordinary | `0` | $\lfloor (8-2)/7 \rfloor = 0$ |
| `9` | `2` | ordinary | `1` | $\lfloor (9-2)/7 \rfloor = 1$, distribution `8`, `1` |
| `12` | `2` | forced four | `0` | $12 = 8 \cdot 2 - 4$, so $2 - 2 = 0$; distribution `11`, `1` |
| `16` | `2` | ordinary | `2` | $16 = 8 \cdot 2$ exactly, so $\lfloor (16-2)/7 \rfloor = 2$, both children receive `8` |
| `17` | `2` | excess | `1` | $17 > 16$, so $2 - 1 = 1$; distribution `8`, `9` |
| `20` | `3` | forced four | `1` | $20 = 8 \cdot 3 - 4$, so $3 - 2 = 1$ |
| `23` | `3` | ordinary | `2` | $\lfloor (23-3)/7 \rfloor = 2$; the third child takes `7` |
| `24` | `3` | ordinary | `3` | $24 = 8 \cdot 3$, so every child receives `8` |
| `25` | `3` | excess | `2` | $25 > 24$, so $3 - 1 = 2$ |
| `29` | `30` | impossible | `-1` | $29 < 30$ |
| `200` | `30` | ordinary | `24` | $\lfloor (200-30)/7 \rfloor = \lfloor 170/7 \rfloor = 24$, with `8` dollars left for `6` children |

The `23` and `25` rows are a matched pair worth comparing: adding one dollar to a budget that already pays two eights and leaves `7` reduces the answer, because the extra dollar must go somewhere and the only place left is the child holding the remainder. This is the same forced-amount phenomenon as Section 4 in a milder form: a residual that cannot be split without displacing an eight.

## 7. Attaining the counting bound in the ordinary regime

It remains to justify the third column of the ordinary regime, since a bound that is not attained would produce an over-count. Let

$$
x = \left\lfloor \frac{\text{money} - \text{children}}{7} \right\rfloor,
\qquad r = \text{children} - x,
\qquad R = \text{money} - 8x .
$$

By the definition of $x$ we have $7x \le \text{money} - \text{children}$, which is exactly $R \ge r$: there is enough money for the $r$ remaining children to receive their mandatory dollars. Pay each of them `1` dollar, which uses $r$ dollars and leaves

$$
E = R - r \ge 0
$$

dollars of slack. If $E = 0$ the construction is complete. Otherwise distribute the slack as follows.

| Slack $E$ | Number of remaining children $r$ | Construction | Amounts produced | Contains a `4`? |
|---|---|---|---|---|
| `0` | any | Give no extra | All `1` | no |
| $E \ne 3$, $E > 0$ | $r \ge 1$ | Give all slack to one child | One child receives $1 + E$, the rest `1` | no, because $1 + E \ne 4$ |
| $E = 3$ | $r \ge 2$ | Give `2` to one child and `1` to another | Amounts `3`, `2`, and `1` for the rest | no |
| $E = 3$ | $r = 1$ | Impossible for this $x$ | The single child would receive `4` | yes — this is the forced-four regime |

One detail of the second row deserves a check, because a leftover child receiving exactly `8` would raise the count of eights above $x$ and contradict the bound of Section 3. That cannot happen: $1 + E = 8$ means $E = 7$, and then $R = r + 7$, so $\text{money} = 8x + r + 7 = 7x + \text{children} + 7$, which would make $\lfloor (\text{money} - \text{children})/7 \rfloor$ equal to $x + 1$ and contradict the definition of $x$. The construction therefore creates exactly $x$ eights, never more.

The only failing row is the last one, and it identifies the forced-four regime exactly: $r = 1$ means $x = \text{children} - 1$, and $E = 3$ means $R = 1 + 3 = 4$, hence $\text{money} = 8(\text{children} - 1) + 4 = 8 \cdot \text{children} - 4$. In every other case the construction distributes all money, respects the minimum of `1`, never produces a `4`, and realises exactly $x$ eight-dollar children. Note that the third row is why two remaining children are needed to absorb a slack of exactly `3`: with a single remaining child the whole slack is forced onto that child.

## 8. Boundaries and traps

| Situation | Instance | Outcome | Why |
|---|---|---|---|
| Budget below the mandatory minimum | `money = 1`, `children = 2` | `-1` | Every child needs `1` dollar, so `2` dollars are required |
| Budget exactly at the minimum | `money = 2`, `children = 2` | `0` | The only distribution is `1` and `1`, with no eights |
| Residual forced to `4` | `money = 20`, `children = 3` | `1` | Two eights force the last child to receive exactly `4` |
| Every child can receive `8` exactly | `money = 24`, `children = 3` | `3` | No money is left over, so no child needs to be raised above `8` |
| One dollar more than all eights | `money = 25`, `children = 3` | `2` | The surplus must be spent, so one child necessarily exceeds `8` |
| No eight is affordable | `money = 8`, `children = 2` | `0` | The counting bound is $\lfloor (8-2)/7 \rfloor = 0$ |
| Exactly one eight is affordable | `money = 9`, `children = 2` | `1` | Distribution `8`, `1` |
| Largest legal budget | `money = 200`, `children = 30` | `24` | $\lfloor 170/7 \rfloor = 24$; six children share the remaining `8` dollars |
| Largest children count | `money = 29`, `children = 30` | `-1` | $29 < 30$ |
| A child receiving more than `8` | any excess regime | allowed | Only the amount `4` is forbidden, and only `8` is counted |
| A child receiving `0` | never legal | disallowed | The minimum of `1` dollar is absolute |

Two traps are worth naming. First, an amount larger than `8` is perfectly legal — the rules forbid only `4` and require only a minimum — so treating `8` as a cap would wrongly reject the excess regime. Second, the forbidden value is a *single* excluded amount, not an interval: `3` and `5` are as acceptable as `11`, which is why the repairs in Section 5 have so much freedom.

## 9. Why the reasoning is correct

**The bound is necessary.** If some distribution has $x$ children receiving `8`, the other $\text{children} - x$ children each receive at least `1`, so the total is at least $8x + (\text{children} - x)$; since the total must equal `money`, the inequality $\text{money} \ge 7x + \text{children}$ holds and therefore $x \le \lfloor (\text{money} - \text{children})/7 \rfloor$. No distribution can beat that bound, and if $\text{money} < \text{children}$ then even $x = 0$ is infeasible, which gives the `-1` reply.

**Each regime attains its claim.** In the excess regime, paying $\text{children} - 1$ children `8` dollars leaves $\text{money} - 8(\text{children} - 1) \ge 9$ dollars for the last child, so that child receives at least `9`, no amount equals `4`, and the upper bound of $\text{children} - 1$ is met because all `children` eights would spend only $8 \cdot \text{children} < \text{money}$, leaving money that cannot be discarded. In the forced-four regime, $\text{children} - 1$ eights are impossible by Section 4, and $\text{children} - 2$ eights are realised by giving `8` to each of those children and splitting the remaining `12` dollars between the last two as `11` and `1`. In the ordinary regime, Section 7 constructs a valid distribution with $x = \lfloor (\text{money} - \text{children})/7 \rfloor$ eights, and the bound proved above shows nothing larger is possible.

Every case is therefore both bounded and attained, so the four regimes return exactly the maximum. The reasoning is a complete case analysis rather than a search, because the one obstruction that can invalidate the counting bound — a forced residual of `4` on a single remaining child — is a single algebraic condition, $\text{money} = 8 \cdot \text{children} - 4$, and it can be checked directly.

## 10. Complexity: time and auxiliary space

**Time.** The answer is decided by a constant number of comparisons, one subtraction, one division, and one special equality test, so the running time is $\Theta(1)$: it does not depend on `money` or on `children` beyond reading them. No distribution is ever enumerated — the case analysis replaced the search over splits, whose naive size would be exponential in the number of children — and no loop over the children is needed even to verify feasibility.

**Auxiliary space.** Only a handful of integer intermediates are needed (the residual, the child remainder, and the bound), so the extra space is $O(1)$ and independent of both inputs. Intermediate values stay far inside ordinary integer range: `money` is at most `200` and `8 * children` at most `240`, so no overflow consideration arises for this problem.