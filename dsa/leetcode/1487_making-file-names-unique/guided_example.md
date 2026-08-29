# Guided Example: Making File Names Unique

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"names": ["pes", "fifa", "gta", "pes(2019)"]}`
- **Required output:** `["pes", "fifa", "gta", "pes(2019)"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `names` of size `n`. You will create `n` folders in your file system **such that**, at the $i^{\text{th}}$ minute, you will create a folder with the name $\text{names}[i]$.

The objective is to compute `["pes", "fifa", "gta", "pes(2019)"]` from `{"names": ["pes", "fifa", "gta", "pes(2019)"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What must be remembered while processing names

Folders are created in input order, so every decision depends only on names assigned earlier. If the requested name has not been assigned, the system must use it unchanged. If it is already occupied, the system must find the smallest positive integer $k$ for which the candidate formed as `name + '(' + k + ')'` is free.

The stored implementation uses a dictionary `d` for two related purposes:

- Membership in `d` means that a complete folder name has already been assigned.
- The integer stored at key `name` is the next suffix number from which a future search for that requested base name should start.

This second meaning is an optimization. Repeated requests for the same base do not restart at one and recheck suffixes that were already proved occupied.

The code uses `defaultdict(int)`, but it checks membership with `name in d` and candidate membership before reading absent keys. Those membership operations do not invoke the default factory. In practice, the dictionary is being used like an ordinary map whose explicitly inserted keys are all assigned names.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"names": ["pes", "fifa", "gta", "pes(2019)"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Following one iteration exactly

The loop `for i, name in enumerate(names)` visits requests from left to right and keeps both the current index and the original string at that position.

If `name not in d`, no earlier folder has that exact complete name. The conditional body is skipped, `names[i]` remains unchanged, and `d[names[i]] = 1` records the newly assigned name. Storing one means that if this exact string is requested again, its first suffix candidate will use $k=1$.

If `name in d`, the exact name is occupied. The code starts with `k = d[name]`. It repeatedly tests `f'{name}({k})' in d`. While that candidate is also occupied, it increases `k` by one. The first candidate that fails the membership test is free. The code then performs three important updates:

1. `d[name] = k + 1` remembers that the next duplicate request for this base can begin after the suffix just selected.
2. `names[i] = f'{name}({k})'` replaces the current input position with the actual assigned name.
3. The common line `d[names[i]] = 1` records the newly generated full name as occupied and initializes its own future suffix search.

The method mutates the supplied `names` list in place and returns that same list object. The returned sequence contains assigned names, not necessarily the original requested strings.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why generated names need their own entries

Suppose the requests are `gta`, `gta(1)`, and then `gta`. After the first request, `gta` is occupied. The second string is itself a complete requested name, so it is also inserted as a key. When the third request searches from suffix one, membership detects that `gta(1)` is unavailable and advances to `gta(2)`.

Recording only base names or only counters would miss this collision. A generated or literal name can later appear as a request in its own right. The dictionary must therefore contain every complete assigned string.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["pes", "fifa", "gta", "pes(2019)"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"names": ["pes", "fifa", "gta", "pes(2019)"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["pes", "fifa", "gta", "pes(2019)"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Restarting at one for every duplicate:** This is simple and correct, but repeated copies of the same base can recheck a long occupied prefix each time and degrade toward quadratic work. The saved next-suffix pointer avoids that repetition.
- **A set plus a next-suffix map:** Keeping assigned names in a set and counters in a separate map makes the two roles explicit. It has the same asymptotic behavior but uses two containers instead of one dictionary.
- **Sorting requests first:** This is incorrect because folder creation is chronological. Reordering requests changes which name is already occupied at each minute and therefore changes the output.
- **Counting occurrences only:** A simple duplicate count fails when a would-be generated name was already supplied literally, such as `gta(1)` before another `gta` request. Membership of complete names must be checked.
- **All names initially distinct:** Every conditional body is skipped, the list remains unchanged, and each name is recorded with starting suffix one.
- **Many identical requests:** Results progress through the smallest available suffixes, and the saved pointer prevents rescanning suffixes already passed for that base.
- **Literal suffix-like names:** Parentheses and digits are ordinary characters in a name. The algorithm does not parse them; `a(1)` is simply another possible base key that may later become `a(1)(1)`.
- **Collision with a previously generated name:** Because every assigned result is inserted as a key, a later literal request for that same string is recognized as occupied.
- **Input mutation:** The source overwrites duplicated entries in `names`. Callers that need the original requests must pass a copy or preserve the original list before calling.
- **Smallest positive suffix:** Search begins at one for a newly assigned base and advances by one, so zero and negative suffixes are never considered.
- **Dictionary default values:** Membership checks are important. Directly reading a missing `defaultdict` key would insert it with zero and could falsely mark a name as occupied in later iterations.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of requested names. Under expected constant-time dictionary lookup and a model that treats bounded-length string construction and hashing as constant time, the algorithm runs in amortized $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
