# Guided Example: Palindrome Permutation II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabb"}`
- **Required output:** `["abba", "baab"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string s, return *all the palindromic permutations (without duplicates) of it*.

The objective is to compute `["abba", "baab"]` from `{"s": "aabb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate palindromes directly instead of filtering permutations

The obvious interpretation is to generate every permutation of `s` and keep the ones that read the same in both directions. That spends nearly all of its work on strings that could never be answers. A palindrome is much more structured: apart from a possible center character, every character must be placed as a mirrored pair. The exact solution uses that structure during generation, so every completed string it constructs is already a valid palindrome.

The current order of `s` is irrelevant because permutations may rearrange it freely. What matters is the frequency of each distinct character. The solution starts with `Counter(s)`, which maps every character to its remaining number of copies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject an impossible frequency pattern before searching

Every position away from the center of a palindrome has a mirror position containing the same character. Those positions consume equal characters two at a time. Consequently, all character frequencies must be even, with one possible exception: an odd-length palindrome has one center position that can hold the unpaired copy of one odd-frequency character.

Thus a palindromic permutation exists exactly when at most one character has an odd frequency. This condition is necessary because two odd-frequency groups would both need the single center. It is sufficient because one copy of the only odd-frequency character can be reserved for the center, after which all remaining copies have even counts and can be placed in mirrored pairs.

The solution records the reserved center in `mid`, initially the empty string. It scans the counter entries and recognizes an odd count using `v & 1`. For the first odd count, it assigns that character to `mid` and subtracts one from its counter entry. Subtracting one is essential: the reserved copy is already represented by the center and must not be used again by the search. The remaining count becomes even.

If another odd count appears after `mid` has been filled, the solution immediately returns an empty list. There is no point entering the recursive search because the necessary frequency condition has failed. If the original length is even, no count can be odd, `mid` remains empty, and every character is available entirely in pairs. If the length is odd and generation is possible, `mid` contains exactly one character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every position away from the center of a palindrome has a mi... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Grow a palindrome from its center outward

The recursive function receives a string `t` that is already a palindrome. Initially, `t` is `mid`: either the forced one-character center or the empty center between the two middle positions.

At one recursive step, the function considers each character `c` in the counter. If at least two copies remain, it uses them as a mirrored pair:

1. subtract two from `cnt[c]`;
2. form the larger palindrome `c + t + c`;
3. recursively place another pair around that palindrome;
4. add the two copies back to `cnt[c]` after the recursive call returns.

The decrement marks the pair as used on the current search branch. The later increment is backtracking: it restores the exact state needed to explore a different choice at the same level. Without restoration, copies consumed in one branch would incorrectly disappear from its sibling branches.

Wrapping with the same `c` on both ends preserves the palindrome property. If `t` reads identically in both directions, then `c + t + c` also does: the new first and last characters match, and the interior remains symmetric. Because the initial `mid` is itself a palindrome, induction shows that every intermediate and completed `t` is a palindrome. The search never needs a separate palindrome check.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["abba", "baab"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["abba", "baab"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Permute one half with a mutable buffer:** Buil:** - **Permute one half with a mutable buffer:** Build a multiset containing half of each even count, backtrack over its distinct permutations, and mirror each completed half around `mid`. This expresses the same combinatorial search and can attain the manifest's $O(n+pn)$ time with $O(n)$ auxiliary space by avoiding repeated immutable center-wrapping.
- **Sort a half-string and skip equal choices:** A sorted list allows index-based permutation backtracking with a `used` array and the standard duplicate-skip rule. It is valid, but the counter-based search represents multiplicities more directly and never creates separate indistinguishable copies at a level.
- **Generate all permutations of `s`:** This explores as many as $n!$ arrangements and then spends $O(n)$ checking each candidate. It ignores palindrome symmetry and remains wasteful even if a set later removes duplicate results.
- **Use a result set to deduplicate:** Generating duplicate palindromes and inserting them into a set can make the final collection unique, but it does not recover the time already spent generating duplicates and uses additional hash storage. Count-based branching prevents those duplicates at their source.
- **More than one odd frequency:** The answer must be empty. Returning before DFS is both mathematically required and an important pruning step; no pair ordering can repair two characters that both need the unique center.
- **Exactly one odd frequency:** That character is forced into the center. The solution subtracts exactly one copy, not the whole frequency, because its remaining even number of copies still belongs in mirrored pairs.
- **No odd frequency:** `mid` is empty and the recursion begins from the gap between the middle positions. This is correct for every even-length feasible input.
- **Length one:** The only character becomes `mid`, its remaining count becomes zero, and `len(mid) == len(s)` immediately. DFS appends that one-character palindrome.
- **All characters the same:** There is only one available character choice at every level, so exactly one palindrome is produced. Count-based branching avoids the huge number of duplicate copy permutations that an index-based naïve search would create.
- **Empty string outside the contract:** The stated input is nonempty. If the exact implementation received `""`, `mid` would stay empty and the initial DFS call would immediately append `""`, treating the empty string as its one palindromic permutation.
- **Answer order:** Counter iteration order influences traversal order, so the returned list need not be lexicographically sorted. The contract explicitly allows any order, and uniqueness and completeness do not depend on that order.
- **Restoration after recursion:** The `cnt[c] += 2` step must occur after every child returns. Omitting it would make later sibling branches operate with missing copies and silently lose valid palindromes.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`, let $k$ be its number of distinct characters, let $m = \lfloor n/2 \rfloor$ be the number of mirrored pairs, and let $p$ be the number of returned palindromes. If the usable pair multiplicity of character $i$ is $q_i$, then, for a feasible input,
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
