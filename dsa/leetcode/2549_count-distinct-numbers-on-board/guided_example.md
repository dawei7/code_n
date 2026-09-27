# Guided Example: Count Distinct Numbers on Board

## 1. The instance, and a billion days that never need to happen

Take the first official sample: `n = 5`, whose required output is `4`. The number $5$ starts alone on a board, and each day every number $x$ currently on the board looks for all integers $i$ with $1 \le i \le n$ and $x \bmod i = 1$; those $i$ are then placed on the board. Numbers are never removed. After $10^9$ days we must report how many *distinct* values the board holds.

The stated horizon is deliberately absurd: $10^9$ days against the constraint $n \le 100$. That mismatch is the first clue that the day counter is not part of the algorithm. The board can only ever hold integers in the range $1$ to $n$, so it has at most $100$ members and, as this lesson shows, it stops changing after at most $n - 2$ days. The right move is to find the reachable set directly and never iterate a day loop.

## 2. Which numbers a board value can place

The condition $x \bmod i = 1$ says $x = q \cdot i + 1$ for some integer $q \ge 0$, so $i$ divides $x - 1$ and $i \le x - 1$ whenever $q \ge 1$ and $x \ge 2$. Three facts follow immediately and constrain everything:

- $i = 1$ is never a legal placement, because $x \bmod 1 = 0$ for every $x$. The value $1$ therefore can never be placed, and since $1$ only enters a board by being placed, the board never contains $1$.
- Every value on the board except the initial $n$ satisfies $x \ge 2$, so every placement has $q \ge 1$ and hence $i \le x - 1 < x$. Each addition is strictly smaller than the value that produced it, which is the monotone rank that keeps the board bounded by $n$ forever.
- The largest possible placement from $x$ is $i = x - 1$, valid exactly when $x \ge 3$, because $x \bmod (x-1) = 1$ for every $x \ge 3$.

The third fact is the engine of the whole problem: whenever $x \ge 3$ sits on the board, $x - 1$ joins it on the next day. Checking the instance's values against $i \le 5$ gives the complete placement table.

| $x$ on the board | $i \le 5$ with $x \bmod i = 1$ | Values placed | Comment |
|---|---|---|---|
| 5 | 2, 4 | 2, 4 | $5 = 2 \cdot 2 + 1$ and $5 = 1 \cdot 4 + 1$ |
| 4 | 3 | 3 | $4 = 1 \cdot 3 + 1$ |
| 3 | 2 | 2, already present | $3 = 1 \cdot 2 + 1$ |
| 2 | none | none | $2 \bmod 1 = 0$ and $2 \bmod 2 = 0$ |

Value $2$ is a dead end: it satisfies the bound but divides nothing of the form $x - 1$ that is legally usable, so once $2$ is present no further value can appear from it.

## 3. Day-by-day trace of `n = 5`

Simulating the rule with the placement table above produces the following history. Every newly placed value is recorded once, in the day it first appears.

| Day | New values placed | Board after the day | Distinct count |
|---|---|---|---|
| 0 (initial) | none, $5$ is given | $\{5\}$ | 1 |
| 1 | 2, 4 from $x = 5$ | $\{2,4,5\}$ | 3 |
| 2 | 3 from $x = 4$ | $\{2,3,4,5\}$ | 4 |
| 3 | none: $x = 3$ re-places $2$, $x = 2$ places nothing | $\{2,3,4,5\}$ | 4 |
| 4 through $10^9$ | none | $\{2,3,4,5\}$ | 4 |

After day 3 the board is a fixed point of the rule, and it stays one for the remaining $10^9 - 3$ days. Notice the shape of the history: $5$ produced the *jump* to $2$ and $4$, but the value that mattered next was $4$, which produced $3$. The board fills from the top down, one step of the descending chain at a time.

## 4. Why the final board is exactly $\{2, 3, \dots, n\}$

Two directions must be proved for $n \ge 2$, and together they are the correctness argument for the whole instance family.

