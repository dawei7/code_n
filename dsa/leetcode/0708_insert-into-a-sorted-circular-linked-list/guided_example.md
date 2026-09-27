# Guided Example: Insert into a Sorted Circular Linked List

We trace the step-by-step circular linked list pointer navigation ($prev, curr$), standard interior sorted placement ($prev.val \le insertVal \le curr.val$), wrap-around boundary pivot detection ($prev.val > curr.val$), global extremum insertion ($insertVal \ge \max \lor insertVal \le \min$), full-cycle loop exhaustion ($curr == head$), and circular link splicing on representative cyclic topologies:

- **Input:**
  - Circular list: $head = [3, 4, 1]$ (cycle: $3 \to 4 \to 1 \to 3$)
  - Value to insert: $insertVal = 2$
- **Required output:** $[3, 4, 1, 2]$ (circularly equivalent to $1 \to 2 \to 3 \to 4 \to 1$)
  - Problem requirements:
    - The linked list is circular (the tail's $.next$ points back to the head).
    - Elements are sorted in non-descending order along the cycle, except at the single pivot wrap-around point where the maximum element connects back to the minimum element ($4 \to 1$).
    - The given $head$ pointer may reference **any arbitrary node** in the cycle.
    - If the list is empty ($head == \text{null}$), create a single-node circular list pointing to itself.
    - After inserting $insertVal$, the cycle must remain completely sorted.
- **The Three Insertion Predicates Invariant:**
  - **The Adjacent Pointers:**
    - Initialize $prev = head, \; curr = head.next$.
    - Advance step-by-step around the cycle until one of the following three mutually exhaustive conditions is met:
  - **1. Standard Interior Insertion:**
    - If the value falls neatly between two ascending nodes:
      $$
      prev.val \le insertVal \le curr.val
      $$
    - The position between $prev$ and $curr$ preserves non-descending order.
  - **2. Wrap-Around Pivot Boundary:**
    - If $prev.val > curr.val$, then $prev$ is the **global maximum** and $curr$ is the **global minimum** of the entire cycle!
    - If $insertVal$ is a new global maximum ($insertVal \ge prev.val$) OR a new global minimum ($insertVal \le curr.val$):
      $$
      prev.val > curr.val \quad \text{and} \quad (insertVal \ge prev.val \lor insertVal \le curr.val)
      $$
    - The value belongs at the wrap-around seam between the maximum and minimum.
  - **3. Full Cycle Exhaustion ($curr == head$):**
    - If the pointers traverse the complete circle without satisfying Condition 1 or 2:
    - This occurs when all nodes in the list have the **exact same value** (e.g. $[3, 3, 3]$).
    - In this degenerate case, any position in the cycle is valid! Splicing between $prev$ and $curr$ is always correct.
- **Step-by-Step Worked Execution Trace on $[3, 4, 1]$ for $insertVal = 2$:**
  - Initial nodes:
    $$
    head = \text{Node}(3), \quad prev = \text{Node}(3), \quad curr = \text{Node}(4)
    $$
  - Create new node: $newNode = \text{Node}(2)$.
  - **Iteration 1 ($prev = 3, curr = 4$):**
    - Check Condition 1:
      $$
      prev.val \le insertVal \le curr.val \implies 3 \le 2 \le 4 \quad \mathbf{(False)}
      $$
    - Check Condition 2:
      $$
      prev.val > curr.val \implies 3 > 4 \quad \mathbf{(False)}
      $$
    - Pointers advance:
      $$
      prev \leftarrow \text{Node}(4), \quad curr \leftarrow \text{Node}(1)
      $$
  - **Iteration 2 ($prev = 4, curr = 1$):**
    - Check Condition 1:
      $$
      4 \le 2 \le 1 \quad \mathbf{(False)}
      $$
    - Check Condition 2 (Pivot Wrap-Around):
      $$
      prev.val > curr.val \implies 4 > 1 \quad \mathbf{(True!)}
      $$
      - Test extremum qualification:
        $$
        insertVal \ge 4 \implies 2 \ge 4 \quad \mathbf{(False)}
        $$
        $$
        insertVal \le 1 \implies 2 \le 1 \quad \mathbf{(False)}
        $$
      - Value 2 is neither $\ge 4$ nor $\le 1$, so it does not belong at the wrap-around seam.
    - Pointers advance:
      $$
      prev \leftarrow \text{Node}(1), \quad curr \leftarrow \text{Node}(3)
      $$
  - **Iteration 3 ($prev = 1, curr = 3$):**
    - Check Condition 1:
      $$
      prev.val \le insertVal \le curr.val \implies 1 \le 2 \le 3 \quad \mathbf{(True!)}
      $$
    - Satisfies Condition 1! Natural sorted location identified.
    - Break traversal loop.
  - **Step 4: Splice New Node into Cycle:**
    - Link $newNode$ into the seam between $prev$ and $curr$:
      $$
      prev.next \leftarrow newNode \quad (1.next \leftarrow 2)
      $$
      $$
      newNode.next \leftarrow curr \quad (2.next \leftarrow 3)
      $$
  - **Step 5: Output:**
    - Cycle topology is now:
      $$
      3 \to 4 \to 1 \to \mathbf{2} \to 3
      $$
    - Return original $head$ pointer ($\text{Node } 3$).
- **Insert at Wrap-Around Seam Trace ($[3, 5, 1], insertVal = 0$):**
  - Node 5 is maximum, Node 1 is minimum.
  - At $prev = 5, curr = 1$:
    - $prev.val > curr.val$ ($5 > 1$).
    - $insertVal \le curr.val$ ($0 \le 1$ is True).
    - Belongs between 5 and 1!
    - Splice: $5 \to 0 \to 1$.
- **Empty List Case ($head = \text{null}, insertVal = 1$):**
  - Create $node = \text{Node}(1)$.
  - Set self-loop: $node.next = node$.
  - Return $node$.

This instance demonstrates cyclic data structure traversal and circular invariant preservation, mathematically proves why partition into monotonic arcs and pivot boundaries guarantees a valid insertion seam, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a circular sorted linked list and value $insertVal$:
Insert $insertVal$ so that the list remains **sorted and circular**.
$head$ can be any node in the cycle.

```text
Cycle: 3 -> 4 -> 1 -> (back to 3)
Target to insert: 2

Traversal:
  Step 1: prev = 3, curr = 4 -> 2 is not between 3 and 4
  Step 2: prev = 4, curr = 1 -> wrap-around, but 2 is not >= 4 or <= 1
  Step 3: prev = 1, curr = 3 -> 1 <= 2 <= 3 -> FOUND SEAM!

Splice:
  1 -> 2 -> 3
Cycle becomes: 3 -> 4 -> 1 -> 2 -> 3
```

### The Invariant of the Three Insertion Criteria
- Across any circular sorted list, a new value $v$ fits if and only if:
  1. It lies between two normal ascending nodes: $prev \le v \le curr$.
  2. It is a new extreme at the wrap seam ($prev > curr$): $v \ge prev$ or $v \le curr$.
  3. The cycle has completed a full loop ($curr == head$), meaning all elements are identical.

---

## 2. Conceptual Foundation & Invariants

### 1. Loop Exit Predicates:
Break traversal when:
$$
(prev.val \le v \le curr.val) \quad \lor \quad (prev.val > curr.val \land (v \ge prev.val \lor v \le curr.val))
$$
Or when $curr == head$ (cycle exhausted).

### 2. Splicing Invariant:
$$
prev.next \leftarrow newNode
$$
$$
newNode.next \leftarrow curr
$$

> **Circular Total Order Preservation Invariant.** The quotient group $\mathbb{R} / \mathbb{Z}$ maintains a total cyclic order under adjacent arc insertion: any real $x$ falls into either an ascending geodesic arc $[u, w]$ or the unique discontinuity gap $[\max, \min]$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Pair $(3, 4)$
- $3 \le 2 \le 4$ is False. Advance.

---

### Step 2: Pair $(4, 1)$
- $4 > 1$, but $2 \not\ge 4$ and $2 \not\le 1$. Advance.

---

### Step 3: Pair $(1, 3)$
- $1 \le 2 \le 3$ is **True!** Break.

---

### Step 4: Splicing
- $1.next \leftarrow 2$.
- $2.next \leftarrow 3$.
- Return $head$ (Node 3).

---

## 4. Complete Execution Trace

| Step | Current $prev$ | Current $curr$ | Ascending Test | Wrap-Around Test | Match Condition? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | Node $3$ | Node $4$ | $3 \le 2 \le 4$ (No) | $3 > 4$ (No) | No | Advance |
| $2$ | Node $4$ | Node $1$ | $4 \le 2 \le 1$ (No) | $2 \ge 4 \lor 2 \le 1$ (No)| No | Advance |
| **$3$** | **Node $1$** | **Node $3$** | **$1 \le 2 \le 3$ (Yes)** | — | **Match!** | **Splice $1 \to 2 \to 3$** |

---

## 5. Boundary Cases & Failure Modes

- **Empty List ($head = \text{null}$):** Create $node$, set $node.next = node$, return $node$.
- **Single Node Cycle ($[1]$):** Loop condition $curr == head$ fires immediately $\implies$ splices $1 \to 0 \to 1$.
- **All Elements Identical ($[3, 3, 3]$):** Traverses full cycle back to $head$, splices anywhere without infinite looping.
- **New Maximum ($[1, 3, 5], val = 6$):** At $5 \to 1$, $6 \ge 5$ matches wrap-around test $\implies$ splices $5 \to 6 \to 1$.

---

## 6. Traps & Common Anti-Patterns

- **Infinite While Loop on Uniform Lists:** If the condition `while curr != head:` is missing or incorrect, identical lists like $[3, 3, 3]$ loop forever.
- **Overlooking New Global Minimums:** Inserting $0$ into $[3, 4, 1]$ requires recognizing that $0 \le 1$ at the wrap-around boundary $4 \to 1$.
- **Returning the Inserted Node Instead of Head:** When the list is non-empty, you must return the **original given $head$**, not the newly inserted node.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Traverses at most one complete cycle of the list: at most $N$ node visits.
  - At each node, performs constant number of pointer updates: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 0.1$ ms for $N = 5 \times 10^4$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only allocated new node and local pointers $prev, curr$).
