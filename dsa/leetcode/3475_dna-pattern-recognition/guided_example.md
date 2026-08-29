# Guided Example: DNA Pattern Recognition 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Samples": [{"sample_id": 1, "dna_sequence": "ATGCTAGCTAGCTAA", "species": "Human"}, {"sample_id": 2, "dna_sequence": "GGGTCAATCATC", "species": "Human"}, {"sample_id": 3, "dna_sequence": "ATATATCGTAGCTA", "species": "Human"}, {"sample_id": 4, "dna_sequence": "ATGGGGTCATCATAA", "species": "Mouse"}, {"sample_id": 5, "dna_sequence": "TCAGTCAGTCAG", "species": "Mouse"}, {"sample_id": 6, "dna_sequence": "ATATCGCGCTAG", "species": "Zebrafish"}, {"sample_id": 7, "dna_sequence": "CGTATGCGTCGTA", "species": "Zebrafish"}]}}`
- **Required output:** `{"columns": ["sample_id", "dna_sequence", "species", "has_start", "has_stop", "has_atat", "has_ggg"], "rows": [[1, "ATGCTAGCTAGCTAA", "Human", 1, 1, 0, 0], [2, "GGGTCAATCATC", "Human", 0, 0, 0, 1], [3, "ATATATCGTAGCTA", "Human", 0, 0, 1, 0], [4, "ATGGGGTCATCATAA", "Mouse", 1, 1, 0, 1], [5, "TCAGTCAGTCAG", "Mouse", 0, 0, 0, 0], [6, "ATATCGCGCTAG", "Zebrafish", 0, 1, 1, 0], [7, "CGTATGCGTCGTA", "Zebrafish", 0, 0, 0, 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Samples`

