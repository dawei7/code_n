# Guided Example: Consecutive Available Seats

`Cinema` holds one row per seat: `seat_id` is an auto-incrementing identifier and `free` is a two-valued flag, $1$ meaning the seat is available and $0$ meaning it is occupied. The task is to list every seat that belongs to a *consecutive available* group — a free seat with at least one free immediate neighbour — and to return the identifiers in ascending order. The generated tests are stated to contain more than two consecutively available seats, so a run longer than a pair is always present and the duplicate-suppression step is always exercised.

The instance below is the official seating chart, and it is well chosen: it contains an isolated free seat that must be rejected, a run of three that must be accepted in full, and a middle seat of that run that is matched twice by the naive pairwise reasoning.

## 1. Instance, Contract, and the Definition of Consecutive

The seating chart:

| `seat_id` | `free` | Reading |
|:---:|:---:|:---|
| $1$ | $1$ | Free, but isolated |
| $2$ | $0$ | Occupied |
| $3$ | $1$ | Free, next to seat $4$ |
| $4$ | $1$ | Free, next to seats $3$ and $5$ |
| $5$ | $1$ | Free, next to seat $4$ |

The required output:

| `seat_id` | Why it qualifies |
|:---:|:---|
| $3$ | Free, and seat $4$ is free |
| $4$ | Free, and both seat $3$ and seat $5$ are free |
| $5$ | Free, and seat $4$ is free |

### The rule, stated exactly

A seat $a$ qualifies if and only if **both** conditions hold:

1. $a.free = 1$ — the seat itself is available;
2. there exists a seat $b$ in the relation with $b.free = 1$ and $b.seat\_id = a.seat\_id \pm 1$ — at least one immediate neighbour is available.

The output column is `seat_id` alone, sorted ascending. Free-ness of the *neighbour* is checked, but the neighbour's identifier is not reported and does not appear in the result.

## 2. Adjacency as a Metric Predicate on Identifiers

Consecutiveness is a statement about the integer values of `seat_id`, not about the physical order of rows. Two seats are adjacent exactly when the absolute difference of their identifiers is one:

$$
\operatorname{adj}(a, b) \;\equiv\; \lvert a.seat\_id - b.seat\_id \rvert = 1 .
$$

Using the absolute value makes the predicate symmetric in its two arguments, so a single formulation captures both "the seat to my left" and "the seat to my right". Writing the relation twice under two names and pairing rows through that predicate turns the question into a search for neighbours, and the availability flags then act as an additional filter on the pair.

| Candidate adjacency predicate | Seats it considers neighbours of $4$ | Verdict |
|:---|:---|:---|
| $b.seat\_id = a.seat\_id + 1$ | $5$ only | Asymmetric — the left neighbour is invisible |
| $b.seat\_id = a.seat\_id - 1$ | $3$ only | Asymmetric in the other direction |
| $b.seat\_id = a.seat\_id \pm 1$ | $3$ and $5$ | Correct, but requires an explicit disjunction |
| $\lvert a.seat\_id - b.seat\_id \rvert = 1$ | $3$ and $5$ | Correct and direction-free |

The one-sided predicates are not merely inelegant; they are wrong on this instance. With only the "right neighbour" test, seat $3$ would be matched through $4$ and seat $4$ through $5$, but seat $5$ would find no seat $6$ and would be dropped even though it is plainly consecutive with seat $4$.

## 3. Neighbour-Existence Invariant

Let $F = \{\, s \;\mid\; s.free = 1 \,\}$ be the free seats, ordered by identifier, and let $N = \lvert \text{Cinema} \rvert$.

> **Neighbour-existence invariant.** A seat $a \in F$ qualifies if and only if it belongs to a maximal contiguous run of free seats whose length is at least $2$. Equivalently, if $R \subseteq F$ is a run $\{i, i+1, \dots, i+k-1\}$ of consecutive identifiers, then every seat of $R$ qualifies when $k \ge 2$, and none qualifies when $k = 1$.

The equivalence matters because it explains the shape of the answer. Inside a maximal run of length $k \ge 3$, the two end seats have exactly one free neighbour and the $k-2$ interior seats have two. The *qualifying set* is therefore the whole run regardless of how many neighbours each seat has, and the *match multiplicity* varies from one to two — a distinction that the next sections separate carefully, because conflating them is the source of duplicate output rows.

## 4. Worked Evaluation of the Official Auditorium

**Step 1 — Test each seat's neighbourhood.** For each seat, inspect the two identifier-adjacent rows and record whether either is free.

| Seat $a$ | $a.free$ | Left neighbour $a-1$ | Right neighbour $a+1$ | Free neighbour found? |
|:---:|:---:|:---|:---|:---|
| $1$ | $1$ | Absent from the relation | Seat $2$, $free = 0$ | No |
| $2$ | $0$ | Seat $1$, $free = 1$ | Seat $3$, $free = 1$ | Irrelevant — the seat itself is occupied |
| $3$ | $1$ | Seat $2$, $free = 0$ | Seat $4$, $free = 1$ | Yes, on the right |
| $4$ | $1$ | Seat $3$, $free = 1$ | Seat $5$, $free = 1$ | Yes, on both sides |
| $5$ | $1$ | Seat $4$, $free = 1$ | Absent from the relation | Yes, on the left |

Seat $1$ is free and has a neighbour, but that neighbour is occupied, so the neighbour test fails and seat $1$ is rejected. Seat $2$ has two free neighbours yet is occupied itself, so the first condition fails; this is why availability must be required of *both* members of the pair, not just one.

