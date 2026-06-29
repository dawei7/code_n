# Generate All Possible Pairs of Balanced Parenthese

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAPROB7 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [DSAPROB7](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/DSAPROB7) |

---

## Problem Statement

Given a number $n$, generate all possible $n$ pairs of balanced parentheses.  A balanced parentheses string has opening and closing parentheses in a way that every opening parenthesis has a matching closing parenthesis and the pairs are properly nested.

You simply need to complete the provided function and don’t worry about the main function.

---

## Input Format

The input contains a single integer $n$.

---

## Output Format

Generate all combinations of $n$ pairs of balanced parentheses. Printing of the brackets will be done by the main function.

---

## Constraints

- $ 1 \leq n \leq 13 $

---

## Examples

**Example 1**

**Input**

```text
3
```

**Output**

```text
((()))
(()())
(())()
()(())
()()()
```

**Explanation**

For Sample Input 1, the valid combinations of 3 pairs of balanced parentheses are shown above.

**Example 2**

**Input**

```text
2
```

**Output**

```text
(())
()()
```

**Explanation**

For Sample Input 2, the valid combinations of 2 pairs of balanced parentheses are shown above.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

Given an integer `n`, generate all possible strings that contain `n` pairs of balanced parentheses. A balanced parentheses string has properly nested pairs of opening and closing parentheses.

#### [](#approach-2)Approach:

The core idea behind generating all possible balanced parentheses strings of `n` pairs is to use a **recursive backtracking** approach. The main challenge is to ensure that, at any point in constructing the string, the parentheses remain balanced. This means that at no point should the number of closing parentheses `)` exceed the number of opening parentheses `(`, and the total number of `(` and `)` should both be exactly `n` by the end of the construction.

### [](#step-by-step-explanation-3)Step-by-Step Explanation:

-

**Recursive Function Design**:

- We use a recursive function `generateParenthesis` that keeps track of:

- `open`: the number of opening parentheses used so far.

- `close`: the number of closing parentheses used so far.

- `str`: the current string being constructed.

- `result`: a vector that stores all valid balanced parentheses strings.

-

**Base Case**:

- The recursion stops when both `open` and `close` equal `n`, which means we’ve used all `n` pairs of parentheses. The constructed string `str` is then a valid balanced parentheses string and is added to the `result` vector.

-

**Recursive Steps**:

- **Add an Opening Parenthesis**: If the number of opening parentheses used so far (`open`) is less than `n`, we can add an opening parenthesis `(` to the current string and make a recursive call to build further.

- **Add a Closing Parenthesis**: If the number of closing parentheses used so far (`close`) is less than the number of opening parentheses (`open`), we can add a closing parenthesis `)` to the current string and make a recursive call.

-

**Termination**:

- The function continues recursively adding opening and closing parentheses while maintaining the validity of the string until all combinations are exhausted.

### [](#time-complexity-4)Time Complexity:

- The time complexity is `O(2^2n)` or exponential, as the number of valid balanced parentheses strings grows exponentially with `n`.

- However, the backtracking ensures that only valid strings are generated, making it much more efficient than brute-force generation of all possible strings.

</details>
