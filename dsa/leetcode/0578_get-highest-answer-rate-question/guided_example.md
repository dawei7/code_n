# Guided Example: Get Highest Answer Rate Question

We trace the step-by-step survey action classification (differentiating `show`, `answer`, `skip`), conditional count aggregation ($\sum \mathbf{1}[\text{action} = \text{'answer'}]$, $\sum \mathbf{1}[\text{action} = \text{'show'}]$), answer rate ratio computation ($N_{ans} / N_{show}$), descending rate ordering with ascending question ID tie-breaking, and top-1 question extraction on representative survey logs:

- **Input:**
  - `SurveyLog` table:
    | `id` | `action` | `question_id` | `answer_id` | `q_num` | `timestamp` |
    |:---:|:---:|:---:|:---:|:---:|:---:|
    | $5$ | `show` | $285$ | `null` | $1$ | $123$ |
    | $5$ | `answer` | $285$ | $124124$ | $1$ | $124$ |
    | $5$ | `show` | $369$ | `null` | $2$ | $125$ |
    | $5$ | `skip` | $369$ | `null` | $2$ | $126$ |
- **Required output:**
  | `survey_log` |
  |:---:|
  | $285$ |
  - Business metric definition:
    $$
    \text{Answer Rate} = \frac{\text{Total times action = 'answer' for that question}}{\text{Total times action = 'show' for that question}}
    $$
  - Tie-breaking requirement: If multiple questions share the identical maximum answer rate, choose the question with the **smallest `question_id`**.
  - Output schema: The resulting column must be renamed to `survey_log`.
- **Relational Aggregation & Ratio Evaluation Trace:**
  - **Step 1: Partition Events by `question_id`:**
    - Two distinct questions appear in the log: $285$ and $369$.
  - **Step 2: Tally Action Categories per Question:**
    - **Question $285$:**
      - Action `show`: 1 event (timestamp 123) $\implies N_{show} = \mathbf{1}$
      - Action `answer`: 1 event (timestamp 124) $\implies N_{ans} = \mathbf{1}$
      - Action `skip`: 0 events
      - Calculate Answer Rate:
        $$
        \text{Rate}(285) = \frac{N_{ans}}{N_{show}} = \frac{1}{1} = \mathbf{1.0}
        $$
    - **Question $369$:**
      - Action `show`: 1 event (timestamp 125) $\implies N_{show} = \mathbf{1}$
      - Action `answer`: 0 events $\implies N_{ans} = \mathbf{0}$
      - Action `skip`: 1 event (timestamp 126) $\implies$ Does not count towards answer numerator.
      - Calculate Answer Rate:
        $$
        \text{Rate}(369) = \frac{N_{ans}}{N_{show}} = \frac{0}{1} = \mathbf{0.0}
        $$
  - **Step 3: Multi-Column Ordering (Rate DESC, question_id ASC):**
    - Ordered candidate list:
      1. Question $285$: Rate $1.0$
      2. Question $369$: Rate $0.0$
  - **Step 4: Slice Top 1 Record with `LIMIT 1`:**
    - Highest rate: Question $285$.
    - Rename column header to `survey_log`:
      | `survey_log` |
      |:---:|
      | $285$ |
- **Tie-Breaking Demonstration:**
  - Suppose Question $100$ has $1$ show and $1$ answer ($rate = 1.0$).
  - Question $200$ has $1$ show and $1$ answer ($rate = 1.0$).
  - Tie on answer rate ($1.0 == 1.0$) $\implies$ Secondary sort `question_id ASC` picks $\min(100, 200) = \mathbf{100}$.
- **Multiple Answers for a Question:**
  - If a question is shown 2 times and answered 2 times $\implies 2 / 2 = 1.0$.

This instance demonstrates ratio aggregation across heterogeneous categorical event logs, mathematically proves why composite sorting resolves rate maximization with identifier tie-breaking, and derives $O(N \log K)$ execution time and $O(K)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a table `SurveyLog` with actions (`"show"`, `"answer"`, `"skip"`):
Find the `question_id` that has the **highest answer rate**.
If there is a tie, return the question with the **smallest `question_id`**.
Rename the column to `survey_log`.