**Step 2 — Enumerate the qualifying pairs.** The predicate produces one matched pair for each (seat, free neighbour) combination.

| Matched pair $(a, b)$ | Seat $a$ it contributes | Run it belongs to |
|:---:|:---:|:---|
| $(3, 4)$ | $3$ | $\{3,4,5\}$ |
| $(4, 3)$ | $4$ | $\{3,4,5\}$ |
| $(4, 5)$ | $4$ | $\{3,4,5\}$ |
| $(5, 4)$ | $5$ | $\{3,4,5\}$ |

Four matched pairs. Seat $4$ appears twice because it is an interior seat of the run, which is exactly what the invariant predicts: interior seats have two neighbours.

**Step 3 — Project to the seat under test and collapse.** Projecting the first column of each pair gives the multiset $\{3, 4, 4, 5\}$. Collapsing duplicates yields the set

$$
\{3, 4, 5\},
$$

and ordering it ascending gives the required output. The collapse is not cosmetic: without it the result would hold four rows and would report seat $4$ twice, violating the one-row-per-seat reading of the answer.

## 5. Duplicate Elimination and the Required Ordering

The next table makes the multiplicity pattern explicit, since it is the only place where runs of different lengths behave differently.

| Maximal run of free seats | Length $k$ | End seats and their free neighbours | Interior seats and their free neighbours | Rows before collapse | Rows after collapse |
|:---|:---:|:---|:---|:---:|:---:|
| $\{3,4,5\}$ | $3$ | $3$ and $5$, one neighbour each | $4$, two neighbours | $4$ | $3$ |
| $\{1,2\}$ | $2$ | both seats, one neighbour each | none | $2$ | $2$ |
| $\{8\}$ | $1$ | the single seat, no free neighbour | none | $0$ | $0$ |

The required ordering by `seat_id` ascending is a genuine requirement rather than a formality: the qualifying set is produced by a grouping-like operation that has no inherent order, so the sequence must be imposed explicitly.

## 6. Gaps, Isolated Seats, and Short Runs

| Seating pattern | Qualifying seats | Why |
|:---|:---|:---|
| $\{1, 3, 5\}$ all free, no two adjacent | none | Every free seat is isolated; the empty result still carries the `seat_id` column |
| $\{1, 2, 3\}$ all free | $1, 2, 3$ | A run of three: the ends qualify through one neighbour each, the middle through two |
| $\{1, 2\}$ free, $\{3\}$ occupied | $1, 2$ | A minimal run of length two qualifies in full |
| $\{1\}$ free, $\{2\}$ occupied | none | A run of length one never qualifies, however the seat is surrounded |
| Identifiers $\{3, 4\}$ and $\{7, 8\}$ free, nothing between | $3, 4, 7, 8$ | Adjacency is a difference of one; the gap from $4$ to $7$ is three and does not connect |
| Occupied seats in the middle of a long free stretch | the two sub-runs | An occupied seat splits a run; each resulting run is judged on its own length |

The fifth row is the sharpest trap. Because `seat_id` is an auto-increment column, identifiers are dense in a freshly loaded chart — but the relation may be loaded with gaps, and the predicate is defined on values rather than on row positions. Two free seats at $4$ and $7$ are *not* consecutive merely because no row sits between them; their difference is three. Any formulation that ranks rows and compares ranks instead of identifiers would silently join them.

**Elimination of tempting alternatives.**

| Alternative | Why it attracts | Why it fails or costs more |
|:---|:---|:---|
| Testing only the right neighbour | One simple equality, no absolute value | Drops the last seat of every run, as seat $5$ above demonstrates |
| Testing only the left neighbour | Symmetric flaw, equally simple | Drops the first seat of every run |
| Omitting the duplicate collapse | The pair enumeration is otherwise correct | Reports interior seats once per neighbour, so seat $4$ appears twice |
| Requiring *both* neighbours to be free | Reads as "really consecutive" | Rejects the end seats of every run, so a run of three would yield only its middle seat |
| Looking for runs of three or more | Confuses "consecutive" with "long enough" | A run of exactly two is consecutive and must be returned in full |
| Comparing row ranks instead of identifiers | Avoids arithmetic on `seat_id` | Joins seats across identifier gaps that are not adjacent |

## 7. Cost of the Method

Let $N$ be the number of rows in `Cinema` and $K$ the number of qualifying seats, so $K \le N$.

**Time complexity.** With an index or hash structure on `seat_id`, each seat probes at most two candidate neighbours, so the neighbour search is $O(N)$ expected: the work per row is bounded by a constant and does not depend on how many seats exist. Collapsing the $O(N)$ matched pairs is likewise $O(N)$ with a hash set. Imposing the required order costs $O(K \log K)$ for a comparison sort. Because $K \le N$,

$$
O(N) + O(N) + O(K \log K) = O(N \log N),
$$

and the bound is the safe one to quote whenever a sort is present. If the order could be obtained for free — for instance when the relation is already read in ascending `seat_id` order and the collapse preserves that order — the total drops to $O(N)$, since no other step is superlinear.

**Auxiliary-space complexity.** The method keeps the identifiers of the qualifying seats, $O(K)$, together with the hash structure used to suppress duplicates, which is also $O(K)$ because it holds at most one entry per distinct qualifying seat. The matched-pair stream itself need not be materialized: pairs can be consumed as they are produced. A window-based formulation that examines only the previous and next seat keeps just $O(1)$ additional state beyond the output, which is the minimum possible for a method that must still emit $K$ identifiers.
