# Guided Example: Building H2O

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"water": "HOH"}`
- **Required output:** `"HHO"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are two kinds of threads: `oxygen` and `hydrogen`. Your goal is to group these threads to form water molecules.

The objective is to compute `"HHO"` from `{"water": "HOH"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The intended permit budget for one molecule

One water molecule needs exactly two hydrogen callbacks and one oxygen callback. The protected implementation starts `h` with two permits and `o` with zero.

At the intended high level, two hydrogen threads consume the two hydrogen permits. Once both have printed, one oxygen permit should be released. Oxygen consumes it, prints, and releases two new hydrogen permits for the next molecule.

This creates molecule-sized rounds without explicitly assigning thread identities to a molecule.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"water": "HOH"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Hydrogen’s intended role

Each hydrogen call acquires one `h` permit before invoking `releaseHydrogen`. Since only two permits exist at the beginning of a round, a third hydrogen thread cannot pass until oxygen finishes the round and replenishes them.

After printing, the code checks `h._value == 0`. The intention is that the hydrogen which observes both permits consumed is the second hydrogen and should release one oxygen permit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Each hydrogen call acquires one `h` permit before invoking `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Oxygen’s intended role

Oxygen waits on `o.acquire()`. With an initial count of zero, it cannot print before some hydrogen call releases permission.

After oxygen prints, `h.release(2)` restores two hydrogen permits. The next pair can then proceed. If exactly one oxygen permit were created per pair, the logical output would divide into groups containing two H values and one O value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"HHO"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"water": "HOH"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"HHO"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Reusable barrier:** Admit exactly two hydrogen:** - **Reusable barrier:** Admit exactly two hydrogen threads and one oxygen thread, then release the group together. This directly models molecule formation.
- **Mutex-protected counter:** Update hydrogen completion count under a lock and let exactly the transition from one to two release oxygen. Reset only after oxygen completes.
- **Semaphore choreography without private fields:** Use explicit permits whose acquire/release operations encode which hydrogen is first and which is second.
- **Private `_value` access:** It is unsupported API and, more importantly, its observation is not atomic with the earlier acquire.
- **Two hydrogens acquire before checking:** Both may release oxygen, demonstrating the protected race.
- **Oxygen arrives first:** It blocks on zero permits, which is intended.
- **Many hydrogens arrive first:** At most two initially acquire, but the duplicate oxygen-release race can corrupt later permit counts.
- **One molecule:** The problematic interleaving can already create an extra oxygen permit even at the smallest domain.
- **Callback order within a molecule:** Any of HHO, HOH, or OHH is allowed if grouping is correct.
- **Cross-molecule mixing:** No callback from the next molecule may complete before the current three bond; replenishment timing must enforce this.
- **Callback exception:** Failure before a release can block progress; normal callback completion is assumed.
- **Complexity target:** A corrected method should retain constant work per atom and $O(1)$ coordination state.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $m$ be the total number of atom threads, equal to three times the molecule count. Each call performs a constant number of intended semaphore operations and one callback, so the algorithmic target is $O(m)$ time with constant work per atom.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
