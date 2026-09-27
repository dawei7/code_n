# Guided Example: Check if All A's Appears Before All B's

We trace the step-by-step execution of the optimal substring-pattern invariant check on representative problem instances:

- **Representative Instance 1:** `s = "aaabbb"` $\implies$ Expected Output: `true`
- **Representative Instance 2:** `s = "abab"` $\implies$ Expected Output: `false`
- **Representative Instance 3:** `s = "bbb"` $\implies$ Expected Output: `true`

This instance illustrates the equivalence between global monotonic ordering in a two-letter alphabet and the local absence of inverted adjacent character transitions.

---

## 1. Problem Overview & Representative Instance

Given a string $s$ consisting solely of characters `'a'` and `'b'`, we must verify whether every occurrence of `'a'` appears strictly before every occurrence of `'b'`.

Consider the structural contrast among three cases:
- In $s = \text{"aaabbb"}$, the string consists of three `'a'`s followed by three `'b'`s. All `'a'`s precede all `'b'`s. The condition is met.
- In $s = \text{"abab"}$, the character `'a'` at index $2$ appears after the character `'b'` at index $1$. The condition is violated.
- In $s = \text{"bbb"}$, no `'a'` exists in the string, which satisfies the condition vacuously.

Rather than running nested loops to verify all pairs $(i, j)$ with $i < j$, we can resolve the problem in a single linear pass or via direct local substring inspection.

---

## 2. Mathematical & Algorithmic Principles

### Global Monotonicity vs. Local Inversions
Let the string $s$ of length $n$ be an array of characters $s[0 \dots n-1]$ over the ordered alphabet $\Sigma = \{'a', 'b'\}$ with standard lexicographical order $'a' < 'b'$.
The formal requirement states:

$$\forall i, j \in \{0, \dots, n-1\}, \quad (i < j) \implies \neg(s[i] = \text{'b'} \land s[j] = \text{'a'})$$

Equivalently, the string must be non-decreasing with respect to the ordering $'a' \le 'b'$, matching the regular expression language $a^* b^*$.

### The Inverted Substring Equivalence Theorem
**Theorem.** For any string $s \in \{'a', 'b'\}^*$, all occurrences of `'a'` precede all occurrences of `'b'` if and only if $s$ does not contain the substring `"ba"`.

*Proof.*
1. **Sufficiency ($\implies$):** Suppose $s$ contains `"ba"`. Then there exists some index $k$ such that $s[k] = \text{'b'}$ and $s[k+1] = \text{'a'}$. Setting $i = k$ and $j = k + 1$, we have $i < j$ with $s[i] = \text{'b'}$ and $s[j] = \text{'a'}$, violating the condition.
2. **Necessity ($\impliedby$):** Suppose the condition is violated. Then there exist indices $i < j$ with $s[i] = \text{'b'}$ and $s[j] = \text{'a'}$. Consider the sequence of adjacent pairs $(s[t], s[t+1])$ for $t = i, i+1, \dots, j-1$. Because $s[i] = \text{'b'}$ and $s[j] = \text{'a'}$, the sequence must transition from `'b'` to `'a'` at least once. At that transition point $k$, $s[k] = \text{'b'}$ and $s[k+1] = \text{'a'}$, meaning the substring `"ba"` must be present.

Thus, verifying validity reduces strictly to testing:

$$\text{Valid}(s) \iff \text{"ba"} \notin s$$

| String Pattern | Regular Form | Inverted Substring `"ba"` Present? | Outcome |
|---|---|---|---|
| Prefix `'a'`s then `'b'`s | $a^p b^q$ ($p, q \ge 0$) | No | `true` |
| All `'a'`s | $a^n$ ($n \ge 1$) | No | `true` |
| All `'b'`s | $b^n$ ($n \ge 1$) | No | `true` |
| Interleaved or trailing `'a'` | $a^* b^+ a^+ \dots$ | Yes | `false` |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We inspect adjacent pairs across the representative test strings:

