# Guided Example: Restore the Array From Adjacent Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"adjacentPairs": [[2, 1], [3, 4], [3, 2]]}`
- **Required output:** `[1, 2, 3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an integer array `nums` that consists of `n` **unique **elements, but you have forgotten it. However, you do remember every pair of adjacent elements in `nums`.

The objective is to compute `[1, 2, 3, 4]` from `{"adjacentPairs": [[2, 1], [3, 4], [3, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View every pair as an undirected edge

Each distinct value in the forgotten array can be treated as a graph vertex. A pair `[a, b]` says that `a` and `b` were next to each other, but the pair may be written in either direction. The exact solution therefore creates an undirected edge by appending `b` to `g[a]` and `a` to `g[b]`.

Because the original array has unique elements, every interior value has exactly two neighbors: the values immediately before and after it. Each endpoint has exactly one neighbor. The supplied pairs include every original adjacency and are guaranteed to describe a valid array, so the resulting graph is not a branching general graph. It is one connected path containing all $n$ values.

This structural observation is the key. Restoring the array does not require trying permutations. Walking from either endpoint of the path to the other lists the values in a valid order. Starting at the opposite endpoint merely produces the reversed array, which is also accepted.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"adjacentPairs": [[2, 1], [3, 4], [3, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the adjacency lists

`g` is a `defaultdict(list)`. For every input pair, the source appends both directions. A list is appropriate because valid degrees are only one or two. There is no need for a set, sorting, or duplicate removal under the problem guarantees.

The array length is recovered as `n = len(adjacentPairs) + 1`. A path with $n$ vertices always has exactly $n-1$ edges, and the input contains one pair per adjacency. The answer list is preallocated as `[0] * n`. These zeros are placeholders only; actual values may also be zero, but positions are overwritten according to the traversal rather than tested for emptiness.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose one endpoint and establish the direction

The loop over `g.items()` searches for the first vertex whose neighbor list has length one. Such a vertex must be an endpoint. It writes that endpoint into `ans[0]` and its only neighbor into `ans[1]`, then stops searching.

There are exactly two endpoints, and dictionary iteration may encounter either one first. That nondeterminism is harmless. If one endpoint generates the original order, the other generates its reverse, and both contain every required adjacent pair.

Seeding two values is particularly useful because it establishes a travel direction without needing a visited set. Once `ans[0]` and `ans[1]` are known, the algorithm can always distinguish the neighbor it came from from the neighbor it should visit next.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"adjacentPairs": [[2, 1], [3, 4], [3, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive DFS:** Start at an endpoint and pass the previous vertex through recursion. It is logically equivalent but risks stack overflow on a path of length 100000.
- **Visited set:** A normal graph traversal can mark every visited value, but a path needs only the immediately previous value, so the set adds unnecessary $O(n)$ storage.
- **Degree map plus neighbor map:** Degrees can be counted separately, but adjacency lists already reveal endpoint degrees and are needed for traversal.
- **Try to order the input pairs directly:** Pair order and orientation are arbitrary, so sorting or chaining raw rows without a graph is unreliable.
- **Two possible answers:** Starting from either endpoint returns opposite orientations; the contract accepts both.
- **Exactly two values:** There is one pair, the endpoint seed fills both answer positions, and the reconstruction loop is empty.
- **Negative values:** Dictionary keys and equality comparisons handle them without any index conversion.
- **Zero as a real value:** Preallocated zeros are overwritten; the algorithm never interprets zero as an unused marker.
- **Large magnitudes:** Values up to the stated limits affect neither graph shape nor complexity.
- **Unique elements:** This guarantee is essential because the algorithm represents each numeric value as one graph vertex.
- **Endpoint degree:** A valid nontrivial path has exactly two vertices with degree one, guaranteeing that the seed loop finds one.
- **Interior degree:** Whenever the main loop needs a next value, the current vertex has two neighbors, making `v[1]` safe to access.
- **No cycle handling:** The code intentionally has no visited set because the valid-input guarantee says the graph is a path, not a cycle.
- **Dictionary order:** It influences only which accepted orientation is returned, not correctness.
- **Input preservation:** The pair list is read to build `g` and is never reordered or modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of values in the original array. The input contains $n-1$ pairs. Building both directions takes $O(n)$ time. Scanning dictionary entries to find an endpoint takes at most $O(n)$ time. The reconstruction loop writes the remaining values once, and inspecting a valid adjacency list costs $O(1)$ because its degree is at most two. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
