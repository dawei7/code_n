# Guided Example: Rotate String

We trace the step-by-step cyclic string shift kinematics ($s \to s[1:] + s[0]$), string doubling universe invariant ($s + s$), cyclic substring containment theorem ($goal \in s + s$), length equality gate ($|s| == |goal|$), and rotation isomorphism verification on representative character strings:

- **Input:**
  $$
  s = \text{"abcde"}, \quad goal = \text{"cdeab"}
  $$
- **Required output:** `true`
  - Cyclic shift mechanics:
    - A single shift on string $s$ removes the leftmost character and appends it to the rightmost end:
      $$
      s = s_0 s_1 s_2 \dots s_{n-1} \implies \text{shift}(s) = s_1 s_2 \dots s_{n-1} s_0
      $$
    - Objective: Determine if there exists some non-negative integer $k$ such that applying $k$ shifts to $s$ produces $goal$.
    - For $s = \text{"abcde"}$ and $goal = \text{"cdeab"}$:
      - Shift 0: `"abcde"`
      - Shift 1: `"bcdea"`
      - Shift 2: `"cdeab"`
      - After 2 shifts, the string matches $goal$ exactly!
      - Result is **`true`**.
- **String Doubling & Cyclic Substring Invariant:**
  - **The All-Rotations Generator ($s + s$):**
    - Notice what happens when we concatenate $s$ with itself:
      $$
      s + s = s_0 s_1 \dots s_{n-1} \; s_0 s_1 \dots s_{n-1}
      $$
    - Consider any contiguous window of length $n = |s|$ starting at index $k \in [0, n - 1]$:
      - Window at index 0: $s_0 s_1 \dots s_{n-1}$ (Shift 0)
      - Window at index 1: $s_1 s_2 \dots s_{n-1} s_0$ (Shift 1)
      - Window at index $k$: $s_k s_{k+1} \dots s_{n-1} s_0 \dots s_{k-1}$ (Shift $k$)
    - The doubled string $s + s$ contains **all $n$ possible cyclic rotations of $s$** as contiguous substrings of length $n$!
  - **Necessary and Sufficient Equivalence:**
    - A string $goal$ is a cyclic shift of $s$ if and only if:
      1. $|s| == |goal|$ (their lengths are identical).
      2. $goal$ is a substring of $s + s$.
    - This converts cyclic shift testing into standard string substring search in $\mathcal{O}(N)$ time!
- **Step-by-Step Worked Execution Trace on $s = \text{"abcde"}, goal = \text{"cdeab"}$:**
  - Length check:
    $$
    |s| = 5, \quad |goal| = 5 \implies 5 == 5 \quad \mathbf{(Length\ Gate\ Passed)}
    $$
  - **Step 1: Construct Doubled String $s + s$:**
    $$
    s + s = \text{"abcde"} + \text{"abcde"} = \mathbf{\text{"abcdeabcde"}}
    $$
  - **Step 2: Substring Search for $goal$:**
    - Test window 0 (index $0 \dots 4$): `"abcde"` $\ne$ `"cdeab"`
    - Test window 1 (index $1 \dots 5$): `"bcdea"` $\ne$ `"cdeab"`
    - Test window 2 (index $2 \dots 6$):
      $$
      (s + s)[2 \dots 6] = \mathbf{\text{"cdeab"}} == goal
      $$
    - Match found at offset $k = 2$!
  - **Step 3: Verification:**
    - Offset $k = 2$ corresponds to exactly 2 cyclic shifts:
      $$
      \text{"abcde"} \xrightarrow{\text{shift 1}} \text{"bcdea"} \xrightarrow{\text{shift 2}} \text{"cdeab"}
      $$
    - Return:
      $$
      ans = \mathbf{true}
      $$
- **Permutation Order Mismatch Trace ($s = \text{"abcde"}, goal = \text{"abced"}$):**
  - $|s| = |goal| = 5$.
  - Doubled string: `"abcdeabcde"`.
  - Looking for `"abced"`:
    - Letters `'e'` and `'d'` are reversed relative to the original cyclic order.
    - `"abced"` does not appear anywhere in `"abcdeabcde"`.
    - Returns **`false`**.