### Evaluating String 1: $s = \text{"aaabbb"}$ (Length $n = 6$)
- Index $0 \to 1$: $(s[0], s[1]) = (\text{'a'}, \text{'a'})$ (Valid)
- Index $1 \to 2$: $(s[1], s[2]) = (\text{'a'}, \text{'a'})$ (Valid)
- Index $2 \to 3$: $(s[2], s[3]) = (\text{'a'}, \text{'b'})$ (Legal transition from $a$ to $b$)
- Index $3 \to 4$: $(s[3], s[4]) = (\text{'b'}, \text{'b'})$ (Valid)
- Index $4 \to 5$: $(s[4], s[5]) = (\text{'b'}, \text{'b'})$ (Valid)
No `"ba"` transition is detected. Return `true`.

### Evaluating String 2: $s = \text{"abab"}$ (Length $n = 4$)
- Index $0 \to 1$: $(s[0], s[1]) = (\text{'a'}, \text{'b'})$ (Legal transition)
- Index $1 \to 2$: $(s[1], s[2]) = (\text{'b'}, \text{'a'})$ (Forbidden inverted transition detected!)
- The substring `"ba"` is found at index interval $[1, 2]$.
Simulation halts immediately. Return `false`.

### Evaluating String 3: $s = \text{"bbb"}$ (Length $n = 3$)
- Index $0 \to 1$: $(s[0], s[1]) = (\text{'b'}, \text{'b'})$
- Index $1 \to 2$: $(s[1], s[2]) = (\text{'b'}, \text{'b'})$
No `"ba"` transition is detected. Return `true`.

---

## 4. Comprehensive State Trace

The execution details across various input profiles are summarized below:

| Input String $s$ | Length $n$ | State After First Pass | First Observed Inversion | Substring `"ba"` Status | Returned Value |
|---|---|---|---|---|---|
| `"aaabbb"` | $6$ | Reached end of string | None | Not Found | `true` |
| `"abab"` | $4$ | Aborted at index $1$ | $(s[1], s[2]) = (\text{'b'}, \text{'a'})$ | Found at index $1$ | `false` |
| `"bbb"` | $3$ | Reached end of string | None | Not Found | `true` |
| `"a"` | $1$ | Single character | None | Not Found | `true` |
| `"b"` | $1$ | Single character | None | Not Found | `true` |
| `"ba"` | $2$ | Aborted at index $0$ | $(s[0], s[1]) = (\text{'b'}, \text{'a'})$ | Found at index $0$ | `false` |

All results adhere strictly to the non-decreasing character property.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Suppose an algorithm returns `false` due to detecting the substring `"ba"` at position $k$. By definition, $s[k] = \text{'b'}$ and $s[k+1] = \text{'a'}$. Because $k < k + 1$, an occurrence of `'a'` appears after an occurrence of `'b'`, directly falsifying the universal condition.

**Completeness.** Suppose an algorithm returns `true` because `"ba"` does not appear anywhere in $s$. If the string contained any `'a'` after a `'b'`, there would exist at least one step along the index chain where a `'b'` transitions to an `'a'`, creating an instance of `"ba"`. The absence of `"ba"` guarantees that no such pair can exist, ensuring that no false positives can occur.

---

## 6. Edge Cases & Anti-Patterns

- **Uniform Strings (`"aaaa"` or `"bbbb"`):** Strings containing only one character type naturally satisfy the condition because no opposite character exists to form an inversion.
- **Minimal Length ($n = 1$):** A single character `'a'` or `'b'` can never contain a two-character substring, correctly evaluating to `true`.
- **Minimal Inversion (`"ba"`):** Immediately detected at the first pair, correctly returning `false`.
- **Anti-Pattern — Full String Sorting:** Sorting the string to compare `s == sorted(s)` requires $\mathcal{O}(n \log n)$ time and creates new string objects. Searching for `"ba"` executes in a single linear scan $\mathcal{O}(n)$ with early termination.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of string $s$. The substring search scans characters from left to right, comparing adjacent characters and halting immediately upon encountering `"ba"` or the end of the string.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$. The verification operates directly on the input string using constant index pointers without allocating additional heap memory.
