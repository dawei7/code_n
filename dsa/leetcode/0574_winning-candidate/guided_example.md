# Guided Example: Winning Candidate

We trace the step-by-step vote tally aggregation (`GROUP BY CandidateId`), plurality sorting (`ORDER BY COUNT(id) DESC`), winner isolation (`LIMIT 1`), candidate registry relational joining (`INNER JOIN Candidate`), and winning candidate name projection on representative ballot tables:

- **Input:**
  - `Candidate` table:
    | `id` | `Name` |
    |:---:|:---:|
    | $1$ | `A` |
    | $2$ | `B` |
    | $3$ | `C` |
    | $4$ | `D` |
    | $5$ | `E` |
  - `Vote` table:
    | `id` | `CandidateId` |
    |:---:|:---:|
    | $1$ | $2$ |
    | $2$ | $4$ |
    | $3$ | $3$ |
    | $4$ | $2$ |
    | $5$ | $5$ |
- **Required output:**
  | `Name` |
  |:---:|
  | `B` |
  - Election rule: Identify the candidate who accumulated the **strictly largest number of votes**.
  - Guarantee: Exactly one candidate is guaranteed to win the election in all valid test cases.
- **Relational Aggregation & Winner Selection Trace:**
  - **Step 1: Tally Votes per Candidate:**
    - Group the `Vote` table by `CandidateId` and count records:
      - Votes for `CandidateId = 2`: Vote $1$, Vote $4$ $\implies \mathbf{2}$ votes.
      - Votes for `CandidateId = 3`: Vote $3$ $\implies \mathbf{1}$ vote.
      - Votes for `CandidateId = 4`: Vote $2$ $\implies \mathbf{1}$ vote.
      - Votes for `CandidateId = 5`: Vote $5$ $\implies \mathbf{1}$ vote.
      - Candidate $1$ received $0$ votes.
  - **Step 2: Order by Descending Vote Count and Take Top 1:**
    - Sort vote tallies in descending order:
      1. `CandidateId = 2`: $2$ votes (**Highest!**)
      2. `CandidateId = 3`: $1$ vote
      3. `CandidateId = 4`: $1$ vote
      4. `CandidateId = 5`: $1$ vote
    - Slice the leading record with `LIMIT 1`:
      $$
      t = [(\text{id}: 2)]
      $$
  - **Step 3: Join with `Candidate` to Retrieve Winner's Name:**
    - Perform inner join between derived table $t$ and `Candidate` on $t.id = Candidate.id$:
      - Match $t.id = 2$ with $Candidate.id = 2$.
      - Retrieve attribute:
        $$
        Name = \mathbf{\text{"B"}}
        $$
    - Project final column:
      $$
      \mathbf{\text{"B"}}
      $$
- **Unanimous Election Instance:**
  - All votes cast for Candidate $3 \implies$ Candidate $3$ has $100\%$ of votes $\implies$ projects Name of Candidate 3.
- **Large Electorate with Multiple Candidates:**
  - Plurality sorting (`ORDER BY COUNT(...) DESC LIMIT 1`) executes via a top-1 heap or index scan, extracting the singular winner in logarithmic time.

This instance demonstrates plurality voting resolution through relational group aggregation and foreign-key joins, mathematically proves why top-1 ranking isolates the unique maximum vote receiver, and derives $O(V \log K)$ execution time and $O(K)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two tables `Candidate` and `Vote`:
Find the **name of the winning candidate** (the candidate with the most votes).

```text
Vote Counts:
  Candidate 2: 2 votes  <-- Most votes!
  Candidate 3: 1 vote
  Candidate 4: 1 vote
  Candidate 5: 1 vote

Candidate 2 is named "B".
Output: "B"
```

### The Two-Stage Relational Flow
- **Stage 1 (Vote Counting):**
  Aggregate the `Vote` table to find which `CandidateId` accumulated the highest vote count:
  $$
  \text{WinnerId} = \text{argmax}_{c} \left( \sum_{v \in Vote} \mathbf{1}[v.CandidateId == c] \right)
  $$
- **Stage 2 (Identity Projection):**
  Join the winning ID with the `Candidate` table to output the candidate's string `Name`.

---

## 2. Conceptual Foundation & Invariants

### 1. Winner Identification Subquery:
```sql
SELECT CandidateId AS id
FROM Vote
GROUP BY CandidateId
ORDER BY COUNT(id) DESC
LIMIT 1
```
- Groups votes by `CandidateId`.
- Orders by frequency in descending order.
- Slices the top 1 winning candidate ID.

### 2. Candidate Join:
```sql
SELECT c.Name
FROM ( ... subquery ... ) AS t
INNER JOIN Candidate AS c ON t.id = c.id
```

> **Uniqueness Invariant.** By the problem specification, exactly one candidate is guaranteed to have the strict maximum number of votes, ensuring `LIMIT 1` uniquely captures the election winner without arbitrary tie-breaking.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Aggregate Ballots
Group `Vote` by `CandidateId`:
- Candidate 2: $[1, 4] \implies count = 2$.
- Candidate 3: $[3] \implies count = 1$.
- Candidate 4: $[2] \implies count = 1$.
- Candidate 5: $[5] \implies count = 1$.

---

### Step 2: Sort and Select Maximum
- Order: $2 \to (count = 2)$, followed by other candidates $(count = 1)$.
- `LIMIT 1` selects $id = 2$.

---

### Step 3: Join on `Candidate.id = 2`
- Look up $id = 2$ in `Candidate`:
  - `Name = "B"`
- Result:
  $$
  \mathbf{\text{"B"}}
  $$

---

## 4. Complete Execution Trace

| `CandidateId` | Individual Vote IDs | Total Tally | Rank in Plurality | Subquery Top 1 Output | Joined Name |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$2$** | $1, 4$ | **$2$** | **$1$ (Winner)** | **`id = 2`** | **`"B"`** |
| $3$ | $3$ | $1$ | $2$ | Discarded | — |
| $4$ | $2$ | $1$ | $2$ | Discarded | — |
| $5$ | $5$ | $1$ | $2$ | Discarded | — |
| **Result** | — | — | — | — | **`"B"`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Vote Cast ($Vote$ has 1 row):** That single vote directly decides the winner $\implies$ projected in $O(1)$ time.
- **Candidates with 0 Votes:** Do not appear in the `Vote` table; grouped tally focuses exclusively on cast ballots.
- **Large Ballot Volume ($10^5$ votes):** Grouping via hash aggregation aggregates votes in a single linear scan of `Vote`.

---

## 6. Traps & Common Anti-Patterns

- **Joining Before Grouping ($O(V \cdot C)$):** Joining `Vote` with `Candidate` before grouping duplicates candidate names across every ballot row, creating unnecessary string comparisons. Grouping integers first and joining only the single winner takes $O(1)$ join time.
- **Forgetting `LIMIT 1`:** Omitting `LIMIT 1` returns every candidate sorted by votes, failing the expected single-value schema.
- **Assuming Candidate IDs are 1-Indexed Sequential:** Candidates may have arbitrary unique integer IDs. Joining on `Candidate.id` ensures correct mapping.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $V$ be the number of votes and $C$ be the number of candidates.
  - Grouping `Vote`: $\mathcal{O}(V)$ time.
  - Sorting the $C$ candidate tallies: $\mathcal{O}(C \log C)$ (or $O(C)$ with top-1 min-heap).
  - Joining the 1 winning row with `Candidate`: $\mathcal{O}(\log C)$ with primary key index.
  - Total Time: $\mathcal{O}(V + C \log C)$. For $V = 10^5, C = 1000$, completes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(C)$ space to store the aggregated vote tallies.
