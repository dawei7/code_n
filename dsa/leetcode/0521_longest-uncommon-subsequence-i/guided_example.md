# Guided Example: Longest Uncommon Subsequence I

We trace the step-by-step definition of uncommon subsequences, string equality identity testing ($a == b \implies -1$), length asymmetry dominance ($|a| \ne |b| \implies \max(|a|, |b|)$), and whole-string self-subsequence maximality on representative string pairs:

- **Input:** $a = \text{"aba"}, \quad b = \text{"cdc"}$
- **Required output:** `3`
  - Formal definition: An **uncommon subsequence** between two strings $a$ and $b$ is a string that is a subsequence of one string but **not** a subsequence of the other.
  - Length of $a$: $|a| = 3$. Length of $b$: $|b| = 3$.
- **Mathematical proof and decision trace:**
  - **Step 1: Test String Identity ($a == b$):**
    - $a = \text{"aba"}$ and $b = \text{"cdc"}$.
    - $a \ne b$ (they are distinct strings).
  - **Step 2: Evaluate the Self-Subsequence Property:**
    - Any string $s$ is always a subsequence of itself, with maximal length $|s|$.
    - Consider string $a = \text{"aba"}$ itself:
      - Is `"aba"` a subsequence of $a$? **Yes** (trivial).
      - Is `"aba"` a subsequence of $b = \text{"cdc"}$?
        - Both strings have length 3.
        - The only subsequence of length 3 of $b$ is $b$ itself (`"cdc"`).
        - Since `"aba" \ne \text{"cdc"}$, `"aba"` **cannot** be a subsequence of $b$!
    - Therefore, $a$ is an uncommon subsequence of $b$ with length $3$.
  - **Step 3: Evaluate Maximality:**
    - No subsequence of either $a$ or $b$ can have length greater than $\max(|a|, |b|) = 3$.
    - Since length $3$ is achieved by $a$ itself, the longest uncommon subsequence length is:
      $$
      \max(|a|, |b|) = \max(3, 3) = \mathbf{3}
      $$
- **Unequal Length Instance ($a = \text{"a"}, b = \text{"aaa"}$):**
  - $|a| = 1, |b| = 3$.
  - String $b = \text{"aaa"}$ has length 3.
  - A subsequence of $a$ can have length at most $|a| = 1$.
  - Therefore, `"aaa"` can never be a subsequence of `"a"`.
  - Length: $\max(1, 3) = \mathbf{3}$.
- **Identical Strings Instance ($a = \text{"abc"}, b = \text{"abc"}$):**
  - $a == b$.
  - Every subsequence of $a$ is also a subsequence of $b$, and vice-versa.
  - No uncommon subsequence exists $\implies \mathbf{-1}$.

This instance demonstrates subsequence set theory and structural length bounds, mathematically proves why the longest uncommon candidate is always the longer string itself whenever $a \ne b$, and derives $O(\min(|a|, |b|))$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two strings $a = \text{"aba"}$ and $b = \text{"cdc"}$:
Return the **length of the longest uncommon subsequence** between $a$ and $b$.
If no uncommon subsequence exists, return `-1`.

```text
Definitions:
  Subsequence of a: String obtained by deleting zero or more characters from a.
  Uncommon Subsequence: Subsequence of a that is NOT a subsequence of b (or vice versa).

Evaluating a = "aba", b = "cdc":
  "aba" is a subsequence of a (length 3).
  Can "aba" be formed by deleting characters from "cdc"?
    No! "cdc" only contains 'c' and 'd', never 'a' or 'b'.
  Therefore, "aba" is an uncommon subsequence of length 3.

