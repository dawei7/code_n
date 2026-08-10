## General

**Separate the one-passenger case**

When \(n=1\), there is one passenger and one seat. The first passenger’s random choice has only one option, so the probability of getting the assigned seat is exactly one. This is why the exact code returns `1` for `n == 1`.

For every \(n\geq2\), the surprising result is always one half. The value does not approach one or zero as the airplane grows because the displacement process has a symmetry between two special seats.

**What happens after the first choice**

Label passengers and their assigned seats from 1 through \(n\). Passenger one chooses uniformly among all seats.

- If passenger one chooses seat 1, every later passenger finds their own seat available. Passenger \(n\) gets seat \(n\), so this branch is a success.
- If passenger one chooses seat \(n\), the final passenger’s seat is already occupied. This branch is a failure.
- If passenger one chooses some intermediate seat \(k\), passengers 2 through \(k-1\) take their own seats. Passenger \(k\) then finds seat \(k\) occupied and must choose randomly among the remaining seats.

In the third case, passenger \(k\) becomes the new “displaced” passenger. Seats belonging to passengers before \(k\), apart from seat 1, are no longer relevant. The same type of process continues on a smaller set of available seats.

**Only two absorbing outcomes matter**

During this chain of displaced passengers, consider the moment when someone must choose randomly. Among the available seats are:

- seat 1, the original first passenger’s assigned seat;
- seat \(n\), the final passenger’s assigned seat;
- possibly some seats belonging to later intermediate passengers.

Choosing an intermediate seat merely passes the displacement to that seat’s owner later. The process continues. It stops in one of two decisive ways:

- someone chooses seat 1, after which the displacement chain ends and all later passengers, including passenger \(n\), get their own seats;
- someone chooses seat \(n\), after which passenger \(n\) cannot get the assigned seat.

Until one of those special seats is selected, both remain available and play symmetric roles in the random choice set. Every chain that first ends at seat 1 has a corresponding chain with the two special seat labels exchanged that first ends at seat \(n\), with the same probability. Therefore, each absorbing outcome has probability one half.

**An induction that makes the constant result explicit**

Let \(P(n)\) be the probability that the last passenger gets the assigned seat in an \(n\)-passenger instance.

Passenger one has \(n\) equally likely choices. Choosing seat 1 contributes success probability one. Choosing seat \(n\) contributes zero. If seat \(k\) is chosen for \(2\leq k\leq n-1\), the remaining displacement process is equivalent to a smaller instance with \(n-k+1\) relevant passengers and seats. Therefore,

\[
P(n)=\frac{1+\sum_{m=2}^{n-1}P(m)}{n}.
\]

The base values are \(P(1)=1\) and \(P(2)=1/2\). Assume \(P(m)=1/2\) for every \(2\leq m<n\). There are \(n-2\) terms in the sum, so

\[
P(n)
=\frac{1+(n-2)/2}{n}
=\frac{n/2}{n}
=\frac12.
\]

By induction, every \(n\geq2\) has probability one half.

**A concrete three-passenger trace**

With three passengers, passenger one chooses each seat with probability one third.

- Seat 1 leads to success.
- Seat 3 leads to failure.
- Seat 2 displaces passenger two. The remaining available seats are 1 and 3, chosen with equal probability. Seat 1 leads to success and seat 3 to failure.

The total success probability is

\[
\frac13+\frac13\cdot\frac12=\frac12.
\]

Adding more passengers adds more ways to pass the displacement forward, but it does not favor seat 1 over seat \(n\). That is why the final probability remains constant.

**Why direct simulation is unnecessary**

A randomized simulation could estimate the probability, but the problem asks for the exact value. Simulation would introduce sampling error and require many trials, while the symmetry and recurrence give a closed form immediately.

Likewise, a dynamic-programming array could compute \(P(1),P(2),\ldots,P(n)\), but once the induction establishes that every value after the first is identical, storing or iterating through those values has no purpose. The exact source expresses the closed form directly:

`return 1 if n == 1 else 0.5`.

Python returns an integer in the first branch and a floating-point number in the second. An integer one is numerically equal to floating-point `1.0` and is accepted for the required probability result.

**Why the answer does not depend on intermediate seating details**

Passengers who find their own seats free act deterministically and cannot affect the outcome. Only displaced passengers make random choices. Each intermediate choice transfers the same uncertainty to a later passenger, while the two special seats remain the ultimate success and failure endpoints.

The random-choice sets shrink over time, but both special seats survive together until one is chosen. This shared survival is the key symmetry; simply saying “there are two seats left” would be misleading because the process can end before literally only two physical seats remain.

## Complexity detail

The method performs one comparison and returns one of two constants. Its time complexity is \(O(1)\), independent of \(n\), and its auxiliary space complexity is \(O(1)\).

The mathematical derivation may reason about many passengers, but the implemented computation does not simulate them or allocate any collection. The input bound \(n\leq10^5\) therefore has no effect on runtime or memory.

## Alternatives and edge cases

- **Iterative probability DP:** Evaluate the recurrence for every size up to \(n\). It can be made \(O(n)\) time and \(O(1)\) space with a running sum, but the closed form makes all iterations redundant.
- **State simulation:** Model occupied seats and displaced passengers exactly. Exact enumeration grows rapidly, while Monte Carlo simulation only estimates the answer and can be inaccurate.
- **Symmetry proof:** Pair displacement histories that terminate at seat 1 with histories terminating at seat \(n\). This gives the same one-half result without writing the recurrence.
- **One passenger:** This is the only exception. The sole passenger must take the sole seat, so the probability is one.
- **Two passengers:** The first passenger chooses between seats 1 and 2 uniformly, making the result one half directly.
- **Large \(n\):** The result is still exactly one half. No convergence approximation or floating-point accumulation is involved.
- **Uniform random choice assumption:** The proof requires each displaced passenger to choose uniformly among currently available seats, as stated. A biased choice rule could break the symmetry and change the answer.
- **Seat and passenger numbering:** The proof singles out the first passenger’s seat and the final passenger’s seat. Intermediate labels affect only how the displacement is passed onward.
- **Return representation:** `0.5` is exactly representable in binary floating point. The first branch’s integer `1` is numerically the required probability `1.0`.
