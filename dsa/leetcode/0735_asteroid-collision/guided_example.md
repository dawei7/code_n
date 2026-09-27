# Guided Example: Asteroid Collision

We trace the step-by-step momentum and direction resolution on a 1D axis, LIFO stack persistence for right-moving bodies ($x > 0$), left-moving body collision cascades ($x < 0$ vs $top > 0$), smaller asteroid explosion ($top < -x \implies \text{pop}$), mutual annihilation on equal mass ($top == -x \implies \text{pop}$ and halt), larger blocker absorption ($top > -x \implies \text{incoming destroyed}$), and stable orbital remnant output on representative asteroid sequences:

- **Input:** $asteroids = [10, 2, -5]$
- **Required output:** `[10]`
  - Collision dynamics:
    - Absolute value $|x|$ represents the **mass/size** of the asteroid.
    - Sign of $x$ represents its **direction of travel**:
      - Positive ($+x$): Moving **right** ($\to$).
      - Negative ($-x$): Moving **left** ($\leftarrow$).
    - All asteroids move at the same uniform velocity.
    - Collision rules:
      - Two asteroids moving in the same direction never meet.
      - A left-moving asteroid ($< 0$) to the left of a right-moving asteroid ($> 0$) moves away from it ($\leftarrow \quad \to$) and never collides.
      - A collision occurs strictly when a **right-moving asteroid precedes a left-moving asteroid** ($\to \quad \leftarrow$).
      - If sizes differ, the strictly smaller asteroid explodes and is obliterated.
      - If sizes are identical, **both asteroids explode** (mutual annihilation).
    - For $[10, 2, -5]$:
      - $10$ moves right.
      - $2$ moves right behind $10$.
      - $-5$ moves left, meeting $2$: mass $5 > 2 \implies 2$ explodes!
      - $-5$ continues left, meeting $10$: mass $5 < 10 \implies -5$ explodes!
      - Surviving asteroid: $[10]$.
- **Stack-Based LIFO Collision Invariant:**
  - **The Collision Surface:**
    - Any asteroid moving right enters the stack:
      $$
      x > 0 \implies stk.\text{append}(x)
      $$
    - An incoming left-moving asteroid ($x < 0$) can only collide with right-moving asteroids currently waiting on the top of the stack ($stk[-1] > 0$).
  - **Resolution Protocol for $x < 0$:**
    1. **Demolish Smaller Right-Movers:**
       - While the stack has right-moving asteroids smaller than the incoming asteroid ($stk[-1] > 0 \land stk[-1] < -x$):
         $$
         stk.\text{pop}() \quad (\text{Top asteroid obliterated})
         $$
    2. **Mutual Annihilation:**
       - If the top asteroid has the exact same size ($stk[-1] == -x$):
         $$
         stk.\text{pop}() \quad (\text{Both asteroids destroyed})
         $$
         - The incoming asteroid does not survive; collision loop terminates.
    3. **Incoming Annihilation:**
       - If the top asteroid is strictly larger ($stk[-1] > -x$):
         - The incoming asteroid explodes against the larger blocker; stack remains unchanged.
    4. **Survival & Penetration:**
       - If the stack becomes empty, or the top asteroid is also moving left ($stk[-1] < 0$):
         - The incoming left-mover has cleared all opposing obstacles.
         - Push it to the stack:
           $$
           stk.\text{append}(x)
           $$
- **Step-by-Step Worked Execution Trace on $asteroids = [10, 2, -5]$:**
  - Initialize empty stack: $stk = []$.
  - **Asteroid 0 ($x = 10$):**
    - $10 > 0 \implies$ Moving right.
    - No opposing bodies can exist ahead of it.
    - Push to stack:
      $$
      stk = [\mathbf{10}]
      $$
  - **Asteroid 1 ($x = 2$):**
    - $2 > 0 \implies$ Moving right.
    - Moves in the same direction as $10$ ($\to \quad \to$), never colliding.
    - Push to stack:
      $$
      stk = [10, \; \mathbf{2}]
      $$
  - **Asteroid 2 ($x = -5$):**
    - $-5 < 0 \implies$ Moving left.
    - Collision loop initiates against right-moving stack elements ($top > 0$):
      - **Encounter 1: Compare with top $stk[-1] = 2$:**
        - Incoming magnitude $|-5| = 5$.
        - Stack magnitude $|2| = 2$.
        - Compare: $5 > 2 \implies \mathbf{Asteroid\ 2\ Obliterated!}$
        - Pop top:
          $$
          stk.\text{pop}() \implies stk = [10]
          $$
        - Incoming $-5$ survives and continues its leftward trajectory.
      - **Encounter 2: Compare with next top $stk[-1] = 10$:**
        - Incoming magnitude: $5$.
        - Stack magnitude: $10$.
        - Compare: $5 < 10 \implies \mathbf{Incoming\ -5\ Obliterated!}$
        - Incoming asteroid explodes against the larger $10$.
        - Collision loop halts without modifying $stk$.
  - **Step 4: Output Remnants:**
    $$
    ans = stk = [\mathbf{10}]
    $$
