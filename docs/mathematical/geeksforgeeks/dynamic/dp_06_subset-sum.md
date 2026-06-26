# Formal Mathematical Specification: Subset Sum

## 1. Definitions and Notation
Set $A = \{a_1 \dots a_n\}$. Target $S$. Return boolean $\exists B \subseteq A, \sum_{x \in B} x = S$.

## 2. Algebraic Characterization (Recurrence Relation)
Let $P(i, s) \in \{\text{True}, \text{False}\}$ indicating sum $s$ using subset of $A[1 \dots i]$. $$ P(i, s) = \begin{cases} \text{True} & \text{if } s = 0 \\ \text{False} & \text{if } i = 0 \land s > 0 \\ P(i-1, s) \lor P(i-1, s - a_i) & \text{otherwise (assuming } a_i \leq s \text{)} \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(nS)$.
- **Space Complexity:** $O(S)$ via space reduction.
