# Guided Example: Find Candidates for Data Scientist Position II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Candidates": [{"candidate_id": 101, "skill": "Python", "proficiency": 5}, {"candidate_id": 101, "skill": "Tableau", "proficiency": 3}, {"candidate_id": 101, "skill": "PostgreSQL", "proficiency": 4}, {"candidate_id": 101, "skill": "TensorFlow", "proficiency": 2}, {"candidate_id": 102, "skill": "Python", "proficiency": 4}, {"candidate_id": 102, "skill": "Tableau", "proficiency": 5}, {"candidate_id": 102, "skill": "PostgreSQL", "proficiency": 4}, {"candidate_id": 102, "skill": "R", "proficiency": 4}, {"candidate_id": 103, "skill": "Python", "proficiency": 3}, {"candidate_id": 103, "skill": "Tableau", "proficiency": 5}, {"candidate_id": 103, "skill": "PostgreSQL", "proficiency": 5}, {"candidate_id": 103, "skill": "Spark", "proficiency": 4}], "Projects": [{"project_id": 501, "skill": "Python", "importance": 4}, {"project_id": 501, "skill": "Tableau", "importance": 3}, {"project_id": 501, "skill": "PostgreSQL", "importance": 5}, {"project_id": 502, "skill": "Python", "importance": 3}, {"project_id": 502, "skill": "Tableau", "importance": 4}, {"project_id": 502, "skill": "R", "importance": 2}]}}`
- **Required output:** `{"columns": ["project_id", "candidate_id", "score"], "rows": [[501, 101, 105], [502, 102, 130]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Candidates`

