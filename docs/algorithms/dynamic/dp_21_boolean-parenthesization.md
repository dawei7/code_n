# Boolean Parenthesization

| | |
|---|---|
| **ID** | `dp_21` |
| **Category** | dynamic |
| **Complexity (required)** | $O(N^3)$ Time, $O(N^2)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 5/10 |
| **GeeksForGeeks Equivalent** | [Boolean Parenthesization Problem](https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/) |

## Problem statement

Given a boolean expression consisting of symbols `T` (True) and `F` (False), separated by boolean operators `&` (AND), `|` (OR), and `^` (XOR).
Count the number of ways we can parenthesize the expression so that the entire expression evaluates to `True`.

**Input:** A string `s` of length N, containing symbols `T, F` at even indices and operators `&, |, ^` at odd indices.
**Output:** An integer representing the number of valid parenthesizations. (Often modulo 10^9 + 7).

## When to use it

- The ultimate test of **Interval DP** combined with combinatorial logic.
- If you can solve this, Matrix Chain Multiplication (`dp_13`) is trivial to you.

## Approach

**1. Define the State:**
Unlike Matrix Chain Multiplication, a single DP array is not enough! We don't just need to know how many ways a sub-expression evaluates to `True`. Because of the `^` (XOR) operator, a `True` can be formed by `True ^ False` AND `False ^ True`!
Therefore, we must track BOTH the `True` ways and the `False` ways.
- `dpT[i][j]` = number of ways the sub-expression from index `i` to `j` evaluates to `True`.
- `dpF[i][j]` = number of ways the sub-expression from index `i` to `j` evaluates to `False`.

*(Note: `i` and `j` only point to the `T/F` symbols, which are at even indices 0, 2, 4...)*

**2. Find the Base Cases:**
If `i == j`, the sub-expression is a single symbol!
- If `s[i] == 'T'`, then `dpT[i][i] = 1` and `dpF[i][i] = 0`.
- If `s[i] == 'F'`, then `dpT[i][i] = 0` and `dpF[i][i] = 1`.

**3. Find the Transition (The recurrence relation):**
To evaluate an expression from `i` to `j`, we split it at every possible operator `k`.
Since symbols are at even indices, the operators are at odd indices k = i+1, i+3, \dots, j-1.
The left sub-expression is `i` to `k-1`. The right sub-expression is `k+1` to `j`.
For a specific operator at `s[k]`, we cross-multiply the combinations:
- `leftT = dpT[i][k-1]`, `leftF = dpF[i][k-1]`
- `rightT = dpT[k+1][j]`, `rightF = dpF[k+1][j]`

Depending on `s[k]`:
- **If `&` (AND):**
  - To get `True`, both sides MUST be True. `Ways = leftT * rightT`.
  - To get `False`, anything else works. `Ways = (leftT * rightF) + (leftF * rightT) + (leftF * rightF)`.
- **If `|` (OR):**
  - To get `True`, at least one side must be True. `Ways = (leftT * rightF) + (leftF * rightT) + (leftT * rightT)`.
  - To get `False`, both sides MUST be False. `Ways = leftF * rightF`.
- **If `^` (XOR):**
  - To get `True`, the sides must be DIFFERENT. `Ways = (leftT * rightF) + (leftF * rightT)`.
  - To get `False`, the sides must be the SAME. `Ways = (leftT * rightT) + (leftF * rightF)`.

We sum these `Ways` across ALL possible split points `k` to build `dpT[i][j]` and `dpF[i][j]`!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_21: Boolean Parenthesization.

Count the number of ways to parenthesize a boolean
expression (operands T/F, operators &|^) so it evaluates
to True. Interval DP: T[i][j] / F[i][j] = count of ways
for s[i..j]. At each split, combine the four quadrants
based on the operator.
"""


def solve(s, n):
    if n == 0:
        return 0
    T = [[0] * n for _ in range(n)]
    F = [[0] * n for _ in range(n)]
    for i in range(0, n, 2):
        T[i][i] = 1 if s[i] == "T" else 0
        F[i][i] = 1 if s[i] == "F" else 0
    for gap in range(2, n, 2):
        for i in range(0, n - gap, 2):
            j = i + gap
            T[i][j] = F[i][j] = 0
            for k in range(i + 1, j, 2):
                op = s[k]
                lt, lf = T[i][k - 1], F[i][k - 1]
                rt, rf = T[k + 1][j], F[k + 1][j]
                if op == "&":
                    T[i][j] += lt * rt
                    F[i][j] += lt * rf + lf * rt + lf * rf
                elif op == "|":
                    T[i][j] += lt * rt + lt * rf + lf * rt
                    F[i][j] += lf * rf
                else:  # ^
                    T[i][j] += lt * rf + lf * rt
                    F[i][j] += lt * rt + lf * rf
    return T[0][n - 1]
```

</details>

## Walk-through

`s = "T|F&T"`. N=5.
Base Cases (Length 1):
`dpT[0][0]=1` (T), `dpF[2][2]=1` (F), `dpT[4][4]=1` (T).

1. **Length 3:**
   - **i=0, j=2 (`T|F`):** Split at k=1 (`|`).
     - `dpT[0][2] = (1*0) + (1*1) + (0*0) = 1`.
     - `dpF[0][2] = (0*1) = 0`.
   - **i=2, j=4 (`F&T`):** Split at k=3 (`&`).
     - `dpT[2][4] = (0*1) = 0`.
     - `dpF[2][4] = (0*0) + (1*1) + (1*0) = 1`.

2. **Length 5:**
   - **i=0, j=4 (`T|F&T`):**
     - Split at k=1 (`|`): Left `T` (0...0), Right `F&T` (2...4).
       - `leftT=1`, `rightT=0` (from `dpT[2][4]`), `rightF=1`.
       - `Ways True` for `|`: `(1*0) + (1*1) + (0*0) = 1`.
     - Split at k=3 (`&`): Left `T|F` (0...2), Right `T` (4...4).
       - `leftT=1`, `rightT=1`, `rightF=0`.
       - `Ways True` for `&`: `(1*1) = 1`.
     - Total `dpT[0][4]` = 1 + 1 = 2.

Result `dpT[0][4]` is 2. ✓ (Ways are `(T|F)&T` -> `T&T` -> `T`, and `T|(F&T)` -> `T|F` -> `T`).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^3)$ | $O(N^2)$ |
| **Average** | $O(N^3)$ | $O(N^2)$ |
| **Worst** | $O(N^3)$ | $O(N^2)$ |

The loops generate $O(N^2)$ intervals. For each interval, we test $O(N)$ split points k. Total time is strictly $O(N^3)$.
Space complexity requires two N x N matrices, taking $O(N^2)$ space.

## Variants & optimizations

- **Top-Down Memoization:** Interval DP is notoriously difficult to loop correctly (bottom-up by length). Many developers prefer to write this as a recursive function `solve(i, j, is_true)` with an N x N x 2 memoization cache. The time/space complexity is mathematically identical, but it is vastly easier to read and implement under time pressure in an interview!

## Real-world applications

- **Compiler Design:** Parsing logical expressions and calculating the number of valid AST (Abstract Syntax Tree) generations for ambiguous grammars.

## Related algorithms in cOde(n)

- **[dp_13 - Matrix Chain Multiplication](dp_13_matrix-chain-multiplication.md)** — The foundational Interval DP framework.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
