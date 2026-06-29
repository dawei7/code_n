# Ciel and A-B Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CIELAB |
| Difficulty Rating | 1136 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CIELAB](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CIELAB) |

---

## Problem Statement

In Ciel's restaurant, a waiter is training.
Since the waiter isn't good at arithmetic, sometimes he gives guests wrong change.
Ciel gives him a simple problem.
What is **A**-**B** (**A** minus **B**) ?

Surprisingly, his answer is wrong.
To be more precise, his answer has exactly one wrong digit.
Can you imagine this?
Can you make the same mistake in this problem?

### Input

An input contains 2 integers **A** and **B**.

### Output

Print a wrong answer of **A**-**B**.
Your answer must be a *positive* integer containing the same number of digits as the correct answer, and exactly one digit must differ from the correct answer.
Leading zeros are not allowed.
If there are multiple answers satisfying the above conditions, anyone will do.

### Constraints

1 ≤ **B** < **A** ≤ 10000

---

## Examples

**Example 1**

**Input**

```text
5858 1234
```

**Output**

```text
1624
```

**Explanation**

The correct answer of 5858-1234 is 4624.
So, for instance, 2624, 4324, 4623, 4604 and 4629 will be accepted, but 0624, 624, 5858, 4624 and 04624 will be rejected.

### Notes

The problem setter is also not good at arithmetic.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/CIELAB/)

[Contest](http://www.codechef.com/COOK17/problems/CIELAB/)

### DIFFICULTY

EASY

### EXPLANATION

This is the easiest problem in the set. This problem can be solved various methods. For instance,           if **A - B** mod 10 = 9, print **A - B** - 1, otherwise print **A - B** + 1. Be careful not to print 0 if **A - B**    = 1. Your answer must be a positive integer.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK17/Setter/CIELAB.c).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK17/Tester/CIELAB.cpp).

</details>