- **Length Mismatch Gate Trace ($s = \text{"a"}, goal = \text{"aa"}$):**
  - $|s| = 1 \ne |goal| = 2$.
  - Even though `"a" + "a" = "aa"` contains $goal$, lengths differ!
  - Pre-condition $|s| == |goal|$ immediately rejects this $\implies$ **`false`**.

This instance demonstrates cyclic group actions on free monoids and Cayley string embedding, mathematically proves why the set of conjugate words corresponds bijectively to length-$n$ subsegments of the periodic word $s^2$, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given strings $s$ and $goal$:
Can $s$ become $goal$ after some number of cyclic shifts?

```text
s    = "abcde"
goal = "cdeab"

Concatenate s with itself:
  s + s = "abcdeabcde"

Windows of length 5 in s + s:
  Offset 0: "abcde"
  Offset 1: "bcdea"
  Offset 2: "cdeab" -> Matches goal!

Result: true
```

### The Invariant of the Doubled String Universe
- $s + s$ contains **all cyclic shifts of $s$** as contiguous substrings of length $|s|$.
- A string $goal$ is a cyclic shift of $s \iff |s| == |goal|$ and $goal \in s + s$.

---

## 2. Conceptual Foundation & Invariants

### 1. Length Identity Gate:
$$
|s| = |goal|
$$

### 2. Conjugacy Criterion:
$$
\text{canRotate}(s, goal) \iff (|s| == |goal|) \;\land\; (goal \subseteq s \cdot s)
$$

> **Free Monoid Conjugacy Invariant.** Two words $u, v \in \Sigma^*$ are conjugate (cyclically equivalent) if and only if there exist words $x, y$ such that $u = xy$ and $v = yx$. Conjugacy in the free monoid is decidable by testing whether $v$ is a factor of $u^2$ of equal length $|u| = |v|$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abcde"}, goal = \text{"cdeab"}$:

---

### Step 1: Check Lengths
- $|s| = 5 == |goal| = 5 \implies$ Passed.

---

### Step 2: Form $s + s$
- $s + s = \text{"abcdeabcde"}$.

---

### Step 3: Check Substring
- `"cdeab"` is at indices $2 \dots 6$ of `"abcdeabcde"`.

---

### Step 4: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Cyclic Shift Count $k$ | Shifted String $s^{(k)}$ | Substring Range in $s+s$ | Matches $goal = \text{"cdeab"}$? |
|:---:|:---:|:---:|:---:|
| $0$ | `"abcde"` | $[0 \dots 4]$ | No |
| $1$ | `"bcdea"` | $[1 \dots 5]$ | No |
| **$2$** | **`"cdeab"`** | **$[2 \dots 6]$** | **Yes (Match Found!)** |
| **Final** | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Character ($s = \text{"a"}, goal = \text{"a"}$):** 0 shifts $\implies$ returns `true`.
- **Length Mismatch ($s = \text{"a"}, goal = \text{"aa"}$):** Substring check alone would falsely say `"aa" in "aa"`, but length gate $|s| == |goal|$ correctly rejects it (`false`).
- **Empty Strings:** Returns `true` if both empty.
- **Goal Contains Characters Not in $s$:** Rejection guaranteed $\implies$ `false`.

---

## 6. Traps & Common Anti-Patterns

- **Simulating All Shifts Explicitly ($O(N^2)$):** Slicing $s[1:] + s[0]$ in a loop creates $N$ intermediate strings. Checking `goal in s + s` uses optimized KMP/Boyer-Moore substring search in linear $O(N)$ time.
- **Forgetting the Length Check:** If $s = \text{"ab"}$ and $goal = \text{"a"}$, then $goal$ is in $s + s = \text{"abab"}$, but $goal$ is not a valid cyclic rotation of $s$. The length check `len(s) == len(goal)` is mandatory!
- **Quadratic Memory Allocations:** Concatenating $s + s$ uses $2N$ memory, which is negligible for $N \le 100$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Length check: $\mathcal{O}(1)$.
  - Creating $s + s$: $\mathcal{O}(N)$.
  - Substring search in length $2N$: $\mathcal{O}(N)$ using standard string search.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 100$. Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for doubled string $s + s$.