- **Every value from $2$ to $n$ is reached.** Let $P(x)$ be the claim that $x$ lies on the board eventually, for $2 \le x \le n$. The value $n$ is given. If $x \ge 3$ is on the board, then $x - 1$ is legal to place because $x \bmod (x-1) = 1$ and $1 \le x - 1 \le n - 1 \le n$; so $P(x)$ implies $P(x-1)$. Descending induction from $P(n)$ gives $P(n-1), P(n-2), \dots, P(2)$. Concretely, the chain needs one day per step, so $n - 2$ days suffice, and $n - 2 \le 98 < 10^9$.
- **Nothing else is reached.** Every placed value $i$ is at least $2$, because $i = 1$ fails the modulo test, and at most $x - 1 \le n - 1$ for the value $x \ge 2$ that placed it. So the board is always a subset of $\{2, \dots, n\}$, and by the first direction that subset is exactly $\{2, \dots, n\}$.

The invariant that makes the second direction work is *every board value other than the initial $n$ is at least $2$ and strictly smaller than the value that placed it*. The chain $n \to n-1 \to \dots \to 2$ is therefore not merely one way to fill the board; it is the only set of values that can ever exist, and the process merely discovers them in descending order. Once $2$ appears, no rule application can place anything new, because $2$ is the smallest legal target and it produces nothing — so the board is frozen well before the stated horizon, and the count at day $10^9$ equals the count at day $n - 2$.

Counting the members of $\{2, \dots, n\}$ gives $n - 1$ values. The single exception is $n = 1$: the initial value is $1$, the rule places nothing since $1 \bmod 1 = 0$, and the board stays at one element. Both regimes are captured by

$$
\text{count}(n) = \max(1,\ n - 1),
$$

which yields $4$ for the traced instance, matching the required output, and which the boundary table below confirms at every legal extreme.

| $n$ | Final board | Count $\max(1, n-1)$ | Regime |
|---|---|---|---|
| 1 | $\{1\}$ | 1 | the only value is $1$, and $1$ can never be placed |
| 2 | $\{2\}$ | 1 | $2 \bmod 1 = 0$ and $2 \bmod 2 = 0$: nothing to add |
| 3 | $\{2,3\}$ | 2 | one descending step, $3 \to 2$ |
| 57 | $\{2, \dots, 57\}$ | 56 | 55 descending steps, all within the horizon |
| 100 | $\{2, \dots, 100\}$ | 99 | 98 descending steps, the largest legal input |

## 5. Traps this instance exposes

| Situation | Naive expectation | Actual behaviour | Where it bites |
|---|---|---|---|
| The value $1$ | it starts the descending chain | it can never be placed, since $x \bmod 1 = 0$ always | `n = 1` returns `1`, and every other $n$ omits $1$ |
| The $10^9$-day horizon | the loop must run that long | the board freezes after at most $n - 2$ days | iterating days is hopeless; the answer never changes again |
| Numbers larger than $n$ | new values might exceed the starting value | every placement is strictly smaller than its source | the board is bounded by $n$ |
| Only $n - 1$ is placed | the largest legal divisor is the whole story | $5$ also places $2$; several divisors can qualify | multiple values appear per day, so counting days is not counting values |
| The count for $n = 2$ | the chain still gives $2 - 1 = 1$ | it does, but for a different reason: nothing is placed at all | a "chain of length $n-2$" story breaks at the bottom |
| The formula | use $n - 1$ everywhere | $n - 1$ gives $0$ at $n = 1$ | the `max(1, ...)` guard is exactly the $n = 1$ repair |

The last row is the trap that costs the most: $n - 1$ is correct for every input except the smallest one, and the single legal input where it fails is the minimum of the constraint range.

## 6. Time and auxiliary space

The closed form $\max(1, n - 1)$ is a constant amount of arithmetic, so the running time is $\Theta(1)$ and the auxiliary space is $O(1)$: one comparison and one subtraction, with no board, no visited set, and no day counter.

For contrast, discovering the reachable set by simulation instead of by proof costs $O(n^2)$ time in the worst case, because each of the at most $n$ board values must be tested against the at most $n$ candidate divisors, and $O(n)$ space to store the board. That is easily fast enough for $n \le 100$, but only if the day loop is bounded by the day on which the last value appears — at most $n - 2$ productive days — rather than by the stated $10^9$. The formula wins on both axes by replacing the simulation with the two structural facts of Section 2: every addition is smaller than its source, and every value from $2$ to $n$ is forced by the descending chain.