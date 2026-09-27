# Guided Example: Reverse String

We trace the step-by-step two-pointer inward symmetric swapping ($s[i], s[j] = s[j], s[i]$), boundary convergence ($i < j$), in-place mutation, and array element inversion on representative character list instances:

- **Input:** $s = [\text{"h"}, \text{"e"}, \text{"l"}, \text{"l"}, \text{"o"}]$
- **Required output:** $[\text{"o"}, \text{"l"}, \text{"l"}, \text{"e"}, \text{"h"}]$
  - $i = 0, j = 4$: Swap `'h'` and `'o'` $\implies [\text{"o"}, \text{"e"}, \text{"l"}, \text{"l"}, \text{"h"}]$
  - $i = 1, j = 3$: Swap `'e'` and `'l'` $\implies [\text{"o"}, \text{"l"}, \text{"l"}, \text{"e"}, \text{"h"}]$
  - $i = 2, j = 2$: $i = j$, middle element `'l'` remains stationary
  - Final array: $[\text{"o"}, \text{"l"}, \text{"l"}, \text{"e"}, \text{"h"}]$
- **Even Length String:** $s = [\text{"H"}, \text{"a"}, \text{"n"}, \text{"n"}, \text{"a"}, \text{"h"}] \implies [\text{"h"}, \text{"a"}, \text{"n"}, \text{"n"}, \text{"a"}, \text{"H"}]$
- **Single Character Base Case:** $s = [\text{"A"}] \implies [\text{"A"}]$ ($i = 0, j = 0 \implies 0$ swaps)
- **Two Elements:** $s = [\text{"a"}, \text{"b"}] \implies [\text{"b"}, \text{"a"}]$

This instance demonstrates in-place two-pointer array manipulation, mathematically proves why $\lfloor N / 2 \rfloor$ pairwise swaps reverse any array without auxiliary memory buffers, and operates in $O(N)$ linear time and strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an array of characters:
$$
s = [\text{"h"}, \; \text{"e"}, \; \text{"l"}, \; \text{"l"}, \; \text{"o"}] \quad (N = 5)
$$
Reverse the order of characters **in-place** with $O(1)$ extra memory:

```text
Original:  ['h', 'e', 'l', 'l', 'o']
Indices:     0    1    2    3    4
Pointers:    i                   j

Swap 1:    ['o', 'e', 'l', 'l', 'h'] (swap index 0 and 4)
                  i         j

Swap 2:    ['o', 'l', 'l', 'e', 'h'] (swap index 1 and 3)
                       i=j

Stop:      ['o', 'l', 'l', 'e', 'h'] (i == j == 2)
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Symmetric Reflection Principle
In an array of length $N$, the character at index $p$ must move to index $N - 1 - p$.
Because reflection is an involution (symmetric mapping):
$$
(N - 1 - (N - 1 - p)) = p
$$
Swapping the values at indices $i$ and $j = N - 1 - i$ simultaneously places both characters into their correct final positions!

### 2. The Two-Pointer Invariant:
Initialize: $i = 0, \quad j = N - 1$.
While $i < j$:
1. Swap elements:
   $$
   s[i], \; s[j] = s[j], \; s[i]
   $$
2. Advance pointers inward:
   $$
   i \leftarrow i + 1, \quad j \leftarrow j - 1
   $$

> **Invariant.** At the start of each iteration, all elements at indices $< i$ and all elements at indices $> j$ are in their final reversed positions. The remaining unreversed subsegment is $s[i \dots j]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = [\text{"h"}, \text{"e"}, \text{"l"}, \text{"l"}, \text{"o"}]$ ($N = 5$):
Pointers: $i = 0, j = 4$.

---

### Step 1: Iteration 1 ($i = 0, j = 4$)
- Check condition: $i < j \iff 0 < 4$ (**True**).
- Elements to swap: $s[0] = \text{'h'}$ and $s[4] = \text{'o'}$.
- Perform swap:
  $$
  s[0], s[4] \leftarrow \text{'o'}, \text{'h'}
  $$
- Array state:
  $$
  [\mathbf{\text{"o"}}, \; \text{"e"}, \; \text{"l"}, \; \text{"l"}, \; \mathbf{\text{"h"}}]
  $$
- Advance pointers:
  $$
  i \leftarrow 0 + 1 = 1, \quad j \leftarrow 4 - 1 = 3
  $$

---

### Step 2: Iteration 2 ($i = 1, j = 3$)
- Check condition: $i < j \iff 1 < 3$ (**True**).
- Elements to swap: $s[1] = \text{'e'}$ and $s[3] = \text{'l'}$.
- Perform swap:
  $$
  s[1], s[3] \leftarrow \text{'l'}, \text{'e'}
  $$
- Array state:
  $$
  [\text{"o"}, \; \mathbf{\text{"l"}}, \; \text{"l"}, \; \mathbf{\text{"e"}}, \; \text{"h"}]
  $$
- Advance pointers:
  $$
  i \leftarrow 1 + 1 = 2, \quad j \leftarrow 3 - 1 = 2
  $$

---

### Step 3: Loop Termination ($i = 2, j = 2$)
- Check condition: $i < j \iff 2 < 2$ (**False**).
- Both pointers meet at middle element $s[2] = \text{'l'}$.
- A single middle element in an odd-length array remains in place.
- In-place reversal completed:
  $$
  \mathbf{[\text{"o"}, \text{"l"}, \text{"l"}, \text{"e"}, \text{"h"}]}
  $$

---

## 4. Complete Execution Trace

```text
s = ['h', 'e', 'l', 'l', 'o']
i = 0, j = 4

