# Guided Example: Find Substring With Given Hash Value

We analyze and execute the reverse rolling hash algorithm on a representative string instance, establishing why backward window sliding eliminates the need for modular multiplicative inverses under non-coprime moduli.

- **Input:** `s = "leetcode"`, `power = 7`, `modulo = 20`, `k = 2`, `hashValue = 0`
- **Output:** `"ee"`

This instance illustrates reverse polynomial sliding, avoiding modular division by multiplying by the base, tracking the tail power factor $p^k \pmod m$, and capturing the leftmost matching substring.

---

## 1. Problem Overview & Representative Instance

Given a lowercase string $s$ of length $n$, and parameters `power` ($p$), `modulo` ($m$), window length $k$, and target `hashValue`, the hash of any length-$k$ substring $t = s[i \dots i + k - 1]$ is defined by the polynomial:
$$\operatorname{hash}(t) = \left( \sum_{j=0}^{k-1} \operatorname{val}(t[j]) \cdot p^j \right) \bmod m$$
where character values map algebraically: $\operatorname{val}(\text{'a'}) = 1, \operatorname{val}(\text{'b'}) = 2, \dots, \operatorname{val}(\text{'z'}) = 26$.

We are guaranteed that at least one length-$k$ substring evaluates to `hashValue`. If multiple such substrings exist, we must return the **leftmost** (first occurrence).

In our representative instance:
- String: `s = "leetcode"` ($n = 8$).
- Target window size: $k = 2$.
- Base: $p = 7$.
- Modulus: $m = 20$.
- Target hash: $\text{hashValue} = 0$.

Notice that $\gcd(p, m) = \gcd(7, 20) = 1$ in this instance, but in general LeetCode constraints, $\gcd(p, m)$ may be strictly greater than $1$ (for instance, $p = 20, m = 100$). A forward rolling hash requires division by $p$, which is mathematically undefined when $\gcd(p, m) > 1$. Backward sliding completely circumvents this issue.

---

## 2. Mathematical & Algorithmic Principles

### The Forward Sliding Hazard: Modular Inverses

Consider sliding a window forward from $s[i \dots i+k-1]$ to $s[i+1 \dots i+k]$:
- In the hash definition, the exponent of each character corresponds to its relative position from the left of the window:
$$H_i = \operatorname{val}(s[i]) \cdot p^0 + \operatorname{val}(s[i+1]) \cdot p^1 + \dots + \operatorname{val}(s[i+k-1]) \cdot p^{k-1}$$
- If we advance forward to $H_{i+1}$:
$$H_{i+1} = \operatorname{val}(s[i+1]) \cdot p^0 + \operatorname{val}(s[i+2]) \cdot p^1 + \dots + \operatorname{val}(s[i+k]) \cdot p^{k-1}$$
- Expressing $H_{i+1}$ in terms of $H_i$:
$$H_{i+1} \equiv \frac{H_i - \operatorname{val}(s[i])}{p} + \operatorname{val}(s[i+k]) \cdot p^{k-1} \pmod m$$
This requires multiplying by $p^{-1} \pmod m$, which **does not exist** if $\gcd(p, m) \ne 1$.

### The Backward Sliding Remedy: Multiplication by $p$

Now consider sliding the window **backward** from $i + 1$ to $i$:
$$H_i = \operatorname{val}(s[i]) \cdot p^0 + p \cdot \Big(\operatorname{val}(s[i+1]) \cdot p^0 + \dots + \operatorname{val}(s[i+k-1]) \cdot p^{k-2}\Big)$$
Notice that the term in parentheses is $H_{i+1} - \operatorname{val}(s[i+k]) \cdot p^{k-1}$.
Multiplying by $p$ shifts every exponent up by $+1$:
$$H_i \equiv \Big( H_{i+1} \cdot p + \operatorname{val}(s[i]) - \operatorname{val}(s[i+k]) \cdot p^k \Big) \pmod m$$

Every operation in this recurrence is purely multiplication, addition, and subtraction. Zero divisions are performed, guaranteeing mathematical validity across all arbitrary values of $p$ and $m$.

### Leftmost Occurrence Collection via Reverse Iteration

By iterating $i$ from $n - k$ backward down to $0$:
- We initialize $H_{n-k}$ on the rightmost window $s[n-k \dots n-1]$.
- Whenever $H_i == \text{hashValue}$, we update:
$$\text{best\_start} = i$$
- Because $i$ decreases monotonically toward $0$, the final overwrite naturally stores the smallest (leftmost) valid starting index.

| Operation / Constant | Mathematical Formulation | Concrete Value in Instance |
|---|---|---|
| Base Multiplier $p$ | Given parameter `power` | $7$ |
| Modulus $m$ | Given parameter `modulo` | $20$ |
| Tail Exponent Factor | $p^k \pmod m$ | $7^2 = 49 \equiv 9 \pmod{20}$ |
| Backward Step Shift | $(H_{i+1} \cdot p + \operatorname{val}(s[i]) - \operatorname{val}(s[i+k]) \cdot p^k) \bmod m$ | Transition from window $i+1$ to window $i$ |
| Target Residue | Given `hashValue` | $0$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `s = "leetcode"`, $p = 7, m = 20, k = 2, \text{hashValue} = 0$.

