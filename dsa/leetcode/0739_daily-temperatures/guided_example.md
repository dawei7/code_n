# Guided Example: Daily Temperatures

We trace the step-by-step next-greater-element monotonic stack traversal, right-to-left reverse array indexing ($i = n - 1 \dots 0$), non-increasing temperature stack maintenance ($temperatures[stk[-1]] > temperatures[i]$), obsolete smaller candidate pruning ($pop()$), wait-day span calculation ($ans[i] \leftarrow stk[-1] - i$), and boundary zero padding on representative weather forecasts:

- **Input:**
  $$
  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
  $$
- **Required output:**
  $$
  [1, 1, 4, 2, 1, 1, 0, 0]
  $$
  - Daily wait criteria:
    - For each day $i$, find the number of days until the **next warmer temperature** ($temperatures[j] > temperatures[i]$ with $j > i$).
    - If no future day has a strictly higher temperature, record $0$.
    - For the input array:
      - Day 0 (73): Next warmer is Day 1 (74) $\implies$ wait $1 - 0 = 1$ day.
      - Day 1 (74): Next warmer is Day 2 (75) $\implies$ wait $2 - 1 = 1$ day.
      - Day 2 (75): Next warmer is Day 6 (76) $\implies$ wait $6 - 2 = 4$ days.
      - Day 3 (71): Next warmer is Day 5 (72) $\implies$ wait $5 - 3 = 2$ days.
      - Day 4 (69): Next warmer is Day 5 (72) $\implies$ wait $5 - 4 = 1$ day.
      - Day 5 (72): Next warmer is Day 6 (76) $\implies$ wait $6 - 5 = 1$ day.
      - Day 6 (76): No future day exceeds 76 $\implies 0$.
      - Day 7 (73): Last day, no future days $\implies 0$.
- **Monotonic Decreasing Stack Invariant:**
  - **The Next Greater Element Formulation:**
    - For day $i$, we seek the minimum index $j > i$ such that $temperatures[j] > temperatures[i]$.
  - **Right-to-Left Traversal Advantage:**
    - Scanning from right to left ($i = n - 1$ down to $0$) ensures all future days $\{i+1, \dots, n-1\}$ have already been processed and are candidates in the stack.
  - **The Dominated Element Elimination Property:**
    - If a future day $k > i$ has temperature $temperatures[k] \le temperatures[i]$:
      - Any earlier day $h < i$ that is warmer than $i$ is also warmer than $k$.
      - Furthermore, day $i$ is closer to $h$ than day $k$ is ($i < k$).
      - Therefore, day $k$ can **never** be the first warmer day for any day to the left of $i$!
      - Day $k$ is permanently obsolete and can be popped from the stack.
  - **Stack Operation Protocol:**
    1. **Prune Obsolete Days:**
       $$
       \text{while } stk \ne \emptyset \text{ and } temperatures[stk.\text{top}()] \le temperatures[i]: \quad stk.\text{pop}()
       $$
    2. **Read First Warmer Day:**
       - If stack is non-empty, the top of the stack is the immediate next warmer day:
         $$
         ans[i] \leftarrow stk.\text{top}() - i
         $$
       - If stack is empty, no warmer future day exists: $ans[i] \leftarrow 0$.
    3. **Register Current Day:**
       $$
       stk.\text{push}(i)
       $$
