# Guided Example: Shortest Palindrome

We trace the step-by-step longest palindromic prefix reduction, KMP prefix-function ($\pi$-table) construction, and rolling polynomial hash matching on representative string instances:

- **Input:** $s = \text{"aacecaaa"}$
- **Required output:** `"aaacecaaa"` (Longest palindromic prefix is `"aacecaa"` of length 7; prepend reversed suffix `"a"`)
- **Strict Asymmetric Instance:** $s = \text{"abcd"} \implies \text{"dcbabcd"}$ (Longest palindromic prefix is `"a"` of length 1; prepend reversed suffix `"dcb"`)
- **Already Palindromic Instance:** $s = \text{"racecar"} \implies \text{"racecar"}$ (Entire string is palindromic; 0 characters added)
- **Single Character Instance:** $s = \text{"a"} \implies \text{"a"}$
- **Empty String Instance:** $s = \text{""} \implies \text{""}$

This instance demonstrates transforming palindrome completion into a longest palindromic prefix search, proves why prepending $\text{suffix}^R$ produces the minimal-length palindrome, constructs the KMP composite string ($s + \text{"\#"} + s^R$), evaluates Rabin-Karp rolling hashes, and operates in strictly $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given string $s = \text{"aacecaaa"}$ of length $N = 8$:
Convert $s$ into a palindrome by **only adding characters in front of it**, minimizing the total length of the resulting string.

### Mathematical Reduction to Longest Palindromic Prefix
Any valid palindrome formed by prepending characters has the structure:
$$
\text{prepended\_prefix} + s
$$
Because the original string $s$ forms the suffix of the palindrome, the beginning of $s$ must mirror itself around the center!
Suppose $s$ is partitioned into two parts:
$$
s = P + T
$$
where $P$ is a prefix of $s$ that is **already a palindrome** ($P = P^R$), and $T$ is the remaining suffix.
To make the entire string a palindrome, we must prepend the reverse of $T$ ($T^R$):
$$
\text{palindrome} = T^R + P + T
$$
- $T^R$ and $T$ mirror each other.
- $P$ is a palindrome and mirrors itself.
- Total length added is $|T^R| = |T| = |s| - |P|$.

To **minimize** the added characters $|T|$, we must **maximize** the length of the palindromic prefix $|P|$!
For $s = \text{"aacecaaa"}$:
- Prefix $P_1 = \text{"a"}$: palindrome of length 1.
- Prefix $P_2 = \text{"aa"}$: palindrome of length 2.
- Prefix $P_3 = \text{"aacecaa"}$: palindrome of length 7! ($|P| = 7$).
- Suffix $T = s[7:] = \text{"a"}$.
- Prepend $T^R = \text{"a"}$:
  $$
  \text{Result} = \text{"a"} + \text{"aacecaaa"} = \mathbf{\text{"aaacecaaa"}}
  $$

---

## 2. Conceptual Foundation & Invariants

### Method A: KMP Prefix Function on Composite String
A string $P$ is a palindromic prefix of $s$ if and only if $P$ is both:
1. A prefix of $s$.
2. A suffix of $s^R$ (the reversed string).

Create the composite string with an unambiguous delimiter `\#` (which does not appear in $s$):
$$
\text{temp} = s + \text{"\#"} + s^R
$$
Compute the KMP $\pi$ table (prefix function), where $\pi[i]$ is the length of the longest proper prefix of $\text{temp}$ that matches a suffix ending at $i$.
Because `\#` separates $s$ and $s^R$:
The final value $\pi[\text{len}(\text{temp}) - 1]$ equals the length of the longest prefix of $s$ that matches a suffix of $s^R$. That is precisely the **longest palindromic prefix of $s$**!

