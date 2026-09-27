# Guided Example: Minimum Addition to Make Integer Beautiful

## 1. The Problem in One Quantity: the Digit Sum

We are handed a positive integer `n` and a threshold `target`. Write $S(m)$ for
the digit sum of a non-negative integer $m$ in base ten. If $m$ has decimal
digits $d_{k-1} d_{k-2} \dots d_1 d_0$, then

$$
S(m) = \sum_{j \ge 0} d_j .
$$

An integer is *beautiful* exactly when $S(m) \le \texttt{target}$. The task is to
produce the smallest non-negative integer $x$ with

$$
S(n + x) \le \texttt{target}, \qquad x \ge 0 .
$$

Two features of this framing drive everything that follows. First, the object
being constrained is the digit sum, not the magnitude: adding 1 can drop the
digit sum enormously, as when `19` becomes `20` and $S$ falls from $10$ to $2$.
Second, $x$ is bounded below by $0$, so an already-beautiful `n` answers $0$
without any rounding at all. The constraints ($n \le 10^{12}$ and
$\texttt{target} \le 150$) mean the digit sum of the input is small enough that
a rounding-based search terminates in a handful of rounds.

## 2. Why Naive Counting Fails, and What Replaces It

Scanning $x = 0, 1, 2, \dots$ and testing $S(n+x) \le \texttt{target}$ is
obviously correct and obviously hopeless: with `n = 19` and `target = 1` the
answer is $x = 81$, and with a twelve-digit input the first feasible $x$ can be
on the order of $10^{12}$. The candidate space is bounded only by the next power
of ten, so unit-by-unit enumeration is not the right instrument.

The replacement rests on a single structural observation. Suppose the current
candidate $c$ has a nonzero digit immediately to the left of a block of $z$
trailing zeros. Write $c = q \cdot 10^{\,z+1} + d \cdot 10^{\,z}$ with
$1 \le d \le 9$. Every number strictly between $c$ and
$(q+1) \cdot 10^{\,z+1}$ shares the same high part $q$ and therefore its digit
sum is at least $S(q) + d$. In particular the *first* number after $c$ that
discards that offending digit is

$$
\operatorname{next}(c) = (q + 1) \cdot 10^{\,z+1},
$$

obtained by clearing the lowest nonzero digit and propagating the carry. Its
digit sum is $S(q+1)$, which is often dramatically smaller than $S(c)$. So the
search never needs to visit the intervening integers one at a time: it can jump
straight from one ten-aligned candidate to the next, and those jumps are exactly
the values whose digit sum is worth testing.

## 3. The Invariant That Makes the Jump Sound

The whole method is a *frontier invariant* over ten-aligned candidates.

> **Invariant.** At the start of every round, the maintained offset $x$ is such
> that $c = n + x$ is ten-aligned, and no integer $m$ with
> $n \le m < c$ satisfies $S(m) \le \texttt{target}$.

The invariant is established for free at the start: $x = 0$ and the region
$[n, n)$ is empty, so "no feasible $m$ below $c$" holds vacuously even though
$c = n$ need not be ten-aligned. It is *preserved* by the jump because the next
round's candidate is precisely $\operatorname{next}(c)$: the entire interval
$[c, \operatorname{next}(c))$ is discarded only after $c$ itself has been tested
and rejected. And it is *terminating* because the aligned candidates strictly
increase and are bounded above by the next power of ten exceeding $n$, which is
beautiful whenever its digit sum $1$ is at most `target` — and `target >= 1` is
guaranteed, so a feasible candidate always exists. When the loop stops, the
current candidate is the first feasible integer at or above `n`, and since no
smaller integer is feasible, $x = c - n$ is the minimum addition.

Note carefully what the invariant does **not** claim: it does not claim that
$S$ decreases monotonically. In the example below $S$ rises from $11$ to $12$ to
$13$ before collapsing to $5$. Only the *candidates* are monotone, not their
digit sums, and the correctness argument relies solely on candidate monotonicity
plus exhaustive rejection of the skipped gap.

## 4. Worked Instance: `n = 467`, `target = 6`

We trace the second official example, because it forces two distinct rounding
positions instead of one. Here $S(467) = 4 + 6 + 7 = 17$, well above
$\texttt{target} = 6$.