```
String indices:  0   1   2   3   4   5   6   7
Characters:      l   e   e   t   c   o   d   e
Values:         12   5   5  20   3  15   4   5

Tail factor: p^k mod m = 7^2 mod 20 = 49 mod 20 = 9
Windows of length 2 evaluate from i = 6 down to i = 0.
```

### Step 1: Precompute Initial Suffix Window ($i = 6$)
The rightmost length-$2$ window is $s[6 \dots 7] = \text{"de"}$:
- $\operatorname{val}(s[6]) = \operatorname{val}(\text{'d'}) = 4$.
- $\operatorname{val}(s[7]) = \operatorname{val}(\text{'e'}) = 5$.
- Compute initial hash:
  $$H_6 = (4 \cdot 7^0 + 5 \cdot 7^1) \bmod 20 = (4 + 35) \bmod 20 = 39 \bmod 20 = 19$$
- Compare: $19 == 0$ is False.

### Step 2: Backward Step to $i = 5$ (Window $s[5 \dots 6] = \text{"od"}$)
- Outgoing character at right: $s[5 + 2] = s[7] = \text{'e'}$ (value $5$).
- Incoming character at left: $s[5] = \text{'o'}$ (value $15$).
- Compute transition:
  $$H_5 = (19 \times 7 + 15 - 5 \times 9) \bmod 20 = (133 + 15 - 45) \bmod 20 = 103 \bmod 20 = 3$$
- Compare: $3 == 0$ is False.

### Step 3: Backward Step to $i = 4$ (Window $s[4 \dots 5] = \text{"co"}$)
- Outgoing character: $s[4 + 2] = s[6] = \text{'d'}$ (value $4$).
- Incoming character: $s[4] = \text{'c'}$ (value $3$).
- Compute transition:
  $$H_4 = (3 \times 7 + 3 - 4 \times 9) \bmod 20 = (21 + 3 - 36) \bmod 20 = -12 \bmod 20 = 8$$
- Compare: $8 == 0$ is False.

### Step 4: Backward Step to $i = 3$ (Window $s[3 \dots 4] = \text{"tc"}$)
- Outgoing character: $s[3 + 2] = s[5] = \text{'o'}$ (value $15$).
- Incoming character: $s[3] = \text{'t'}$ (value $20$).
- Compute transition:
  $$H_3 = (8 \times 7 + 20 - 15 \times 9) \bmod 20 = (56 + 20 - 135) \bmod 20 = -59 \bmod 20 = 1$$
- Compare: $1 == 0$ is False.

### Step 5: Backward Step to $i = 2$ (Window $s[2 \dots 3] = \text{"et"}$)
- Outgoing character: $s[2 + 2] = s[4] = \text{'c'}$ (value $3$).
- Incoming character: $s[2] = \text{'e'}$ (value $5$).
- Compute transition:
  $$H_2 = (1 \times 7 + 5 - 3 \times 9) \bmod 20 = (7 + 5 - 27) \bmod 20 = -15 \bmod 20 = 5$$
- Compare: $5 == 0$ is False.

### Step 6: Backward Step to $i = 1$ (Window $s[1 \dots 2] = \text{"ee"}$)
- Outgoing character: $s[1 + 2] = s[3] = \text{'t'}$ (value $20$).
- Incoming character: $s[1] = \text{'e'}$ (value $5$).
- Compute transition:
  $$H_1 = (5 \times 7 + 5 - 20 \times 9) \bmod 20 = (35 + 5 - 180) \bmod 20 = -140 \bmod 20 = 0$$
- Compare: $0 == 0$ is **True!**
- Action: Match found! Record $\text{best\_start} = 1$.

### Step 7: Backward Step to $i = 0$ (Window $s[0 \dots 1] = \text{"le"}$)
- Outgoing character: $s[0 + 2] = s[2] = \text{'e'}$ (value $5$).
- Incoming character: $s[0] = \text{'l'}$ (value $12$).
- Compute transition:
  $$H_0 = (0 \times 7 + 12 - 5 \times 9) \bmod 20 = (12 - 45) \bmod 20 = -33 \bmod 20 = 7$$
- Compare: $7 == 0$ is False.

### Step 8: Emit Leftmost Match
- Loop finishes at index $0$.
- Lowest recorded index: $\text{best\_start} = 1$.
- Substring of length $k = 2$ starting at $1$: $s[1 \dots 2] = \text{"ee"}$.

---

## 4. Comprehensive State Trace

The table below catalogs every window evaluated during the backward sweep:

| Window Index $i$ | Substring $s[i \dots i+1]$ | Characters | Incoming / Outgoing | Raw Value Before Modulo | Computed $H_i \pmod{20}$ | Equals Target ($0$)? | Best Match Index |
|---|---|---|---|---|---|---|---|
| $6$ | `"de"` | `d`(4), `e`(5) | Initial Suffix | $4 + 5(7) = 39$ | $19$ | No | None |
| $5$ | `"od"` | `o`(15), `d`(4) | In: `o`(15), Out: `e`(5) | $19(7) + 15 - 5(9) = 103$ | $3$ | No | None |
| $4$ | `"co"` | `c`(3), `o`(15) | In: `c`(3), Out: `d`(4) | $3(7) + 3 - 4(9) = -12$ | $8$ | No | None |
| $3$ | `"tc"` | `t`(20), `c`(3) | In: `t`(20), Out: `o`(15) | $8(7) + 20 - 15(9) = -59$ | $1$ | No | None |
| $2$ | `"et"` | `e`(5), `t`(20) | In: `e`(5), Out: `c`(3) | $1(7) + 5 - 3(9) = -15$ | $5$ | No | None |
| $1$ | `"ee"` | `e`(5), `e`(5) | In: `e`(5), Out: `t`(20) | $5(7) + 5 - 20(9) = -140$ | **0** | **Yes** | $\mathbf{1}$ |
| $0$ | `"le"` | `l`(12), `e`(5) | In: `l`(12), Out: `e`(5) | $0(7) + 12 - 5(9) = -33$ | $7$ | No | $1$ |

Resulting substring: $s[1 \dots 2] = \text{"ee"}$.

---

## 5. Algorithmic Correctness & Soundness

### Algebraic Invariance of Backward Recurrence
Let $P(i) = \sum_{j=0}^{k-1} \operatorname{val}(s[i+j]) \cdot p^j$.
Multiplying $P(i+1)$ by $p$:
$$p \cdot P(i+1) = \sum_{j=0}^{k-1} \operatorname{val}(s[i+1+j]) \cdot p^{j+1} = \sum_{l=1}^k \operatorname{val}(s[i+l]) \cdot p^l$$
Adding $\operatorname{val}(s[i])$ and subtracting $\operatorname{val}(s[i+k]) \cdot p^k$:
$$\operatorname{val}(s[i]) + p \cdot P(i+1) - \operatorname{val}(s[i+k]) \cdot p^k = \operatorname{val}(s[i]) \cdot p^0 + \sum_{l=1}^{k-1} \operatorname{val}(s[i+l]) \cdot p^l = P(i)$$
Taking this identity modulo $m$ yields exact congruence for every integer ring $\mathbb{Z} / m\mathbb{Z}$. Zero division is required, proving universal algebraic correctness.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Window Equals Entire String ($k = n$):** Only one window exists ($i = 0$). Suffix initialization evaluates it directly in $O(k)$ time; no sliding steps occur.
2. **Window of Length 1 ($k = 1$):** Each character's hash is simply its own value modulo $m$. The backward transition simplifies to $H_i = \operatorname{val}(s[i]) \bmod m$.
3. **Negative Residues in Modulo Operations:** In languages like C++, Java, or JavaScript, the `%` operator retains negative signs (e.g., `-12 % 20 = -12`). We must normalize using `(val % m + m) % m` to ensure residues lie in $[0, m - 1]$.
4. **Non-Coprime Moduli ($\gcd(p, m) > 1$):** Forward sliding crashes or yields incorrect hashes due to undefined modular division. Backward sliding operates purely with valid ring homomorphisms.

### Common Anti-Patterns
- **Forward Sliding with Modular Inverse:** Assuming $p^{-1} \pmod m$ exists fails tests where $\gcd(p, m) > 1$.
- **Recomputing Hash from Scratch for Every Window ($O(n \cdot k)$):** Evaluating each substring independently costs $O(n \cdot k)$, which reaches $2 \cdot 10^4 \times 2 \cdot 10^4 = 4 \cdot 10^8$ operations, causing Time Limit Exceeded.
- **Overlooking Leftmost Tie-Breaker:** Halting at the first match discovered when sliding backwards captures the *rightmost* match instead of the leftmost. The backward loop must continue down to index $0$, updating $\text{best\_start}$ on every match.

---

## 7. Complexity Analysis

### Time Complexity
- **Tail Factor Precomputation:** Computing $p^k \bmod m$ takes $O(\log k)$ using binary exponentiation (or $O(k)$ with sequential multiplication).
- **Initial Suffix Window:** Computing $H_{n-k}$ takes $O(k)$ operations.
- **Backward Sliding Pass:** The loop runs $n - k$ times. Each iteration performs $O(1)$ arithmetic operations (multiplications and modular reductions).
- Total time complexity is strictly $O(n)$, processing strings of length $2 \cdot 10^4$ in under $2$ milliseconds.

### Auxiliary Space Complexity
- The algorithm tracks scalar integers ($H$, $p^k \bmod m$, `best_start`).
- No auxiliary strings or dynamic arrays are allocated during execution.
- Total auxiliary space complexity is $O(1)$.
