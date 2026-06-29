# Beautiful Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTAR |
| Difficulty Rating | 1800 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [BTAR](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/BTAR) |

---

## Problem Statement

A sequence of integers is *beautiful* if each element of this sequence is divisible by 4.

You are given a sequence **a1, a2, ..., an**. In one step, you may choose any two elements of this sequence, remove them from the sequence and append their sum to the sequence. Compute the minimum number of steps necessary to make the given sequence beautiful.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains a single integer **n**.

- The second line contains **n** space-separated integers **a1, a2, ..., an**.

### Output

For each test case, print a single line containing one number — the minimum number of steps necessary to make the given sequence beautiful. If it's impossible to make the sequence beautiful, print -1 instead.

### Constraints

- 1 ≤ **T** ≤ 105

- 1 ≤ **n** ≤ 105

- 1 ≤ sum of **n** over all test cases ≤ 106

- 0 ≤ **ai** ≤ 109

---

## Examples

**Example 1**

**Input**

```text
1
7
1 2 3 1 2 3 8
```

**Output**

```text
3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](https://www.codechef.com/problems/BTAR)

[Contest](https://www.codechef.com/COOK89/problems/BTAR)

**Setter:** [Trung Nguyen](https://www.codechef.com/users/chemthan)

**Tester:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

# Difficulty

EASY

# Prerequisites

Modular Operation, Greedy Algorithms

# Problem

Find the minimum number of steps to convert the array such that each element is divisible by 4 or tell it is not possible to do so. Each step takes 2 elements of the array, removes them and puts back their sum back into the array.

# Explanation

Since we want all the numbers to be divisible by 4 in the end, it is easy to convert all numbers modulo 4 initially as all addition operations can be performed in modulo field only.

First of all, let us see when the answer will exist. The invariant here is that the sum of numbers before and after the operation doesn’t change. In the end, we want all the numbers to be divisible by 4, meaning that their sum should be also divisible by 4. Thus, if the initial sum is divisible by 4, then only the solution exists.

Let us call an element bad if it is not divisible by 4 else good. The basic observation is that we should not apply any operation on the good elements.

Now, let us try to find the minimum number of steps to convert the array into one with every number divisible by 4, only when the solution exists. In each step, we take 2 numbers and put back one number back into the array. Thus, each step can essentially fix a maximum of 2 bad elements in the array. Let us assume the count of elements leaving remainder 1, 2, 3 when divided by 4 are a_1, a_2 and a_3 respectively.

We will try to greedily pair elements of a_2 with a_2 and elements of a_1 with a_3. This helps us to achieve fixing a maximum of 2 elements at a time. Now, we can either we left with only 1 a_2 element or none. If we are left with 1 a_2 element, then we can pair with 2 remaining a_1 or a_3 elements. This will incur a total of 2 steps.

At last, we would be only left with a_1 or a_3 elements (if possible). This can only we fixed in one way. That is taking 4 of them and fixing them all together in 3 steps. Thus, we are able to fix all the elements of the array.

To prove this is the optimal strategy, see the claim we made regarding the maximum number of elements that can be fixed at any moment of time. Our approach strictly tries to maximise the number of elements that can be fixed in one step at any given moment of time. Thus, we proved our greedy algorithm. It is also recommended to go through the discussion by [@lebron](/u/lebron) [below](https://discuss.codechef.com/questions/119997/btar-editorial/120258) so that you get more details regarding the same.

For more details, refer to the editorialist solution below.

# Time Complexity

O(N), per test case

# Space Complexity

O(N) or O(1)

# Solution Links

[Setter’s solution](http://www.codechef.com/download/Solutions/COOK89/Setter/BTAR.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/COOK89/Tester/BTAR.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/COOK89/Editorialist/BTAR.cpp)

</details>
