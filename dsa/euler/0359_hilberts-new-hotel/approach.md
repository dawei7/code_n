# Hilbert's New Hotel - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In Hilbert's newest infinite hotel, there are infinitely many floors (numbered $f = 1, 2, 3, \dots$) each with infinitely many rooms (numbered $r = 1, 2, 3, \dots$).
Initially the hotel is empty. An infinite sequence of people (numbered $n = 1, 2, 3, \dots$) enter the hotel in order according to Hilbert's rule:
- Person $n$ is placed in the first vacant room of the lowest numbered floor $f$ such that either:
  1. The floor is currently empty ($r = 1$), or
  2. The room before it (occupied by person $m$) satisfies: $m + n = k^2$ for some integer $k \ge 1$ (a perfect square).

Let $P(f, r)$ denote the person who occupies room $r$ on floor $f$.
We are given sample values:
- $P(1, 1) = 1$, $P(1, 2) = 3$, $P(2, 1) = 2$
- $P(10, 20) = 440$, $P(25, 75) = 4863$, $P(99, 100) = 19454$

We seek to evaluate the last $8$ digits (modulo $10^8$) of:
$$\sum_{f \times r = 71328803586048} P(f, r) \pmod{10^8}$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Step-by-Step Person Placement Simulation
A naive approach simulates person arrivals $n = 1, 2, 3, \dots$, scanning floors $f = 1, 2, \dots$ to find the first valid room.
- **Scale of Operation**: The target product $N = 71328803586048 \approx 7.13 \times 10^{13}$.
  For $f = 1, r = N$, person $P(1, N) \approx \frac{N^2}{2} \approx 2.5 \times 10^{27}$.
  Simulating up to $10^{27}$ people requires $> 10^{18}$ CPU years.

---

## 3. Core Intuition & Mathematical Structure

### First Occupant $P(f, 1)$ Along Each Floor
Analyzing the starting occupant of each floor $f$:
- $f = 1$: $P(1, 1) = 1$
- $f = 2$: $P(2, 1) = 2$
- $f = 3$: $P(3, 1) = 4 = \frac{3^2 - 1}{2}$
- $f = 4$: $P(4, 1) = 8 = \frac{4^2}{2}$
- $f = 5$: $P(5, 1) = 12 = \frac{5^2 - 1}{2}$
- $f = 6$: $P(6, 1) = 18 = \frac{6^2}{2}$
In general:
$$P(f, 1) = \begin{cases} 1 & \text{if } f = 1 \\ \frac{f^2}{2} & \text{if } f \text{ is even} \\ \frac{f^2 - 1}{2} & \text{if } f \text{ is odd and } f > 1 \end{cases}$$

### Square Base Progression $B(f, r)$
For any floor $f$, consecutive room occupants satisfy:
$$P(f, r) + P(f, r-1) = (B(f, 2) + r - 2)^2$$
where the base square for room 2 is:
$$B(f, 2) = \begin{cases} 2 & \text{if } f = 1 \\ f + 1 & \text{if } f \text{ is even} \\ f & \text{if } f \text{ is odd and } f > 1 \end{cases}$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Closed-Form Quadratic Formula for $P(f, r)$
Let $m = r - 1$ denote the number of transitions along floor $f$.
Using the alternating sum of consecutive square differences $(x+1)^2 - x^2 = 2x + 1$, the sum telescopes into closed-form quadratic expressions:

1. **For $f = 1$**:
   $$P(1, r) = \frac{r(r + 1)}{2}$$

2. **For Even $f$**:
   - If $r = 2k + 1$ (odd room):
     $$P(f, 2k+1) = \frac{f^2}{2} + (2f + 1)k + 2k^2$$
   - If $r = 2k$ (even room):
     $$P(f, 2k) = 2k^2 + (2f - 1)k + \frac{f^2}{2}$$

3. **For Odd $f > 1$**:
   - If $r = 2k + 1$ (odd room):
     $$P(f, 2k+1) = \frac{f^2 - 1}{2} + (2f - 1)k + 2k^2$$
   - If $r = 2k$ (even room):
     $$P(f, 2k) = 2k^2 + (2f - 3)k + \frac{(f-1)^2}{2} - (f - 1)$$

### Divisor Enumeration
$N = 71328803586048 = 2^{27} \times 3^{12}$.
The number of divisors $d(N) = (27 + 1)(12 + 1) = 28 \times 13 = 364$.
For each divisor $f \mid N$, we compute $r = N / f$ and evaluate $P(f, r) \bmod 10^8$ in $O(1)$ time.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example Walkthrough for $P(10, 20)$
- $f = 10$ (even), $r = 20$ (even, $k = 10$).
- $P(10, 20) = 2(10)^2 + (2(10) - 1)(10) + \frac{10^2}{2} = 200 + 190 + 50 = 440$ ($\checkmark$).

### Example Walkthrough for $P(25, 75)$
- $f = 25$ (odd), $r = 75$ (odd, $k = 37$).
- $P(25, 75) = \frac{25^2 - 1}{2} + (2(25) - 1)(37) + 2(37)^2 = 312 + 49(37) + 2(1369) = 312 + 1813 + 2738 = 4863$ ($\checkmark$).

---

## 6. Implementation Architecture & Algorithmic Blueprint

```
[Prime Factorization: N = 2^27 * 3^12]
                  │
                  ▼
[Generate All 364 Divisors f | N]
   ├─► Compute r = N // f
   ├─► Evaluate P(f, r) mod 10^8 via O(1) quadratic formulas
   └─► Accumulate total = (total + P(f, r)) mod 10^8
                  │
                  ▼
[Return total mod 10^8: 40632119]
```

---

## 7. Mathematical Complexity & Edge Case Invariants

### Complexity Analysis
- **Divisor Generation**: $28 \times 13 = 364$ pairs generated in $< 0.0001$ seconds.
- **Evaluation**: $364 \times O(1)$ arithmetic operations take $< 0.001$ seconds in pure Python.
- **Space Complexity**: $O(1)$ auxiliary storage.

### Invariants Handled
- **Special Floor $f = 1$**: Handled by exact triangular polynomial $\frac{r(r+1)}{2}$.
- **Even/Odd Parity Matrix**: Covers all four combinations of $(f \bmod 2, r \bmod 2)$ with verified algebraic closure.
