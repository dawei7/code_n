# Guided Example: Minimum Moves to Reach Target Score

We analyze and execute the reverse greedy reduction algorithm on a representative problem instance, demonstrating how working backward from the target guarantees optimal move selection.

- **Input:** `target = 19`, `maxDoubles = 2`
- **Output:** `7`

This instance illustrates parity-directed decisions, double-budget exhaustion, and arithmetic shortcutting when no doubles remain.

---

## 1. Problem Overview & Representative Instance

The game begins at integer $1$ and aims to reach a given positive integer $\text{target}$ using the minimum number of valid transitions:
1. **Increment:** Add $1$ to the current value.
2. **Double:** Multiply the current value by $2$, permitted at most $\text{maxDoubles}$ times.

Forward search from $1$ creates a branching tree with ambiguous choices: when is it better to increment versus double? In contrast, reversing the perspective—traveling backward from $\text{target}$ down to $1$—converts a nondeterministic forward search into a fully deterministic greedy sequence:
- Reversing an increment is a decrement by $1$.
- Reversing a double is integer division by $2$, permitted only when the current number is even and $\text{maxDoubles} > 0$.

For our representative instance:
- Start at $\text{target} = 19$ with $\text{maxDoubles} = 2$.
- The goal is to reach $1$ in the minimum number of inverse moves.

---

## 2. Mathematical & Algorithmic Principles

### Parity Determinism in Reverse

Consider an integer state $v > 1$:
- If $v$ is odd, it could not have been produced by a forward doubling because doubling any integer produces an even number. Therefore, the immediate predecessor of an odd $v$ must have been $v - 1$. The reverse move is forced: subtract $1$.
- If $v$ is even and doubles remain ($\text{maxDoubles} > 0$), we have a choice between halving $v \to v/2$ or decrementing $v \to v - 1$.

### Greedy Optimality of Halving Even Numbers

Why is halving always superior to decrementing when $v$ is even?
- Halving $v$ reaches $v/2$ in $1$ move.
- If we instead decrement $v$, we reach the odd number $v - 1$ in $1$ move. Since $v - 1$ is odd, the next move is forced to decrement again to $v - 2$ ($2$ moves total). If we then halve $v - 2$, we reach $(v - 2)/2 = v/2 - 1$ in $3$ moves.
- However, starting from $v/2$ (reached in $1$ move by halving), a single decrement reaches $v/2 - 1$ in $2$ moves. Halving immediately is strictly faster.
- More fundamentally, halving eliminates $v/2$ remaining increment steps in a single move. Because $v/2$ decreases as $v$ gets smaller, doubling contributes the greatest reduction when applied to the largest possible values. Therefore, greedy reverse halving consumes doubling budget on the largest available even numbers.

### Constant-Time Tail Shortcutting

When $\text{maxDoubles} = 0$, no further divisions are permitted. The only available reverse operation is decrementing by $1$ until reaching $1$. For any remaining value $v$, exactly $v - 1$ decrements are required. Rather than simulating these decrements individually, we add $v - 1$ to the move count in $O(1)$ time.

| Principle / Condition | State Condition | Action Taken | Invariant Maintained |
|---|---|---|---|
| Budget Exhausted | $\text{maxDoubles} = 0$ | Add $v - 1$ to moves, terminate | Reaches $1$ via remaining single-step decrements |
| Odd Parity | $v \pmod 2 = 1, v > 1$ | $v \leftarrow v - 1$, $\text{moves} \leftarrow \text{moves} + 1$ | Even parity restored for subsequent halving |
| Even Parity with Budget | $v \pmod 2 = 0, \text{maxDoubles} > 0$ | $v \leftarrow v / 2$, $\text{maxDoubles} \leftarrow \text{maxDoubles} - 1$ | Maximum possible reduction of remaining distance |
| Base Identity | $v = 1$ | Stop, return $\text{moves}$ | Starting integer reached |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the representative instance $\text{target} = 19$, $\text{maxDoubles} = 2$.

```
Forward view:  1 -> 2 -> 4 -> 8 -> 9 -> 18 -> 19  (7 moves)
Reverse view: 19 -> 18 -> 9 -> 8 -> 4 -> 1        (4 steps + 3 decrements = 7 moves)
```

### Step 1: Initial State Inspection
- Current value: $v = 19$.
- Available doubles: $\text{maxDoubles} = 2$.
- Cumulative moves: $0$.
- Parity evaluation: $19 \pmod 2 = 1$ (odd).
- Decision: $19$ cannot be formed by doubling. Subtract $1$: $v \leftarrow 18$.
- Moves incremented by $1$: $\text{moves} = 1$.

### Step 2: First Halving Opportunity
- Current value: $v = 18$.
- Available doubles: $\text{maxDoubles} = 2 > 0$.
- Parity evaluation: $18 \pmod 2 = 0$ (even).
- Decision: Halve immediately: $v \leftarrow 18 / 2 = 9$.
- Budget decremented: $\text{maxDoubles} \leftarrow 2 - 1 = 1$.
- Moves incremented by $1$: $\text{moves} = 2$.

### Step 3: Odd Value Handling
- Current value: $v = 9$.
- Available doubles: $\text{maxDoubles} = 1$.
- Parity evaluation: $9 \pmod 2 = 1$ (odd).
- Decision: Odd value must be decremented: $v \leftarrow 9 - 1 = 8$.
- Moves incremented by $1$: $\text{moves} = 3$.

### Step 4: Second Halving Opportunity
- Current value: $v = 8$.
- Available doubles: $\text{maxDoubles} = 1 > 0$.
- Parity evaluation: $8 \pmod 2 = 0$ (even).
- Decision: Halve immediately: $v \leftarrow 8 / 2 = 4$.
- Budget decremented: $\text{maxDoubles} \leftarrow 1 - 1 = 0$.
- Moves incremented by $1$: $\text{moves} = 4$.

