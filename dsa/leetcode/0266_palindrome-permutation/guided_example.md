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

### Parity Table Across the Case Set

The verdict is a function of the parity multiset alone, so one table can record
every authored instance with the same three quantities: the frequencies, the
characters left with an odd count, and the budget test.

| Input $s$ | Length $N$ | Frequencies | Odd-frequency characters | Odd count | Verdict | Structural note |
|:---|:---:|:---|:---|:---:|:---:|:---|
| `"code"` | 4 | `c:1, d:1, e:1, o:1` | `c, d, e, o` | 4 | `false` | Every character is unpaired, so four characters compete for a single center |
| `"aab"` | 3 | `a:2, b:1` | `b` | 1 | `true` | Odd length with exactly one center candidate |
| `"carerac"` | 7 | `a:2, c:2, e:1, r:2` | `e` | 1 | `true` | The input already reads as a palindrome, but the verdict never depends on that |
| `"a"` | 1 | `a:1` | `a` | 1 | `true` | Minimum length: the one character is the entire palindrome |
| `"zz"` | 2 | `z:2` | none | 0 | `true` | Even length with the smallest possible all-even multiset |
| `"az"` | 2 | `a:1, z:1` | `a, z` | 2 | `false` | Shortest rejection: two singles cannot share one center |
| `"aabb"` | 4 | `a:2, b:2` | none | 0 | `true` | The input is not a palindrome, but the permutation `abba` is |
| `"aabbc"` | 5 | `a:2, b:2, c:1` | `c` | 1 | `true` | Two complete pairs plus exactly one center |
| All 26 letters twice | 52 | every letter twice | none | 0 | `true` | Maximum number of distinct characters, still zero odd counts |
| `"az"` repeated 2500 times | 5000 | `a:2500, z:2500` | none | 0 | `true` | Maximum length; both counts are even and far above $1$ |

The length column is not decoration. Summing the frequencies gives
$\sum_c f(c) = N$, and taking that identity modulo 2 shows that the parity of
$N$ always equals the parity of the odd-count total. An even-length input
therefore has $0, 2, 4, \dots$ odd characters and can never have exactly one, so
the test $\le 1$ means *exactly zero* for even $N$; for odd $N$ the odd-count
total is itself odd and hence at least one, so $\le 1$ means *exactly one*. The
single comparison covers both cases because these are the only possibilities.

### Bitmask Trace of a Valid Instance

The second implementation protocol replaces the counter with a single integer
whose set bits are exactly the characters seen an odd number of times. Tracing
$s = \text{"carerac"}$ shows the mask growing and shrinking as characters repeat,
with no count ever stored.

| Step | Character | Bit toggled | `mask` after the toggle | Low bits of `mask` | Characters currently odd |
|:---:|:---:|:---|:---:|:---|:---|
| 1 | `'c'` | bit 2 (value 4) | 4 | `00000000000000000000000100` | `c` |
| 2 | `'a'` | bit 0 (value 1) | 5 | `00000000000000000000000101` | `a, c` |
| 3 | `'r'` | bit 17 (value 131072) | 131077 | `00000000100000000000000101` | `a, c, r` |
| 4 | `'e'` | bit 4 (value 16) | 131093 | `00000000100000000000010101` | `a, c, e, r` |
| 5 | `'r'` | bit 17 again | 21 | `00000000000000000000010101` | `a, c, e` |
| 6 | `'a'` | bit 0 again | 20 | `00000000000000000000010100` | `c, e` |
| 7 | `'c'` | bit 2 again | 16 | `00000000000000000000010000` | `e` |

Step 5 is where the mask pays for itself: the second `'r'` cancels the bit that
step 3 set, so the mask falls from $131093$ back to $21$ without any subtraction
or lookup. The final value $16$ has one bit set, and
`mask & (mask - 1) = 16 & 15 = 0` confirms the budget in a single test — the
same conclusion the frequency table reaches by inspecting four separate counts.

---

## 5. Algorithmic Correctness

**Soundness.** In any palindrome, every character at index $i \ne N - 1 - i$ must have a corresponding partner at $N - 1 - i$. Thus, non-central characters must have even multiplicity. At most one index satisfies $i == N - 1 - i$ (the exact center of an odd-length string). If more than one character has an odd frequency, at least two characters would require placement in the center, which is structurally impossible.

**Completeness.** If the odd-count is $\le 1$, we can construct an explicit palindrome: place $\lfloor f(c) / 2 \rfloor$ copies of each character on the left, mirror them on the right, and place the single odd character (if any) in the center. The construction is always feasible, proving sufficiency.

---

## 6. Traps This Instance Exposes

- **Testing All Permutations ($N!$):** Generating all permutations and checking each with a two-pointer palindrome test takes $O(N! \cdot N)$ time. For $N = 10$, $10! \approx 3.6 \times 10^6$ operations. Counting frequencies solves it in $O(N)$ time.
- **Checking if the Original String is a Palindrome:** The question asks if a **permutation** can form a palindrome, not if the input itself is currently palindromic.
- **Bitmask Popcount Shortcut:** Toggling bits in a single 32-bit integer `mask` tracks parities in $O(1)$ auxiliary space without any hash table allocations. The expression `mask & (mask - 1) == 0` verifies that at most one bit is set in $O(1)$ CPU time.

### Alternatives and the Two Wrong Questions

Two of the rows below are correct algorithms that answer a different question from
the one asked, which is why they are listed with the verdicts they would return
on the authored cases.

| Strategy | Mechanism | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Frequency map plus odd-count sum | Count every character, then add up the parities | $O(N)$ | $O(\lvert \Sigma \rvert) = 26$ counters | The direct method; the alphabet pass is fixed at 26 steps regardless of $N$ |
| 26-bit mask toggle | XOR one bit per character, then test whether at most one bit remains set | $O(N)$ | $O(1)$: a single integer | Requires a bounded alphabet; 26 lowercase letters fit in 32 bits, a wider alphabet would not |
| Set of currently odd characters | Insert a character on its first occurrence and delete it on its second | $O(N)$ expected | $O(\lvert \Sigma \rvert)$ | Stores only the live odd set, but each update pays hashing instead of a bit operation |
| Sort and count runs | Sort the characters and measure each run of equal letters | $O(N \log N)$ | $O(N)$ for the reordered copy | An extra logarithmic factor for parity information that a single pass already exposes |
| Enumerate every permutation | Generate each rearrangement and verify it with two pointers | $O(N! \cdot N)$ | $O(N!)$ if the arrangements are materialised | Infeasible past tiny lengths: $10! \approx 3.6 \times 10^6$ arrangements before any palindrome test runs |
| Two-pointer test of the input itself | Check whether $s$ already reads the same in both directions | $O(N)$ | $O(1)$ | Right complexity, wrong question: it rejects `"aabb"`, which the problem accepts, and its answer depends on the input order rather than the multiset |

The chosen method is the frequency count, with the bitmask as its constant-space
twin. Both decide the question from the parity multiset alone, which is the only
property of $s$ that a rearrangement can change: character order and character
positions are irrelevant, and the two rejected rows differ from the correct ones
precisely because they consult order.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. We perform a single forward pass over $s$ to record character frequencies, followed by a pass over the alphabet entries ($\le 26$). Total time is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. The alphabet has a fixed size $|\Sigma| = 26$ for lowercase English letters (or a single 32-bit integer for the bitmask approach).