Max Possible Length = 3
```

### The Triviality of Uncommon Subsequences
While Longest *Common* Subsequence (LCS) requires 2D dynamic programming:
Longest *Uncommon* Subsequence (LUS) has an immediate closed-form solution:
1. Every string $a$ is a subsequence of itself.
2. If $a \ne b$:
   - If $|a| > |b|$: $a$ has length $|a|$. A subsequence of $b$ can have length at most $|b| < |a|$. Thus $a$ cannot possibly be a subsequence of $b$!
   - If $|a| == |b|$ and $a \ne b$: The only subsequence of $b$ of length $|a|$ is $b$ itself. Since $a \ne b$, $a$ is not a subsequence of $b$.
   - In both cases, **the longer string itself is the longest uncommon subsequence**!
3. If $a == b$:
   Every subsequence of $a$ is identical to a subsequence of $b$. No uncommon subsequence exists $\implies$ return $-1$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Closed-Form Formula:
$$
LUS(a, b) =
\begin{cases}
-1 & \text{if } a == b \\
\max(|a|, |b|) & \text{if } a \ne b
\end{cases}
$$

### 2. Proof of Maximality:
- Can any uncommon subsequence have length strictly greater than $\max(|a|, |b|)$?
  No, because by definition, an uncommon subsequence must be a subsequence of either $a$ or $b$.
- Therefore, the theoretical upper bound for any subsequence is $\max(|a|, |b|)$.
- When $a \ne b$, the string with length $\max(|a|, |b|)$ achieves this theoretical upper bound.

> **Uncommon Extremum Invariant.** If two strings are not completely identical, the entire longer string is guaranteed to be absent from the subsequence set of the other.

---

## 3. Step-by-Step Worked Execution

We trace $a = \text{"aba"}$ and $b = \text{"cdc"}$:

---

### Step 1: String Equality Test
Compare string contents:
$$
a == b \iff \text{"aba"} == \text{"cdc"} \implies \mathbf{False}
$$
Strings are not identical.

---

### Step 2: Compute Maximum Length
$$
|a| = 3, \quad |b| = 3
$$
$$
\max(|a|, |b|) = \max(3, 3) = \mathbf{3}
$$

---

### Step 3: Result
Output:
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

| String $a$ | String $b$ | $a == b$? | $|a|$ | $|b|$ | Action Taken | Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"aba"` | `"cdc"` | False | $3$ | $3$ | $\max(3, 3)$ | **$3$** |
| `"aaa"` | `"bbb"` | False | $3$ | $3$ | $\max(3, 3)$ | **$3$** |
| `"a"` | `"aaa"` | False | $1$ | $3$ | $\max(1, 3)$ | **$3$** |
| `"abc"` | `"abc"` | **True** | $3$ | $3$ | Return $-1$ | **$-1$** |
| `""` | `"hello"` | False | $0$ | $5$ | $\max(0, 5)$ | **$5$** |

---

## 5. Boundary Cases & Failure Modes

- **Identical Strings ($a == b$):** All subsets of characters match $\implies \mathbf{-1}$.
- **One String is Empty ($a = \text{""}, b = \text{"xyz"}$):** Return $|b| = \mathbf{3}$.
- **Different Lengths with Common Substring ($a = \text{"abc"}, b = \text{"abcdef"}$):** $|b| = 6 > |a| = 3 \implies$ entire string $b$ cannot be in $a \implies \mathbf{6}$.
- **Single Character Strings:** `"a"` vs `"b"` $\implies 1$; `"a"` vs `"a"` $\implies -1$.

---

## 6. Traps & Common Anti-Patterns

- **Writing a Full 2D DP Table:** Implementing $O(|a| \cdot |b|)$ dynamic programming (as for LCS) is completely unnecessary. LUS is a mathematical logic puzzle with an $O(1)$ decision rule.
- **Checking Character Overlaps:** Checking whether $a$ and $b$ share characters (e.g. `"abc"` vs `"abd"`) is irrelevant. As long as the two full strings differ, the full length $\max(|a|, |b|)$ is immediately valid.
- **Assuming $a$ is a Subsequence of $b$ Means No Answer:** If $a = \text{"ab"}$ and $b = \text{"abc"}$, $a$ IS a subsequence of $b$, but $b$ is NOT a subsequence of $a$! The answer is $|b| = 3$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - String equality comparison $a == b$ takes $O(\min(|a|, |b|))$ time.
  - Length calculation takes $O(1)$ time.
  - Total Time: $\mathcal{O}(\min(|a|, |b|))$. For strings of length 100, takes $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space.