The decisive quantity each round is the lowest nonzero digit of the current
candidate: it is the digit whose clearing produces the next aligned candidate,
and everything below it is a run of zeros that merely rescales the step size.
Reading the table, `y` is the candidate with its trailing zeros stripped, `d` is
the lowest remaining digit, and `p` is the power of ten that putting the zeros
back requires.

| Round | Candidate $c$ | $S(c)$ | $S(c) > 6$? | Trailing zeros $z$ | Stripped `y` | Lowest digit `d` | Step `p` | Next candidate $(y \div 10 + 1) \cdot p$ | Offset `x = next - n` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `467` | 17 | yes | 0 | `467` | 7 | `10` | `(46 + 1) * 10 = 470` | `470 - 467 = 3` |
| 1 | `470` | 11 | yes | 1 | `47` | 7 | `100` | `(4 + 1) * 100 = 500` | `500 - 467 = 33` |
| 2 | `500` | 5 | no | — | — | — | — | stop | answer `33` |

Round 0 clears the units digit `7` and carries the increment into the tens
place, giving `470`. Round 1 finds `470` already ending in one zero, strips it,
and clears the tens digit `7` — the carry now propagates through two positions
and lands on `500`. Round 2 accepts `500`: $S(500) = 5 \le 6$. The answer
matches the official output, `33`.

## 5. Per-Step State of the Maintained Offset

The same three rounds can be viewed through the state actually carried between
iterations. The offset `x` is never incremented by $1$; it is *recomputed* as a
whole, and it grows in discrete jumps whose size is governed by the position
being cleared.

| Step | State entering the step | Digit-sum test performed | Region discarded as infeasible | State leaving the step | `x` after |
|:---:|:---|:---|:---|:---|:---:|
| A | `x = 0`, candidate `467` | $S(467) = 17 > 6$ | $[467, 470)$ has no beautiful member | candidate `470`, cleared position $10^0$ | `3` |
| B | `x = 3`, candidate `470` | $S(470) = 11 > 6$ | $[470, 500)$ has no beautiful member | candidate `500`, cleared position $10^1$ | `33` |
| C | `x = 33`, candidate `500` | $S(500) = 5 \le 6$ | none — accepted | terminate | `33` |

The discarded regions are exactly the intervals the frontier invariant forbids
from containing an answer. At step A the interval $[467, 470)$ contains `467`,
`468`, `469`; their digit sums are $17$, $18$, and $18$, all above $6$, so no
information is lost by skipping them wholesale. At step B the interval
$[470, 500)$ contains thirty integers whose hundreds digit is $4$ and whose
digit sum is therefore at least $4 + 7 = 11$; again none can be beautiful. This
is the payoff of the alignment argument in section 2: the digit sum is bounded
below by a quantity fixed on the whole gap, so the gap can be refuted in one
stroke.

## 6. The Candidate Ladder and What Each Rung Contains

Another way to read the same run is as a ladder of ten-aligned values that
partition the range into disjoint blocks, each block sharing a fixed high part.

| Block | Integers in the block | Digit-sum lower bound | Can it contain a beautiful number ($\le 6$)? | Outcome |
|:---|:---|:---:|:---:|:---|
| $[467, 470)$ | `467`, `468`, `469` | $S(46) + 7 = 17$ | no | rejected at round 0 |
| $[470, 500)$ | `470` … `499` | $S(47) = 11$ | no | rejected at round 1 |
| $[500, 1000)$ | `500` … `999` | $S(50) = 5$ | yes | first member `500` accepted |

The lower bounds come from the fact that within a block the high part is
constant and the varying suffix contributes non-negative digits. Once a block's
lower bound exceeds `target`, the entire block is dead, which is why the method
only ever inspects the block's left endpoint. The accepted block
$[500, 1000)$ is entered at `500`, whose digit sum is the block minimum $5$; if
it had exceeded `target`, the method would have cleared the tens position again
and moved to `1000`, whose digit sum is $1$.

## 7. Boundary Behaviour of the Same Method

Every branch of the constraints is handled by the identical loop; no special
case is needed. The table records what the method does at each extreme, with the
arithmetic checked against the package's authored expectations.

