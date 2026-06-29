# Check Isomorphic Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ISOMORPHICST |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [ISOMORPHICST](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/ISOMORPHICST) |

---

## Problem Statement

You are given two strings, $s$ and $t$. Determine whether these two strings are `isomorphic`.

Two strings are said to be **isomorphic** if characters in string $s$ can be replaced to get string $t$, such that:

- Each character in $s$ maps to exactly one character in $t$.
- No two different characters in $s$ map to the same character in $t$.
- The order of characters is preserved.
- A character is allowed to map to itself.

## Function Declaration

### Function Name
$isIsomorphic$ – This function checks whether two strings are isomorphic.

### Parameters

* $s$ : A string representing the source string.
* $t$ : A string representing the target string.

### Return Value

* Returns $true$ if the strings $s$ and $t$ are isomorphic.
* Returns $false$ otherwise.

## Constraints

- $1 \leq N \leq 100$
- $1 \leq |s| = |t| \leq 10^5$
- Strings $s$ and $t$ consist of ASCII characters.

---

## Input Format

- The first line contains a single integer $N$ — the number of test cases.
- For each test case:
  - The first line contains the string $s$.
  - The second line contains the string $t$.

---

## Output Format

- For each test case, print:
  - `"YES"` if the strings are isomorphic.
  - `"NO"` otherwise.

---

## Constraints

- $1 \le |S| = |T| \le 10^{5}$
- $S \text{ and } T \text{ consist of ASCII characters.}$
- $1 \le N \le 100$

---

## Examples

**Example 1**

**Input**

```text
2
mno
pqr
hello
world
```

**Output**

```text
YES
NO
```

**Explanation**

- `"mno"` -> `"pqr"`: mapping `m->p`, `n->q`, `o->r` YES

- `"hello"` -> `"world"`: `'l'` maps to two different letters `'r'` and `'l'` NO

**Separated test cases**

#### Test case 1

**Input for this case**

```text
mno
pqr
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
hello
world
```

**Output for this case**

```text
NO
```



**Example 2**

**Input**

```text
3
abcabc
xyzxyz
pqrpqr
mnopmn
abcd
abcc
```

**Output**

```text
YES
NO
NO
```

**Explanation**

- `"abcabc"` -> `"xyzxyz"` YES

- `"pqrpqr"` -> `"mnopmn"` NO

- `"abcd"` -> `"abcc"` last character maps to two letters.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abcabc
xyzxyz
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
pqrpqr
mnopmn
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
abcd
abcc
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

We are given two strings **S** and **T** for each test case.\
We need to determine whether they are **isomorphic**.

Two strings are said to be **isomorphic** if characters in `S` can be replaced to get `T`, such that:

- The order of characters is preserved.
- No two different characters in `S` map to the same character in `T`.
- A character may map to itself.

If `S` and `T` are isomorphic, we print `"YES"`, otherwise `"NO"`.

---

# Intuition

Think of it like a **one-to-one character** mapping between the two strings.\
Each character in `S` must consistently map to one character in `T`, and vice versa.

Example:

S = "mno", T = "pqr"
m -> p
n -> q
o -> r
✅ All mappings are unique → YES

But if one character in `S` maps to multiple characters in `T`, or vice versa, then the strings are **not isomorphic**.

---

# Algorithm

**Check length**
- If `|S| ≠ |T|`, they cannot be isomorphic → return `"NO"`.

**Use two hash maps (or arrays)**
- `mapST`: stores mapping from characters of `S` → `T`
- `mapTS`: stores mapping from characters of `T` → `S`

**Iterate through both strings**\
For each character pair (s[i], t[i]):

- If `s[i]` is already mapped in `mapST`, ensure it maps to `t[i]`.
Otherwise, set the mapping.\

- Similarly, ensure the reverse mapping in `mapTS`.

**If any mismatch occurs**, return `"NO"`.
If all pairs match consistently, return `"YES"`.

---

# Example Walkthrough

Example 1:

Input:
mno
pqr

| i | s[i] | t[i] | mapST | mapTS | Valid |
| - | ---- | ---- | ----- | ----- | ----- |
| 0 | m    | p    | m→p   | p→m   | ✅     |
| 1 | n    | q    | n→q   | q→n   | ✅     |
| 2 | o    | r    | o→r   | r→o   | ✅     |

✅ All consistent → Output: YES

---

# Complexity Analysis

| Type                 | Analysis                                                                 |
| -------------------- | ------------------------------------------------------------------------ |
| **Time Complexity**  | **O(N)** per test case, where N = length of string                       |
| **Space Complexity** | **O(1)** — since only fixed-size character maps (256 for ASCII) are used |

</details>
