# Counting Sundays - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $D(y, m) \in \{0, 1, \dots, 6\}$ denote the day-of-week residue modulo 7 for the 1st day of month $m \in \{1, \dots, 12\}$ in year $y \in \{1901, \dots, 2000\}$, indexed as $0 = \text{Monday}, 1 = \text{Tuesday}, \dots, 6 = \text{Sunday}$.

The objective is to compute the total number of Sundays falling on the 1st of the month during the entire 20th century ($1901$ to $2000$ inclusive):
$$N_{\text{Sundays}} = \sum_{y=1901}^{2000} \sum_{m=1}^{12} \mathbb{I}\left( D(y, m) \equiv 6 \pmod 7 \right)$$
where $\mathbb{I}(P) \in \{0, 1\}$ is the truth indicator function.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Day-by-Day Simulation
A naive algorithm simulates every single day from Jan 1, 1900 to Dec 31, 2000 (36,890 individual days):
```python
def naive_counting_sundays():
    # Advances day by 1 for 36,890 days
    # ...
```

### Computational Inefficiencies
1. **Redundant Daily Steps**: Stepping day-by-day performs nearly 37,000 loop operations.
2. **Superiority of Month Shifts**: Month lengths directly advance the 1st of the next month by $(M \bmod 7)$, checking only $100 \times 12 = 1200$ month-start transitions.

---

## 3. Core Intuition & Mathematical Structure

### Gregorian Leap Year Congruence
A year $y$ is a leap year iff:
$$\operatorname{is\_leap}(y) = (y \equiv 0 \pmod 4) \land (y \not\equiv 0 \pmod{100} \lor y \equiv 0 \pmod{400})$$
Thus, 1900 was a standard year ($365$ days), while 2000 was a leap year ($366$ days).

### Month Duration & Modulo 7 Shift Table

| Month | Days (Normal) | Shift $M \bmod 7$ | Days (Leap Year) | Shift $M \bmod 7$ |
| :--- | :---: | :---: | :---: | :---: |
| **January, March, May, July, August, October, December** | $31$ | $+3$ | $31$ | $+3$ |
| **April, June, September, November** | $30$ | $+2$ | $30$ | $+2$ |
| **February** | $28$ | $+0$ | $29$ | $+1$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Baseline Alignment from Jan 1, 1900
1. Given: 1 Jan 1900 was a Monday (day $0$).
2. Year 1900 had $365 = 52 \times 7 + 1$ days, advancing the weekday by $+1$.
3. Therefore, 1 Jan 1901 was a Tuesday (day $1$).
4. For each month $m$ in year $y \in [1901, 2000]$:
   - Check if $\text{day} \equiv 6 \pmod 7$.
   - Advance $\text{day} \leftarrow \text{day} + \text{days\_in\_month}$.
5. Total evaluated months $= 100 \times 12 = 1200$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Tracing Initial Months of 1901
- **1 Jan 1901**: Day $1$ (Tuesday). $1 \bmod 7 = 1 \neq 6$.
  - Add 31 days $\to 1 + 31 = 32 \equiv 4$ (Friday).
- **1 Feb 1901**: Day $4$ (Friday). $4 \bmod 7 = 4 \neq 6$.
  - 1901 is not leap: Add 28 days $\to 32 + 28 = 60 \equiv 4$ (Friday).
- **1 Mar 1901**: Day $4$ (Friday). $4 \bmod 7 = 4 \neq 6$.
  - Add 31 days $\to 60 + 31 = 91 \equiv 0$ (Monday).
- **1 Sep 1901**: First 1st-of-month Sunday of the century encountered.
- Continuing across all 1200 months yields:
  $$N_{\text{Sundays}} = \mathbf{171}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Setup** | Set `day = 1` (Jan 1, 1901), `sunday_count = 0` | $\mathcal{O}(1)$ |
| **Stage 2** | **Century Year Loop** | For $y \in [1901, 2000]$: compute `is_leap` | $100$ years |
| **Stage 3** | **Month Loop** | For $m \in [1, 12]$: check `day % 7 == 6` | $1200$ steps |
| **Stage 4** | **Modular Shift** | `day += 29 if (m == 2 and is_leap) else month_days[m]` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Value** | Return scalar integer $171$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(Y \cdot M)$ | $\approx 0.0001$ seconds for $1200$ months |
| **Space Complexity** | $\mathcal{O}(1)$ | In-place integer registers |
| **Dynamic Execution** | $100\%$ Inline | Pure modular arithmetic |

### Critical Invariants & Edge Cases Handled:
1. **End-of-Century Leap Rule**: Correctly treats year 1900 as common (365 days) and year 2000 as leap (366 days).
2. **Exact Range Boundaries**: Begins strictly on Jan 1, 1901 and terminates on Dec 31, 2000.
