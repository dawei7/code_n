# Valid Parenthesis

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STACK05 |
| Difficulty Rating | 932 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [STACK05](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACK05) |

---

## Problem Statement

A string of parentheses is considered valid if each opening parenthesis has a matching closing parenthesis and the pairs are properly nested. In a valid parenthesis string, every opening bracket '(' must have a corresponding closing bracket ')' that occurs after the opening bracket, and there must not be any extra or unpaired brackets.

Here are the rules for a string of parentheses to be valid:

1. **Correct order**: Each closing parenthesis must correspond to the latest unmatched opening parenthesis.
2. **Matching pairs**: For every opening parenthesis, there must be a closing parenthesis.

Let's look at some examples:

- `"()"` - This is valid because the only pair of parentheses correctly matches and is in the right order.
- `"()()"` - This is also valid. There are two separate but correct matches.
- `"(()())"` - Valid as well, since the inner pair is nested within the outer pair and they all match up.
- `"(())"` - The inner pair is nested within the outer pair, with both pairs being correctly matched.
- `")("` or `"("` or `")"` - All invalid because they contain either unmatched or improperly ordered parentheses.

The goal is to determine if parentheses (and optionally other brackets like curly braces and square brackets) in an expression are properly balanced. \
Check the sample test cases given below for expected input and output format.

Complete the code in the IDE to solve this problem.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

For each test case, output on a new line the maximum value of $A_1+A_N$ you can get after several right rotations.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
((()))
()()()
(((())
```

**Output**

```text
((())) : true
()()() : true
(((()) : false
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
((()))
```

**Output for this case**

```text
((())) : true
```



#### Test case 2

**Input for this case**

```text
()()()
```

**Output for this case**

```text
()()() : true
```



#### Test case 3

**Input for this case**

```text
(((())
```

**Output for this case**

```text
(((()) : false
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Valid Parenthesis](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACK05)

### [](#problem-statement-1)Problem Statement -

A string of parentheses is considered valid if each opening parenthesis has a matching closing parenthesis and the pairs are properly nested. In a valid parenthesis string, every opening bracket `(` must have a corresponding closing bracket `)` that occurs after the opening bracket, and there must not be any extra or unpaired brackets.

### [](#approach-2)Approach:

The key idea behind this code is to use a stack to keep track of the parentheses as we traverse the expression.

-

**Stack for Parentheses**:

-

We use an array `a[]` and a `top` variable to implement a stack where we push every opening parenthesis `(` and pop it when a closing parenthesis `)` is encountered.

-

The `push()` function adds an element to the stack, while `pop()` removes the top element.

-

**Checking Matching Pairs**:

-

When a closing parenthesis `)` is found, the program checks if there’s a corresponding opening parenthesis `(` in the stack.

-

We use the `isMatchingPair()` function to ensure the popped character is an opening parenthesis that correctly matches the closing one.

-

**Balanced Expression**:

-

As we go through the expression, if we encounter any mismatched or unpaired closing parenthesis, we immediately return `false`, meaning the expression is unbalanced.

-

After traversing the entire expression, if the stack is empty, it means every opening parenthesis was properly matched with a closing one, and the expression is balanced.

-

**Edge Case**:

- If we find a closing parenthesis but the stack is already empty (i.e., no matching opening parenthesis), the expression is unbalanced.

### [](#time-complexity-3)Time Complexity:

- The time complexity is **O(n)**, where `n` is the length of the expression. This is because we traverse the expression once, pushing and popping elements as we go.

### [](#space-complexity-4)Space Complexity:

- The space complexity is **O(n)** in the worst case, where `n` is the number of characters in the expression, as we might need to store all opening parentheses in the stack.

</details>