```text
Question 285:
  1 'show', 1 'answer' -> Rate = 1 / 1 = 1.0

Question 369:
  1 'show', 0 'answer', 1 'skip' -> Rate = 0 / 1 = 0.0

Winner = 285
Output Column: survey_log = 285
```

### Clarifying the Denominator and Numerator
- **Numerator:** Count of rows where `action = 'answer'`.
- **Denominator:** Count of rows where `action = 'show'`.
- Rows with `action = 'skip'` do **not** enter either the numerator or the denominator directly.
- The resulting fraction must be sorted in descending order, with question ID in ascending order to break ties.

---

## 2. Conceptual Foundation & Invariants

### 1. Conditional Sum Formulation:
For each question:
$$
\text{Answers} = \sum \mathbf{1}[action = \text{'answer'}]
$$
$$
\text{Shows} = \sum \mathbf{1}[action = \text{'show'}]
$$
$$
\text{Rate} = \frac{\text{Answers}}{\text{Shows}}
$$

### 2. SQL Grouping and Ordering:
```sql
SELECT question_id AS survey_log
FROM SurveyLog
GROUP BY question_id
ORDER BY
    SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) * 1.0 /
    SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END) DESC,
    question_id ASC
LIMIT 1;
```

> **Lexicographical Tie-Break Invariant.** The compound sort specification `ORDER BY rate DESC, question_id ASC` uniquely defines a total order across all questions, ensuring reproducible top-1 selection.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Group by `question_id`
- Group 285:
  - Row 1: `action = 'show'`
  - Row 2: `action = 'answer'`
- Group 369:
  - Row 3: `action = 'show'`
  - Row 4: `action = 'skip'`

---

### Step 2: Compute Fractions
- Group 285:
  $$
  \text{Answers} = 1, \quad \text{Shows} = 1 \implies \text{Rate} = \frac{1}{1} = 1.0
  $$
- Group 369:
  $$
  \text{Answers} = 0, \quad \text{Shows} = 1 \implies \text{Rate} = \frac{0}{1} = 0.0
  $$

---

### Step 3: Order and Limit 1
- Ordered list:
  1. $285$ (Rate 1.0)
  2. $369$ (Rate 0.0)
- Select top 1 $\implies 285$.

---

### Step 4: Emit Output
$$
\text{survey\_log} = \mathbf{285}
$$

---

## 4. Complete Execution Trace

| `question_id` | Shows ($N_{show}$) | Answers ($N_{ans}$) | Skips | Answer Rate ($N_{ans} / N_{show}$) | Plurality Rank |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$285$** | $1$ | $1$ | $0$ | **$1.0$** | **$1$ (Top 1)** |
| $369$ | $1$ | $0$ | $1$ | $0.0$ | $2$ |
| **Output** | — | — | — | — | **`survey_log: 285`** |

---

## 5. Boundary Cases & Failure Modes

- **Tied Rates ($1.0 == 1.0$):** Secondary order `question_id ASC` selects the smaller numeric ID.
- **Zero Answers ($0$ for all questions):** All rates evaluate to $0.0$; secondary order picks the smallest `question_id`.
- **Question Shown Multiple Times:** $N_{show} > 1$ scales the denominator appropriately.

---

## 6. Traps & Common Anti-Patterns

- **Dividing by Total Rows Instead of 'show' Rows:** Dividing answers by all actions (including skips and answers) calculates an incorrect ratio. The problem explicitly defines the denominator as the number of times it was **shown**.
- **Forgetting `* 1.0` (Integer Division Truncation):** In dialects like PostgreSQL or SQL Server, dividing integer $1 / 2$ yields $0$. Multiplying by $1.0$ or casting to float prevents integer truncation.
- **Forgetting the Column Alias `survey_log`:** Returning `question_id` without `AS survey_log` fails the automated output schema comparison.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of rows in `SurveyLog` and $K$ be the number of distinct questions.
  - Grouping and conditional sums: $\mathcal{O}(N)$ operations.
  - Sorting $K$ questions: $\mathcal{O}(K \log K)$ (or $O(K)$ with top-1 selection).
  - Total Time: $\mathcal{O}(N + K \log K)$. For $N = 10^5, K = 1000$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space to maintain group accumulator totals.