- **Mutual Annihilation Trace ($asteroids = [8, -8]$):**
  - Push 8 $\implies stk = [8]$.
  - Incoming $-8$: top is 8, same size ($8 == 8$).
  - Both explode! $stk.\text{pop}() \implies stk = []$.
  - Output: `[]`.
- **Diverging Asteroids Trace ($asteroids = [-2, -1, 1, 2]$):**
  - Left-moving $-2, -1$ are pushed to stack (nothing to collide with).
  - Right-moving $1, 2$ are pushed to stack.
  - No opposite facing pairs meet.
  - Output: `[-2, -1, 1, 2]`.

This instance demonstrates physical particle kinetics simulation and monotonic stack priority queue reduction, mathematically proves why pairwise elimination preserves total invariant ordering across spatial projections, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array of asteroids:
Positive = moving right ($\to$). Negative = moving left ($\leftarrow$).
Value = size. Same speed.
Opposite-moving asteroids collide ($\to \leftarrow$):
- Smaller one explodes.
- Equal sizes: both explode.
- Same direction: never collide.

```text
asteroids = [ 10, 2, -5 ]

Step 1: 10 moves right -> stack: [ 10 ]
Step 2: 2 moves right  -> stack: [ 10, 2 ]
Step 3: -5 moves left:
  Meets 2: |-5| > 2 -> 2 explodes! -> stack: [ 10 ]
  Meets 10: |-5| < 10 -> -5 explodes! -> stack: [ 10 ]

Final surviving asteroids: [ 10 ]
```

### The Invariant of the Collision Stack
- A stack stores all asteroids that have survived so far.
- An incoming left-moving asteroid ($< 0$) collides with the top right-moving asteroid ($> 0$).
- Each asteroid is pushed at most once and popped at most once, guaranteeing linear $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Collision Trigger:
$$
\text{Collision occurs} \iff x < 0 \ \land \ |stk| > 0 \ \land \ stk.\text{top}() > 0
$$

### 2. Elimination Rules:
- If $stk.\text{top}() < -x \implies stk.\text{pop}()$ (repeat loop).
- If $stk.\text{top}() == -x \implies stk.\text{pop}()$ (halt loop, incoming destroyed).
- If $stk.\text{top}() > -x \implies$ halt loop (incoming destroyed).
- If $stk$ becomes empty or $stk.\text{top}() < 0 \implies stk.\text{append}(x)$.

> **Kinematic Elimination Invariant.** The collision dynamics on the 1D line define a confluence rewriting system $(\mathcal{A}, \to)$ where every sequence of valid local pairwise reductions yields the identical terminal irreducible configuration $stk$.

---

## 3. Step-by-Step Worked Execution

We trace $asteroids = [10, 2, -5]$:

---

### Step 1: Asteroid 10
- $10 > 0 \implies stk = [10]$.

---

### Step 2: Asteroid 2
- $2 > 0 \implies stk = [10, 2]$.

---

### Step 3: Asteroid -5
- Top is $2 > 0$. $|-5| = 5 > 2 \implies$ pop 2. $stk = [10]$.
- Top is $10 > 0$. $|-5| = 5 < 10 \implies$ -5 explodes.
- Stack remains $[10]$.

---

### Step 4: Output
$$
[\mathbf{10}]
$$

---

## 4. Complete Execution Trace

| Step | Asteroid $x$ | Direction | Current Stack $stk$ | Collision Encountered? | Outcome | New Stack State |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $10$ | Right | `[]` | No | Push $10$ | `[10]` |
| $2$ | $2$ | Right | `[10]` | No | Push $2$ | `[10, 2]` |
| $3\text{a}$ | $-5$ | Left | `[10, 2]` | Yes: vs $2$ | $5 > 2 \implies$ pop $2$ | `[10]` |
| $3\text{b}$ | $-5$ | Left | `[10]` | Yes: vs $10$ | $5 < 10 \implies$ $-5$ destroyed | `[10]` |
| **Final** | — | — | — | — | — | **`[10]`** |

---

## 5. Boundary Cases & Failure Modes

- **All Moving Same Direction ($[1, 2, 3]$ or $[-1, -2]$):** Zero collisions $\implies$ all survive.
- **Mutual Annihilation Cascade ($[5, 10, -10, -5]$):**
  - $10$ and $-10$ annihilate $\implies [5]$.
  - $5$ and $-5$ annihilate $\implies []$.
- **Left-Movers First ($[-5, 5]$):** $-5$ moves left away from $5$ moving right $\implies$ no collision! Returns `[-5, 5]`.
- **Large Chain Annihilation:** A large negative asteroid can demolish multiple preceding positive asteroids sequentially.

---

## 6. Traps & Common Anti-Patterns

- **Colliding Diverging Asteroids:** Asteroid moving left followed by asteroid moving right (e.g. `[-2, 2]`) move **away** from each other, not towards each other. They never collide. Only positive followed by negative collides.
- **Forgetting Mutual Annihilation ($top == -x$):** When sizes match, both must be destroyed. Do not push either to the stack.
- **Nested Loops without Amortization:** While loop runs inside for loop, but each element is popped at most once $\implies$ amortized strictly $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each of the $N$ asteroids is pushed onto the stack at most once.
  - Each asteroid is popped from the stack at most once.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 2$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space in the worst case to store surviving asteroids in the stack.
