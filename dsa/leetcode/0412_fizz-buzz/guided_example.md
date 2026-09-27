# Guided Example: Fizz Buzz

We trace the step-by-step modular arithmetic partitioning, priority-ordered branch evaluation, least common multiple intersection testing ($\text{lcm}(3, 5) = 15$), and sequential token generation on representative problem instances:

- **Input:** $n = 15$
- **Required output:** `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]`
  - Step-by-step partition verification:
    - Multiples of 15 ($i \in \{15\}$): mapped to `"FizzBuzz"`
    - Multiples of 3 only ($i \in \{3, 6, 9, 12\}$): mapped to `"Fizz"`
    - Multiples of 5 only ($i \in \{5, 10\}$): mapped to `"Buzz"`
    - Neither 3 nor 5 ($i \in \{1, 2, 4, 7, 8, 11, 13, 14\}$): converted to decimal string $str(i)$
- **Smallest Non-Trivial Instance ($n = 3$):** `["1", "2", "Fizz"]`
- **First Buzz Instance ($n = 5$):** `["1", "2", "Fizz", "4", "Buzz"]`

This instance demonstrates disjoint partition of natural numbers modulo coprime bases, explains why evaluating the composite condition $i \bmod 15 == 0$ first prevents branch starvation, and establishes $O(N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n = 15$:
Construct a 1-indexed list of strings representing every integer $i \in [1, 15]$ according to the divisibility rules:

```text
Integers 1 to 15:
  1  -> "1"
  2  -> "2"
  3  -> "Fizz"      (Divisible by 3)
  4  -> "4"
  5  -> "Buzz"      (Divisible by 5)
  6  -> "Fizz"      (Divisible by 3)
  7  -> "7"
  8  -> "8"
  9  -> "Fizz"      (Divisible by 3)
 10  -> "Buzz"      (Divisible by 5)
 11  -> "11"
 12  -> "Fizz"      (Divisible by 3)
 13  -> "13"
 14  -> "14"
 15  -> "FizzBuzz"  (Divisible by both 3 and 5 -> LCM 15)
```

### The Divisibility Venn Diagram
The set of integers divisible by 3 and the set of integers divisible by 5 are not disjoint:
- Multiples of 3: $\{3, 6, 9, 12, 15, 18, \dots\}$
- Multiples of 5: $\{5, 10, 15, 20, \dots\}$
- Intersection: $\{15, 30, 45, \dots\}$

Because 3 and 5 are coprime ($\gcd(3, 5) = 1$), an integer is divisible by both if and only if it is divisible by their product:
$$
\text{lcm}(3, 5) = 3 \times 5 = 15
$$
Any evaluation strategy must resolve this intersection before evaluating the independent sets.

---

## 2. Conceptual Foundation & Invariants

### 1. Priority-Ordered Decision Tree:
When using `if / elif / else` branching:
1. **Branch 1 (Most Specific):** If $i \bmod 15 == 0 \implies$ emit `"FizzBuzz"`.
2. **Branch 2:** Else if $i \bmod 3 == 0 \implies$ emit `"Fizz"`.
3. **Branch 3:** Else if $i \bmod 5 == 0 \implies$ emit `"Buzz"`.
4. **Branch 4 (Default):** Else $\implies$ emit $str(i)$.

```text
        [ i % 15 == 0 ? ]
           /         \
        YES           NO
        /               \
   "FizzBuzz"      [ i % 3 == 0 ? ]
                      /         \
                   YES           NO
                   /               \
                "Fizz"        [ i % 5 == 0 ? ]
                                 /         \
                              YES           NO
                              /               \
                           "Buzz"           str(i)
```

### 2. String Concatenation Alternative:
Alternatively, one can decouple the tests by string concatenation:
- Start with an empty string $S = \text{""}$.
- If $i \bmod 3 == 0$, append `"Fizz"`.
- If $i \bmod 5 == 0$, append `"Buzz"`.
- If $S$ remains empty, set $S = str(i)$.
This eliminates the composite check $i \bmod 15$ by allowing `"Fizz"` and `"Buzz"` to naturally concatenate into `"FizzBuzz"`.

> **Invariant.** At iteration $i$, exactly one output token is appended to the result sequence, corresponding to the unique partition class of $i \pmod{15}$.

---

## 3. Step-by-Step Worked Execution

We trace the execution for $n = 15$ across all indices $i \in [1, 15]$:

---

### Step 1 to 5: First Quintile
- **$i = 1$:** $1 \bmod 15 = 1, 1 \bmod 3 = 1, 1 \bmod 5 = 1 \implies$ Default $\implies$ `"1"`
- **$i = 2$:** $2 \bmod 15 = 2, 2 \bmod 3 = 2, 2 \bmod 5 = 2 \implies$ Default $\implies$ `"2"`
- **$i = 3$:** $3 \bmod 15 = 3, 3 \bmod 3 = 0 \implies$ Divisible by 3 $\implies$ `"Fizz"`
- **$i = 4$:** $4 \bmod 15 = 4, 4 \bmod 3 = 1, 4 \bmod 5 = 4 \implies$ Default $\implies$ `"4"`
- **$i = 5$:** $5 \bmod 15 = 5, 5 \bmod 3 = 2, 5 \bmod 5 = 0 \implies$ Divisible by 5 $\implies$ `"Buzz"`

---

### Step 6 to 10: Second Quintile
- **$i = 6$:** $6 \bmod 3 = 0 \implies$ Divisible by 3 $\implies$ `"Fizz"`
- **$i = 7$:** Neither $\implies$ Default $\implies$ `"7"`
- **$i = 8$:** Neither $\implies$ Default $\implies$ `"8"`
- **$i = 9$:** $9 \bmod 3 = 0 \implies$ Divisible by 3 $\implies$ `"Fizz"`
- **$i = 10$:** $10 \bmod 5 = 0 \implies$ Divisible by 5 $\implies$ `"Buzz"`

---

### Step 11 to 15: Third Quintile (Reaching the LCM)
- **$i = 11$:** Neither $\implies$ Default $\implies$ `"11"`
- **$i = 12$:** $12 \bmod 3 = 0 \implies$ Divisible by 3 $\implies$ `"Fizz"`
- **$i = 13$:** Neither $\implies$ Default $\implies$ `"13"`
- **$i = 14$:** Neither $\implies$ Default $\implies$ `"14"`
- **$i = 15$:**
  - Test $15 \bmod 15 == 0$: **True!**
  - Branch 1 triggers immediately.
  - Appends `"FizzBuzz"`.
  - Python bypasses branches for `% 3` and `% 5`.

---

## 4. Complete Execution Trace

| Number $i$ | $i \bmod 3$ | $i \bmod 5$ | $i \bmod 15$ | Active Branch Condition | Emitted Token | Cumulative Output Size |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| $1$ | $1$ | $1$ | $1$ | `else` | `"1"` | $1$ |
| $2$ | $2$ | $2$ | $2$ | `else` | `"2"` | $2$ |
| $3$ | **$0$** | $3$ | $3$ | `elif i % 3 == 0` | `"Fizz"` | $3$ |
| $4$ | $1$ | $4$ | $4$ | `else` | `"4"` | $4$ |
| $5$ | $2$ | **$0$** | $5$ | `elif i % 5 == 0` | `"Buzz"` | $5$ |
| $6$ | **$0$** | $1$ | $6$ | `elif i % 3 == 0` | `"Fizz"` | $6$ |
| $7$ | $1$ | $2$ | $7$ | `else` | `"7"` | $7$ |
| $8$ | $2$ | $3$ | $8$ | `else` | `"8"` | $8$ |
| $9$ | **$0$** | $4$ | $9$ | `elif i % 3 == 0` | `"Fizz"` | $9$ |
| $10$ | $1$ | **$0$** | $10$ | `elif i % 5 == 0` | `"Buzz"` | $10$ |
| $11$ | $2$ | $1$ | $11$ | `else` | `"11"` | $11$ |
| $12$ | **$0$** | $2$ | $12$ | `elif i % 3 == 0` | `"Fizz"` | $12$ |
| $13$ | $1$ | $3$ | $13$ | `else` | `"13"` | $13$ |
| $14$ | $2$ | $4$ | $14$ | `else` | `"14"` | $14$ |
| **$15$** | **$0$** | **$0$** | **$0$** | **`if i % 15 == 0`** | **`"FizzBuzz"`** | **$15$** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** Single element list `["1"]`. No divisibility conditions met.
- **$n = 3$:** `["1", "2", "Fizz"]`. First occurrence of 3-divisibility.
- **$n = 5$:** `["1", "2", "Fizz", "4", "Buzz"]`. First occurrence of 5-divisibility.
- **Large $n$ ($n = 10^4$):** Generates $10^4$ strings. Linear time complexity $O(N)$ ensures rapid execution in milliseconds.

---

## 6. Traps & Common Anti-Patterns

- **Branch Ordering Hazard:** Placing `if i % 3 == 0` before `if i % 15 == 0`. Since any multiple of 15 is divisible by 3, $i = 15$ enters the first branch and emits `"Fizz"` instead of `"FizzBuzz"`, starving the composite check.
- **Off-By-One Index Range:** Iterating over `range(n)` generates indices $0 \dots n-1$. Divisibility by zero ($0 \bmod 3 == 0$) erroneously produces `"FizzBuzz"` at index 0, and the sequence ends prematurely at $n-1$. The loop must strictly run over `range(1, n + 1)`.
- **Inefficient String Allocations:** In languages with immutable strings, repeatedly reallocating arrays instead of preallocating size $n$ adds garbage collection overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The loop executes exactly $N$ iterations.
  - In each iteration, at most two integer modulo operations and one comparison are performed in $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space beyond the output array of $N$ string references.