The objective is to compute `{"columns": ["sample_id", "dna_sequence", "species", "has_start", "has_stop", "has_atat", "has_ggg"], "rows": [[1, "ATGCTAGCTAGCTAA", "Human", 1, 1, 0, 0], [2, "GGGTCAATCATC", "Human", 0, 0, 0, 1], [3, "ATATATCGTAGCTA", "Human", 0, 0, 1, 0], [4, "ATGGGGTCATCATAA", "Mouse", 1, 1, 0, 1], [5, "TCAGTCAGTCAG", "Mouse", 0, 0, 0, 0], [6, "ATATCGCGCTAG", "Zebrafish", 0, 1, 1, 0], [7, "CGTATGCGTCGTA", "Zebrafish", 0, 0, 0, 0]]}` from `{"tables": {"Samples": [{"sample_id": 1, "dna_sequence": "ATGCTAGCTAGCTAA", "species": "Human"}, {"sample_id": 2, "dna_sequence": "GGGTCAATCATC", "species": "Human"}, {"sample_id": 3, "dna_sequence": "ATATATCGTAGCTA", "species": "Human"}, {"sample_id": 4, "dna_sequence": "ATGGGGTCATCATAA", "species": "Mouse"}, {"sample_id": 5, "dna_sequence": "TCAGTCAGTCAG", "species": "Mouse"}, {"sample_id": 6, "dna_sequence": "ATATCGCGCTAG", "species": "Zebrafish"}, {"sample_id": 7, "dna_sequence": "CGTATGCGTCGTA", "species": "Zebrafish"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Project four independent Boolean indicators for every sample.** This query does not filter out any row. It selects the original `sample_id`, `dna_sequence`, and `species`, then evaluates four pattern expressions. MySQL returns the truth value of each expression as zero or one, giving the requested indicator columns.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Samples": [{"sample_id": 1, "dna_sequence": "ATGCTAGCTAGCTAA", "species": "Human"}, {"sample_id": 2, "dna_sequence": "GGGTCAATCATC", "species": "Human"}, {"sample_id": 3, "dna_sequence": "ATATATCGTAGCTA", "species": "Human"}, {"sample_id": 4, "dna_sequence": "ATGGGGTCATCATAA", "species": "Mouse"}, {"sample_id": 5, "dna_sequence": "TCAGTCAGTCAG", "species": "Mouse"}, {"sample_id": 6, "dna_sequence": "ATATCGCGCTAG", "species": "Zebrafish"}, {"sample_id": 7, "dna_sequence": "CGTATGCGTCGTA", "species": "Zebrafish"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Because the schema states that DNA sequences use `A`, `T`, `G`, and `C`, the literal uppercase patterns directly match the declared representation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Detect a start codon only at the beginning.** The expression

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["sample_id", "dna_sequence", "species", "has_start", "has_stop", "has_atat", "has_ggg"], "rows": [[1, "ATGCTAGCTAGCTAA", "Human", 1, 1, 0, 0], [2, "GGGTCAATCATC", "Human", 0, 0, 0, 1], [3, "ATATATCGTAGCTA", "Human", 0, 0, 1, 0], [4, "ATGGGGTCATCATAA", "Mouse", 1, 1, 0, 1], [5, "TCAGTCAGTCAG", "Mouse", 0, 0, 0, 0], [6, "ATATCGCGCTAG", "Zebrafish", 0, 1, 1, 0], [7, "CGTATGCGTCGTA", "Zebrafish", 0, 0, 0, 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Samples": [{"sample_id": 1, "dna_sequence": "ATGCTAGCTAGCTAA", "species": "Human"}, {"sample_id": 2, "dna_sequence": "GGGTCAATCATC", "species": "Human"}, {"sample_id": 3, "dna_sequence": "ATATATCGTAGCTA", "species": "Human"}, {"sample_id": 4, "dna_sequence": "ATGGGGTCATCATAA", "species": "Mouse"}, {"sample_id": 5, "dna_sequence": "TCAGTCAGTCAG", "species": "Mouse"}, {"sample_id": 6, "dna_sequence": "ATATCGCGCTAG", "species": "Zebrafish"}, {"sample_id": 7, "dna_sequence": "CGTATGCGTCGTA", "species": "Zebrafish"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["sample_id", "dna_sequence", "species", "has_start", "has_stop", "has_atat", "has_ggg"], "rows": [[1, "ATGCTAGCTAGCTAA", "Human", 1, 1, 0, 0], [2, "GGGTCAATCATC", "Human", 0, 0, 0, 1], [3, "ATATATCGTAGCTA", "Human", 0, 0, 1, 0], [4, "ATGGGGTCATCATAA", "Mouse", 1, 1, 0, 1], [5, "TCAGTCAGTCAG", "Mouse", 0, 0, 0, 0], [6, "ATATCGCGCTAG", "Zebrafish", 0, 1, 1, 0], [7, "CGTATGCGTCGTA", "Zebrafish", 0, 0, 0, 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Put pattern conditions in `WHERE`:** That would remove nonmatching samples, but the required output includes every sample with zero indicators.
- **Use `LIKE '%ATG%'` for `has_start`:** A leading wildcard would incorrectly accept `ATG` in the middle.
- **Omit the stop-codon end anchors:** Sequences containing `TAA`, `TAG`, or `TGA` internally would be false positives.
- **Anchor only the final alternative:** A pattern such as `TAA|TAG|TGA$` leaves the first two alternatives unanchored; the source correctly anchors all three.
- **Use `LIKE '%GGG%'`:** This also detects at least three consecutive Gs and is simpler, while `GGG+` explicitly accepts arbitrary longer runs.
- **Exactly two Gs:** `GGG+` cannot match because at least three G characters are required.
- **Four or more Gs:** The `+` consumes the additional Gs and still returns one.
- **Overlapping `ATAT` motifs:** Presence remains one regardless of how many overlapping matches occur.
- **Short sequences:** A sequence shorter than three cannot match start or stop codons, and one shorter than four cannot match `ATAT`; the expressions naturally return zero.
- **Multiple simultaneous patterns:** Columns are independent, so any combination of zeros and ones is possible.
- **Case sensitivity:** The schema declares uppercase DNA characters. If mixed-case data were allowed under a case-insensitive collation, explicit binary or case-sensitive matching might be needed.
- **`NULL` DNA sequence:** Pattern expressions evaluate to SQL null rather than zero; the reference schema does not specify null rows, so the query follows the declared data model.
- **`ORDER BY 1` maintainability:** It is correct while `sample_id` is the first selected column, though naming the column directly can be clearer during later query edits.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S + r log r)$. Let $S$ be the total number of characters across all DNA sequences and let $r$ be the number of sample rows. Each of the four fixed patterns can scan a sequence in time linear in its length in the ordinary engine model. Four constant-many scans still total $O(S)$.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
