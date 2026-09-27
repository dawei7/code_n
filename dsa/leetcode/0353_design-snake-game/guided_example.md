# Guided Example: Design Snake Game

We trace the step-by-step deque body representation (`deque([(0, 0)])`), hash set occupancy tracking (`vis`), boundary wall detection, lazy tail eviction vs elongation on food consumption, and self-collision prevention on representative Snake game sequences:

- **Input:** `width = 3, height = 2, food = [[1, 2], [0, 1]]`, sequence of moves:
  1. `move("R")` $\implies 0$ (Head moves $(0, 0) \to (0, 1)$, tail popped)
  2. `move("D")` $\implies 0$ (Head moves $(0, 1) \to (1, 1)$, tail popped)
  3. `move("R")` $\implies 1$ (Head reaches food at $(1, 2)$! Snake grows to length 2)
  4. `move("U")` $\implies 1$ (Head moves $(1, 2) \to (0, 2)$, tail popped)
  5. `move("L")` $\implies 2$ (Head reaches food at $(0, 1)$! Snake grows to length 3)
  6. `move("U")` $\implies -1$ (Head moves $(0, 1) \to (-1, 1)$, hits top boundary wall!)
- **Required output:** `[0, 0, 1, 1, 2, -1]`
- **Immediate Wall Collision:** $\text{width} = 1, \text{height} = 2, \text{moves} = [\text{"R"}] \implies -1$ (Column 1 exceeds width 1)
- **Vacating Tail Self-Move:** Moving into the cell currently occupied by the tail is **legal** on a non-food step, because the tail vacates the square in the same tick before the head enters!

This instance demonstrates real-time 2D grid simulation, mathematically proves why combining a double-ended queue with a hash set guarantees $O(1)$ time per move without full body scanning, explains tail eviction timing, and analyzes memory constraints.

---

## 1. Instance & Teaching Goal

Given a 2D grid of dimensions $\text{height} = 2, \text{width} = 3$ and food coordinates `[[1, 2], [0, 1]]`:
The snake starts at `(0, 0)` with initial length 1 and score 0.
Move the snake according to directional commands (`"U"`, `"D"`, `"L"`, `"R"`):
- Return the current **score** (number of foods eaten).
- If the snake collides with a wall or with its own body, return **$-1$** (Game Over).

```text
Board (Height=2, Width=3):
Initial: Snake at (0,0), Food at (1,2)
  [S, ., .]
  [., ., F]

Move 1 ("R"): Snake head moves to (0,1), tail (0,0) vacated
  [., S, .]
  [., ., F]  -> Return score 0

Move 2 ("D"): Snake head moves to (1,1), tail (0,1) vacated
  [., ., .]
  [., S, F]  -> Return score 0

Move 3 ("R"): Snake head reaches Food at (1,2)! Tail (1,1) NOT vacated
  [., ., .]
  [., S, S]  -> Snake grows to length 2! Return score 1
```

---

## 2. Conceptual Foundation & Invariants

### 1. Dual Body Tracking Architecture
1. **Deque (`q`):**
   Maintains the ordered body segments from head (`q[0]`) to tail (`q[-1]`).
   Allows $O(1)$ insertion at the head (`appendleft`) and $O(1)$ removal at the tail (`pop`).
2. **Hash Set (`vis`):**
   Stores all active coordinate pairs currently occupied by the snake.
   Allows $O(1)$ instantaneous self-collision testing.

### 2. The Move Lifecycle on `move(direction)`:
1. **Compute Candidate Head:**
   From current head $(i, j) = q[0]$:
   - `"U"`: $x = i - 1, y = j$
   - `"D"`: $x = i + 1, y = j$
   - `"L"`: $x = i, y = j - 1$
   - `"R"`: $x = i, y = j + 1$
2. **Wall Collision Guard:**
   If $x < 0$ or $x \ge m$ or $y < 0$ or $y \ge n$: return **$-1$**.
3. **Food Consumption vs Tail Eviction:**
   - If $(x, y) == \text{food}[idx]$:
     - Increment `score += 1` and `idx += 1`.
     - Do NOT pop tail (snake grows).
   - Else:
     - Pop tail: `vis.remove(q.pop())`.
4. **Self-Collision Guard:**
   If $(x, y) \in vis$: return **$-1$**.
5. **Finalize Head:**
   `q.appendleft((x, y))`, `vis.add((x, y))`.
   Return `self.score`.

> **Invariant.** The tail is evicted *before* self-collision evaluation. A snake can safely chase its own tail into the cell it is simultaneously vacating.

---

## 3. Step-by-Step Worked Execution

We trace `width = 3, height = 2, food = [[1, 2], [0, 1]]`:
Initial state: `q = deque([(0, 0)]), vis = {(0, 0)}, score = 0, idx = 0`.

---

### Step 1: `move("R")`
- Current head: $(0, 0) \implies$ New head: $(0, 0 + 1) = (0, 1)$.
- Wall check: $0 \le 0 < 2$ and $0 \le 1 < 3 \implies$ valid.
- Food check: Target food is $[1, 2] \ne (0, 1)$ (No food).
- Evict tail: Pop $(0, 0)$ from `q` and remove from `vis`.
- Collision check: $(0, 1) \notin vis$ (Clear).
- Push head: `q = [(0, 1)], vis = {(0, 1)}`.
- Return score: **$0$**.

---

### Step 2: `move("D")`
- Current head: $(0, 1) \implies$ New head: $(0 + 1, 1) = (1, 1)$.
- Wall check: valid.
- Food check: $[1, 2] \ne (1, 1)$ (No food).
- Evict tail: Pop $(0, 1)$ from `q` and remove from `vis`.
- Push head: `q = [(1, 1)], vis = {(1, 1)}`.
- Return score: **$0$**.

