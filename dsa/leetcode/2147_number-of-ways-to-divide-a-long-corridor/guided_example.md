# Guided Example: Number of Ways to Divide a Long Corridor

We analyze and execute the seat-pairing combinatorial decomposition algorithm on a representative problem instance, demonstrating how strict section parity constraints reduce continuous partition choices to independent inter-pair gap product counting.

- **Input:** `corridor = "SSPPSPS"`
- **Output:** `3`

This instance illustrates parity gating, seat-index grouping into disjoint duos, isolating inter-duo plant gaps, and applying the multiplication principle modulo $10^9 + 7$.

---

## 1. Problem Overview & Representative Instance

A library corridor is represented as a string consisting of characters:
- `'S'`: A seat.
- `'P'`: A decorative plant.

Fixed walls enclose the corridor immediately before the first position and immediately after the last position. We may install additional dividers in the boundaries between adjacent characters. Every resulting partition must satisfy:
- Exactly two seats (`'S'`) per section.
- Any number of plants (`'P'`) per section (including zero).

We seek the number of valid distinct divider configurations modulo $10^9 + 7$. If no valid division is possible, the result is $0$.

In our representative instance:
- `corridor = "SSPPSPS"` of length $n = 7$.
- Seats appear at indices: $0, 1, 4, 6$.
- Total number of seats: $4$.

Since $4$ is an even positive integer, the corridor can be partitioned into $4 / 2 = 2$ valid sections. Exactly $1$ internal divider must be installed between the second seat and the third seat.

---

## 2. Mathematical & Algorithmic Principles

### Global Parity & Positivity Precondition

Let $N_S$ be the total count of seats in `corridor`. Because every valid section requires exactly $2$ seats:
$$N_S = 2k \quad \text{for some integer } k \ge 1$$

If $N_S = 0$ or $N_S$ is odd ($N_S \pmod 2 \ne 0$), no valid partitioning exists, and the answer is immediately $0$.

### Fixed Intra-Duo Boundaries & Flexible Inter-Duo Gaps

Let the sorted 0-indexed positions of all seats be:
$$s_0 < s_1 < s_2 < s_3 < \dots < s_{2k-2} < s_{2k-1}$$

Every valid division must group seats in fixed consecutive pairs:
- Section 1 must contain seats $s_0$ and $s_1$.
- Section 2 must contain seats $s_2$ and $s_3$.
- In general, Section $j$ must contain seats $s_{2j-2}$ and $s_{2j-1}$ for $j \in \{1, \dots, k\}$.

Within each pair $(s_{2j-2}, s_{2j-1})$, **no divider may ever be placed**, because doing so would split the pair and isolate a single seat.

Between adjacent pairs $(s_{2j-1}, s_{2j})$, **exactly one divider must be placed**:
- The divider must appear strictly after the second seat of the preceding section ($s_{2j-1}$).
- The divider must appear at or before the first seat of the following section ($s_{2j}$).
- The number of available boundary slots between index $s_{2j-1}$ and $s_{2j}$ is:
$$\text{Choices}_j = s_{2j} - s_{2j-1}$$

For example, if $s_1 = 1$ and $s_2 = 4$, dividers may be placed after index $1$, after index $2$, or after index $3$ ($4 - 1 = 3$ valid slots).

### The Multiplication Principle

Because the choice of divider position between Section $j$ and Section $j + 1$ has zero influence on the divider position between Section $j + 1$ and Section $j + 2$, all inter-pair gap choices are mutually independent.

By the Rule of Product:
$$\text{Total Divisions} = \prod_{j=1}^{k-1} (s_{2j} - s_{2j-1}) \pmod{10^9 + 7}$$

When $k = 1$ ($N_S = 2$), the corridor already consists of a single valid section requiring zero dividers. An empty product evaluates to $1$.

| Structural Element | Condition / Formula | Instance Role (`corridor = "SSPPSPS"`) |
|---|---|---|
| Total Seats $N_S$ | Count of `'S'` | $4$ (valid positive even number) |
| Sections Created $k$ | $N_S / 2$ | $2$ sections |
| Internal Dividers Needed | $k - 1$ | $1$ divider |
| Seat Positions | Array $s$ | $[0, 1, 4, 6]$ |
| Inter-Pair Gap Index Delta | $s_2 - s_1$ | $4 - 1 = 3$ choices |
| Global Answer | Product of deltas $\pmod{10^9 + 7}$ | $3$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `corridor = "SSPPSPS"` of length $7$.

```
Index:    0    1    2    3    4    5    6
Symbol:   S    S    P    P    S    P    S
Seat ID: s_0  s_1             s_2       s_3
Pairs:   [Section 1]  [Gap]   [Section 2]
```

### Step 1: Collect All Seat Indices
Scan the string and record every index containing `'S'`:
- Index $0$: `'S'` $\to s_0 = 0$.
- Index $1$: `'S'` $\to s_1 = 1$.
- Index $2$: `'P'`.
- Index $3$: `'P'`.
- Index $4$: `'S'` $\to s_2 = 4$.
- Index $5$: `'P'`.
- Index $6$: `'S'` $\to s_3 = 6$.

Total seats recorded: $s = [0, 1, 4, 6]$, length $N_S = 4$.

### Step 2: Validate Parity and Positivity
- Check $N_S > 0$: $4 > 0$ (True).
- Check $N_S \pmod 2 = 0$: $4 \pmod 2 = 0$ (True).
- Number of required sections: $k = 4 / 2 = 2$.
- Number of internal dividers required: $k - 1 = 1$.

