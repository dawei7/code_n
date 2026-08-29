# Prize Strings - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A particular school offers cash awards to children with good attendance and punctuality.
If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an $n$-day period a trinary string is formed for each child consisting of:
- `L`s (late)
- `O`s (on time)
- `A`s (absent)

For an $n = 4$ day period, there are $81$ possible strings, and exactly $43$ of these strings are prize-winning:
$$N_{\text{prize}}(4) = 43$$

The objective is to find the **number of prize-winning attendance strings that exist over a 30-day period ($n = 30$)**:
$$N_{\text{prize}}(30) = \text{number of valid prize-winning strings}$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Exhaustive Trinary String Generation
A naive approach generates all $3^{30}$ strings:
```python
def naive_prize_strings():
    # 3^30 = 2.06 x 10^14 strings takes months to evaluate
    # ...
```

### 6-State Finite Automaton Dynamic Programming
1. **Minimal State Representation:**
   To determine if a new day character (`O`, `L`, `A`) can be appended, we only need:
   - Total `L` count so far: $l \in \{0, 1\}$.
   - Consecutive `A` count ending at the current day: $a \in \{0, 1, 2\}$.
   Total state space: $2 \times 3 = \mathbf{6}$ states!
2. **State Transitions for Character Appended:**
   - **Append `'O'`:** $(l, a) \to (l, 0)$ (resets consecutive absents to 0).
   - **Append `'L'`:** $(0, a) \to (1, 0)$ (only permitted if $l = 0$; forbidden if $l = 1$).
   - **Append `'A'`:** $(l, a) \to (l, a + 1)$ (only permitted if $a < 2$; forbidden if $a = 2$).
3. Advancing the 6 DP states over 30 days runs in $180$ operations in $\approx 0.0001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### The 6 Finite Automaton States and Transitions

| State $(l, a)$ | Meaning | On `'O'` | On `'L'` | On `'A'` |
| :---: | :---: | :---: | :---: | :---: |
| **$(0, 0)$** | 0 lates, 0 consecutive absents | $(0, 0)$ | $(1, 0)$ | $(0, 1)$ |
| **$(0, 1)$** | 0 lates, 1 consecutive absent | $(0, 0)$ | $(1, 0)$ | $(0, 2)$ |
| **$(0, 2)$** | 0 lates, 2 consecutive absents | $(0, 0)$ | $(1, 0)$ | **Invalid** (3 absents) |
| **$(1, 0)$** | 1 late, 0 consecutive absents | $(1, 0)$ | **Invalid** (2 lates) | $(1, 1)$ |
| **$(1, 1)$** | 1 late, 1 consecutive absent | $(1, 0)$ | **Invalid** (2 lates) | $(1, 2)$ |
| **$(1, 2)$** | 1 late, 2 consecutive absents | $(1, 0)$ | **Invalid** (2 lates) | **Invalid** (3 absents) |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master 6-State DP Pipeline
```python
def solve(days: int = 30) -> int:
    dp = [[0] * 3 for _ in range(2)]
    dp[0][0] = 1

    for day in range(days):
        next_dp = [[0] * 3 for _ in range(2)]
        for lates in range(2):
            for a in range(3):
                count = dp[lates][a]
                if count == 0:
                    continue
                next_dp[lates][0] += count
                if lates == 0:
                    next_dp[1][0] += count
                if a < 2:
                    next_dp[lates][a + 1] += count
        dp = next_dp

    return sum(dp[lates][a] for lates in range(2) for a in range(3))
```
Evaluating for $D = 30$:
$$N_{\text{prize}}(30) = \mathbf{1\,918\,080\,160}$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Verification for $D = 4$
- Day 0: $\text{dp}[0][0] = 1$.
- Day 1: $\text{dp}[0][0] = 1, \text{dp}[1][0] = 1, \text{dp}[0][1] = 1 \implies \text{sum} = 3$.
- Day 2: $\text{sum} = 8$.
- Day 3: $\text{sum} = 19$.
- Day 4: $\text{sum} = \mathbf{43}$.
- Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $D = 30$
- Summing all 6 states after 30 days:
  $$N_{\text{prize}}(30) = \mathbf{1\,918\,080\,160}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Base State** | `dp = [[0]*3 for _ in range(2)]; dp[0][0] = 1` | $6$ states |
| **Stage 2** | **Day Loop** | For $\text{day} \in [1, 30]$ | $30$ iterations |
| **Stage 3** | **Branch Transitions**| Transitions for `'O'`, `'L'`, `'A'` with guards | $18$ updates per day |
| **Stage 4** | **State Update** | `dp = next_dp` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Sum** | Return `sum(dp) = 1918080160` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(D)$ where $D = 30$ | $\approx 0.0001$ seconds ($180$ operations) |
| **Space Complexity** | $\mathcal{O}(1)$ | Fixed $2 \times 3$ matrix |
| **Dynamic Execution** | $100\%$ Inline | 6-state finite automaton dynamic programming |

### Critical Invariants & Edge Cases Handled:
1. **Lates Upper Bound**: Guard `if lates == 0:` strictly prevents strings with $\ge 2$ lates.
2. **Consecutive Absence Reset**: Appending `'O'` or `'L'` resets the consecutive absence counter $a$ to 0.
