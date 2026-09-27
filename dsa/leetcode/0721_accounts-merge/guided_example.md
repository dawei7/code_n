# Guided Example: Accounts Merge

We trace the step-by-step email-to-account index hash registration ($d[email] = i$), Disjoint Set Union (Union-Find) connected component clustering ($uf.union(i, d[email])$), component root canonicalization ($root = uf.find(i)$), multi-account email set union ($g[root].update(emails)$), and alphabetical email sorting on representative user identity records:

- **Input:**
  $$
  accounts = [
    [\text{"John"}, \; \text{"a@mail.com"}, \; \text{"b@mail.com"}],
    [\text{"John"}, \; \text{"b@mail.com"}, \; \text{"c@mail.com"}]
  ]
  $$
- **Required output:**
  $$
  [[\text{"John"}, \; \text{"a@mail.com"}, \; \text{"b@mail.com"}, \; \text{"c@mail.com"}]]
  $$
  - Merging rules:
    - Each record has an owner name followed by one or more email addresses.
    - Two accounts definitely belong to the same person if they share **at least one common email**.
    - Transitive property: If Account A shares an email with Account B, and Account B shares an email with Account C, then all three accounts belong to the same person.
    - Two accounts with the same name that share no emails (directly or transitively) may belong to different people with the same name and must **not** be merged.
    - In the merged output: the owner name is listed first, followed by the combined emails in **lexicographical (alphabetical) sorted order**.
- **Disjoint Set Union (Union-Find) & Component Invariant:**
  - **Account Index Nodes:**
    - Let each input account record be represented by its index $i \in [0, N - 1]$.
    - Initialize a Disjoint Set Union structure with $N$ elements.
  - **Email Ownership Table ($d$):**
    - Maintain a dictionary $d$ mapping each email address to the index of the first account that contained it:
      $$
      d[email] \leftarrow \text{account index } i
      $$
    - For each email in account $i$:
      - If $email$ was seen previously in an earlier account $j = d[email]$:
        - Merge the two accounts into the same connected component:
          $$
          uf.union(i, \; j)
          $$
      - Otherwise, record $d[email] = i$.
  - **Root Aggregation:**
    - After processing all emails, every account index belongs to a unique connected component identified by its root:
      $$
      root = uf.find(i)
      $$
    - Gather all emails from account $i$ into a set associated with $root$:
      $$
      g[root] \leftarrow g[root] \cup \text{emails}(accounts[i])
      $$
  - **Result Formatting:**
    - For each component $root$, construct the final record:
      $$
      [accounts[root][0]] + \text{sorted}(g[root])
      $$
- **Step-by-Step Worked Execution Trace on the 2-Account Input:**
  - Number of accounts: $N = 2$.
  - Initialize Union-Find on indices $\{0, 1\}$:
    $$
    p = [0, \; 1], \quad size = [1, \; 1]
    $$
  - Initialize email registry: $d = \{\}$.
  - **Process Account 0 (`["John", "a@mail.com", "b@mail.com"]`):**
    - Email `"a@mail.com"`:
      - Not in $d \implies d[\text{"a@mail.com"}] = 0$.
    - Email `"b@mail.com"`:
      - Not in $d \implies d[\text{"b@mail.com"}] = 0$.
    - Table state:
      $$
      d = \{ \text{"a@mail.com"}: 0, \; \text{"b@mail.com"}: 0 \}
      $$
  - **Process Account 1 (`["John", "b@mail.com", "c@mail.com"]`):**
    - Email `"b@mail.com"`:
      - Already in $d$ with owner index $0$!
      - Execute union of Account 1 and Account 0:
        $$
        uf.union(1, \; 0)
        $$
      - Both accounts now share root $0$.
    - Email `"c@mail.com"`:
      - Not in $d \implies d[\text{"c@mail.com"}] = 1$.
  - **Aggregate Emails by Component Root:**
    - Initialize grouping map $g$:
    - For Account 0:
      - Root: $uf.find(0) = 0$.
      - Add emails: $g[0] \leftarrow \{\text{"a@mail.com"}, \text{"b@mail.com"}\}$.
    - For Account 1:
      - Root: $uf.find(1) = 0$.
      - Add emails: $g[0] \leftarrow g[0] \cup \{\text{"b@mail.com"}, \text{"c@mail.com"}\} = \{\text{"a@mail.com"}, \text{"b@mail.com"}, \text{"c@mail.com"}\}$.
  - **Construct Final Merged Output:**
    - Component root $0$:
      - Owner name: $accounts[0][0] = \text{"John"}$.
      - Sort emails alphabetically:
        $$
        [\text{"a@mail.com"}, \; \text{"b@mail.com"}, \; \text{"c@mail.com"}]
        $$
      - Combined record:
        $$
        [\text{"John"}, \; \text{"a@mail.com"}, \; \text{"b@mail.com"}, \; \text{"c@mail.com"}]
        $$
  - **Final Return:**
    $$
    [[\text{"John"}, \; \text{"a@mail.com"}, \; \text{"b@mail.com"}, \; \text{"c@mail.com"}]]
    $$