- **Step-by-Step Worked Execution Trace on $temperatures = [73, 74, 75, 71, 69, 72, 76, 73]$:**
  - Array length: $n = 8$. Initialize $ans = [0, 0, 0, 0, 0, 0, 0, 0], \; stk = []$.
  - **Day $i = 7$ ($temp = 73$):**
    - Stack empty.
    - $ans[7] = 0$.
    - Push index 7: $stk = [\mathbf{7}(73)]$.
  - **Day $i = 6$ ($temp = 76$):**
    - Top is $7(73) \le 76 \implies$ Pop 7!
    - Stack now empty.
    - $ans[6] = 0$.
    - Push index 6: $stk = [\mathbf{6}(76)]$.
  - **Day $i = 5$ ($temp = 72$):**
    - Top is $6(76) > 72 \implies$ Pruning halts.
    - Immediate warmer day is index 6:
      $$
      ans[5] \leftarrow 6 - 5 = \mathbf{1}
      $$
    - Push index 5: $stk = [6(76), \; \mathbf{5}(72)]$.
  - **Day $i = 4$ ($temp = 69$):**
    - Top is $5(72) > 69 \implies$ Pruning halts.
    - Warmer day is index 5:
      $$
      ans[4] \leftarrow 5 - 4 = \mathbf{1}
      $$
    - Push index 4: $stk = [6(76), \; 5(72), \; \mathbf{4}(69)]$.
  - **Day $i = 3$ ($temp = 71$):**
    - Top is $4(69) \le 71 \implies$ Pop 4!
    - Next top is $5(72) > 71 \implies$ Pruning halts.
    - Warmer day is index 5:
      $$
      ans[3] \leftarrow 5 - 3 = \mathbf{2}
      $$
    - Push index 3: $stk = [6(76), \; 5(72), \; \mathbf{3}(71)]$.
  - **Day $i = 2$ ($temp = 75$):**
    - Top is $3(71) \le 75 \implies$ Pop 3!
    - Next top is $5(72) \le 75 \implies$ Pop 5!
    - Next top is $6(76) > 75 \implies$ Pruning halts.
    - Warmer day is index 6:
      $$
      ans[2] \leftarrow 6 - 2 = \mathbf{4}
      $$
    - Push index 2: $stk = [6(76), \; \mathbf{2}(75)]$.
  - **Day $i = 1$ ($temp = 74$):**
    - Top is $2(75) > 74 \implies$ Pruning halts.
    - Warmer day is index 2:
      $$
      ans[1] \leftarrow 2 - 1 = \mathbf{1}
      $$
    - Push index 1: $stk = [6(76), \; 2(75), \; \mathbf{1}(74)]$.
  - **Day $i = 0$ ($temp = 73$):**
    - Top is $1(74) > 73 \implies$ Pruning halts.
    - Warmer day is index 1:
      $$
      ans[0] \leftarrow 1 - 0 = \mathbf{1}
      $$
    - Push index 0.
  - **Output Array Compiled:**
    $$
    ans = [\mathbf{1}, \; \mathbf{1}, \; \mathbf{4}, \; \mathbf{2}, \; \mathbf{1}, \; \mathbf{1}, \; \mathbf{0}, \; \mathbf{0}]
    $$
- **Strictly Increasing Sequence ($[30, 40, 50, 60]$):**
  - Each day finds the immediate next day as warmer.
  - Returns `[1, 1, 1, 0]`.
- **Strictly Decreasing Sequence ($[60, 50, 40, 30]$):**
  - No day ever sees a warmer temperature.
  - Returns `[0, 0, 0, 0]`.

This instance demonstrates monotonic stack next-greater-element identification and amortized constant-time interval search, mathematically proves why strictly dominated elements cannot serve as optimal future witnesses, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given daily temperatures:
For each day, return the number of days until a **strictly warmer temperature**.
If no future day is warmer, return 0.

```text
temperatures = [ 73, 74, 75, 71, 69, 72, 76, 73 ]

Day 0 (73): Day 1 (74) is warmer -> wait 1 - 0 = 1 day
Day 1 (74): Day 2 (75) is warmer -> wait 2 - 1 = 1 day
Day 2 (75): Day 6 (76) is warmer -> wait 6 - 2 = 4 days
Day 3 (71): Day 5 (72) is warmer -> wait 5 - 3 = 2 days
Day 4 (69): Day 5 (72) is warmer -> wait 5 - 4 = 1 day
Day 5 (72): Day 6 (76) is warmer -> wait 6 - 5 = 1 day
Day 6 (76): none warmer -> 0
Day 7 (73): none warmer -> 0

Result: [ 1, 1, 4, 2, 1, 1, 0, 0 ]
```

### The Invariant of the Monotonic Decreasing Stack
- Scanning from right to left maintains a stack of future day indices with strictly decreasing temperatures.
- Any future day colder or equal to today is popped because today's temperature is both closer and warmer to any days further left.

---

## 2. Conceptual Foundation & Invariants

### 1. Stack Invariant:
For indices in $stk = [i_1, i_2, \dots, i_k]$ from bottom to top:
$$
i_1 < i_2 < \dots < i_k \quad \text{and} \quad temperatures[i_1] > temperatures[i_2] > \dots > temperatures[i_k]
$$

### 2. Wait Day Calculation:
$$
\text{while } stk \ne \emptyset \land temperatures[stk.\text{top}()] \le temperatures[i]: \quad stk.\text{pop}()
$$
$$
ans[i] = \begin{cases} stk.\text{top}() - i & \text{if } stk \ne \emptyset \\ 0 & \text{otherwise} \end{cases}
$$

