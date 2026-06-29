# Practice problem - Transform the Expression

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STACK07 |
| Difficulty Rating | 992 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [STACK07](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACK07) |

---

## Problem Statement

Reverse Polish Notation (RPN) is a mathematical notation where every operator follows all of its operands. For instance, to add three and four, one would write "3 4 +" rather than "3 + 4". If there are multiple operations, the operator is given immediately after its second operand; so the expression written "3 − 4 + 5" would be written "3 4 − 5 +" first subtract 4 from 3, then add 5 to that.

Reverse polish notations are easier to parse for computers and you don't need parentheses to denote precedence of operations.

Transform the algebraic expression with brackets into RPN form.

You can assume that for the test cases below only single letters will be used, brackets [] will not be used and each expression has only one RPN form (no expressions like a*b*c)

---

## Input Format

- The first line contains t, the number of test cases (less then 100).
- Followed by t lines, containing an expression to be translated to RPN form, where the length of the expression is less then 400.

---

## Output Format

The *expression*s in RPN form, one per line.

---

## Examples

**Example 1**

**Input**

```text
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))
```

**Output**

```text
abc*+
ab+zx+*
at+bac++cd+^*
```

**Explanation**

**Test case 1: `(a+(b*c))`**
- Start with innermost brackets: `b*c` becomes `bc*`.
- Replace `(b*c)` in the original expression: it becomes `(a+bc*)`.
- Process the addition: `a+bc*` becomes `abc*+`.\
**Result:** `abc*+`.

**Test case 2: `((a+b)*(z+x))`**
- Start with the first set of brackets: `a+b` becomes `ab+`.
- Process the second set of brackets: `z+x` becomes `zx+`.
- Combine with the multiplication: `(ab+)*(zx+)` becomes `ab+zx+*`.\
**Result:** `ab+zx+*`.

**Test case 3: `((a+t)*((b+(a+c))^(c+d)))`**
- Start with the innermost brackets:
  - `a+c` becomes `ac+`.
  - `b+(a+c)` becomes `bac++`.
- Process the next set of brackets: `bac++^(c+d)`:
  - `c+d` becomes `cd+`.
  - `bac++^cd+` combines to `bac++cd+^`.
- Finally, handle the outermost multiplication: `(a+t)` becomes `at+`, so `(at+)*(bac++cd+^)` becomes `at+bac++cd+^*`.\
**Result:** `at+bac++cd+^*`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
(a+(b*c))
```

**Output for this case**

```text
abc*+
```



#### Test case 2

**Input for this case**

```text
((a+b)*(z+x))
```

**Output for this case**

```text
ab+zx+*
```



#### Test case 3

**Input for this case**

```text
((a+t)*((b+(a+c))^(c+d)))
```

**Output for this case**

```text
at+bac++cd+^*
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### [](#problem-link-stack07httpswwwcodechefcomlearncoursestacks-and-queueslstacks02problemsstack07-1)Problem Link - [STACK07](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACK07)

### [](#problem-statement-2)Problem Statement

Reverse Polish Notation (RPN) is a mathematical notation where every operator follows all of its operands. For instance, to add three and four, one would write `3 4 +` rather than `3 + 4`. If there are multiple operations, the operator is given immediately after its second operand; so the expression written `3 − 4 + 5` would be written `3 4 − 5 +` first subtract `4` from `3`, then add `5` to that.

Reverse polish notations are easier to parse for computers and you don’t need parentheses to denote precedence of operations.

Transform the algebraic expression with brackets into **RPN** form.

### [](#approach-3)Approach:

The key idea is to use a stack to maintain operators and their precedence while converting the infix expression to postfix:

-

**Stack for Operators**: A stack stores operators and parentheses, allowing us to manage the order of operations based on their precedence.

-

**Traversing the Infix Expression**: For each character in the infix expression:

- If it’s an operand, add it directly to the result.

- If it’s `(`, push it onto the stack.

- If it’s `)`, pop from the stack until the matching `(` is found.

-

**Handling Operators**: For an operator, pop operators from the stack to the result until the top of the stack has a lower precedence, then push the current operator.

-

**Final Step**: After processing all characters, pop any remaining operators from the stack to the result.

### [](#time-complexity-4)Time Complexity:

**O(n)**, where `n` is the length of the infix expression, since we process each character once.

### [](#space-complexity-5)Space Complexity:

**O(n)**, as the stack may need to store all operators and parentheses in the worst case.

</details>
