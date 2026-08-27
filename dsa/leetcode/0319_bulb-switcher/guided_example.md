# Guided Example: Bulb Switcher

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000000000}`
- **Required output:** `31622`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

The objective is to compute `31622` from `{"n": 1000000000}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Replace the round-by-round story with a question about one bulb.

Simulating the switches is tempting: round `1` touches every bulb, round `2` touches bulbs `2, 4, 6, ...`, and so on. That view follows the statement literally, but it hides the useful pattern and would perform far too much work when $n$ can be as large as $10^9$. Instead, fix one bulb position $k$ and ask exactly which rounds toggle that bulb.

Round $i$ toggles every bulb whose position is a multiple of $i$. Therefore, it toggles bulb $k$ precisely when $i$ divides $k$. For example, bulb `12` is touched in rounds `1`, `2`, `3`, `4`, `6`, and `12`, because those are exactly the positive divisors of `12`. This gives a direct translation:

- the number of times bulb $k$ is toggled equals the number of positive divisors of $k$;
- a bulb that starts off ends on after an odd number of toggles;
- a bulb that starts off ends off after an even number of toggles.

The final state of bulb $k$ therefore depends only on whether $k$ has an odd or even number of positive divisors. We no longer need to model the individual rounds.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000000000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why almost every divisor has a partner.

Whenever $d$ divides $k$, the quotient $k/d$ is also a divisor, and the two values multiply to $k$. Thus divisors naturally form pairs

$$
(d, k/d).
$$

For `12`, the pairs are `(1, 12)`, `(2, 6)`, and `(3, 4)`. Every pair contains two different divisors, so there are six divisors in total—an even count. Pairing is exactly what matters because each two-member pair contributes two toggles, and two toggles cancel: off becomes on and then off again, or on becomes off and then on again.

There is only one way for such a pair not to contain two different values. Its two members are equal when

$$
d = k/d,
$$

which is equivalent to

$$
d^2 = k.
$$

That happens precisely when $k$ is a perfect square. For example, the divisor pairs of `16` are `(1, 16)`, `(2, 8)`, and `(4, 4)`. The first two pairs contribute four distinct divisors, while the last pair contributes only the single divisor `4`. Consequently, `16` has five positive divisors and is toggled five times. It finishes on.

If $k$ is not a perfect square, no divisor can be paired with itself. Every divisor belongs to a distinct two-member pair, so the divisor count is even and bulb $k$ finishes off. If $k$ is a perfect square, exactly one divisor—$sqrt{k}$—is self-paired. All other divisors still cancel in pairs, leaving one unpaired toggle, so bulb $k$ finishes on. This proves the complete characterization:

> After all rounds, the bulbs that remain on are exactly the bulbs at perfect-square positions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Whenever $d$ divides $k$, the quotient $k/d$ is also a divis... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count squares instead of examining bulbs.

The remaining problem is simply to count perfect squares in the inclusive interval from `1` through `n`. They are

$$
1^2, 2^2, 3^2, \ldots, m^2,
$$

where $m$ is the largest nonnegative integer satisfying $m^2 \le n$. By definition,

$$
m = \lfloor \sqrt{n} \rfloor.
$$

There is one square for every integer base from `1` through $m$, so there are exactly $m$ surviving bulbs. This is why the method returns the integer part of `sqrt(n)` directly. It is not estimating how many bulbs survive; it is counting the square positions through a one-to-one correspondence between bases $j$ and positions $j^2$.

For `n = 10`, the integer square root is `3`. The square positions are `1`, `4`, and `9`, so three bulbs remain on. Bulb `1` is toggled in round `1`; bulb `4` is toggled in rounds `1`, `2`, and `4`; bulb `9` is toggled in rounds `1`, `3`, and `9`. Each has an odd toggle count. A nonsquare such as bulb `10` is toggled in rounds `1`, `2`, `5`, and `10`, an even count, and ends off.

The boundary between consecutive answers is also useful for understanding the floor. If `n = 24`, then $\lfloor\sqrt{24}\rfloor = 4$, accounting for `1`, `4`, `9`, and `16`. At `n = 25`, the answer increases to `5` because `25 = 5^2` becomes available. It remains `5` for every `n` from `25` through `35`, then increases at `36 = 6^2`. The answer changes only when the range gains another perfect square.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `31622` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000000000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `31622` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Direct round simulation:** Store `n` Boolean b:** - **Direct round simulation:** Store `n` Boolean bulb states and toggle every `i`-th entry during round `i`. This mirrors the statement and can help discover the pattern on tiny examples, but it requires $O(n \log n)$ total toggles and $O(n)$ storage. It is infeasible near $n = 10^9$ and ignores the divisor structure.
- **- **Count divisors for every bulb:** For each posi:** - **Count divisors for every bulb:** For each position $k$, enumerate divisors up to $\sqrt{k}$ and decide whether the divisor count is odd. This eventually identifies the same perfect squares, but repeats work for every bulb and is much slower than using the proven square characterization directly.
- **- **Check every candidate square:** Increment `j` :** - **Check every candidate square:** Increment `j` while $j^2 \le n$ and count the iterations. This uses $O(1)$ space and is easy to reason about, but it takes $O(\sqrt{n})$ time. The count reached by that loop is exactly $\lfloor\sqrt{n}\rfloor$, which the optimal source obtains in one fixed-size numeric operation.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $n$ be both the number of bulbs and the number of rounds described by the problem. The implementation performs one square-root operation and one conversion to an integer. Under the problem's bounded integer domain, $0 \le n \le 10^9$, these are fixed-size machine-number operations, so the time complexity is $O(1)$. The running time does not grow by iterating through the $n$ bulbs or the $n$ rounds; there is no such iteration in the source.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