> **Right-Monotone Horizon Invariant.** The upper boundary envelope of the temperature trajectory $\max_{k \ge j} T[k]$ defines an upper lower-set whose extreme points are preserved in the monotonic stack, guaranteeing that the first element strictly dominating $T[i]$ is the stack top.

---

## 3. Step-by-Step Worked Execution

We trace $temperatures = [73, 74, 75, 71, 69, 72, 76, 73]$:

---

### Step 1: Days 7 and 6
- Day 7 (73): stack empty $\implies 0$, push 7.
- Day 6 (76): pop 7 (73) $\implies$ stack empty $\implies 0$, push 6.

---

### Step 2: Days 5 and 4
- Day 5 (72): top 6 (76) $> 72 \implies 6 - 5 = 1$, push 5.
- Day 4 (69): top 5 (72) $> 69 \implies 5 - 4 = 1$, push 4.

---

### Step 3: Day 3
- Day 3 (71): pop 4 (69) $\implies$ top 5 (72) $> 71 \implies 5 - 3 = 2$, push 3.

---

### Step 4: Day 2
- Day 2 (75): pop 3 (71), pop 5 (72) $\implies$ top 6 (76) $> 75 \implies 6 - 2 = 4$, push 2.

---

### Step 5: Days 1 and 0
- Day 1 (74): top 2 (75) $> 74 \implies 2 - 1 = 1$, push 1.
- Day 0 (73): top 1 (74) $> 73 \implies 1 - 0 = 1$, push 0.

---

### Step 6: Output
$$
[\mathbf{1}, \; \mathbf{1}, \; \mathbf{4}, \; \mathbf{2}, \; \mathbf{1}, \; \mathbf{1}, \; \mathbf{0}, \; \mathbf{0}]
$$

---

## 4. Complete Execution Trace

| Day $i$ | Temp $T[i]$ | Popped Elements | Stack Top Index | Warmer Temp | Wait Span $(j - i)$ | Result Array Slot |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $7$ | $73$ | None | None | None | $0$ | $ans[7] = 0$ |
| $6$ | $76$ | $7(73)$ | None | None | $0$ | $ans[6] = 0$ |
| $5$ | $72$ | None | $6$ | $76$ | $6 - 5 = 1$ | $ans[5] = 1$ |
| $4$ | $69$ | None | $5$ | $72$ | $5 - 4 = 1$ | $ans[4] = 1$ |
| $3$ | $71$ | $4(69)$ | $5$ | $72$ | $5 - 3 = 2$ | $ans[3] = 2$ |
| $2$ | $75$ | $3(71), 5(72)$ | $6$ | $76$ | $6 - 2 = 4$ | $ans[2] = 4$ |
| $1$ | $74$ | None | $2$ | $75$ | $2 - 1 = 1$ | $ans[1] = 1$ |
| **$0$** | **$73$** | **None** | **$1$** | **$74$** | **$1 - 0 = 1$** | **$ans[0] = 1$** |

---

## 5. Boundary Cases & Failure Modes

- **Strictly Decreasing ($[90, 80, 70]$):** All elements pop smaller predecessors $\implies$ output is all 0s.
- **Strictly Increasing ($[30, 40, 50]$):** Each day finds the immediate adjacent day $\implies [1, 1, 0]$.
- **All Identical Temperatures ($[70, 70, 70]$):** The next warmer day must be *strictly* warmer ($>$); equal temperatures pop $\implies [0, 0, 0]$.
- **Single Day ($[50]$):** Returns `[0]`.

---

## 6. Traps & Common Anti-Patterns

- **Brute Force Double Loop ($O(N^2)$):** For $N = 10^5$, scanning to the right for every element takes $10^{10}$ operations (TLE). A monotonic stack solves it in strictly linear $O(N)$ time.
- **Storing Temperature Values instead of Indices:** The stack must store the **indices** of the days, because the answer requires calculating the day distance $j - i$.
- **Non-Strict Comparison ($\ge$ instead of $>$):** The problem requires a *strictly* warmer day. Use $\le$ when popping (`temperatures[top] <= temperatures[i]`).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each index $i \in [0, N - 1]$ is pushed to the stack exactly once.
  - Each index is popped from the stack at most once.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 10$ ms for $N = 10^5$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space in the worst case for the monotonic stack and output array.
