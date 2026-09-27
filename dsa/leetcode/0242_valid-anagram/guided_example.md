# Guided Example: Valid Anagram

We trace the step-by-step length disparity rejection, character inventory tracking, and zero-sum frequency conservation on representative string anagram instances:

- **Input:** $s = \text{"anagram"}, \quad t = \text{"nagaram"}$
- **Required output:** `true` (Both strings contain identical multiset frequencies: 3 `'a'`, 1 `'n'`, 1 `'g'`, 1 `'r'`, 1 `'m'`)
- **Character Mismatch Instance:** $s = \text{"rat"}, \quad t = \text{"car"} \implies \text{false}$ (Character `'c'` not in inventory; count becomes $-1 < 0$)
- **Unequal Length Instance:** $s = \text{"a"}, \quad t = \text{"ab"} \implies \text{false}$ (Length $1 \ne 2$; rejected immediately)
- **Same Letter Set But Different Counts:** $s = \text{"aacc"}, \quad t = \text{"ccac"} \implies \text{false}$ (Count of `'a'` is 2 in $s$ vs 1 in $t$)

This instance demonstrates multiset character frequency conservation, mathematically proves why pre-verifying $\text{len}(s) == \text{len}(t)$ combined with an early negative-inventory check guarantees an exact match without a final array scan, details fixed-size 26-element array allocation for $O(|\Sigma|)$ space, and operates in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given two lowercase English strings:
$$
s = \text{"anagram"}, \quad t = \text{"nagaram"}
$$
Determine whether $t$ is an anagram of $s$ (meaning $t$ is formed by rearranging all original letters of $s$ exactly once).

- Sorting both strings and comparing equality takes $O(N \log N)$ time and $O(N)$ extra space.
- A hash map or fixed 26-element frequency vector provides a **character inventory**:
  - Positive counts represent characters available from $s$.
  - Consuming characters in $t$ decrements their inventory.
  - If any count ever becomes negative, $t$ has overused a letter (or used an absent letter), and the algorithm terminates immediately in $O(N)$ time with $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### The Length Equality Invariant
An anagram is a permutation. A permutation must preserve total length:
$$
\text{len}(s) == \text{len}(t)
$$
If $\text{len}(s) \ne \text{len}(t)$, return `false` immediately.
This initial guard is mathematically essential: if lengths were unequal, $t$ could be a proper substring of $s$ without any counter going negative (e.g. $s = \text{"abc"}, t = \text{"ab"}$). Enforcing equal length ensures total counts sum to zero.

### Single-Pass Inventory Protocol:
1. **Length Check:**
   If $\text{len}(s) \ne \text{len}(t)$, return `false`.
2. **Build Inventory:**
   Count character frequencies of $s$ in array `count` of size $26$:
   $$
   \text{for } c \in s: \quad \text{count}[\text{ord}(c) - \text{ord('a')}] \mathrel{+}= 1
   $$
3. **Consume Inventory:**
   For each character $c \in t$:
   $$
   \text{idx} = \text{ord}(c) - \text{ord('a')}
   $$
   $$
   \text{count}[\text{idx}] \mathrel{-}= 1
   $$
   If $\text{count}[\text{idx}] < 0$:
   Return `false`! (Target string $t$ has exhausted the available inventory for character $c$).
4. Return `true`.

> **Invariant.** Because $\sum \text{count} = 0$ at termination, if no individual bucket $\text{count}[c] < 0$, then every bucket $\text{count}[c] == 0$ must hold, proving exact multiset equality without a trailing verification pass.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $s = \text{"anagram"}$ and $t = \text{"nagaram"}$ ($N = 7$):

### Step 1: Length Validation
- $\text{len}(s) = 7, \quad \text{len}(t) = 7$.
- $7 == 7 \implies$ Pass.

---

### Step 2: Build Inventory from $s = \text{"anagram"}$
Record counts:
- `'a'` appears 3 times $\implies \text{count}[\text{'a'}] = 3$
- `'n'` appears 1 time $\implies \text{count}[\text{'n'}] = 1$
- `'g'` appears 1 time $\implies \text{count}[\text{'g'}] = 1$
- `'r'` appears 1 time $\implies \text{count}[\text{'r'}] = 1$
- `'m'` appears 1 time $\implies \text{count}[\text{'m'}] = 1$
All other 21 characters have count 0.

---

### Step 3: Consume Inventory with $t = \text{"nagaram"}$
- **Char 1 ($'n'$):**
  - $\text{count}[\text{'n'}] \leftarrow 1 - 1 = 0 \ge 0$ (Valid).
- **Char 2 ($'a'$):**
  - $\text{count}[\text{'a'}] \leftarrow 3 - 1 = 2 \ge 0$ (Valid).
