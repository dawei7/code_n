# Guided Example: Palindrome Permutation

We trace the step-by-step character frequency parity invariant, center element budget allocation, and odd-count summation on representative string permutation instances:

- **Input:** $s = \text{"code"}$
- **Required output:** `false` (Four characters each with odd frequency 1; impossible to pair up)
- **Valid Odd-Length Instance:** $s = \text{"aab"} \implies \text{true}$ (Can be rearranged to $\text{"aba"}$; only `'b'` has odd frequency)
- **Multi-Pair Palindrome:** $s = \text{"carerac"} \implies \text{true}$ (`c:2, a:2, r:2, e:1`; can be arranged as $\text{"carerac"}$)
- **Single Character Instance:** $s = \text{"a"} \implies \text{true}$ (Trivially palindromic)
- **Even-Length Strict Symmetry:** $s = \text{"aabb"} \implies \text{true}$ (All counts even; 0 odd counts)

This instance demonstrates multiset parity invariants for palindromic symmetry, proves why a palindromic permutation exists if and only if at most one character has an odd frequency ($\sum (\text{freq}[c] \bmod 2) \le 1$), details frequency array and bitmask parity tracking, and operates in strictly $O(N)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"code"}$, determine whether any rearrangement of its characters can form a **palindrome**:
```text
Character counts in "code":
'c': 1
'o': 1
'd': 1
'e': 1
Total odd frequencies = 4 (Exceeds allowed budget of 1) -> Output: False
```

Contrast with $s = \text{"aab"}$:
$$
\text{'a'}: 2, \quad \text{'b'}: 1
$$
Only `'b'` has an odd count. We place `'b'` in the center and split the two `'a'`s symmetrically on both sides:
$$
\text{"a"} + \text{"b"} + \text{"a"} = \mathbf{\text{"aba"}} \quad (\text{Valid Palindrome!})
$$

### The Symmetrical Pairing Principle
In any palindrome:
- Every character away from the center must have an exact mirror image on the opposite side:
  $$
  s[i] == s[N - 1 - i]
  $$
- Therefore, characters must appear in pairs (even counts).
- At most **one single character** can occupy the center position without a mirror partner (if total length is odd).
A valid palindromic permutation exists **if and only if the number of characters with odd frequencies is at most 1**.

---

## 2. Conceptual Foundation & Invariants

### The Palindromic Parity Theorem
Let $\Sigma$ be the alphabet, and let $f(c)$ be the frequency of character $c$ in string $s$.
Define the parity bit:
$$
\text{parity}(c) = f(c) \pmod 2 \in \{0, 1\}
$$
A permutation of $s$ forms a palindrome **if and only if**:
$$
\sum_{c \in \Sigma} \text{parity}(c) \le 1
$$
- If length $|s|$ is even: $\sum \text{parity}(c) = 0$ (all counts must be even).
- If length $|s|$ is odd: $\sum \text{parity}(c) = 1$ (exactly one odd count).
Checking $\le 1$ automatically handles both even and odd length strings simultaneously without branching!

### Implementation Protocols:
1. **Method 1 (Frequency Array / Hash Map):**
   Count occurrences of each character, sum $f(c) \pmod 2$, and check if the sum is $\le 1$.
2. **Method 2 (Bitmask Toggle):**
   Maintain a 32-bit integer `mask = 0`.
   For each character $c \in s$:
   $$
   \text{mask} \mathrel{\text{\^{}}}= (1 \ll (\text{ord}(c) - \text{ord('a')}))
   $$
   At the end, check if `mask` has at most one bit set:
   $$
   (\text{mask} \ \& \ (\text{mask} - 1)) == 0
   $$

> **Invariant.** Characters with even frequencies contribute zero net parity. Only characters with odd frequencies contribute $1$ to the center budget.

---

## 3. Step-by-Step Worked Execution

We trace the frequency counting on $s = \text{"code"}$ ($N = 4$):

### Step 1: Initialize Frequency Counter
Empty frequency map:
$$
\text{freq} = \{\}
$$

---

### Step 2: Accumulate Character Counts
- Char 1: `'c'` $\implies \text{freq}[\text{'c'}] = 1$.
- Char 2: `'o'` $\implies \text{freq}[\text{'o'}] = 1$.
- Char 3: `'d'` $\implies \text{freq}[\text{'d'}] = 1$.
- Char 4: `'e'` $\implies \text{freq}[\text{'e'}] = 1$.

