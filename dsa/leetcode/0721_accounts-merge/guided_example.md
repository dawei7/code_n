# Guided Example: Accounts Merge

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"accounts": [["Alex", "x@mail.com"], ["Alex", "y@mail.com"]]}`
- **Required output:** `[["Alex", "x@mail.com"], ["Alex", "y@mail.com"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a list of `accounts` where each element $\text{accounts}[i]$ is a list of strings, where the first element $\text{accounts}[i][0]$ is a name, and the rest of the elements are **emails** representing emails of the account.

The objective is to compute `[["Alex", "x@mail.com"], ["Alex", "y@mail.com"]]` from `{"accounts": [["Alex", "x@mail.com"], ["Alex", "y@mail.com"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model accounts as connected components

Each row begins with a name and then lists email addresses. Two account rows describe the same person when they share at least one email. That relationship is transitive: if account A shares an email with B, and B shares another email with C, all three accounts belong to one merged person even if A and C have no email directly in common.

This is a connectivity problem. Treat every account index as a node. A shared email creates an edge between the account rows containing it. The desired merged accounts are exactly the connected components of this implicit graph.

The exact solution finds those components with a disjoint-set union structure, also called union-find. It does not explicitly store every graph edge. Instead, it discovers shared emails while scanning the accounts and immediately joins the corresponding account indices.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"accounts": [["Alex", "x@mail.com"], ["Alex", "y@mail.com"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the union-find arrays mean

For `n` account rows, `p[i]` is the current parent of account index `i`. Initially every account is its own component, so `p[i] = i`. A root is an index whose parent is itself.

The `size` array stores the number of union-find nodes in each root’s component. It is meaningful at roots and helps keep trees shallow.

The `find(x)` operation follows parent pointers until it reaches the component root. On the recursive return path it performs path compression by assigning `p[x]` directly to that root. Future finds from the same path become faster.

The `union(a, b)` operation finds both roots. If the roots already match, the accounts are already connected and nothing changes. Otherwise, the smaller component is attached below the larger component and the new root’s size is updated. In an equal-size tie, this exact code attaches `pa` under `pb` because it uses `>` rather than `>=`. Either tie direction is correct.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For `n` account rows, `p[i]` is the current parent of accoun... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use each email as evidence of a connection

The dictionary `d` maps an email to one account index where that email was previously seen.

While scanning account `i`:

- If an email is new, store `d[email] = i`.
- If it was seen before in account `d[email]`, union `i` with that stored account.

There is no need to retain a list of every account for each email. The first observed account serves as a hub. If the same email appears in five accounts, unioning the later four with the first connects all five into one component.

This scan also handles chains across different emails. Suppose account 0 shares `a@mail` with account 1, while account 1 shares `b@mail` with account 2. The first shared email unions 0 and 1; the second unions 1 and 2. Union-find then gives all three the same root, correctly applying transitivity.

The account name is deliberately not used as a union key. Different people may have the same name, so equal names alone do not prove identity. Conversely, the problem guarantees that all account rows belonging to the same person have the same name, making it safe to choose the name later from any component member.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[["Alex", "x@mail.com"], ["Alex", "y@mail.com"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"accounts": [["Alex", "x@mail.com"], ["Alex", "y@mail.com"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[["Alex", "x@mail.com"], ["Alex", "y@mail.com"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit account graph plus DFS or BFS:** Conn:** - **Explicit account graph plus DFS or BFS:** Connect account indices that share emails, then traverse connected components. This is correct but may store more adjacency data than union-find. Care is needed not to create a quadratic clique for an email appearing in many accounts; connecting all occurrences to one representative is sufficient.
- **- **Email-node graph:** Treat emails as vertices, :** - **Email-node graph:** Treat emails as vertices, connect all emails within each account, and traverse components. This also works and can associate a name with each component, but it creates graph edges and traversal state that the union-find solution avoids.
- **- **Union emails instead of accounts:** Assign an :** - **Union emails instead of accounts:** Assign an identifier to every unique email and union addresses appearing in the same row. This is a valid design, but the exact solution’s account-index nodes make selecting a guaranteed component name particularly direct.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E log E)$. Let `A` be the number of account rows, `E` the total number of email occurrences across all rows, and `U` the number of distinct emails.
- **Auxiliary Space Complexity:** $O(E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