### Method B: Rabin-Karp Dual Rolling Hash
Scan characters $i = 0 \dots N - 1$ maintaining:
- Forward hash: $H_{\text{fwd}} = (H_{\text{fwd}} \cdot B + \text{val}) \pmod M$
- Reverse hash: $H_{\text{rev}} = (H_{\text{rev}} + \text{val} \cdot B^i) \pmod M$
Whenever $H_{\text{fwd}} == H_{\text{rev}}$, prefix $s[0 \dots i]$ reads identically forwards and backwards! The maximum matching index $i$ gives $|P| = i + 1$.

> **Invariant.** For the composite string $T = s + \text{"\#"} + s^R$, the KMP array value $\pi[k]$ strictly bounds the longest palindromic prefix of $s$ that extends to index $k$.

---

## 3. Step-by-Step Worked Execution

We trace the KMP construction on $s = \text{"aacecaaa"}$:
- $s = \text{"aacecaaa"}$ ($N = 8$)
- $s^R = \text{"aaacecaa"}$
- $\text{temp} = \text{"aacecaaa\#aaacecaa"}$ (Length $= 8 + 1 + 8 = 17$)

### KMP Prefix Table ($\pi$) Computation:
Initialize $\pi = [0] \times 17$, $j = 0$:

1. $i = 1$ ($T[1] = \text{'a'}, T[j] = \text{'a'}$): Match! $j = 1, \, \pi[1] = 1$.
2. $i = 2$ ($T[2] = \text{'c'}, T[j] = \text{'a'}$): Mismatch. $j = \pi[0] = 0. \, T[2] \ne T[0] \implies \pi[2] = 0$.
3. $i = 3$ ($T[3] = \text{'e'}, T[j] = \text{'a'}$): $\pi[3] = 0$.
4. $i = 4$ ($T[4] = \text{'c'}, T[j] = \text{'a'}$): $\pi[4] = 0$.
5. $i = 5$ ($T[5] = \text{'a'}, T[j] = \text{'a'}$): Match! $j = 1, \, \pi[5] = 1$.
6. $i = 6$ ($T[6] = \text{'a'}, T[j] = \text{'a'}$): Match! $j = 2, \, \pi[6] = 2$.
7. $i = 7$ ($T[7] = \text{'a'}, T[j] = \text{'c'}$): Mismatch. $j = \pi[1] = 1. \, T[7] == T[1] \implies j = 2, \, \pi[7] = 2$.
8. $i = 8$ ($T[8] = \text{'\#'}$): Delimiter breaks matches $\implies \pi[8] = 0$.

Now scan into the reversed string $s^R$ ($i \ge 9$):
9. $i = 9$ ($T[9] = \text{'a'}$): Match with $T[0] = \text{'a'} \implies j = 1, \, \pi[9] = 1$.
10. $i = 10$ ($T[10] = \text{'a'}$): Match with $T[1] = \text{'a'} \implies j = 2, \, \pi[10] = 2$.
11. $i = 11$ ($T[11] = \text{'a'}$): Mismatch with $T[2] = \text{'c'}$. Fallback $j = \pi[1] = 1$. $T[11] == T[1] \implies j = 2, \, \pi[11] = 2$.
12. $i = 12$ ($T[12] = \text{'c'}$): Match with $T[2] = \text{'c'} \implies j = 3, \, \pi[12] = 3$ (Prefix `"aac"`).
13. $i = 13$ ($T[13] = \text{'e'}$): Match with $T[3] = \text{'e'} \implies j = 4, \, \pi[13] = 4$ (Prefix `"aace"`).
14. $i = 14$ ($T[14] = \text{'c'}$): Match with $T[4] = \text{'c'} \implies j = 5, \, \pi[14] = 5$ (Prefix `"aacec"`).
15. $i = 15$ ($T[15] = \text{'a'}$): Match with $T[5] = \text{'a'} \implies j = 6, \, \pi[15] = 6$ (Prefix `"aaceca"`).
16. $i = 16$ ($T[16] = \text{'a'}$): Match with $T[6] = \text{'a'} \implies j = 7, \, \pi[16] = \mathbf{7}$ (Prefix `"aacecaa"`).

---