Resulting frequencies:
$$
\{\text{'c'}: 1, \; \text{'o'}: 1, \; \text{'d'}: 1, \; \text{'e'}: 1\}
$$

---

### Step 3: Compute Parity Sum
Evaluate $f(c) \pmod 2$ for each character:
- $\text{parity}(\text{'c'}) = 1 \pmod 2 = 1$
- $\text{parity}(\text{'o'}) = 1 \pmod 2 = 1$
- $\text{parity}(\text{'d'}) = 1 \pmod 2 = 1$
- $\text{parity}(\text{'e'}) = 1 \pmod 2 = 1$

Sum of odd counts:
$$
\text{odd\_count} = 1 + 1 + 1 + 1 = \mathbf{4}
$$

---

### Step 4: Validate Invariant
Compare with budget:
$$
\text{odd\_count} \le 1 \iff 4 \le 1 \quad (\mathbf{\text{False}})
$$
**Return `false`!**

---

## 4. Complete Execution Trace

```text
s = "code"

Frequencies: {'c': 1, 'o': 1, 'd': 1, 'e': 1}
Parities:
  'c': 1 % 2 = 1 (Odd)
  'o': 1 % 2 = 1 (Odd)
  'd': 1 % 2 = 1 (Odd)
  'e': 1 % 2 = 1 (Odd)

Total Odd Counts = 4 > 1 -> Return False
```

| Character $c$ | Frequency $f(c)$ | Parity ($f(c) \pmod 2$) | Cumulative Odd Frequencies | Invariant Status ($\le 1$) |
|:---:|:---:|:---:|:---:|:---:|
| `'c'` | 1 | 1 | 1 | Valid so far |
| `'o'` | 1 | 1 | 2 | Violated ($> 1$) |
| `'d'` | 1 | 1 | 3 | Violated |
| `'e'` | 1 | 1 | **4** | **Violated ($4 > 1$)** |
| **Output** | - | - | - | **`false`** |

### Contrast: Valid Palindromic Permutation ($s = \text{"carerac"}$)
- Frequencies: `{'c': 2, 'a': 2, 'r': 2, 'e': 1}`.
- Parities:
  - $\text{'c'}: 2 \pmod 2 = 0$
  - $\text{'a'}: 2 \pmod 2 = 0$
  - $\text{'r'}: 2 \pmod 2 = 0$
  - $\text{'e'}: 1 \pmod 2 = 1$
- Odd count $= 0 + 0 + 0 + 1 = \mathbf{1} \le 1$.
- **Returns `true`!** (Forms palindrome `"carerac"`).

---

## 5. Algorithmic Correctness

**Soundness.** In any palindrome, every character at index $i \ne N - 1 - i$ must have a corresponding partner at $N - 1 - i$. Thus, non-central characters must have even multiplicity. At most one index satisfies $i == N - 1 - i$ (the exact center of an odd-length string). If more than one character has an odd frequency, at least two characters would require placement in the center, which is structurally impossible.

**Completeness.** If the odd-count is $\le 1$, we can construct an explicit palindrome: place $\lfloor f(c) / 2 \rfloor$ copies of each character on the left, mirror them on the right, and place the single odd character (if any) in the center. The construction is always feasible, proving sufficiency.

---

## 6. Traps This Instance Exposes

- **Testing All Permutations ($N!$):** Generating all permutations and checking each with a two-pointer palindrome test takes $O(N! \cdot N)$ time. For $N = 10$, $10! \approx 3.6 \times 10^6$ operations. Counting frequencies solves it in $O(N)$ time.
- **Checking if the Original String is a Palindrome:** The question asks if a **permutation** can form a palindrome, not if the input itself is currently palindromic.
- **Bitmask Popcount Shortcut:** Toggling bits in a single 32-bit integer `mask` tracks parities in $O(1)$ auxiliary space without any hash table allocations. The expression `mask & (mask - 1) == 0` verifies that at most one bit is set in $O(1)$ CPU time.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. We perform a single forward pass over $s$ to record character frequencies, followed by a pass over the alphabet entries ($\le 26$). Total time is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. The alphabet has a fixed size $|\Sigma| = 26$ for lowercase English letters (or a single 32-bit integer for the bitmask approach).
