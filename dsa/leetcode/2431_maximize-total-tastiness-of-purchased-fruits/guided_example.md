# Guided Example: Maximize Total Tastiness of Purchased Fruits

## 1. The Instance and the Three-Way Choice

Consider the instance in which the fruits are priced and rated as follows, the shopping
budget is `maxAmount = 10`, and at most `maxCoupons = 2` coupons may be used.

| Fruit index $i$ | `price[i]` | Coupon price $\lfloor \text{price}[i]/2 \rfloor$ | `tastiness[i]` |
|---|---|---|---|
| 0 | 10 | 5 | 5 |
| 1 | 15 | 7 | 8 |
| 2 | 7 | 3 | 20 |

The coupon price of fruit $1$ is $\lfloor 15/2 \rfloor = 7$, not $7.5$ and not $8$: the
problem rounds the discount down to the nearest integer, and fruit $1$ is the only
odd-priced fruit in this instance.

The authored answer for `price = [10, 15, 7]`, `tastiness = [5, 8, 20]`,
`maxAmount = 10`, `maxCoupons = 2` is `28`. Every fruit may be bought at most once, a
coupon may be applied to a given fruit at most once, and the discounted price is always
the floor of half the list price. Spending less than the budget and leaving coupons unused
are both allowed, because the goal is tastiness rather than thrift.

For each fruit there are exactly three mutually exclusive decisions: skip it, buy it at
full price, or buy it once with a coupon. That three-way branch per fruit is the whole
difficulty — the choices are coupled through two shared resources, money and coupons, so a
locally attractive fruit can crowd out two better ones.

## 2. Why a State Needs Three Coordinates

A decision for fruit $i$ consumes budget and possibly a coupon, and both resources are
shared with every later fruit. Histories that reach the same position with the same
remaining budget and the same remaining coupon count are therefore interchangeable: the
fruit indices already decided cannot be revisited, so nothing else about the past matters.

This motivates the state

$$
G(i, b, k) \;=\; \text{maximum additional tastiness obtainable from fruits } i, i+1, \dots, n-1
$$

given $b$ units of remaining budget and $k$ remaining coupons. The required answer is
$G(0, \text{maxAmount}, \text{maxCoupons})$. The base case is $G(n, b, k) = 0$ for every
budget and coupon count, because no fruit remains.

The transition is the maximum over the three admissible decisions:

$$
G(i,b,k) = \max \begin{cases}
G(i+1,\, b,\, k) & \text{skip fruit } i \\[2pt]
G(i+1,\, b - \text{price}[i],\, k) + \text{tastiness}[i] & \text{buy at full price, if } b \ge \text{price}[i] \\[2pt]
G(i+1,\, b - \lfloor \text{price}[i]/2 \rfloor,\, k-1) + \text{tastiness}[i] & \text{buy with a coupon, if } k \ge 1 \text{ and } b \ge \lfloor \text{price}[i]/2 \rfloor
\end{cases}
$$

Every branch advances the index from $i$ to $i+1$, which is exactly what enforces the
"at most one purchase per fruit" rule. The coupon branch is the only one that changes $k$,
which enforces "at most one coupon per fruit". A branch whose affordability test fails is
simply absent from the maximum, not merely unattractive.

## 3. Enumerating the Reachable States

The states below are the ones the recursion actually visits for this instance. Budgets are
listed as they are consumed, and each row collects the three candidate values before the
maximum is taken. Illegal branches are marked because they are conditioned out entirely.

| State $(i,b,k)$ | Fruits still available | Skip candidate | Full-price candidate | Coupon candidate | $G$ |
|---|---|---|---|---|---|
| $(3,\cdot,\cdot)$ | none | — | — | — | 0 |
| $(2,0,2)$ | fruit 2 | 0 | illegal ($7 > 0$) | illegal ($3 > 0$) | 0 |
| $(2,3,1)$ | fruit 2 | 0 | illegal ($7 > 3$) | $G(3,0,0) + 20 = 20$ | 20 |
| $(2,5,1)$ | fruit 2 | 0 | illegal ($7 > 5$) | $G(3,2,0) + 20 = 20$ | 20 |
| $(2,10,1)$ | fruit 2 | 0 | $G(3,3,1) + 20 = 20$ | $G(3,7,0) + 20 = 20$ | 20 |
| $(2,10,2)$ | fruit 2 | 0 | $G(3,3,2) + 20 = 20$ | $G(3,7,1) + 20 = 20$ | 20 |
| $(1,0,2)$ | fruits 1, 2 | $G(2,0,2) = 0$ | illegal ($15 > 0$) | illegal ($7 > 0$) | 0 |
| $(1,3,1)$ | fruits 1, 2 | $G(2,3,1) = 20$ | illegal ($15 > 3$) | illegal ($7 > 3$) | 20 |
| $(1,5,1)$ | fruits 1, 2 | $G(2,5,1) = 20$ | illegal ($15 > 5$) | illegal ($7 > 5$) | 20 |
| $(1,10,1)$ | fruits 1, 2 | $G(2,10,1) = 20$ | illegal ($15 > 10$) | $G(2,3,0) + 8 = 8$ | 20 |
| $(1,10,2)$ | fruits 1, 2 | $G(2,10,2) = 20$ | illegal ($15 > 10$) | $G(2,3,1) + 8 = 28$ | 28 |
| $(0,10,2)$ | all three | $G(1,10,2) = 28$ | $G(1,0,2) + 5 = 5$ | $G(1,5,1) + 5 = 25$ | 28 |

