# Add Strings (Big Integer Addition)

| | |
|---|---|
| **ID** | `math_05` |
| **Category** | math |
| **Complexity (required)** | $O(max(N, M)$) Time, $O(max(N, M)$) Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Add Strings](https://leetcode.com/problems/add-strings/) |

## Problem statement

Given two non-negative integers `num1` and `num2` represented as strings.
Return the sum of `num1` and `num2` as a string.
You must not use any built-in BigInteger library or convert the inputs to integers directly (e.g., you cannot do `return str(int(num1) + int(num2))`).

**Input:** Two strings `num1` and `num2`.
**Output:** A string representing their sum.

## When to use it

- To handle mathematical overflow limits in languages with strict 32-bit or 64-bit integer limits (like C++, Java, or Go).
- An incredibly common warm-up or screener interview question to test basic array iteration and boundary handling.

## Approach

**1. The Grade-School Addition Logic:**
We must simulate how we add numbers on paper: vertically, starting from the rightmost digit (the ones place), moving left, and carrying over any overflow to the next column.

**2. Two Pointers and a Carry:**
Set two pointers `p1` and `p2` to the last indices of `num1` and `num2`.
Initialize a `carry = 0`.
While either pointer is \ge 0, or the `carry` is > 0:
1. Extract the digit from `num1[p1]`. (If `p1 < 0`, treat it as `0`).
2. Extract the digit from `num2[p2]`. (If `p2 < 0`, treat it as `0`).
3. Add them together: `total = digit1 + digit2 + carry`.
4. The digit to append to our result is `total % 10`.
5. The new carry to pass to the next loop is `total // 10`.
6. Decrement both pointers.

**3. String Construction:**
Because strings are immutable in most languages, constantly prepending to a string `result = char + result` takes $O(N)$ time per character, turning the algorithm into $O(N^2)$!
Always append the characters to an array/list, and then `reverse()` the array and `join()` it at the very end to maintain $O(N)$ time.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_05: Big Integer Add (Strings).

Add two non-negative integers given as digit strings.
"""


def solve(a, b):
    if not a:
        return b
    if not b:
        return a
    a_rev = a[::-1]
    b_rev = b[::-1]
    n = max(len(a_rev), len(b_rev))
    carry = 0
    out = []
    for i in range(n):
        da = int(a_rev[i]) if i < len(a_rev) else 0
        db = int(b_rev[i]) if i < len(b_rev) else 0
        s = da + db + carry
        out.append(str(s % 10))
        carry = s // 10
    if carry:
        out.append(str(carry))
    return "".join(reversed(out))
```

</details>

## Walk-through

`num1 = "456"`, `num2 = "77"`.
`p1 = 2 ('6')`, `p2 = 1 ('7')`. `carry = 0`.

1. `digit1 = 6`, `digit2 = 7`.
   - `sum = 6 + 7 + 0 = 13`.
   - `curr = 13 % 10 = 3`. `carry = 1`.
   - `res = ['3']`.
   - `p1 = 1`, `p2 = 0`.
2. `digit1 = 5`, `digit2 = 7`.
   - `sum = 5 + 7 + 1 = 13`.
   - `curr = 13 % 10 = 3`. `carry = 1`.
   - `res = ['3', '3']`.
   - `p1 = 0`, `p2 = -1`.
3. `digit1 = 4`, `digit2 = 0` (Out of bounds!).
   - `sum = 4 + 0 + 1 = 5`.
   - `curr = 5 % 10 = 5`. `carry = 0`.
   - `res = ['3', '3', '5']`.
   - `p1 = -1`, `p2 = -2`.
4. `p1 < 0` AND `p2 < 0` AND `carry == 0`. Loop terminates.

Reverse `res`: `['5', '3', '3']`.
Join: `"533"`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\max(N, M)$) | $O(\max(N, M)$) |
| **Average** | $O(\max(N, M)$) | $O(\max(N, M)$) |
| **Worst** | $O(\max(N, M)$) | $O(\max(N, M)$) |

Let N and M be the lengths of the two strings.
We iterate a number of times exactly equal to the length of the longest string, plus at most 1 extra iteration for a final carry. Time complexity is strictly linear $O(\max(N, M)$).
Space complexity is $O(\max(N, M)$) to store the output character array before joining it.

## Variants & optimizations

- **Multiply Strings:** A harder variant! You create a result array of size `N + M` initialized to zeros. You run a nested loop multiplying every digit in `num1` by every digit in `num2`. The product of `num1[i]` and `num2[j]` ALWAYS adds its value to `result[i + j + 1]` and its carry to `result[i + j]`.
- **Add Binary:** The exact same algorithm, but instead of `% 10` and `// 10`, you use `% 2` and `// 2`.

## Real-world applications

- **Arbitrary-Precision Arithmetic:** Standard implementation inside standard libraries (like Java's `BigInteger` or C++'s GNU MP library) to handle numbers that exceed physical CPU register limits.

## Related algorithms in cOde(n)

- **[math_04 - Karatsuba Multiplication](math_04_karatsuba-multiplication.md)** — The advanced algorithm to multiply big integers incredibly fast, which internally relies on this addition algorithm.
- **[linked_list_03 - Add Two Numbers](../linked_list/ll_03_add-two-numbers.md)** — The exact same logic, but the digits are stored as nodes in a Linked List instead of characters in a string.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
