# Largest Palindrome Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 479 |
| Difficulty | Hard |
| Topics | Math, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-palindrome-product/) |

## Problem Description
### Goal
Given a digit count `n` from `1` through `8`, consider products $a \cdot b$ where both factors are positive decimal integers with exactly `n` digits. A product qualifies when its decimal representation reads the same forward and backward.

Find the largest qualifying palindrome product, then return that palindrome modulo `1337`. The factors may be equal, and the modulo operation is applied only to the final largest palindrome rather than used to compare candidate sizes. The function returns the reduced value, not the factors or unreduced palindrome. For $n = 1$, the largest product is included under the same rule.

### Function Contract
**Inputs**

- `n`: the factor digit count, restricted to $1 \le n \le 8$

**Return value**

- The largest qualifying palindrome product modulo `1337`

### Examples
**Example 1**

- Input: `n = 1`
- Output: `9`

**Example 2**

- Input: `n = 2`
- Output: `987`

**Example 3**

- Input: `n = 3`
- Output: `123`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Recognize the deliberately finite domain**

The public contract permits only eight input values. The largest palindrome product for each digit count is deterministic, and the required return value is its residue modulo 1337. Store the eight reviewed residues in frontend-input order and index by $n - 1$.

**Why lookup preserves the mathematical result**

Each table entry is the result of the full constrained enumeration problem for that one digit count, not an approximation or heuristic. Since no ninth digit count is valid, the table exhausts the input domain and returns the same result that online palindrome/factor search would compute.

**How the values can be derived offline**

For a given `n`, enumerate palindrome candidates downward by mirroring a leading half. For each candidate, test whether it has an `n`-digit factor whose paired quotient is also `n` digits, stopping at the first success. Performing that expensive derivation once produces the constant canonical table used at runtime.

#### Complexity detail

Runtime lookup takes $O(1)$ time and the fixed eight-entry table occupies $O(1)$ space. The offline derivation is not repeated by the submitted algorithm.

#### Alternatives and edge cases

- **Descending mirrored-palindrome search:** avoids storing results but performs substantial factor enumeration for every call.
- **Enumerate all factor pairs:** is simpler conceptually but has an enormous search space for eight-digit factors.
- **Generate decimal strings and reverse:** can construct palindromes during offline search but adds conversion overhead.
- **$n = 1$:** the largest product palindrome is `9`.
- **Modulo timing:** identify the largest palindrome first, then take its residue; maximizing residues would solve a different problem.
- **Fixed input bound:** there is no required behavior outside `1` through `8`.

</details>