Iter 1: i=0, j=4 -> swap 'h' and 'o' -> ['o', 'e', 'l', 'l', 'h'], i=1, j=3
Iter 2: i=1, j=3 -> swap 'e' and 'l' -> ['o', 'l', 'l', 'e', 'h'], i=2, j=2
Iter 3: i=2, j=2 -> 2 < 2 is False   -> Terminate

Final Array: ['o', 'l', 'l', 'e', 'h']
```

| Iteration | Left Index $i$ | Right Index $j$ | Condition $i < j$ | Left Char $s[i]$ | Right Char $s[j]$ | Action Taken | Array State After Swap |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| Init | 0 | 4 | - | `'h'` | `'o'` | Setup | `['h', 'e', 'l', 'l', 'o']` |
| 1 | 0 | 4 | True ($0 < 4$) | `'h'` | `'o'` | Swap $s[0] \leftrightarrow s[4]$ | `['o', 'e', 'l', 'l', 'h']` |
| 2 | 1 | 3 | True ($1 < 3$) | `'e'` | `'l'` | Swap $s[1] \leftrightarrow s[3]$ | `['o', 'l', 'l', 'e', 'h']` |
| **Exit** | **2** | **2** | **False ($2 < 2$)** | `'l'` | `'l'` | **Terminate** | **`['o', 'l', 'l', 'e', 'h']`** |

---

## 5. Algorithmic Correctness

**Soundness.** Reversing an array requires mapping each index $k$ to $N - 1 - k$. The algorithm performs simultaneous assignments $s[i], s[j] = s[j], s[i]$ with $j = N - 1 - i$, ensuring that each swapped pair directly satisfies the reversal definition without overwriting unread elements.

**Completeness.** Pointers $i$ and $j$ advance inward by 1 at each step, halving the remaining distance. The loop terminates when $i \ge j$. Every element at an index $< \lfloor N/2 \rfloor$ is swapped with its symmetric counterpart, ensuring all elements are accurately inverted.

---

## 6. Traps This Instance Exposes

- **Allocating Slices:** Doing `s = s[::-1]` or creating a new list violates the in-place constraint. The problem requires mutating the input array $s$ directly with zero allocations.
- **Odd vs Even Parity:** When $N$ is odd, the pointers meet at the exact center ($i = j$). Using $i \le j$ would redundantly swap the center element with itself, whereas $i < j$ cleanly stops without unnecessary operations.
- **Python Tuple Unpacking Safety:** In Python, `s[i], s[j] = s[j], s[i]` evaluates the right-hand tuple before assigning to the left-hand targets, ensuring values are not overwritten before being read.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = \text{len}(s)$. The while loop executes exactly $\lfloor N / 2 \rfloor$ iterations, performing $O(1)$ operations per swap.
- **Auxiliary Space Complexity:** $O(1)$ strictly constant memory, using only two pointer integers ($i, j$).