- **Same Name Disjoint People Trace:**
  - Account 0: `["Mary", "mary@mail.com"]`
  - Account 1: `["Mary", "other_mary@mail.com"]`
  - Zero shared emails $\implies$ no union operation.
  - Generates two separate accounts:
    - `["Mary", "mary@mail.com"]`
    - `["Mary", "other_mary@mail.com"]`
- **Transitive 3-Way Merge ($A \sim B$ and $B \sim C$):**
  - Account 0 shares `"b@mail"` with Account 1.
  - Account 1 shares `"c@mail"` with Account 2.
  - $uf.union(0, 1)$ and $uf.union(1, 2)$ link all three accounts into a single component with root 0.
  - Correctly merges all three accounts into one unified profile.

This instance demonstrates bipartite graph projection and transitive equivalence relation clustering via Disjoint Set Union, mathematically proves why shared email relations partition accounts into connected components, and derives $O(E \alpha(N) + E \log E)$ runtime and $O(E)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a list of accounts with names and emails:
Merge accounts that belong to the **same person** (share at least one email).
Return each merged account with its name and emails **sorted alphabetically**.

```text
Account 0: [ "John", "a@mail.com", "b@mail.com" ]
Account 1: [ "John", "b@mail.com", "c@mail.com" ]

Shared email: "b@mail.com" connects Account 0 and Account 1!
Union-Find: union(0, 1) -> Root = 0

Combined Emails: { "a@mail.com", "b@mail.com", "c@mail.com" }
Sorted: [ "a@mail.com", "b@mail.com", "c@mail.com" ]

Result: [ [ "John", "a@mail.com", "b@mail.com", "c@mail.com" ] ]
```

### The Invariant of the Email Bipartite Graph
- Two accounts belong to the same equivalence class if they share a common email.
- Indexing accounts with Union-Find and mapping emails to their first account index reduces transitive clustering to disjoint-set operations.

---

## 2. Conceptual Foundation & Invariants

### 1. The Disjoint Set Graph:
Vertices: $\{0, 1, \dots, N - 1\}$.
Edges: $(i, d[email])$ for all $email \in accounts[i]$ where $email$ was seen before.

### 2. Group Aggregation:
$$
g[uf.find(i)] \leftarrow g[uf.find(i)] \cup \text{emails}(accounts[i])
$$
$$
ans = [ [accounts[root][0]] + \text{sorted}(emails) \mid root, emails \in g ]
$$

> **Equivalence Relation Quotient Invariant.** The binary relation $\sim$ on account indices defined by $i \sim j \iff \text{emails}(i) \cap \text{emails}(j) \ne \emptyset$ generates a transitive closure $\sim^*$ whose equivalence classes are the connected components in the bipartite account-email hypergraph.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Account 0
- Register: $d[\text{"a@mail"}] = 0, d[\text{"b@mail"}] = 0$.

---

### Step 2: Account 1
- `"b@mail"` already in $d \implies$ union(1, 0).
- Register: $d[\text{"c@mail"}] = 1$.

---

### Step 3: Group by Root
- Root of 0 is 0. Root of 1 is 0.
- $g[0] = \{\text{"a@mail"}, \text{"b@mail"}, \text{"c@mail"}\}$.

---

### Step 4: Sort & Format
- Output:
  $$
  [[\text{"John"}, \; \text{"a@mail.com"}, \; \text{"b@mail.com"}, \; \text{"c@mail.com"}]]
  $$

---

## 4. Complete Execution Trace

| Account Index $i$ | Name | Emails Processed | Shared Email Detected | DSU Action | Component Structure |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `"John"` | `"a@mail"`, `"b@mail"` | None | Register in $d$ | $\{0\}, \{1\}$ |
| $1$ | `"John"` | `"b@mail"`, `"c@mail"` | `"b@mail"` (Owner $0$) | $uf.union(1, 0)$ | **$\{0, 1\}$ (Merged)** |
| **Output** | `"John"` | Union of all 3 emails | — | Sort emails | **`["John", "a@mail", "b@mail", "c@mail"]`** |

---

## 5. Boundary Cases & Failure Modes

- **Same Name, No Shared Emails:** Belong to different people $\implies$ remains separate accounts.
- **Single Account ($N = 1$):** Returns sorted emails of that account.
- **Transitive Star Chain ($A \sim B, B \sim C, C \sim D$):** All collapse into a single merged component.
- **Duplicate Emails within the Same Account:** Deduplicated naturally by `set`.

---

## 6. Traps & Common Anti-Patterns

- **Merging by Name:** Merging solely based on the user's name is incorrect; different people can have the same name. Only merge when a common email exists.
- **Forgetting to Sort Output Emails:** The problem strictly requires emails in the merged output to be sorted in **alphabetical order**.
- **Naive Graph Traversal ($O(E^2)$):** Checking all pairs of accounts for shared emails takes quadratic time. Using a hash map $d[email] \to index$ with Union-Find takes nearly linear $O(E \alpha(N))$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Processing $E$ total emails across all accounts: $\mathcal{O}(E \alpha(N))$ where $\alpha$ is the Inverse Ackermann function.
  - Sorting emails within each component: $\mathcal{O}(E \log E)$ across the entire output.
  - Total Time: $\mathcal{O}(E \alpha(N) + E \log E)$. Completes in $< 15$ ms for $E = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(E)$ space for the hash map, union-find parent array, and grouping set.