| Boundary instance | Why it is dangerous | First test | Method's action | Result |
|:---|:---|:---|:---|:---|
| `n = 1`, `target = 1` | already beautiful; the temptation is to round "to a nicer number" | $S(1) = 1 \le 1$ | loop never entered; $x = 0$ | `0` |
| `n = 999`, `target = 1` | the carry must cross two consecutive nines | $S(999) = 27 > 1$ | strip `999` to `99`, then `9`, then `0`; step `p` becomes `1000` | `1`, giving `1000` |
| `n = 1090`, `target = 2` | the lowest digit is already `0`, so clearing it would waste a round | $S(1090) = 10 > 2$ | the zero suffix is stripped first; `p` becomes `100` | `10`, giving `1100` |
| `n = 19`, `target = 1` | the aligned rung must be the *next* power of ten, not the next multiple of ten | $S(19) = 10 > 1$ | strip to `1`, clear the `1`, carry into a new digit | `81`, giving `100` |
| `n = 16`, `target = 6` | official example; only the units position changes | $S(16) = 7 > 6$ | clear the `6` | `4`, giving `20` |
| `n = 888`, `target = 10` | the nearest valid rung is $900$, not a power of ten | $S(888) = 24 > 10$ | clear the units `8`, carrying into the tens `8` | `12`, giving `900` |
| `n = 1000000000000`, `target = 1` | maximum input, the top of the allowed range | $S(10^{12}) = 1 \le 1$ | loop never entered | `0` |

Two traps are visible here. The zero-digit trap (`n = 1090`) shows why the
stripping loop must run before the carry: the units digit is `0`, so a naive
"increment the units place" rule would test `1091` instead of jumping, and would
need many more rounds. The all-nines trap (`n = 999`) shows why the step must
grow while zeros are consumed: the carry passes through three digit positions
and the final step is $10^3$, so the offset is $1$ rather than $100$.

## 8. Why No Smaller Answer Exists: the Exchange Argument

Consider any $x' < x$ and let $c' = n + x'$. By the frontier invariant, $c'$ lies
strictly below the final candidate and therefore inside some already-refuted
block $q \cdot 10^{\,z+1} + d \cdot 10^{\,z}$. Inside that block the high part is
$q$ and the digit at position $z$ is at least $d$, so

$$
S(c') \ge S(q) + d > \texttt{target},
$$

where the strict inequality is exactly the test that caused the block to be
refuted. Hence $c'$ is not beautiful and no smaller $x'$ works; the returned
offset is minimal. Equivalently: the loop returns the *first* beautiful value in
the ascending sequence of ten-aligned candidates, and each rejected predecessor
was rejected because its whole block is infeasible. Completeness (a feasible
candidate is always reached) follows from the next power of ten being beautiful,
since its digit sum is $1 \le \texttt{target}$.

## 9. Alternatives and Their Costs

| Alternative | Idea | Why it loses or when it wins |
|:---|:---|:---|
| Unit-by-unit scan | test every $x = 0, 1, 2, \dots$ | Correct but up to $10^{12}$ digit-sum evaluations; unusable. |
| Enumerate every multiple of ten | test $n$, the next multiple of ten, and so on | Misses non-multiples of ten such as `900` for `n = 888`, which is a legal and minimal answer. |
| Round at every suffix position independently | compute the rounding cost for each position and take the minimum | Equivalent answer, but it must handle the carry interaction between positions explicitly; the single frontier already encodes that interaction. |
| Digit-by-digit carry model | walk positions from the units end and choose the first feasible carry pattern | Natural for a harder variant with a per-position budget, but here it is strictly more machinery than the greedy needs. |

The greedy wins because one test per aligned candidate is enough: the block
lower bound it computes doubles as the feasibility certificate for the entire
gap it skips.

## 10. Complexity

Let $L = O(\log_{10} n)$ be the number of decimal digits of `n`, so $L \le 13$
for the stated constraints. Each round inspects at most $L$ digits while summing
them and at most $L$ more while stripping zeros, and the number of rounds is
bounded by $L$ because each round clears at least one digit position that is
never revisited. Hence:

- **Time:** $O(L)$ rounds with $O(L)$ digit work per round, giving $O(L^2)$
  digit operations. With $L \le 13$ this is effectively constant work,
  independent of the magnitude of the answer `x`.
- **Auxiliary space:** $O(1)$. The state is the current candidate, the stripped
  value, the step multiplier, and the offset — a fixed number of integer
  registers, with no dependence on $L$ or on the size of the answer.

The important contrast is with the enumeration baseline, whose running time is
proportional to the answer itself rather than to its digit count.