### Step 3: Compute Inter-Pair Gap Combinations
- Initialize accumulator: $\text{ways} = 1$.
- For $j = 1$ to $k - 1 = 1$:
  - Left boundary seat: $s_{2j-1} = s_1 = 1$.
  - Right boundary seat: $s_{2j} = s_2 = 4$.
  - Available divider slots:
    $$\Delta = s_2 - s_1 = 4 - 1 = 3$$
  - Update product:
    $$\text{ways} = (1 \times 3) \pmod{10^9 + 7} = 3$$

### Step 4: Finalization
- All inter-pair boundaries processed.
- Final result: $3$.

---

## 4. Comprehensive State Trace

The table below catalogs each character, running seat count, and divider assignment actions:

| Index $i$ | Character | Seat Index Recorded | Active Pair Formed | Gap Action | Available Gap Options | Running Multiplier |
|---|---|---|---|---|---|---|
| $0$ | `'S'` | $s_0 = 0$ | Pair 1 (Seat 1) | None | - | $1$ |
| $1$ | `'S'` | $s_1 = 1$ | Pair 1 (Seat 2) | Pair 1 Closed | - | $1$ |
| $2$ | `'P'` | None | - | Plant in Gap 1 | Slot 1: after index 1 | $1$ |
| $3$ | `'P'` | None | - | Plant in Gap 1 | Slot 2: after index 2 | $1$ |
| $4$ | `'S'` | $s_2 = 4$ | Pair 2 (Seat 1) | Gap 1 Closed ($s_2 - s_1 = 3$) | Slot 3: after index 3 | $1 \times 3 = 3$ |
| $5$ | `'P'` | None | - | Plant in Pair 2 | Intra-pair (No divider) | $3$ |
| $6$ | `'S'` | $s_3 = 6$ | Pair 2 (Seat 2) | Pair 2 Closed | - | $3$ |

### Visual Layout of the Three Valid Configurations

1. **Option 1 (Divider after index 1):**
   ```
   [S  S]  |  [P  P  S  P  S]
   Section 1 has 2 seats (indices 0, 1). Section 2 has 2 seats (indices 4, 6).
   ```
2. **Option 2 (Divider after index 2):**
   ```
   [S  S  P]  |  [P  S  P  S]
   Section 1 has 2 seats (indices 0, 1). Section 2 has 2 seats (indices 4, 6).
   ```
3. **Option 3 (Divider after index 3):**
   ```
   [S  S  P  P]  |  [S  P  S]
   Section 1 has 2 seats (indices 0, 1). Section 2 has 2 seats (indices 4, 6).
   ```

All three configurations yield sections with exactly two seats.

---

## 5. Algorithmic Correctness & Soundness

### Section Uniqueness & Exhaustion
- Any divider placed between $s_{2j-2}$ and $s_{2j-1}$ leaves seat $s_{2j-2}$ isolated in a section with at most $1$ seat, violating the two-seat invariant. Thus, zero dividers can exist in $[s_{2j-2}, s_{2j-1}]$.
- Any division that fails to place a divider in $[s_{2j-1}, s_{2j}]$ forces seats $s_{2j-1}$ and $s_{2j}$ into the same section. Combined with $s_{2j-2}$ and $s_{2j+1}$, that section would contain at least $3$ seats, violating the two-seat invariant. Thus, at least one divider must exist.
- Placing more than one divider in $[s_{2j-1}, s_{2j}]$ creates a section between the two dividers containing only plants and zero seats, which violates the two-seat invariant.
- Therefore, **exactly one** divider must be placed in each interval $(s_{2j-1}, s_{2j}]$. The choices across different intervals are Cartesian-product independent, establishing total correctness of the product formula.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Odd Number of Seats ($N_S \pmod 2 \ne 0$):** For example, `corridor = "S"`. No valid pairing is possible. The algorithm detects odd parity and returns $0$.
2. **Zero Seats ($N_S = 0$):** `corridor = "PPPP"`. Since each section requires two seats, zero sections can be formed. The algorithm returns $0$.
3. **Exactly Two Seats ($N_S = 2$):** `corridor = "PPSPSP"`. Entire corridor forms $1$ section. Zero dividers needed. Loop $j \in [1, 0]$ does not run, returning initial value $1$.
4. **Adjacent Seats Across Gaps ($s_{2j} - s_{2j-1} = 1$):** When two seats are adjacent without any plants between pairs (e.g., `corridor = "SSSS"`), $s_2 - s_1 = 2 - 1 = 1$. Exactly $1$ slot exists between them; multiplying by $1$ leaves the total ways unchanged.

### Common Anti-Patterns
- **Dynamic Programming on Strings:** Trying to maintain state over each character index with top-down memoization or $O(n)$ array allocations wastes memory when a closed-form gap product can be accumulated in a single pass.
- **Counting Plants Globally:** Simply counting total plants does not determine divider choices; only plants located *between* consecutive pairs provide divider flexibility. Plants before the first seat, after the last seat, or inside a seat pair have zero effect on divider placement.
- **Neglecting Modulo During Multiplication:** With up to $50000$ seat pairs, repeated multiplication of gap lengths can exceed 64-bit integer limits without modular reduction.

---

## 7. Complexity Analysis

### Time Complexity
- A single linear scan through `corridor` of length $n$ identifies all seat indices in $O(n)$ time.
- Computing the product of $(k - 1)$ gap differences takes $O(k) \le O(n)$ scalar operations.
- Total time complexity is strictly $O(n)$, executing in under $5$ milliseconds for $n = 10^5$.

### Auxiliary Space Complexity
- One-pass streaming allows tracking the index of the previous second seat without even allocating an array for seat positions.
- Using an index array stores at most $n$ integers ($O(n)$ space), or $O(1)$ space when using three scalar tracking pointers.
- Total auxiliary space complexity is $O(1)$ auxiliary memory.
