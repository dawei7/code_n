# Guided Example: Find Products with Valid Serial Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"products": [{"product_id": 1, "product_name": "Widget A", "description": "This is a sample product with SN1234-5678"}, {"product_id": 2, "product_name": "Widget B", "description": "A product with serial SN9876-1234 in the description"}, {"product_id": 3, "product_name": "Widget C", "description": "Product SN1234-56789 is available now"}, {"product_id": 4, "product_name": "Widget D", "description": "No serial number here"}, {"product_id": 5, "product_name": "Widget E", "description": "Check out SN4321-8765 in this description"}]}}`
- **Required output:** `{"columns": ["product_id", "product_name", "description"], "rows": [[1, "Widget A", "This is a sample product with SN1234-5678"], [2, "Widget B", "A product with serial SN9876-1234 in the description"], [5, "Widget E", "Check out SN4321-8765 in this description"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `products`

The objective is to compute `{"columns": ["product_id", "product_name", "description"], "rows": [[1, "Widget A", "This is a sample product with SN1234-5678"], [2, "Widget B", "A product with serial SN9876-1234 in the description"], [5, "Widget E", "Check out SN4321-8765 in this description"]]}` from `{"tables": {"products": [{"product_id": 1, "product_name": "Widget A", "description": "This is a sample product with SN1234-5678"}, {"product_id": 2, "product_name": "Widget B", "description": "A product with serial SN9876-1234 in the description"}, {"product_id": 3, "product_name": "Widget C", "description": "Product SN1234-56789 is available now"}, {"product_id": 4, "product_name": "Widget D", "description": "No serial number here"}, {"product_id": 5, "product_name": "Widget E", "description": "Check out SN4321-8765 in this description"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Filter rows with one pattern that expresses the whole token contract.** The query reads `product_id`, `product_name`, and `description` from `products`, then applies MySQL's `REGEXP` operator to each description. The regular expression is:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"products": [{"product_id": 1, "product_name": "Widget A", "description": "This is a sample product with SN1234-5678"}, {"product_id": 2, "product_name": "Widget B", "description": "A product with serial SN9876-1234 in the description"}, {"product_id": 3, "product_name": "Widget C", "description": "Product SN1234-56789 is available now"}, {"product_id": 4, "product_name": "Widget D", "description": "No serial number here"}, {"product_id": 5, "product_name": "Widget E", "description": "Check out SN4321-8765 in this description"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

The doubled backslashes belong to the SQL string literal. They cause the regular-expression engine to receive the word-boundary marker `\b` rather than treating the backslash as a string escape. Each remaining component has a specific role.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Force case-sensitive letters.** `(?-i)` is an inline regular-expression mode modifier that disables case-insensitive matching. This matters because database text comparisons and regular expressions can otherwise inherit case-insensitive behavior from a collation or default mode. With the modifier, only uppercase `SN` matches. Text such as `sn1234-5678` or `Sn1234-5678` is rejected, exactly as the statement requires.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "product_name", "description"], "rows": [[1, "Widget A", "This is a sample product with SN1234-5678"], [2, "Widget B", "A product with serial SN9876-1234 in the description"], [5, "Widget E", "Check out SN4321-8765 in this description"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"products": [{"product_id": 1, "product_name": "Widget A", "description": "This is a sample product with SN1234-5678"}, {"product_id": 2, "product_name": "Widget B", "description": "A product with serial SN9876-1234 in the description"}, {"product_id": 3, "product_name": "Widget C", "description": "Product SN1234-56789 is available now"}, {"product_id": 4, "product_name": "Widget D", "description": "No serial number here"}, {"product_id": 5, "product_name": "Widget E", "description": "Check out SN4321-8765 in this description"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "product_name", "description"], "rows": [[1, "Widget A", "This is a sample product with SN1234-5678"], [2, "Widget B", "A product with serial SN9876-1234 in the description"], [5, "Widget E", "Check out SN4321-8765 in this description"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use `LIKE 'SN____-____'`:** Underscores match any character, not specifically digits, and anchoring or surrounding-token rules become awkward.
- **Omit `(?-i)`:** On a case-insensitive setup, lowercase or mixed-case prefixes could be accepted even though `SN` is case-sensitive.
- **Omit the final word boundary:** `SN1234-56789` would incorrectly match through its first four trailing digits.
- **Omit the initial word boundary:** Text such as `ASN1234-5678` or `1SN1234-5678` could be accepted as an embedded suffix.
- **Use `\d` instead of `[0-9]`:** Some regular-expression engines give `\d` broader Unicode semantics; the explicit range clearly expresses the required decimal characters.
- **Anchor the whole description:** `^...$` would reject valid descriptions containing ordinary text before or after the serial number.
- **Punctuation around the serial:** Parentheses, commas, periods, and whitespace create valid boundaries and should be accepted.
- **Underscore next to the serial:** Underscore is a word character, so the boundary fails; the token is treated as embedded in a larger identifier.
- **Multiple valid serials in one description:** `WHERE` is Boolean, so the product appears once rather than once per occurrence.
- **A valid and an invalid serial together:** The row qualifies if at least one complete valid occurrence matches.
- **`NULL` description:** SQL regular-expression evaluation yields unknown rather than true, so such a row is not selected; the reference schema does not state a separate null requirement.
- **`ORDER BY 1` readability:** It is concise and correct here, though spelling out `product_id ASC` can be clearer when a select list is later rearranged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S+r\log r)$. Let $S$ be the total number of characters across all descriptions and let $r$ be the number of rows that match. The regular expression has fixed length and contains no ambiguous nested repetition, so scanning the descriptions takes $O(S)$ under the regular-expression engine's normal linear scan model. Sorting the $r$ qualifying rows by `product_id` costs $O(r\log r)$ unless an execution plan can already deliver them in index order. The manifest's stated time bound $O(S+r\log r)$ is therefore an appropriate worst-case logical bound.
- **Auxiliary Space Complexity:** $O(S + r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
