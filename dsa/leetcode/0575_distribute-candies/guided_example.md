# Guided Example: Distribute Candies

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"candyType": [1, 1, 2, 2, 3, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice has `n` candies, where the $$i^{\text{th}}$$ candy is of type $\text{candyType}[i]$. Alice noticed that she started to gain weight, so she visited a doctor.

The objective is to compute `3` from `{"candyType": [1, 1, 2, 2, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the smaller limit can always be reached

Suppose first that $u \le n/2$. Alice can choose one candy from each of the $u$ types. That uses $u$ candy slots and represents all available types. If $u < n/2$, she fills the remaining slots with any duplicate candies. Those extra candies do not reduce the number of represented types, so she finishes with exactly $u$ different types.

Now suppose that $u > n/2$. There are more available types than eating slots. Alice chooses one candy from any $n/2$ distinct types. That uses every allowed slot and gives her exactly $n/2$ different types. Thus, in both possible relationships between $u$ and $n/2$, Alice reaches the smaller value. This two-case construction proves that the answer is exactly their minimum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"candyType": [1, 1, 2, 2, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the exact code obtains the two limits

The solution is one expression:



`set(candyType)` inserts every type value into a set. A set stores each distinct value only once, so repeated candies collapse into one entry. Consequently, `len(set(candyType))` is $u$, the number of available types.

`len(candyType)` is $n$. The operator `>> 1` shifts the nonnegative integer $n$ one binary position to the right. For a nonnegative integer, this equals floor division by two:

$$
n \mathbin{\text{>>}} 1 = \left\lfloor \frac{n}{2} \right\rfloor.
$$

The contract says $n$ is even, so the floor has no effect and the value is exactly $n/2$. Writing `len(candyType) // 2` would communicate the story more directly to many beginners, but the bit shift in the exact solution computes the same number under this contract.

Finally, `min` returns the tighter of the capacity limit and the availability limit. There is no need to construct Alice’s chosen subset because the proof above guarantees that a choice achieving this count exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution is one expression:



`set(candyType)` inserts ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Tracing the examples

For `[1, 1, 2, 2, 3, 3]`, $n=6$, so Alice has three slots. The set is `{1, 2, 3}` and has size three. The minimum of three and three is three; choosing one of each type realizes it.

For `[1, 1, 2, 3]`, $n=4$, so there are two slots, while the set has three values. The slot limit is tighter, and choosing any two distinct types gives the answer two.

For `[6, 6, 6, 6]`, there are two slots but only one distinct type. Eating a second candy cannot introduce a new type, so the availability limit gives one.

Negative type labels cause no complication. Values such as `-7` are ordinary hashable integers, and the set distinguishes them just as it distinguishes positive values. Their numeric magnitude and ordering do not matter; only equality matters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"candyType": [1, 1, 2, 2, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort and count adjacent changes:** Sorting mak:** - **Sort and count adjacent changes:** Sorting makes equal types consecutive, so one scan can count distinct runs. It needs $O(n \log n)$ time and may modify the input; its extra memory depends on the language’s sorting implementation.
- **Boolean presence array:** Because the constraints bound type values, an offset-indexed boolean array could mark seen types. It can run in $O(n+R)$ initialization time and $O(R)$ space for value range $R$, but a hash set is simpler and stores only types that occur.
- **Manual hash-set loop with early stopping:** Insert values until the set reaches $n/2$ types, then return immediately. This can save work on favorable inputs, though its worst-case time and space remain $O(n)$.
- **Frequency map:** A dictionary of type-to-count also reveals how many types exist, but the counts are unnecessary. A set records exactly the information the answer needs.
- **Trying every subset:** Enumerating choices of $n/2$ candies repeats equivalent decisions and grows combinatorially. The two-limit proof removes the need to search.
- **All candies distinct:** Then $u=n$, but Alice has only $n/2$ slots, so the result is $n/2$.
- **All candies identical:** Then $u=1$, so the answer is one even though Alice eats multiple candies.
- **Exactly enough types:** When $u=n/2$, both limits agree and Alice chooses one candy of each type.
- **Smallest valid input:** With $n=2$, Alice eats one candy, so the answer is always one. The bit shift correctly produces one.
- **Even-length guarantee:** The exact code would compute floor division for an odd length. The problem promises even $n$, so no policy for a fractional half is needed.
- **Bit-shift readability:** `n >> 1` is correct for this nonnegative length, but `n // 2` is often clearer when explaining the domain rule. This is a readability distinction, not an algorithmic one.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `candyType` and $u$ its number of distinct values. Constructing `set(candyType)` visits all $n$ candies. Hash-set insertion and membership handling take $O(1)$ expected time per integer, so the total expected time is $O(n)$. Computing the two lengths, shifting by one bit, and taking the minimum are constant-time operations at this scale. The declared time complexity is therefore $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
