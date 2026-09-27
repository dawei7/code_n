# Guided Example: IP to CIDR

We trace the step-by-step dotted-decimal IPv4 to 32-bit integer conversion, least-significant-set-bit (LSB / lowbit) alignment calculation ($current \ \& \ -current$), power-of-two capacity partitioning ($\le remaining$), greedy CIDR block size selection ($\min(aligned, capacity)$), prefix length derivation ($32 - \log_2 block$), and range coverage on representative network blocks:

- **Input:** $ip = \text{"255.0.0.7"}, \quad n = 10$
- **Required output:**
  $$
  [\text{"255.0.0.7/32"}, \; \text{"255.0.0.8/29"}, \; \text{"255.0.0.16/32"}]
  $$
  - CIDR block specifications:
    - An IPv4 address is a 32-bit integer represented as four 8-bit octets: $A.B.C.D$.
    - A CIDR block format is $A.B.C.D/k$ where $k \in [0, 32]$ is the network prefix length.
    - A $/k$ block covers exactly:
      $$
      \text{Block Size} = 2^{32 - k} \quad \text{addresses}
      $$
    - **Alignment Rule:** A block of size $2^m$ ($k = 32 - m$) starting at address $X$ is valid if and only if $X$ is a multiple of $2^m$ (i.e. the lowest $m$ bits of $X$ are all zeros).
    - Objective: Cover exactly $n$ consecutive IP addresses starting from $ip$ using the **minimum number of CIDR blocks**.
    - For $ip = \text{"255.0.0.7"}$ and $n = 10$:
      - Addresses to cover: $255.0.0.7$ through $255.0.0.16$ (total 10 addresses).
      - Address $255.0.0.7$ has last octet $7$ (binary `...00111`), with lowest set bit at position 0 (size 1). Can only form a $/32$ block of size 1 $\implies 255.0.0.7/32$.
      - Next address $255.0.0.8$ (binary `...01000`) has lowest set bit 8 ($2^3$). With 9 remaining addresses, it can form a $/29$ block covering 8 addresses $\implies 255.0.0.8/29$ (covers $.8$ through $.15$).
      - Final address $255.0.0.16$ covers remaining 1 address $\implies 255.0.0.16/32$.
      - Resulting set of 3 blocks is minimal.
- **Lowbit Alignment & Capacity Bound Invariant:**
  - **The 32-Bit Representation:**
    - Parse $ip = A.B.C.D$:
      $$
      current = (A \ll 24) \mid (B \ll 16) \mid (C \ll 8) \mid D
      $$
  - **Constraint 1 (Alignment Bound):**
    - The starting address $current$ can only support a block of size up to its lowest set bit ($lowbit$):
      $$
      aligned\_size = current \ \& \ (-current)
      $$
      *(If $current == 0$, $aligned\_size = 2^{32}$)*.
  - **Constraint 2 (Capacity Bound):**
    - The block cannot cover more than the $remaining$ required addresses.
    - The largest power of 2 that does not exceed $remaining$ is:
      $$
      remaining\_size = 2^{\lfloor \log_2(remaining) \rfloor}
      $$
  - **Greedy Block Sizing:**
    - Taking the largest possible valid block at each step minimizes total blocks:
      $$
      block\_size = \min(aligned\_size, \; remaining\_size)
      $$
      $$
      \text{prefix } k = 32 - \log_2(block\_size)
      $$
    - Emit block $A.B.C.D/k$.
    - Advance: $current \leftarrow current + block\_size, \; remaining \leftarrow remaining - block\_size$.