### Step 5: Exhausted Budget Shortcut
- Current value: $v = 4$.
- Available doubles: $\text{maxDoubles} = 0$.
- Decision: With zero doubles remaining, the only path to $1$ is repeated subtraction by $1$.
- Additional moves required: $v - 1 = 4 - 1 = 3$.
- Final total moves: $4 + 3 = 7$.
- Value reaches $1$; search concludes.

---

## 4. Comprehensive State Trace

The table below catalogs each step of the reverse reduction process:

| Step | Current Value $v$ | Parity | Budget Left | Operation Executed | Step Cost | New Value $v'$ | Cumulative Moves |
|---|---|---|---|---|---|---|---|
| Initial | $19$ | Odd | $2$ | Setup / Parity Check | $0$ | $19$ | $0$ |
| 1 | $19$ | Odd | $2$ | Decrement ($v - 1$) | $1$ | $18$ | $1$ |
| 2 | $18$ | Even | $2$ | Halve ($v / 2$) | $1$ | $9$ | $2$ |
| 3 | $9$ | Odd | $1$ | Decrement ($v - 1$) | $1$ | $8$ | $3$ |
| 4 | $8$ | Even | $1$ | Halve ($v / 2$) | $1$ | $4$ | $4$ |
| 5 | $4$ | Even | $0$ | Tail Decrements ($v - 1$) | $3$ | $1$ | $7$ |

Forward reconstruction of the optimal move sequence:
1. Start at $1$.
2. Increment to $2$ (move 1).
3. Increment to $3$ (move 2).
4. Increment to $4$ (move 3).
5. Double to $8$ (move 4, double 1 used).
6. Increment to $9$ (move 5).
7. Double to $18$ (move 6, double 2 used).
8. Increment to $19$ (move 7).

Both directions confirm an optimal move count of $7$.

---

## 5. Algorithmic Correctness & Soundness

### Greedy Choice Property
At every even integer $v$ where a doubling budget remains, choosing to divide by $2$ instead of decrementing by $1$ is guaranteed not to increase the total number of moves. 

Let $M(v, d)$ denote the minimum moves to reach $1$ from $v$ with $d$ available doubles:
- If $v$ is odd, $M(v, d) = 1 + M(v - 1, d)$ because no division is valid.
- If $v$ is even and $d > 0$:
  - Transition A (halve): $1 + M(v/2, d - 1)$.
  - Transition B (decrement): $1 + M(v - 1, d) = 2 + M(v - 2, d)$.
- Because $v/2 \le v - 2$ for all even $v \ge 4$, halving achieves an equal or smaller value in $1$ move than decrementing achieves in $2$ moves. When $v = 2$, halving reaches $1$ in $1$ move ($1 + 0 = 1$), while decrementing reaches $1$ in $1$ move ($1 + 0 = 1$). In all cases, Transition A is optimal.

### Optimal Substructure
Each decision leaves an independent subproblem $M(v', d')$ with strictly smaller target $v' < v$ and monotonic decrease in remaining operations. The absence of negative feedback cycles and state overlap guarantees global convergence to the minimum move count.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Target is Already $1$:** If $\text{target} = 1$, zero moves are required regardless of $\text{maxDoubles}$. The algorithm immediately returns $0$.
2. **Zero Doubling Budget ($\text{maxDoubles} = 0$):** Every move must be an increment. The answer is $\text{target} - 1$. For large targets (e.g., $10^9$), arithmetic shortcutting prevents $10^9$ loop iterations.
3. **Abundant Doubling Budget ($\text{maxDoubles} \ge \log_2(\text{target})$):** The budget is never exhausted. The target is repeatedly halved (with intermediate decrements when odd) all the way down to $1$. Unused doubles remain surplus without penalty.
4. **Target is a Power of Two:** For $\text{target} = 2^k$ with $\text{maxDoubles} \ge k$, no decrements are ever needed. The target is halved $k$ times directly to $1$, yielding exactly $k$ moves.

### Common Anti-Patterns
- **Forward Breadth-First Search (BFS):** Exploring forward states with BFS requires storing states up to $10^9$, resulting in catastrophic memory exhaustion and time limit exceeded.
- **Forward Dynamic Programming:** Storing an array of size $\text{target}$ costs $O(\text{target})$ auxiliary space, which fails for $\text{target} = 10^9$.
- **Simulating Tail Decrements Iteratively:** When $\text{maxDoubles}$ hits $0$, running a loop `while target > 1: target -= 1` executes up to $10^9$ times. Using `moves += target - 1` resolves the remaining steps in $O(1)$ operations.

---

## 7. Complexity Analysis

### Time Complexity
- While $\text{maxDoubles} > 0$ and $v > 1$:
  - If $v$ is odd, one decrement makes it even.
  - The subsequent step is guaranteed to halve $v$.
  - Therefore, at most two operations reduce $v$ by at least half.
  - The halving loop runs at most $\min(\text{maxDoubles}, \lfloor\log_2(\text{target})\rfloor)$ times.
- When $\text{maxDoubles} = 0$, the remaining distance is calculated in $O(1)$ arithmetic operations.
- Total time complexity is $O(\min(\text{maxDoubles}, \log \text{target}))$. For $\text{target} \le 10^9$, this is at most approximately $60$ operations, which executes in less than a microsecond.

### Auxiliary Space Complexity
- The algorithm tracks three scalar variables: current value $v$, remaining budget $\text{maxDoubles}$, and accumulated move counter.
- No dynamic memory allocation, recursive call stack, or auxiliary data structures are used.
- Total auxiliary space complexity is $O(1)$.