Two rows deserve attention. State $(1,10,1)$ shows a coupon spent early being wasted: with
one coupon left, using it on fruit $1$ leaves nothing for fruit $2$, so the best continuation
is $8$ rather than $28$. State $(1,10,2)$ shows the opposite: with two coupons the discounted
purchase of fruit $1$ costs $7$, leaving exactly $3$, the discounted price of fruit $2$. The
budget lands on zero by coincidence of this instance, not by rule.

## 4. The Optimal Purchase Plan

Following the argmax choices from the initial state produces the optimal plan.

| Fruit | Decision | Spend | Budget after | Coupons after | Cumulative tastiness |
|---|---|---|---|---|---|
| 0 | skip | 0 | 10 | 2 | 0 |
| 1 | buy with coupon | 7 | 3 | 1 | 8 |
| 2 | buy with coupon | 3 | 0 | 0 | 28 |

Fruit $0$ is the cheapest fruit in the list, and it is skipped anyway. Its tastiness of $5$
is the smallest, and spending $10$ on it — or even $5$ with a coupon — leaves too little for
the pair of fruits that together yield $28$. This is the concrete reason the skip branch must
be present even though all tastiness values are non-negative.

## 5. Comparing the Competing Plans

Enumerating the feasible subsets makes the optimality claim checkable by hand. Since
`maxAmount = 10` and every full price except fruit $0$ exceeds the budget, only two
feasible plans actually use two fruits.

| Plan (fruits, purchase mode) | Coupons used | Total spend | Feasible? | Total tastiness |
|---|---|---|---|---|
| none | 0 | 0 | yes | 0 |
| fruit 1 with coupon | 1 | 7 | yes | 8 |
| fruit 2 with coupon | 1 | 3 | yes | 20 |
| fruit 2 at full price | 0 | 7 | yes | 20 |
| fruit 0 at full price | 0 | 10 | yes | 5 |
| fruit 0 with coupon, fruit 2 with coupon | 2 | 8 | yes | 25 |
| fruit 1 with coupon, fruit 2 with coupon | 2 | 10 | yes | 28 |
| fruit 0 with coupon, fruit 1 with coupon | 2 | 12 | no, exceeds budget | — |
| fruit 1 at full price | 0 | 15 | no, exceeds budget | — |
| fruit 1 at full price, fruit 2 with coupon | 1 | 18 | no, exceeds budget | — |
| any plan using three fruits | ≥ 1 | ≥ 15 | no, exceeds budget | — |

The closest rival is `fruit 0 with coupon, fruit 2 with coupon`, worth $25$ for a spend of
$8$. It has budget left over but nothing left to buy: the remaining $2$ units cannot
purchase fruit $1$ even at the discounted price of $7$. The winning plan converts the
remaining budget into $8$ extra tastiness.

## 6. Why the Recurrence Is Correct

**Invariant.** Every call $G(i, b, k)$ returns the maximum tastiness obtainable from the
suffix of fruits starting at $i$, subject to a budget of $b$ and $k$ coupons.

**Soundness.** Each branch of the transition corresponds to a legal decision for fruit $i$:
skipping spends nothing and uses no coupon; the full-price branch is offered only when
$b \ge \text{price}[i]$; the coupon branch is offered only when $k \ge 1$ and the budget
covers $\lfloor \text{price}[i]/2 \rfloor$. The returned continuation $G(i+1, \cdot, \cdot)$
is itself a legal plan for the remaining fruits by induction, so the concatenation is a
legal plan and the stated value is attainable.

**Completeness.** Take any legal plan for the state $(i, b, k)$. Its decision for fruit $i$
is exactly one of skip, full-price, or coupon — there is no fourth option, and the plan
cannot buy the fruit twice or apply two coupons to it. Each case matches one branch, and
the rest of the plan is legal for the corresponding successor state, so its remaining
tastiness is at most the value returned by that successor. Hence the plan's total is at most
the maximum of the three branches. Taking the maximum over all legal plans gives equality.

