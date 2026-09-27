# Guided Example: Baseball Game

We trace the step-by-step LIFO operand stack maintenance ($stk$), integer value recording ($stk.\text{push}(x)$), recent score doubling ($stk.\text{push}(2 \cdot stk[-1])$), dual predecessor score summation ($stk.\text{push}(stk[-1] + stk[-2])$), score invalidation removal ($stk.\text{pop}()$), and final cumulative score reduction ($\sum stk$) on representative baseball operation streams:

- **Input:** $operations = [\text{"5"}, \; \text{"2"}, \; \text{"C"}, \; \text{"D"}, \; \text{"+"**}]$
- **Required output:** `30`
  - Scoring operations:
    - An integer string $x$: Append integer value $x$ as a new valid score.
    - `"+"`: Append a new score equal to the sum of the **previous two scores** ($stk[-1] + stk[-2]$).
    - `"D"`: Append a new score equal to **double the previous score** ($2 \times stk[-1]$).
    - `"C"`: Invalidate and **remove the previous score** from the record ($stk.\text{pop}()$).
    - Objective: Calculate the sum of all surviving scores on the scorecard at the end of the game.
- **LIFO Stack Mechanics & Operation Invariant:**
  - **The Stack Representation:**
    - Because each operation depends strictly on the most recent scores (the top 1 or top 2 entries), a **Last-In, First-Out (LIFO) stack** $stk$ models the active game record.
  - **State Transitions for Token $op$:**
    1. $op == \text{"+"}$:
       $$
       stk.\text{append}(stk[-1] + stk[-2])
       $$
    2. $op == \text{"D"}$:
       $$
       stk.\text{append}(stk[-1] \times 2)
       $$
    3. $op == \text{"C"}$:
       $$
       stk.\text{pop}()
       $$
    4. Numeric string $x$:
       $$
       stk.\text{append}(\text{int}(x))
       $$
  - **Final Output:**
    $$
    ans = \sum_{v \in stk} v
    $$
- **Step-by-Step Worked Execution Trace on $[\text{"5"}, \text{"2"}, \text{"C"}, \text{"D"}, \text{"+"**}]:$
  - Initialize empty scorecard stack:
    $$
    stk = []
    $$
  - **Operation 1: $op = \text{"5"}$:**
    - Parse integer: $5$.
    - Push onto record:
      $$
      stk = [\mathbf{5}]
      $$
  - **Operation 2: $op = \text{"2"}$:**
    - Parse integer: $2$.
    - Push onto record:
      $$
      stk = [5, \; \mathbf{2}]
      $$
  - **Operation 3: $op = \text{"C"}$ (Cancel):**
    - Invalidate the most recent score ($2$).
    - Pop from top of stack:
      $$
      stk.\text{pop}() \implies \text{removed } 2
      $$
    - Scorecard after cancellation:
      $$
      stk = [\mathbf{5}]
      $$
  - **Operation 4: $op = \text{"D"}$ (Double):**
    - Most recent score is $stk[-1] = 5$.
    - Double it:
      $$
      5 \times 2 = \mathbf{10}
      $$
    - Push onto scorecard:
      $$
      stk = [5, \; \mathbf{10}]
      $$
  - **Operation 5: $op = \text{"+"}$ (Sum of Previous Two):**
    - Top two scores are $stk[-1] = 10$ and $stk[-2] = 5$.
    - Add them:
      $$
      10 + 5 = \mathbf{15}
      $$
    - Push onto scorecard:
      $$
      stk = [5, \; 10, \; \mathbf{15}]
      $$
  - **Step 6: Final Score Calculation:**
    - Operations stream exhausted.
    - Sum all elements surviving in $stk$:
      $$
      ans = 5 + 10 + 15 = \mathbf{30}
      $$
    - Return **`30`**.
- **Negative Scores and Nested Operations ($[\text{"5"}, \text{"-2"}, \text{"4"}, \text{"C"}, \text{"D"}, \text{"9"}, \text{"+"**}, \text{"+"**}]$):**
  - "5", "-2", "4": $stk = [5, -2, 4]$.
  - "C": pop 4 $\implies [5, -2]$.
  - "D": double $-2 \implies -4$, $stk = [5, -2, -4]$.
  - "9": $stk = [5, -2, -4, 9]$.
  - "+": $-4 + 9 = 5$, $stk = [5, -2, -4, 9, 5]$.
  - "+": $9 + 5 = 14$, $stk = [5, -2, -4, 9, 5, 14]$.
  - Total sum: $5 - 2 - 4 + 9 + 5 + 14 = \mathbf{27}$.