### Step 4: Palindrome Assembly
- Longest palindromic prefix length $L = \pi[16] = \mathbf{7}$.
- Suffix of $s$ beyond $L$:
  $$
  T = s[7:] = \text{"a"}
  $$
- Prepend $T^R = \text{"a"}$:
  $$
  \text{Result} = T^R + s = \text{"a"} + \text{"aacecaaa"} = \mathbf{\text{"aaacecaaa"}}
  $$

---

## 4. Complete Execution Trace

```text
s = "aacecaaa",  s_rev = "aaacecaa"
Composite: "aacecaaa#aaacecaa"

i:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
T:  a  a  c  e  c  a  a  a  #  a  a  a  c  e  c  a  a
pi: 0  1  0  0  0  1  2  2  0  1  2  2  3  4  5  6  7

Final pi[16] = 7 -> Longest Palindromic Prefix = s[:7] = "aacecaa"
Suffix to mirror: s[7:] = "a" -> Prepend "a"
Answer: "a" + "aacecaaa" = "aaacecaaa"
```

| Index $i$ | Character $T[i]$ | Previous $j$ | Fallback / Match Evaluation | Updated $j$ | Recorded $\pi[i]$ |
|:---:|:---:|:---:|:---|:---:|:---:|
| $0 \dots 7$ | `aacecaaa` | - | Prefix of $s$ evaluated | - | $[0, 1, 0, 0, 0, 1, 2, 2]$ |
| 8 | `\#` | 2 | Delimiter reset | 0 | 0 |
| 9 | `'a'` | 0 | Match with $T[0]$ | 1 | 1 |
| 10 | `'a'` | 1 | Match with $T[1]$ | 2 | 2 |
| 11 | `'a'` | 2 | Fallback to $j=1$, match | 2 | 2 |
| 12 | `'c'` | 2 | Match with $T[2]$ (`'c'`) | 3 | 3 |
| 13 | `'e'` | 3 | Match with $T[3]$ (`'e'`) | 4 | 4 |
| 14 | `'c'` | 4 | Match with $T[4]$ (`'c'`) | 5 | 5 |
| 15 | `'a'` | 5 | Match with $T[5]$ (`'a'`) | 6 | 6 |
| **16** | **`'a'`** | **6** | **Match with $T[6]$ (`'a'`)** | **7** | **7 (Longest Prefix)** |

---

## 5. Algorithmic Correctness

**Soundness.** The delimiter `\#` prevents any prefix match from spanning across both strings. By definition of the KMP prefix table, $\pi[\text{len}(\text{temp}) - 1]$ is the length of the longest prefix of $s$ that matches a suffix of $s^R$. Since a suffix of $s^R$ is the reverse of a prefix of $s$, this prefix must equal its own reverse, guaranteeing it is a palindrome. Prepending the reverse of the remaining suffix guarantees the entire string is palindromic.

**Completeness.** Since the KMP prefix function computes the maximal proper prefix-suffix match, no longer palindromic prefix can exist. Any shorter palindromic prefix would result in a strictly longer prepended suffix, proving that the generated palindrome has the minimum possible length.

---

## 6. Traps This Instance Exposes

- **Missing Delimiter in KMP:** If $s + s^R$ is used without a delimiter, a string like `"aaaa"` produces `"aaaaaaaa"`, where the KMP table crosses the boundary and reports a prefix length greater than $|s|$. The delimiter `\#` strictly confines prefix matches to $|s|$.
- **$O(N^2)$ Slicing:** Repeatedly testing `s[:k] == s[:k][::-1]` from $k = N$ down to $1$ takes $O(N^2)$ time, which times out for $N = 50,000$. Both KMP and rolling hash achieve strictly $O(N)$.
- **Hash Collisions:** Single-modulus rolling hash can produce false positives. KMP is fully deterministic and eliminates collision risks.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. Constructing the composite string $\text{temp}$ takes $O(N)$ time. The KMP prefix table computation visits each character at most twice (due to the amortized pointer $j$), running in $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for the composite string and the $\pi$ table of size $2N + 1$.