- **Char 3 ($'g'$):**
  - $\text{count}[\text{'g'}] \leftarrow 1 - 1 = 0 \ge 0$ (Valid).
- **Char 4 ($'a'$):**
  - $\text{count}[\text{'a'}] \leftarrow 2 - 1 = 1 \ge 0$ (Valid).
- **Char 5 ($'r'$):**
  - $\text{count}[\text{'r'}] \leftarrow 1 - 1 = 0 \ge 0$ (Valid).
- **Char 6 ($'a'$):**
  - $\text{count}[\text{'a'}] \leftarrow 1 - 1 = 0 \ge 0$ (Valid).
- **Char 7 ($'m'$):**
  - $\text{count}[\text{'m'}] \leftarrow 1 - 1 = 0 \ge 0$ (Valid).

All 7 characters matched and consumed their exact allocations.
**Return `true`!**

---

## 4. Complete Execution Trace

```text
s = "anagram", t = "nagaram"
len(s) == len(t) == 7 -> Continue

Inventory from s: {a: 3, n: 1, g: 1, r: 1, m: 1}

Consuming t:
t[0] = 'n' -> count['n'] becomes 0 >= 0 (OK)
t[1] = 'a' -> count['a'] becomes 2 >= 0 (OK)
t[2] = 'g' -> count['g'] becomes 0 >= 0 (OK)
t[3] = 'a' -> count['a'] becomes 1 >= 0 (OK)
t[4] = 'r' -> count['r'] becomes 0 >= 0 (OK)
t[5] = 'a' -> count['a'] becomes 0 >= 0 (OK)
t[6] = 'm' -> count['m'] becomes 0 >= 0 (OK)

All counts valid -> Return True
```

| Step in $t$ | Character $c$ | Available Inventory Before | Inventory After Decrement | Negative Check ($< 0$)? | Running Verdict |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `'n'` | 1 | 0 | No | Valid |
| 2 | `'a'` | 3 | 2 | No | Valid |
| 3 | `'g'` | 1 | 0 | No | Valid |
| 4 | `'a'` | 2 | 1 | No | Valid |
| 5 | `'r'` | 1 | 0 | No | Valid |
| 6 | `'a'` | 1 | 0 | No | Valid |
| 7 | `'m'` | 1 | 0 | No | Valid |
| **Finish** | - | - | - | - | **`true`** |

### Contrast: Negative Inventory Early Exit ($s = \text{"rat"}, t = \text{"car"}$)
- Inventory from $s$: `{'r': 1, 'a': 1, 't': 1}` (All others 0).
- First character of $t$ is `'c'`:
  - $\text{count}[\text{'c'}] = 0$.
  - Decrement: $\text{count}[\text{'c'}] \leftarrow 0 - 1 = -1$.
  - Check: $-1 < 0 \implies$ **Immediate exit: `false`!**
  - Remaining characters are never scanned.

---

## 5. Algorithmic Correctness

**Soundness.** Let $\vec{u}$ and $\vec{v}$ be the character frequency vectors of $s$ and $t$ over alphabet $\Sigma$. Because $\sum_{c \in \Sigma} u_c = \text{len}(s) = \text{len}(t) = \sum_{c \in \Sigma} v_c$, we have $\sum_{c \in \Sigma} (u_c - v_c) = 0$. If $u_c - v_c \ge 0$ for all $c \in \Sigma$, then the only way a set of non-negative integers can sum to zero is if $u_c - v_c = 0$ for all $c$. Thus, $\vec{u} = \vec{v}$, which is the exact definition of an anagram.

**Completeness.** Every character in $s$ and $t$ is evaluated. If any discrepancy in frequency exists, at least one character in $t$ will exceed the count provided by $s$, triggering the negative check and returning `false`.

---

## 6. Traps This Instance Exposes

- **Missing Length Check:** If length checking is omitted, comparing $s = \text{"abc"}$ and $t = \text{"ab"}$ decrements `'a'` and `'b'` to zero without any counter going negative. It would falsely return `true` unless a trailing check is performed.
- **Sorting Overhead:** In Python, `sorted(s) == sorted(t)` takes $O(N \log N)$ time and allocates two new lists. Frequency counting takes $O(N)$ time with fixed $O(1)$ space.
- **Unicode Follow-up:** If input contains arbitrary Unicode code points (Chinese, emojis, accented characters), a fixed 26-element array is insufficient. A dynamic hash map (`collections.defaultdict(int)`) naturally scales to arbitrary Unicode alphabets in $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = \text{len}(s) = \text{len}(t)$. One forward pass populates the frequency counts, and one forward pass decrements counts. Each character access is an $O(1)$ direct array index lookup.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. The frequency table has fixed size $|\Sigma| = 26$ elements for lowercase English letters.