- **Step-by-Step Worked Execution Trace on $ip = \text{"255.0.0.7"}, n = 10$:**
  - Convert IP to integer:
    $$
    current = (255 \ll 24) + 7 = 4{,}278{,}190{,}087
    $$
  - Remaining count: $remaining = 10$.
  - **Block 1 Selection:**
    - Calculate alignment limit from LSB of $current$:
      $$
      aligned\_size = current \ \& \ (-current) = 7 \ \& \ (-7) = \mathbf{1}
      $$
    - Calculate capacity limit for $remaining = 10$:
      $$
      remaining\_size = 2^{\lfloor \log_2 10 \rfloor} = 2^3 = \mathbf{8}
      $$
    - Optimal block size:
      $$
      block\_size = \min(1, \; 8) = \mathbf{1}
      $$
    - Derive CIDR prefix length:
      $$
      k = 32 - \log_2(1) = 32 - 0 = \mathbf{32}
      $$
    - Format block:
      $$
      \text{"255.0.0.7/32"}
      $$
    - Advance state:
      $$
      current \leftarrow current + 1 = \text{Address } 255.0.0.8
      $$
      $$
      remaining \leftarrow 10 - 1 = \mathbf{9}
      $$
  - **Block 2 Selection:**
    - Current address ends in $.8$ (binary `...01000`):
      $$
      aligned\_size = 8 \ \& \ (-8) = \mathbf{8}
      $$
    - Capacity limit for $remaining = 9$:
      $$
      remaining\_size = 2^{\lfloor \log_2 9 \rfloor} = 2^3 = \mathbf{8}
      $$
    - Optimal block size:
      $$
      block\_size = \min(8, \; 8) = \mathbf{8}
      $$
    - Derive CIDR prefix length:
      $$
      k = 32 - \log_2(8) = 32 - 3 = \mathbf{29}
      $$
    - Format block:
      $$
      \text{"255.0.0.8/29"}
      $$
    - Advance state:
      $$
      current \leftarrow current + 8 = \text{Address } 255.0.0.16
      $$
      $$
      remaining \leftarrow 9 - 8 = \mathbf{1}
      $$
  - **Block 3 Selection:**
    - Current address ends in $.16$ (binary `...10000`):
      $$
      aligned\_size = 16 \ \& \ (-16) = \mathbf{16}
      $$
    - Capacity limit for $remaining = 1$:
      $$
      remaining\_size = 2^{\lfloor \log_2 1 \rfloor} = 2^0 = \mathbf{1}
      $$
    - Optimal block size:
      $$
      block\_size = \min(16, \; 1) = \mathbf{1}
      $$
    - Derive CIDR prefix length:
      $$
      k = 32 - 0 = \mathbf{32}
      $$
    - Format block:
      $$
      \text{"255.0.0.16/32"}
      $$
    - Advance state:
      $$
      remaining \leftarrow 1 - 1 = \mathbf{0}
      $$
  - **Termination:**
    - $remaining = 0 \implies$ all addresses covered!
    - Final list of CIDR blocks:
      $$
      ans = [\text{"255.0.0.7/32"}, \; \text{"255.0.0.8/29"}, \; \text{"255.0.0.16/32"}]
      $$
- **Naturally Aligned Range Trace ($ip = \text{"0.0.0.0"}, n = 4$):**
  - $current = 0$ (aligned to $2^{32}$).
  - $remaining = 4 \implies block\_size = 4 \implies k = 30$.
  - Single block: `"0.0.0.0/30"`.

This instance demonstrates dyadic interval decomposition and binary lowbit alignment reduction, mathematically proves why greedy maximal power-of-two prefix allocation achieves the minimum partition cardinality, and derives $O(\log n)$ runtime and $O(\log n)$ output space bounds.

---

## 1. Instance & Teaching Goal

Given a start IP address and count $n$:
Convert the range of $n$ consecutive IP addresses into the **minimum number of CIDR blocks** ($A.B.C.D/k$).

```text
ip = "255.0.0.7", n = 10

Addresses: 255.0.0.7 to 255.0.0.16

Step 1: Start at .7 (unaligned, ends in ...1):
  Max block size allowed by alignment = 1 (k = 32)
  Covers .7 -> Block: "255.0.0.7/32", remaining = 9

Step 2: Start at .8 (aligned to 8, ends in ...1000):
  Max block size allowed = min(8, remaining 8) = 8 (k = 29)
  Covers .8 to .15 -> Block: "255.0.0.8/29", remaining = 1

Step 3: Start at .16 (aligned to 16):
  Max block size needed = 1 (k = 32)
  Covers .16 -> Block: "255.0.0.16/32", remaining = 0

Result: ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]
```

