# Guided Example: Unique Email Groups

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"emails": ["A@B.com", "a@b.com", "ab+xy@b.com", "a.b@b.com"]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `emails`, where each string is a valid email address.

The objective is to compute `2` from `{"emails": ["A@B.com", "a@b.com", "ab+xy@b.com", "a.b@b.com"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize each part according to its own rules

An email address has two logically separate components:

- the local name before `'@'`; and
- the domain name after `'@'`.

Two addresses belong to one group only when both normalized components match. The normalization function must therefore produce a stable representation of the ordered pair

$$
(\text{normalized local},\text{normalized domain}).
$$

The source begins with `local, domain = email.split("@")`. The contract guarantees exactly one `'@'`, so unpacking produces exactly two strings.

For the local part, the source applies the rules in a compact chain:

`local.split("+")[0].replace(".", "").lower()`.

Splitting on plus and taking element zero retains everything before the first plus. If no plus exists, the split produces a one-element list containing the whole local name. Any later plus signs and all characters after the first are ignored. Dots are then removed from the retained prefix, and the remaining letters are converted to lowercase.

The order of plus truncation and dot removal does not change the intended local result: dots after the first plus are ignored with the entire suffix, while dots before it are removed. Lowercasing could also occur before these two character-structure operations because input is restricted to English letters, digits, dots, and plus signs.

For the domain, the only normalization rule is case conversion, so `domain.lower()` is correct. Dots inside the domain remain meaningful. For example, `"leetcode.com"` and `"lee.tcode.com"` are different domains and must not be merged merely because removing their dots would make them look similar.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"emails": ["A@B.com", "a@b.com", "ab+xy@b.com", "a.b@b.com"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use a set to count normalized identities

After normalization, inserting one canonical identity into a set for each email is the right high-level strategy. A set retains one copy of each equal key, regardless of how many original addresses normalize to it. The number of set entries is then the number of groups.

For the first example, the first two locals both normalize to `"testemail"` and both domains normalize to `"leetcode.com"`. They should insert the same identity. The third local is again `"testemail"`, but its domain remains `"lee.tcode.com"`, so it should insert a second identity.

Case conversion applies on both sides. Thus `"A@B.com"` and `"a@b.com"` both normalize to the pair `("a","b.com")`. By contrast, `"a.b@b.com"` normalizes to `("ab","b.com")`, which differs in the local component.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After normalization, inserting one canonical identity into a... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The exact protected source loses the component boundary

The source does not insert the pair into the set. It constructs

`normalized = local + domain`

with no separator and inserts that concatenated string. This encoding is not one-to-one: when reading the key back, there is no way to know where the local name ends and the domain begins.

For a concrete valid counterexample, consider:

- `"ab@c.com"`, which normalizes to the pair `("ab","c.com")`; and
- `"a@bc.com"`, which normalizes to the pair `("a","bc.com")`.

These pairs are different in both their component boundary and their intended email identity, so the correct answer for the two-address array is two. The protected source concatenates both pairs into `"abc.com"` and stores only one set entry. It therefore returns one.

This is a genuine correctness defect, not merely a stylistic concern. The reference contract says equality must hold for both normalized components. Plain concatenation preserves that implication in one direction—equal pairs always produce equal concatenations—but the reverse implication is false. The source may merge different groups and undercount. It cannot create two keys for one normalized pair, so this defect can undercount but not overcount.

No correctness argument can establish the source for every valid input while this non-injective key remains. The surrounding normalization steps and set strategy are sound; only the representation of the component pair is defective.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"emails": ["A@B.com", "a@b.com", "ab+xy@b.com", "a.b@b.com"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Tuple key:** Store `(local,domain)` directly. :** - **Tuple key:** Store `(local,domain)` directly. This is the clearest collision-safe representation because its equality semantics exactly mirror the problem definition.
- **Delimited normalized address:** Store `local + "@" + domain`. It is safe because `'@'` cannot occur inside either component under the valid-address contract.
- **Length-prefixed concatenation:** Encode the local length before the two strings. This is collision-safe but unnecessarily complicated when tuple keys or the existing separator are available.
- **Sort normalized keys:** Normalize every address, sort the safe keys, and count adjacent changes. This is deterministic but costs `O(E\log E)` key comparisons for `E` emails instead of expected linear hashing.
- **Nested mapping by local then domain:** A dictionary from normalized local names to sets of normalized domains also preserves boundaries, but a set of pairs is simpler.
- **Unseparated concatenation:** The exact source's `local + domain` is unsafe. Different component pairs can share the same character sequence, as `"ab@c.com"` and `"a@bc.com"` demonstrate.
- **Multiple plus signs:** Everything beginning with the first plus is ignored. Taking index zero after `split("+")` produces the intended prefix, although `split("+",1)` would avoid creating unnecessary later pieces.
- **Dots after the first plus:** They are in the ignored suffix and have no effect. Dots before the plus are removed.
- **Dots in the domain:** They must remain. Dot-removal is a local-name rule only.
- **Case differences:** Both components are lowercased, so case alone never creates a new group.
- **Digits:** They are preserved in both components; `lower` affects only letters.
- **Already normalized email:** It maps to the same local-domain pair and inserts normally.
- **Normalized local possibly unusual:** The contract guarantees a nonempty original local name that does not begin with plus, but independent of whether normalization leaves a short or dot-only-derived prefix, tuple encoding still preserves the boundary safely.
- **Source status:** The protected solution should not be represented as fully correct for the stated domain until its key construction is repaired. The complexity remains optimal, but optimal complexity does not compensate for a collision bug.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