---

### Step 3: `move("R")` — Food Eaten!
- Current head: $(1, 1) \implies$ New head: $(1, 1 + 1) = (1, 2)$.
- Wall check: valid.
- Food check: $(1, 2) == \text{food}[0]$! **Food Consumed!**
  - `score += 1 \implies score = 1`.
  - `idx += 1 \implies idx = 1` (Next food: `[0, 1]`).
  - Tail $(1, 1)$ is **retained** (no pop).
- Collision check: $(1, 2) \notin vis$.
- Push head: `q = [(1, 2), (1, 1)], vis = {(1, 2), (1, 1)}`.
- Return score: **$1$**.

---

### Step 4: `move("U")`
- Current head: $(1, 2) \implies$ New head: $(1 - 1, 2) = (0, 2)$.
- Wall check: valid.
- Food check: $[0, 1] \ne (0, 2)$ (No food).
- Evict tail: Pop $(1, 1)$ from `q` and remove from `vis`.
- Push head: `q = [(0, 2), (1, 2)], vis = {(0, 2), (1, 2)}`.
- Return score: **$1$**.

---

### Step 5: `move("L")` — Second Food Eaten!
- Current head: $(0, 2) \implies$ New head: $(0, 2 - 1) = (0, 1)$.
- Food check: $(0, 1) == \text{food}[1]$! **Food Consumed!**
  - `score = 2`, `idx = 2`.
  - Tail $(1, 2)$ is retained.
- Push head: `q = [(0, 1), (0, 2), (1, 2)]`.
- Return score: **$2$**.

---

### Step 6: `move("U")` — Boundary Wall Collision!
- Current head: $(0, 1) \implies$ New head: $(0 - 1, 1) = (-1, 1)$.
- Wall check: $x = -1 < 0$ (**Out of Bounds!**).
- Collision detected with upper wall!
- Return: **$-1$** (Game Over).

---

## 4. Complete Execution Trace

```text
SnakeGame(width = 3, height = 2, food = [[1, 2], [0, 1]])

Move 1 ('R'): head -> (0, 1), food not matched -> pop (0, 0), q=[(0,1)]         -> score 0
Move 2 ('D'): head -> (1, 1), food not matched -> pop (0, 1), q=[(1,1)]         -> score 0
Move 3 ('R'): head -> (1, 2), FOOD [1, 2] HIT! -> keep tail, q=[(1,2), (1,1)]   -> score 1
Move 4 ('U'): head -> (0, 2), food not matched -> pop (1, 1), q=[(0,2), (1,2)]   -> score 1
Move 5 ('L'): head -> (0, 1), FOOD [0, 1] HIT! -> keep tail, q=[(0,1),(0,2),(1,2)]-> score 2
Move 6 ('U'): head -> (-1, 1), x < 0 -> WALL COLLISION!                        -> return -1
```

| Step | Move Direction | Candidate Head $(x, y)$ | Wall Collision? | Food Encountered? | Tail Evicted | Active Snake Body (`q`) | Return Value |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Init | - | $(0, 0)$ | No | - | None | `[(0, 0)]` | - |
| 1 | `"R"` | $(0, 1)$ | No | No | $(0, 0)$ | `[(0, 1)]` | **0** |
| 2 | `"D"` | $(1, 1)$ | No | No | $(0, 1)$ | `[(1, 1)]` | **0** |
| **3** | **`"R"`** | **$(1, 2)$** | **No** | **Yes (`food[0]`)** | **None (Grows)** | **`[(1, 2), (1, 1)]`** | **$\mathbf{1}$** |
| 4 | `"U"` | $(0, 2)$ | No | No | $(1, 1)$ | `[(0, 2), (1, 2)]` | **1** |
| **5** | **`"L"`** | **$(0, 1)$** | **No** | **Yes (`food[1]`)** | **None (Grows)** | **`[(0, 1), (0, 2), (1, 2)]`** | **$\mathbf{2}$** |
| **6** | **`"U"`** | **$(-1, 1)$** | **Yes ($x < 0$)** | - | - | Game Over | **$\mathbf{-1}$** |

---

## 5. Algorithmic Correctness

**Soundness.** Checking wall boundaries before state mutation prevents illegal memory indexing. Removing the tail before self-collision testing ensures that entering the space vacated by the tail in the current turn is not penalized as a collision, strictly conforming to authentic Snake game mechanics. Using `vis` ensures any self-intersection with the body is detected immediately.

**Completeness.** Foods appear sequentially in the exact specified order. The food index `self.idx` increments only after the current target food is eaten, guaranteeing that future food spawns are inactive until all predecessor foods have been consumed.

---

## 6. Traps This Instance Exposes

- **Order of Tail Eviction and Collision Check:** Checking `(x, y) in self.vis` *before* popping the tail creates a false collision when the snake moves into its own tail position. The tail must be removed first on non-food turns.
- **Scanning List Instead of Hash Set:** Testing `(x, y) in self.q` when `q` is a Python `list` or `deque` takes $O(L)$ linear time, slowing down moves for long snakes. Maintaining a parallel `set` `vis` keeps collision testing $O(1)$.
- **Food Exhaustion:** After all foods are eaten (`idx == len(food)`), further food checks must be skipped to avoid `IndexError`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ per `move` call. Deque operations (`pop`, `appendleft`) and set operations (`add`, `remove`, membership lookup) run in $O(1)$ constant time.
- **Auxiliary Space Complexity:** $O(N + F)$, where $N$ is the maximum snake body length ($N \le \text{height} \times \text{width}$) and $F$ is the food list size.
