# Guided Example: Lemonade Change

We trace the step-by-step cash drawer accounting, denomination versatility hierarchy ($5$ vs $10$), greedy change allocation on $20$ dollar bills, and solvency verification on representative customer payment queues:

- **Input:**
  $$
  bills = [5, 5, 5, 10, 20]
  $$
- **Required output:** `true`
  - Transaction rules:
    - Each lemonade costs exactly $\$5$.
    - Customers arrive in strict queue order and pay with either a $\$5$, $\$10$, or $\$20$ bill.
    - We begin with an empty cash drawer (zero bills of any denomination).
    - We must return exact change immediately to each customer:
      - Customer pays $\$5 \implies$ Change required: $\$0$.
      - Customer pays $\$10 \implies$ Change required: $\$5$. Must give one $\$5$ bill.
      - Customer pays $\$20 \implies$ Change required: $\$15$.
    - For $bills = [5, 5, 5, 10, 20]$:
      - Cust 1: pays $\$5$, change $\$0$. Drawer: $\{5: 1, 10: 0\}$.
      - Cust 2: pays $\$5$, change $\$0$. Drawer: $\{5: 2, 10: 0\}$.
      - Cust 3: pays $\$5$, change $\$0$. Drawer: $\{5: 3, 10: 0\}$.
      - Cust 4: pays $\$10$, change $\$5$. Give one $\$5$, receive $\$10$. Drawer: $\{5: 2, 10: 1\}$.
      - Cust 5: pays $\$20$, change $\$15$. Give one $\$10$ + one $\$5$. Drawer: $\{5: 1, 10: 0\}$.
      - All customers served successfully!
      - Result: **`true`**.
- **Denomination Versatility & Greedy Exchange Invariant:**
  - **The Versatility Hierarchy:**
    - A $\$5$ bill can provide change for **both** a $\$10$ bill and a $\$20$ bill.
    - A $\$10$ bill can **only** provide change for a $\$20$ bill.
    - Therefore, a $\$5$ bill is strictly more versatile than a $\$10$ bill.
  - **The Greedy Change Priority for $\$20$:**
    - To provide $\$15$ change, there are only two combinations:
      - **Option A:** One $\$10$ bill and one $\$5$ bill ($10 + 5 = 15$).
      - **Option B:** Three $\$5$ bills ($5 + 5 + 5 = 15$).
    - Because $\$5$ bills are strictly more valuable for future transactions, we must **always prefer Option A whenever a $\$10$ bill is available**, preserving $\$5$ bills for future $\$10$ customers!
    - We only resort to Option B if no $\$10$ bill is present in the drawer.

---

## 1. Instance & Teaching Goal

Given customer payments $bills = [5, 5, 5, 10, 20]$, track the register contents and verify why greedy choice guarantees feasibility.

```text
Cust 1: pays $5  -> Keep $5           (Drawer: 5s=1, 10s=0)
Cust 2: pays $5  -> Keep $5           (Drawer: 5s=2, 10s=0)
Cust 3: pays $5  -> Keep $5           (Drawer: 5s=3, 10s=0)
Cust 4: pays $10 -> Return $5, get $10 (Drawer: 5s=2, 10s=1)
Cust 5: pays $20 -> Return $10 + $5    (Drawer: 5s=1, 10s=0)

All change provided successfully -> true
```

We also contrast this with the failure case $[5, 5, 10, 10, 20]$ where having two $\$10$ bills fails to make $\$15$ change because two $\$10$ bills cannot be broken down.

---

## 2. Conceptual Foundation & Invariants

### 1. State Registers:
Let $five$ and $ten$ denote the counts of $\$5$ and $\$10$ bills currently held in the register.
Notice that $\$20$ bills are never used to give change, so tracking their count is unnecessary.

### 2. Transition Rules:
- **On $\$5$ bill:**
  $$
  five \leftarrow five + 1
  $$
- **On $\$10$ bill:**
  $$
  five \leftarrow five - 1, \quad ten \leftarrow ten + 1
  $$
- **On $\$20$ bill:**
  $$
  \begin{cases}
  ten \leftarrow ten - 1, \; five \leftarrow five - 1 & \text{if } ten > 0 \\
  five \leftarrow five - 3 & \text{if } ten = 0
  \end{cases}
  $$
- **Solvency Invariant:**
  At every step, we must maintain $five \ge 0$. If $five < 0$ at any moment, the transaction fails immediately.

---

## 3. Step-by-Step Worked Execution

We trace $bills = [5, 5, 5, 10, 20]$:

---

### Step 1: Customer 1 ($bill = 5$)
- Change needed: $\$0$.
- Drawer update: $five \leftarrow 0 + 1 = 1$.
- State: $five = 1, ten = 0$.

---

### Step 2: Customer 2 ($bill = 5$)
- Change needed: $\$0$.
- Drawer update: $five \leftarrow 1 + 1 = 2$.
- State: $five = 2, ten = 0$.

---

### Step 3: Customer 3 ($bill = 5$)
- Change needed: $\$0$.
- Drawer update: $five \leftarrow 2 + 1 = 3$.
- State: $five = 3, ten = 0$.

---

### Step 4: Customer 4 ($bill = 10$)
- Change needed: $\$5$.
- Return one $\$5$ bill: $five \leftarrow 3 - 1 = 2$.
- Receive one $\$10$ bill: $ten \leftarrow 0 + 1 = 1$.
- Check solvency: $five = 2 \ge 0$.
- State: $five = 2, ten = 1$.

---

### Step 5: Customer 5 ($bill = 20$)
- Change needed: $\$15$.
- Evaluate Greedy Priority:
  - $ten = 1 > 0 \implies$ We have a $\$10$ bill available!
  - Give one $\$10$ bill and one $\$5$ bill:
    $$
    ten \leftarrow 1 - 1 = 0, \quad five \leftarrow 2 - 1 = 1
    $$
- Check solvency: $five = 1 \ge 0$.
- State: $five = 1, ten = 0$.

---

### Termination:
All customers served.
- **Return: `true`**.

---

## 4. Complete Execution Trace & Counter-Example Contrast

### Successful Queue $[5, 5, 5, 10, 20]$:
| Customer | Payment | Change Required | Change Given | Register After ($five, ten$) | Solvency Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $\$5$ | $\$0$ | None | $(1, 0)$ | Solvent |
| $2$ | $\$5$ | $\$0$ | None | $(2, 0)$ | Solvent |
| $3$ | $\$5$ | $\$0$ | None | $(3, 0)$ | Solvent |
| $4$ | $\$10$ | $\$5$ | $1 \times \$5$ | $(2, 1)$ | Solvent |
| **$5$** | **$\$20$** | **$\$15$** | **$1 \times \$10 + 1 \times \$5$** | **$(1, 0)$** | **`Solvent -> true`** |

### Counter-Example Queue $[5, 5, 10, 10, 20]$:
| Customer | Payment | Change Required | Change Given | Register After ($five, ten$) | Solvency Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $\$5$ | $\$0$ | None | $(1, 0)$ | Solvent |
| $2$ | $\$5$ | $\$0$ | None | $(2, 0)$ | Solvent |
| $3$ | $\$10$ | $\$5$ | $1 \times \$5$ | $(1, 1)$ | Solvent |
| $4$ | $\$10$ | $\$5$ | $1 \times \$5$ | $(0, 2)$ | Solvent |
| **$5$** | **$\$20$** | **$\$15$** | Needs $10+5$ or $3 \times 5$ | Cannot make $\$15$ ($five = 0$) | **`Insolvent -> false`** |

---

## 5. Boundary Cases & Failure Modes

- **First Customer Pays $\$10$ or $\$20$:** Drawer is empty ($five = 0$), so giving $\$5$ change is impossible $\implies$ returns `false` immediately.
- **Queue of All $\$5$ Bills:** No change ever given; simply accumulates $\$5$ bills $\implies$ always returns `true`.
- **Exhaustion of $\$5$ Bills:** Having many $\$10$ bills is useless if a customer paying $\$10$ arrives, because $\$10$ cannot make change for another $\$10$.

---

## 6. Traps & Common Anti-Patterns

- **Using Three $\$5$ Bills for $\$20$ When a $\$10$ Bill is Available:** This squanders three precious $\$5$ bills, which could later be used to serve three $\$10$ customers.
- **Tracking $\$20$ Bills in Memory:** $\$20$ bills can never be handed out as change. Tracking them is dead computation.
- **Simulating with a Dynamic Array/Queue:** Storing individual bills in a list and searching/removing elements takes $\mathcal{O}(N^2)$ time. Two scalar counters reduce this to $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single pass through the array of $N$ bills: $\mathcal{O}(N)$.
  - Fixed number of arithmetic comparisons per bill: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(N)$, completing in $< 2$ ms for $N = 10^5$.
- **Auxiliary Space Complexity:**
  - Exactly two integer variables ($five, ten$): strictly $\mathcal{O}(1)$ space.
