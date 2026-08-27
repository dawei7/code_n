# Guided Example: Palindrome Number

We will determine whether an integer is a decimal palindrome using numeric half-reversal:

- **Input:** $x = 121$
- **Required output:** `true`

This instance is chosen because it demonstrates the odd-length digit mirror property, the extraction of low-order digits into a reversed accumulator, and the halving comparison that ignores the middle pivot without string conversion or risk of integer overflow.

---

## 1. Instance & Teaching Goal

An integer is a palindrome when its sequence of decimal digits reads identically forward and backward. 

Converting the integer to a string or digit array incurs auxiliary heap allocations. Reversing the entire integer arithmetically risks exceeding 32-bit integer limits on platforms with bounded integer widths.

The optimal method processes digits directly in base 10:
1. Immediately filter out negative integers (since the leading minus sign has no counterpart at the end) and non-zero numbers ending in zero (which would require an illegal leading zero).
2. Repeatedly extract the least significant digit of $x$ and append it to an accumulator $y$.
3. Stop when $y \ge x$, which signifies that half of the digits have been transferred.
4. Compare the remaining high-order prefix $x$ with the reversed low-order suffix $y$.

---

## 2. Conceptual Foundation & Invariants

We maintain two integer values: the shrinking high-order portion $x$, and the growing reversed low-order portion $y$, initially $y = 0$.

At each step, transferring the last digit is governed by:

$$
\text{digit} = x \pmod{10}, \qquad y \leftarrow y \times 10 + \text{digit}, \qquad x \leftarrow \left\lfloor \frac{x}{10} \right\rfloor
$$

| State Variable | Role & Definition | Initial Value ($x = 121$) |
|---|---|---|
| $x$ | Remaining unprocessed prefix digits | $121$ |
| $y$ | Accumulated reversed suffix digits | $0$ |

> **Invariant.** After $k$ iterations, $x = \lfloor x_0 / 10^k \rfloor$ and $y = \text{reverse}(x_0 \pmod{10^k})$. When $y \ge x$, exactly $\lceil D/2 \rceil$ digits of a $D$-digit number have been transferred to $y$.

---

## 3. Step-by-Step Worked Execution

### Initial State & Boundary Guards

- **Negative Check:** $x = 121 \ge 0$, valid.
- **Trailing Zero Check:** $x \neq 0$ and $x \pmod{10} = 1 \neq 0$, valid.
- **Initial Setup:** $x = 121$, $y = 0$. Since $y < x$ ($0 < 121$), the transfer loop begins.

---

### Step 1: Transfer the First Low-Order Digit

- **Extract Last Digit:** $121 \pmod{10} = 1$.
- **Update Reversed Half:** $y = 0 \times 10 + 1 = 1$.
- **Truncate Prefix:** $x = \lfloor 121 / 10 \rfloor = 12$.
- **Check Condition:** $y < x$ ($1 < 12$), so the loop continues.

| Parameter | Before Step | Operation | After Step |
|---|---|---|---|
| $x$ | $121$ | $\lfloor 121 / 10 \rfloor$ | $12$ |
| $y$ | $0$ | $0 \times 10 + 1$ | $1$ |
| Comparison | $0 < 121$ | Continue loop | $1 < 12$ (Continue) |

---

### Step 2: Transfer the Middle Pivot Digit

- **Extract Last Digit:** $12 \pmod{10} = 2$.
- **Update Reversed Half:** $y = 1 \times 10 + 2 = 12$.
- **Truncate Prefix:** $x = \lfloor 12 / 10 \rfloor = 1$.
- **Check Condition:** $y \ge x$ ($12 \ge 1$), halfway boundary reached. Terminate loop.

| Parameter | Before Step | Operation | After Step |
|---|---|---|---|
| $x$ | $12$ | $\lfloor 12 / 10 \rfloor$ | $1$ |
| $y$ | $1$ | $1 \times 10 + 2$ | $12$ |
| Comparison | $1 < 12$ | Check $y \ge x$ | $12 \ge 1$ (Terminate) |

---

### Step 3: Evaluate Equality at the Boundary

Since the original number had an odd number of digits ($D = 3$), the middle digit $2$ was absorbed into $y$ as the units place ($y = 12$).

We discard the middle digit from $y$ by taking $\lfloor y / 10 \rfloor = \lfloor 12 / 10 \rfloor = 1$.

Comparing the prefix with the reduced reversed suffix:

$$
x = \left\lfloor \frac{y}{10} \right\rfloor \iff 1 = 1 \implies \text{true}
$$

The number $121$ is confirmed to be a palindrome.

---

## 4. Complete Execution Trace

| Iteration | Extracted Digit | $x$ (Prefix) | $y$ (Reversed Suffix) | Condition $y < x$ | Action |
|---|---|---|---|---|---|
| $0$ (Init) | — | $121$ | $0$ | $0 < 121$ (True) | Enter loop |
| $1$ | $1$ | $12$ | $1$ | $1 < 12$ (True) | Continue |
| $2$ | $2$ | $1$ | $12$ | $12 < 1$ (False) | Exit loop |
| **Final Check** | — | $1$ | $12$ | $x = \lfloor y / 10 \rfloor \implies 1 = 1$ | **Return `true`** |

---

## 5. Algorithmic Correctness

**Soundness.** 
- For an even-length palindrome (e.g. $1221$), the loop halts when $x = 12$ and $y = 12$. The condition $x = y$ holds if and only if the high-order half matches the reversed low-order half.
- For an odd-length palindrome (e.g. $121$), the loop halts when $x = 1$ and $y = 12$. The middle digit occupies the units position of $y$. Discarding it via $\lfloor y / 10 \rfloor$ restores the exact counterpart to $x$. If $x = \lfloor y / 10 \rfloor$, all non-pivot mirror pairs are identical.

**Completeness.**
- Every step decreases $x$ by a factor of $10$ and increases $y$ by a factor of $10$. Because $x_0 > 0$, the strictly monotone sequence $y_k$ must intersect or exceed $x_k$ in exactly $\lceil D/2 \rceil$ steps. No valid palindrome can fail this symmetric equality test.

---

## 6. Traps This Instance Exposes

- **Negative Numbers:** $-121$ reversed becomes $121-$, which cannot match due to the unilateral negation sign.
- **Trailing Zeros:** Numbers like $10$ or $100$ would produce $y = 1$ and $x = 1$ on premature exit if not guarded, falsely reporting true. Pre-filtering $x > 0 \land x \pmod{10} = 0$ prevents this anomaly.
- **Integer Overflow:** Full reversal of a 32-bit integer like $2147483647$ exceeds $2^{31}-1$. Stopping at the midpoint guarantees $y \le \lceil \sqrt{x_0} \cdot 10 \rceil$, ensuring $y$ fits within standard numeric types.
- **Zero as a Palindrome:** The value $0$ is a valid single-digit palindrome and must not be trapped by the trailing-zero filter.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log_{10} N)$ where $N = x$. The loop executes $\lfloor \log_{10}(N) / 2 \rfloor + 1$ times, examining at most half the digits.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space as all operations are performed using two scalar integer variables.