### The Invariant of the Lowbit and Capacity Minimum
- A CIDR block of size $2^m$ starting at $X$ requires $X \equiv 0 \pmod{2^m}$ (the lowest $m$ bits of $X$ must be zero).
- Hence, the maximum allowed block size is governed by $X \ \& \ (-X)$ (the lowest set bit of $X$).
- We also cannot exceed $remaining$. Thus, $block\_size = \min(X \ \& \ -X, \; 2^{\lfloor \log_2 remaining \rfloor})$.

---

## 2. Conceptual Foundation & Invariants

### 1. Lowbit and Capacity Bounds:
$$
aligned\_size = current \ \& \ (-current)
$$
$$
remaining\_size = 2^{\lfloor \log_2(remaining) \rfloor}
$$
$$
block\_size = \min(aligned\_size, \; remaining\_size)
$$

### 2. CIDR Prefix Length:
$$
k = 32 - \log_2(block\_size)
$$

> **Dyadic Interval Canonical Decomposition.** Any half-open integer range $[X, X + n)$ admits a unique minimal partition into canonical dyadic intervals of the form $[k \cdot 2^m, (k + 1) \cdot 2^m)$, constructed greedily by repeatedly taking the largest dyadic interval aligned with the current left endpoint.

---

## 3. Step-by-Step Worked Execution

We trace $ip = \text{"255.0.0.7"}, n = 10$:

---

### Step 1: Address .7
- $current \ \& \ -current = 1$. $block = 1$.
- Emits `"255.0.0.7/32"`.
- Next address: $.8$, $remaining = 9$.

---

### Step 2: Address .8
- $current \ \& \ -current = 8$. $remaining\_size = 8$.
- $block = \min(8, 8) = 8$.
- Emits `"255.0.0.8/29"`.
- Next address: $.16$, $remaining = 1$.

---

### Step 3: Address .16
- $current \ \& \ -current = 16$. $remaining\_size = 1$.
- $block = \min(16, 1) = 1$.
- Emits `"255.0.0.16/32"`.
- $remaining = 0$.

---

### Step 4: Output
$$
[\text{"255.0.0.7/32"}, \; \text{"255.0.0.8/29"}, \; \text{"255.0.0.16/32"}]
$$

---

## 4. Complete Execution Trace

| Step | Current IP Address | Lowbit $X \ \& \ -X$ | Remaining Capacity | Chosen Block Size | Prefix Length $k$ | Emitted Block | Remaining $n$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `255.0.0.7` | $1$ | $10 \implies 8$ | $1$ | $32$ | `"255.0.0.7/32"` | $9$ |
| $2$ | `255.0.0.8` | $8$ | $9 \implies 8$ | $8$ | $29$ | `"255.0.0.8/29"` | $1$ |
| **$3$** | **`255.0.0.16`**| **$16$** | **$1 \implies 1$** | **$1$** | **$32$** | **`"255.0.0.16/32"`**| **$0$** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** Single address $\implies$ always produces a single $/32$ block.
- **Power of Two Aligned Range ($ip = \text{"0.0.0.0"}, n = 256$):** Produces a single $/24$ block.
- **End of IPv4 Range:** Calculations operate strictly within standard 32-bit limits.
- **$current = 0$:** $0 \ \& \ -0 = 0$; handle edge case by setting $aligned\_size = 2^{32}$.

---

## 6. Traps & Common Anti-Patterns

- **Exceeding Remaining Count:** If $current$ is aligned to $256$, but $remaining = 5$, building a block of size 256 covers addresses beyond the requested range. Must take $\min(aligned, capacity)$.
- **Miscomputing Prefix Length:** Prefix length is $32 - \log_2(size)$, **not** $\log_2(size)$. Size 1 gives $/32$, size 2 gives $/31$, size 4 gives $/30$, etc.
- **String Parsing Overhead:** Do all alignment and addition logic directly on the 32-bit integer, and format back to dotted decimal string only when emitting each block.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In each step, the block size is at least the highest power of 2 that divides $current$ or fits in $remaining$.
  - The number of blocks generated is at most $2 \times \log_2(n) \le 30$.
  - Total Time: strictly logarithmic $\mathcal{O}(\log n)$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\log n)$ space for the returned list of CIDR block strings.