**Well-foundedness and memoisation.** Every recursive call moves from $i$ to $i+1$, so the
recursion depth is at most $n$ and the base case $i = n$ is always reached. Different
histories that share the triple $(i, b, k)$ have identical subproblems, so computing each
triple once and reusing the result is exact rather than an approximation.

## 7. Boundary and Degenerate Instances

| Situation | Input | What the recurrence does | Output |
|---|---|---|---|
| Zero budget with zero-priced fruits | `price = [0, 5, 0]`, `tastiness = [4, 9, 6]`, `maxAmount = 0`, `maxCoupons = 1` | full-price purchase of a zero-priced fruit is affordable forever, and the maximum prefers it over wasting a coupon | 10 |
| No coupons at all | `price = [4, 5, 7]`, `tastiness = [6, 8, 12]`, `maxAmount = 9`, `maxCoupons = 0` | the coupon branch is never offered, leaving ordinary 0/1 knapsack | 14 |
| Odd price and exact budget | `price = [7, 8]`, `tastiness = [10, 11]`, `maxAmount = 3`, `maxCoupons = 1` | $\lfloor 7/2 \rfloor = 3$ is affordable while $\lfloor 8/2 \rfloor = 4$ is not | 10 |
| Nothing affordable | `price = [5, 9]`, `tastiness = [7, 13]`, `maxAmount = 1`, `maxCoupons = 1` | every branch is either illegal or worth zero, so the empty plan wins | 0 |
| Coupons left unused | `price = [2, 100, 100]`, `tastiness = [5, 1, 1]`, `maxAmount = 2`, `maxCoupons = 5` | the full-price purchase costs $2$ and gains $5$; the objective never rewards spending coupons | 5 |
| Zero tastiness | `price = [0, 0, 3]`, `tastiness = [0, 0, 7]`, `maxAmount = 1`, `maxCoupons = 1` | buying a zero-tastiness fruit cannot beat skipping it, and the maximum is unaffected | 7 |

Two semantic traps surface here. First, the affordability test for the coupon branch uses
the **discounted** price, so a coupon can unlock a fruit whose full price is far beyond the
budget. Second, the discount uses floor division per fruit: a discount of $15$ never rounds
to $8$, and applying one "half the total" discount to a basket would give different and
incorrect answers.

## 8. Alternative Methods and Their Costs

| Alternative | Idea | Trade-off |
|---|---|---|
| Greedy by tastiness | Buy the most tasty affordable fruit first | Ignores price entirely: it can select an expensive fruit and block two cheaper ones |
| Greedy by tastiness per unit price | Buy the best ratio first, repeat | Not valid for 0/1 knapsack. With prices `[6, 5, 5]`, tastiness `[6, 4, 4]`, and budget `10`, ratio greedy takes the ratio-1.0 fruit for tastiness 6, then cannot afford anything else, while the optimum takes both ratio-0.8 fruits for tastiness 8 |
| Descending 2-D knapsack over (coupons, budget) | Iterate both resource dimensions downward for each fruit | Same $O(nBK)$ time but only $O(BK)$ space; the index dimension disappears, at the cost of careful descending order to preserve the 0/1 rule |
| Enumerate all $3^{n}$ decision vectors | Try every skip/full/coupon combination | Exponential in $n$; the memoised recurrence collapses the histories that share remaining resources |
| Treat the coupon as a global discount | Halve the total spend at the end | Wrong: coupons are per fruit, limited in number, and rounded down per fruit |
| Ignore the coupon dimension | Solve 0/1 knapsack with full prices only | Loses every plan that uses a coupon, including the optimal plan of this instance |

## 9. Complexity Derivation

Let $n$ be the number of fruits, $B = \text{maxAmount}$, and $K = \text{maxCoupons}$.

**Time.** The state is the triple $(i, b, k)$ with $0 \le i \le n$, $0 \le b \le B$, and
$0 \le k \le K$, so there are at most $(n+1)(B+1)(K+1)$ distinct states. Each state
evaluates at most three branches, each doing one subtraction, one comparison, and one
addition, so each state costs $O(1)$ and the total is

$$
O(n \, B \, K).
$$

For the stated constraints $n \le 100$, $B \le 1000$, and $K \le 5$, that is at most
$101 \cdot 1001 \cdot 6 \approx 6.1 \times 10^{5}$ states — comfortably small.

**Auxiliary space.** Memoising one integer per reachable triple costs

$$
O(n \, B \, K)
$$

space, and the recursion stack adds $O(n)$ frames, which is dominated by the table whenever
the state space is well populated. An iterative formulation that keeps only the coupon and
budget dimensions while sweeping the fruit index reduces the table to $O(BK)$ space at the
same time cost, because a state at fruit $i$ depends only on fruit $i+1$. The output itself
is a single integer, so it adds no auxiliary space.
