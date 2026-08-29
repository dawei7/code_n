# Guided Example: Increasing Decreasing String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aaaabbbbcccc"}`
- **Required output:** `"abccbaabccba"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`. Reorder the string using the following algorithm:

The objective is to compute `"abccbaabccba"` from `{"s": "aaaabbbbcccc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace repeated searching with fixed alphabet sweeps

The required process repeatedly takes one copy of each available character in increasing order, then one copy of each available character in decreasing order. Since the input contains only lowercase English letters, there are just 26 possible choices. A frequency table is enough to represent the remaining multiset of characters; their original positions are irrelevant.

`Counter(s)` builds `cnt`, where `cnt[c]` is the number of unused copies of character `c`. Removing a character is simulated by appending it to `ans` and subtracting one from its counter. The original string never needs physical deletion.

The string `cs = ascii_lowercase + ascii_lowercase[::-1]` encodes one complete cycle. Its first half is `a` through `z`, exactly the increasing phase. Its second half is `z` through `a`, exactly the decreasing phase. The loop visits every possible character in that order and takes it if `cnt[c]` is positive.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aaaabbbbcccc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why one alphabet visit implements “smallest greater”

During the forward half, letters are examined from smallest to largest. The first available letter is therefore the smallest remaining character. After taking it, scanning continues strictly to later alphabet positions, so the next available letter is the smallest remaining character greater than the last appended one. Each letter position is visited only once in that half, preventing two equal copies from being taken during one increasing sweep.

The reverse half is symmetric. It begins at the largest letter and scans toward smaller letters. The first available letter is the largest remaining one, and every later chosen letter is the largest available character smaller than the preceding choice.

The two copies of `z` at the boundary of `cs` are deliberate. The forward phase may take one `z` as its final, largest choice. If another `z` remains, the decreasing phase is allowed to begin by taking one largest remaining character, which may also be `z`. Likewise, `a` appears at the end of the reverse half and again at the beginning of the next cycle. Consecutive equal letters across phase boundaries are valid even though equal letters cannot repeat inside one strictly increasing or decreasing phase.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the outer loop stops at exactly the right time

`ans` receives one character for every decrement of a counter. No character is invented and no available copy is used more than once. The loop condition `len(ans) < len(s)` therefore means some input copies remain. Every remaining lowercase character occurs somewhere in `cs`, so a traversal always appends at least one character until all counts reach zero. Once the two lengths match, every original copy has been emitted and the loop ends.

For `"aaaabbbbcccc"`, the first forward half takes `abc` and the reverse half takes `cba`, producing `"abccba"`. The counts are then two for each letter, so the next traversal repeats the same pattern and completes `"abccbaabccba"`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abccbaabccba"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aaaabbbbcccc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abccbaabccba"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeatedly sort remaining characters:** It directly exposes the smallest and largest choices but wastes work by sorting after removals, potentially becoming much slower.
- **Ordered set plus frequencies:** Maintain the currently available letters in a balanced structure and traverse it both ways. This generalizes to a large alphabet but is unnecessary for 26 fixed letters.
- **Explicit two loops:** Scan `ascii_lowercase` and then its reverse in separate loops. It is equally correct and may make the phase boundary clearer; the exact solution concatenates them into `cs`.
- **One character:** The forward sweep takes it and the outer loop ends immediately.
- **All characters equal:** A cycle can take one copy in the forward occurrence and another in the reverse occurrence of that letter. The unchanged output is still the required result.
- **Missing alphabet ranges:** Zero counters are simply skipped, so gaps such as between `a` and `z` do not affect strict ordering.
- **Repeated maximum letter:** One copy may end the increasing phase and another may begin the decreasing phase, explaining adjacent equal maxima.
- **Repeated minimum letter:** One copy may end the decreasing phase and another begin the next increasing phase.
- **Input immutability:** Only `cnt` is changed. Strings are immutable, and `s` remains untouched.
- **Lowercase guarantee:** The traversal includes only lowercase English letters. Unexpected characters outside that alphabet would never be appended and would make the loop fail to finish.
- **Required names:** The environment must provide `Counter` and `ascii_lowercase`, normally from `collections` and `string` respectively.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+AF)$. Let $n$ be the string length, $A=26$ the alphabet size, and $F$ the maximum frequency of any character. Building the counter and joining the answer each take $O(n)$ time. Every outer iteration scans the $2A$ characters in `cs`. No character can require more than roughly $F$ phase cycles before all of its copies are removed, so the scanning cost is $O(AF)$. Total time is
- **Auxiliary Space Complexity:** $O(n+A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