This instance demonstrates stack-based bytecode evaluation and history retraction, mathematically proves why LIFO scoping preserves historical operand availability under cancellation, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a list of baseball score operations:
- Integer $x$: add score $x$.
- `"+"`: add sum of previous two scores.
- `"D"`: add double the previous score.
- `"C"`: invalidate (pop) previous score.
Find the **total sum of scores**.

```text
operations = [ "5", "2", "C", "D", "+" ]

Trace:
  "5" : [ 5 ]
  "2" : [ 5, 2 ]
  "C" : [ 5 ]        (pop 2)
  "D" : [ 5, 10 ]     (double 5 -> 10)
  "+" : [ 5, 10, 15 ] (5 + 10 -> 15)

Total Sum = 5 + 10 + 15 = 30
```

### The Invariant of the Scorecard Stack
- Because all operations only query or modify the top 1 or top 2 scores, a simple dynamic array / stack handles all transitions in strictly $\mathcal{O}(1)$ time per operation.

---

## 2. Conceptual Foundation & Invariants

### 1. Token Evaluation Rules:
$$
stk \leftarrow \begin{cases} stk[:-1] & \text{if } op = \text{"C"} \\ stk \cup \{2 \cdot stk[-1]\} & \text{if } op = \text{"D"} \\ stk \cup \{stk[-1] + stk[-2]\} & \text{if } op = \text{"+"} \\ stk \cup \{\text{int}(op)\} & \text{otherwise} \end{cases}
$$

### 2. Post-Condition Reduction:
$$
\text{Total} = \sum_{x \in stk} x
$$

> **Postfix Operand Valuation Invariant.** The sequence of operations forms a reversible stack grammar over $\mathbb{Z}$, where each operator acts as an endomorphism on $\mathbb{Z}^*$ with guaranteed operand sufficiency.

---

## 3. Step-by-Step Worked Execution

We trace $operations = [\text{"5"}, \text{"2"}, \text{"C"}, \text{"D"}, \text{"+"**}]$:

---

### Step 1: "5" and "2"
- $stk = [5]$.
- $stk = [5, 2]$.

---

### Step 2: "C"
- Pop top score: $2$ removed.
- $stk = [5]$.

---

### Step 3: "D"
- Double top: $5 \times 2 = 10$.
- $stk = [5, 10]$.

---

### Step 4: "+"
- Sum of top two: $5 + 10 = 15$.
- $stk = [5, 10, 15]$.

---

### Step 5: Sum
$$
5 + 10 + 15 = \mathbf{30}
$$

---

## 4. Complete Execution Trace

| Step | Operation $op$ | Semantics | Stack Action | Resulting Stack State | Running Stack Sum |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `"5"` | Push 5 | `append(5)` | `[5]` | $5$ |
| $2$ | `"2"` | Push 2 | `append(2)` | `[5, 2]` | $7$ |
| $3$ | `"C"` | Invalidate | `pop()` (removes 2) | `[5]` | $5$ |
| $4$ | `"D"` | Double top | `append(5 * 2)` | `[5, 10]` | $15$ |
| **$5$** | **`"+"`** | **Sum top two** | **`append(5 + 10)`** | **`[5, 10, 15]`** | **`30`** |
| **End** | — | Total | — | — | **`30`** |

---

## 5. Boundary Cases & Failure Modes

- **Negative Numbers ($"-2"$):** Parsed directly as negative integers.
- **Double Negative ($"D"$ after negative):** Double of $-2$ is $-4$.
- **All Number Operations:** Pure append without pop or arithmetic operators.
- **Guaranteed Validity:** Problem guarantees `"+"`, `"D"`, and `"C"` always have sufficient operands in the stack.

---

## 6. Traps & Common Anti-Patterns

- **Maintaining a Single Running Sum:** Attempting to only keep track of the total sum fails when `"C"` is called after `"+"` or `"D"`, because you cannot know how much to subtract without knowing what was added. The actual history stack is required.
- **Bit Shift Pitfall with Negative Numbers:** In Python, `-2 << 1` correctly evaluates to `-4`, but in C/C++ bit-shifting negative integers can trigger undefined behavior. Using `* 2` is universally safe.
- **Modifying Input Strings In-Place:** Simulating with a dynamic integer list avoids unnecessary string-to-int parsing overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $N$ operations in the input list.
  - Each operation (`push`, `pop`, `+`, `* 2`) runs in strictly $\mathcal{O}(1)$ time.
  - Final sum of $N$ integers takes $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 0.5$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store surviving scores in the stack.
