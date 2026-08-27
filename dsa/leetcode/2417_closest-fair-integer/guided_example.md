# Guided Example: Closest Fair Integer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 100000}`
- **Required output:** `100011`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **positive** integer `n`.

The objective is to compute `100011` from `{"n": 100000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What makes an integer fair

An integer is fair when its decimal representation contains the same number of even and odd digits. Zero is an even digit. Because every digit belongs to exactly one of the two groups, a fair integer must have an even total number of digits. This observation explains the solution's important shortcut for an odd-length input.

The exact protected solution is a recursive candidate search with an odd-length jump. It does not implement the bounded digit-construction algorithm described by the variant summary, so its real behavior and costs must be understood from the code itself. Each call counts the odd digits in `a`, the even digits in `b`, and the number of digits in `k`. It does so by repeatedly inspecting `t % 10` and removing that last digit with `t //= 10`.

The test `(t % 10) & 1` is 1 precisely when the last digit is odd. In that case `a` increases; otherwise `b` increases. Since the input is positive, the loop runs once for every decimal digit. After it ends, `a + b = k`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 100000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an odd digit count permits a direct jump

If `k` is odd, no `k`-digit number can be fair: splitting an odd number of digit positions into two equal integer counts is impossible. Therefore the answer must have more than `k` digits. The smallest possible next length is `k + 1`, which is even.

The code sets `x = 10**k`. Its decimal form is a leading `1` followed by `k` zeros, so it is the smallest number with `k + 1` digits. At this point it has one odd digit and `k` even digits. The code then constructs

`y = int('1' * (k >> 1) or '0')`.

Because `k` is positive and odd for every valid call reaching this branch, `k >> 1` is $\lfloor k/2 \rfloor$. Adding this suffix-sized number turns the last $\lfloor k/2 \rfloor$ zeros of `x` into ones without carrying. The result consists of a leading one, then $\lceil k/2 \rceil$ zeros, then $\lfloor k/2 \rfloor$ ones. Since $k$ is odd, the total number of ones is

$$
1 + \left\lfloor \frac{k}{2} \right\rfloor
= \frac{k+1}{2},
$$

and the number of zeros is also $(k+1)/2$. The constructed number is therefore fair.

It is also the smallest fair number of that new length. Every number with `k + 1` digits must begin with at least `1`. Choosing leading `1` is smallest. A fair result then needs $(k+1)/2 - 1$ additional odd digits and $(k+1)/2$ even digits. To minimize the remaining decimal positions lexicographically, all required even digits should be `0` and should appear as early as possible; the smallest usable odd digit is `1`, placed in the remaining suffix. Thus the returned pattern is minimal. For example, a three-digit candidate jumps to `1001`, the smallest fair four-digit integer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `k` is odd, no `k`-digit number can be fair: splitting an... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What happens when the length is even

If `k` is even and `a == b`, the current `n` is already fair. Because the problem allows an answer equal to `n`, returning it is immediately optimal.

If the counts differ, the code calls `closestFair(n + 1)`. That recursive call performs the same digit count on the next integer. Repeating this operation tests consecutive values in strictly increasing order. Let `f` be the first fair integer at least as large as the original input. Every tested value before `f` is explicitly found not to be fair; when `f` is reached, the equality branch returns it. Hence no smaller valid candidate could have been skipped.

There is one transition worth following carefully. An even-length search can increment past a number made entirely of nines. The next value then has odd length. Rather than continuing through an entire digit-length range that contains no fair number, the odd-length branch jumps directly to the smallest fair number of the following even length. For instance, `99` is not fair. The recursion tests `100` next, recognizes its odd length, and returns `1001`.

The recursive search is therefore correct: the digit-count branch accepts exactly fair candidates; consecutive increments preserve minimality while the length is even; and the odd-length construction skips only numbers that cannot possibly be fair and lands on the smallest feasible number of the next length.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `100011` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 100000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `100011` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Bounded digit construction:** Build the smalle:** - **Bounded digit construction:** Build the smallest decimal string at least `str(n)` with exactly half even and half odd digits, using a tight-prefix state and feasibility checks for the remaining counts. This avoids walking through the numeric gap and can achieve the intended polynomial-in-$d$ behavior, but it needs careful handling of the leading digit and backtracking when a chosen digit makes the suffix impossible.
- **Digit dynamic programming:** A memoized state such as position, remaining odd digits, and whether the prefix is still equal to the lower bound can determine feasibility, after which digits are greedily reconstructed from smallest to largest. This is more involved but matches the manifest's constructive description much better than the exact recursive enumeration.
- **Iterative enumeration:** A `while` loop that increments `n` until it is fair preserves the exact search logic while avoiding `RecursionError`. It still may inspect many candidates and therefore does not solve the time-complexity weakness.
- **Odd number of digits:** No value of that same length can be fair. The direct pattern of zeros followed by the required ones is both fair and the smallest feasible longer value.
- **Already fair:** The equality check returns `n` itself, which matters because the contract asks for greater than or equal to `n`, not strictly greater.
- **Digit zero:** Zero must count as even. The parity expression correctly classifies it that way whenever it occurs inside the positive integer.
- **One-digit input:** Every one-digit positive integer has one odd or one even digit and cannot be fair. The shortcut returns `10`, whose digits have opposite parity.
- **Carry across a power of ten:** Incrementing values such as `99` changes the digit count. The next recursive call recomputes all counts from scratch, so the odd-length shortcut is applied correctly.
- **Maximum stated input:** `10^9` has ten digits and is processed by the even-length branch. The answer may exceed the input constraint because the constraint limits only the argument, not the returned integer.
- **Manifest mismatch:** The local metadata says $O(d^2)$ time and space, but those bounds should not be used to reason about this exact Python file. Its candidate enumeration and recursive depth are observable parts of the implementation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d$ be the number of decimal digits of a candidate, and let $G$ be the number of consecutive non-fair even-length candidates examined before the search returns or reaches an odd-length shortcut. Counting one candidate's digits costs $O(d)$ time. The exact solution therefore takes $O(Gd)$ time in the search phase, plus $O(d)$ time to build the shortcut suffix. This is not the $O(d^2)$ time claimed in the local variant manifest.
- **Auxiliary Space Complexity:** $O(G + d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
