# Shortest Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SHORTPALINDR |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [SHORTPALINDR](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/SHORTPALINDR) |

---

## Problem Statement

You are given a string $s$ consisting of lowercase English letters. You can convert $s$ into a **palindrome** by adding characters **only at the beginning** of the string.

Your task is to **find the shortest palindrome** that can be obtained using this transformation.

## Function Declaration

### Function Name
$shortestPalindrome$ – This function finds the shortest palindrome that can be formed by adding characters **only at the beginning** of the given string.

### Parameters

* $s$ : A string consisting of lowercase English letters.

### Return Value

* Returns a string representing the **shortest palindrome** that can be obtained by adding characters only at the beginning of $s$.

## Constraints

- $1 \leq T \leq 100$
- $0 \leq |s| \leq 5 \times 10^4$
- $s$ consists of lowercase English letters only

**The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled by the driver code.**

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* Each of the next $T$ lines contains a single string $s$.

---

## Output Format

* For each test case, print a single line containing the shortest palindrome that can be formed.

---

## Constraints

- $1 \leq T \leq 100$
- $0 \leq |S| \leq 5 \times 10^{4}$
- $S \text{ consists of lowercase English letters only.}$

---

## Examples

**Example 1**

**Input**

```text
3
race
level
xyz
```

**Output**

```text
ecarace
level
zyxyz
```

**Explanation**

**Test case 1**: `"race"` -> Add `"eca"` at the beginning -> `"ecarace"` is a palindrome.

**Test case 2**: `"level"` -> Already a palindrome, so output is the same -> `"level"`.

**Test case 3**: `"xyz"` -> Add `"zyx"` at the beginning -> `"zyxyz"` is the shortest palindrome.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
race
```

**Output for this case**

```text
ecarace
```



#### Test case 2

**Input for this case**

```text
level
```

**Output for this case**

```text
level
```



#### Test case 3

**Input for this case**

```text
xyz
```

**Output for this case**

```text
zyxyz
```



**Example 2**

**Input**

```text
1
aaab
```

**Output**

```text
baaab
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Restatement

You are given a string `s`.
You may add characters **only at the beginning** of the string.
Your goal is to obtain the **shortest possible palindrome**.

## Key Observation

If we can find the **longest prefix of `s` that is already a palindrome**, then:

* The remaining suffix (after this prefix) must be mirrored and added to the **front**.
* This guarantees minimal additions.

So the problem reduces to:

> **Find the longest palindromic prefix of `s`.**

## Approach 1: Brute Force (Check All Prefixes)

### Idea

* For every prefix `s[0…i]`, check if it is a palindrome.
* Choose the **longest** such prefix.
* Reverse the remaining suffix and prepend it.

### Algorithm

1. For `i` from `n` down to `0`:

   * If `s[0…i-1]` is a palindrome:

     * Let suffix = `s[i…n-1]`
     * Answer = `reverse(suffix) + s`
     * Stop.

### Correctness

* We try all prefixes.
* Choosing the longest palindromic prefix minimizes added characters.
* Adding characters only at the front preserves the constraint.

### Complexity

* Palindrome check: `O(n)`
* Total prefixes: `O(n)`
* **Time:** `O(n²)`
* **Space:** `O(1)` (excluding output)

### Verdict

* Simple and intuitive
* **Too slow** for large inputs (`|s|` up to `5 × 10⁴`)

---

## Approach 2: Two-Pointer Optimization

### Idea

* Use two pointers to check if `s[0…i]` is a palindrome.
* Still checks multiple prefixes, but with early breaks.

### Algorithm

1. Start from the full string.
2. For each prefix end `i`:

   * Use two pointers (`l = 0`, `r = i`) to check palindrome.
3. When found, construct answer.

### Complexity

* Still **O(n²)** worst case
* Slightly faster in practice than brute force

### Verdict

* Better constant factor
* Still not optimal

---

## Approach 3: Rolling Hash

### Idea

* Compare forward hash and reverse hash of prefixes.
* If hashes match, prefix is likely a palindrome.

### Algorithm

1. Compute rolling hash for:

   * Forward string
   * Reverse string
2. For each prefix length:

   * Compare hash of `s[0…i]` with reverse hash.
3. Pick the longest valid prefix.

### Correctness

* Hash equality implies palindrome with high probability.
* Using double hashing avoids collisions.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

### Verdict

* Efficient
* Slight risk of hash collision
* More complex to implement

---

## Approach 4: KMP-Based Optimal Solution (Recommended)

### Core Insight

A palindrome prefix of `s` is equivalent to a **prefix of `s` matching a prefix of `reverse(s)`**.

We use KMP to find the **longest prefix of `s` that matches a suffix of `reverse(s)`**.

---

### Construction

Let:

```
rev = reverse(s)
combined = s + "#" + rev
```

Compute the **LPS (Longest Prefix Suffix)** array for `combined`.

The last value of LPS tells us:

> Length of the longest palindromic prefix of `s`

---

### Algorithm

1. Reverse the string → `rev`
2. Create `combined = s + "#" + rev`
3. Compute LPS array using KMP preprocessing
4. Let `len = LPS[last index]`
5. Remaining suffix = `s[len…end]`
6. Answer = `reverse(remaining suffix) + s`

---

### Example

`s = "race"`

```
rev = "ecar"
combined = "race#ecar"
LPS = [0,0,0,0,0,1,2,3]
```

* Longest palindromic prefix length = `1` (`"r"`)
* Remaining = `"ace"`
* Result = `"eca" + "race" = "ecarace"`

### Correctness Proof

* KMP guarantees the longest prefix match.
* This prefix corresponds to the longest palindromic prefix of `s`.
* Adding the reverse of the remaining suffix creates a palindrome.
* Minimal additions are made since the prefix is maximal.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`
* Works comfortably within constraints

## Edge Cases

* Empty string → return empty string
* Already palindrome → return original string
* Single character → already palindrome

## Final Recommendation

| Approach     | Time     | Space    | Suitable               |
| ------------ | -------- | -------- | ---------------------- |
| Brute Force  | O(n²)    | O(1)     | Small input            |
| Two-Pointer  | O(n²)    | O(1)     | Slightly better brute  |
| Rolling Hash | O(n)     | O(n)     | Fast but probabilistic |
| **KMP**      | **O(n)** | **O(n)** | **Best choice**        |

</details>