The objective is to compute `{"columns": ["project_id", "candidate_id", "score"], "rows": [[501, 101, 105], [502, 102, 130]]}` from `{"tables": {"Candidates": [{"candidate_id": 101, "skill": "Python", "proficiency": 5}, {"candidate_id": 101, "skill": "Tableau", "proficiency": 3}, {"candidate_id": 101, "skill": "PostgreSQL", "proficiency": 4}, {"candidate_id": 101, "skill": "TensorFlow", "proficiency": 2}, {"candidate_id": 102, "skill": "Python", "proficiency": 4}, {"candidate_id": 102, "skill": "Tableau", "proficiency": 5}, {"candidate_id": 102, "skill": "PostgreSQL", "proficiency": 4}, {"candidate_id": 102, "skill": "R", "proficiency": 4}, {"candidate_id": 103, "skill": "Python", "proficiency": 3}, {"candidate_id": 103, "skill": "Tableau", "proficiency": 5}, {"candidate_id": 103, "skill": "PostgreSQL", "proficiency": 5}, {"candidate_id": 103, "skill": "Spark", "proficiency": 4}], "Projects": [{"project_id": 501, "skill": "Python", "importance": 4}, {"project_id": 501, "skill": "Tableau", "importance": 3}, {"project_id": 501, "skill": "PostgreSQL", "importance": 5}, {"project_id": 502, "skill": "Python", "importance": 3}, {"project_id": 502, "skill": "Tableau", "importance": 4}, {"project_id": 502, "skill": "R", "importance": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

The query first builds candidate-project matches through shared skills, rejects pairs missing any required skill, calculates scores, and then selects one winner per project with the required tie-break.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Candidates": [{"candidate_id": 101, "skill": "Python", "proficiency": 5}, {"candidate_id": 101, "skill": "Tableau", "proficiency": 3}, {"candidate_id": 101, "skill": "PostgreSQL", "proficiency": 4}, {"candidate_id": 101, "skill": "TensorFlow", "proficiency": 2}, {"candidate_id": 102, "skill": "Python", "proficiency": 4}, {"candidate_id": 102, "skill": "Tableau", "proficiency": 5}, {"candidate_id": 102, "skill": "PostgreSQL", "proficiency": 4}, {"candidate_id": 102, "skill": "R", "proficiency": 4}, {"candidate_id": 103, "skill": "Python", "proficiency": 3}, {"candidate_id": 103, "skill": "Tableau", "proficiency": 5}, {"candidate_id": 103, "skill": "PostgreSQL", "proficiency": 5}, {"candidate_id": 103, "skill": "Spark", "proficiency": 4}], "Projects": [{"project_id": 501, "skill": "Python", "importance": 4}, {"project_id": 501, "skill": "Tableau", "importance": 3}, {"project_id": 501, "skill": "PostgreSQL", "importance": 5}, {"project_id": 502, "skill": "Python", "importance": 3}, {"project_id": 502, "skill": "Tableau", "importance": 4}, {"project_id": 502, "skill": "R", "importance": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

CTE `S` joins `Candidates` and `Projects` with `USING (skill)`. A row exists only when a candidate possesses a skill required by a project. Because both tables have unique keys on their candidate/project plus skill combinations, each matching skill contributes exactly one joined row to that candidate-project group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | CTE `S` joins `Candidates` and `Projects` with `USING (skill... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`COUNT(*) AS matched_skills` counts how many of the project's requirements this candidate matches. Extra candidate skills that the project does not request never join and do not affect the count or score.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["project_id", "candidate_id", "score"], "rows": [[501, 101, 105], [502, 102, 130]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Candidates": [{"candidate_id": 101, "skill": "Python", "proficiency": 5}, {"candidate_id": 101, "skill": "Tableau", "proficiency": 3}, {"candidate_id": 101, "skill": "PostgreSQL", "proficiency": 4}, {"candidate_id": 101, "skill": "TensorFlow", "proficiency": 2}, {"candidate_id": 102, "skill": "Python", "proficiency": 4}, {"candidate_id": 102, "skill": "Tableau", "proficiency": 5}, {"candidate_id": 102, "skill": "PostgreSQL", "proficiency": 4}, {"candidate_id": 102, "skill": "R", "proficiency": 4}, {"candidate_id": 103, "skill": "Python", "proficiency": 3}, {"candidate_id": 103, "skill": "Tableau", "proficiency": 5}, {"candidate_id": 103, "skill": "PostgreSQL", "proficiency": 5}, {"candidate_id": 103, "skill": "Spark", "proficiency": 4}], "Projects": [{"project_id": 501, "skill": "Python", "importance": 4}, {"project_id": 501, "skill": "Tableau", "importance": 3}, {"project_id": 501, "skill": "PostgreSQL", "importance": 5}, {"project_id": 502, "skill": "Python", "importance": 3}, {"project_id": 502, "skill": "Tableau", "importance": 4}, {"project_id": 502, "skill": "R", "importance": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["project_id", "candidate_id", "score"], "rows": [[501, 101, 105], [502, 102, 130]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Relational division with `NOT EXISTS`:** Rejec:** - **Relational division with `NOT EXISTS`:** Reject a candidate when any project skill lacks a candidate match. This expresses “has all skills” directly but scoring still needs matched rows.
- **Compare counts without unique keys:** It could be unsafe if duplicate skill rows existed. The declared keys make the count equality proof valid.
- **`ROW_NUMBER`:** It more directly signals one winner and is equivalent because candidate identifier makes the ordering unique.
- **Rank by score only:** Then all score ties receive rank one and multiple candidates would be returned, violating the lower-ID rule.
- **Candidate has extra skills:** They do not join to that project's requirements and neither help nor hurt.
- **Exact proficiency match:** The `ELSE 0` branch leaves the starting score unchanged for that skill.
- **No eligible candidate:** The project is absent, as required.
- **One required skill:** Coverage equality reduces to possessing that one skill, and scoring still works.
- **Negative adjustment total:** Starting at one hundred does not prevent a score below one hundred when several skills are underqualified.
- **Identifier tie-break:** Candidate IDs are distinct for separate candidates, so the window order is deterministic.
- **Project with no requirements:** Such a project would have no `Projects` rows and cannot appear in this schema-driven query; the intended data represents projects through required skills.
- **Why `COUNT(*)` equals distinct matched skills:** The composite keys prohibit duplicate candidate-skill and project-skill rows. Their equality join can therefore produce at most one row for a particular candidate, project, and skill.
- **Score base added once:** The expression places `+ 100` outside `SUM`. Putting one hundred inside the sum would incorrectly add the starting score once per required skill.
- **Proficiency scale endpoints:** Values one through five need no normalization. The score depends only on greater, equal, or less comparisons, not the magnitude of the difference.
- **Candidate absent from one skill:** Their group has fewer joined rows than `required_skills` and is removed even if their partial score would otherwise be highest.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C+P+J)$. Let $C$ and $P$ be candidate-skill and project-skill row counts, and $J$ the number of equal-skill join rows. Grouping and window ranking generally require hashing or sorting, with a broad bound of $O((C+P+J)\log(C+P+J))$ time and $O(C+P+J)$ working space.
- **Auxiliary Space Complexity:** $O(C + P + J)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
