# A Plus B Again!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TAAPLUSB |
| Difficulty Rating | 1796 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [TAAPLUSB](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/TAAPLUSB) |

---

## Problem Statement

Have you ever implemented a program adding two big integers that cannot be represented by the primitive data type of your programming language? The algorithm is just simulation of the column addition method that we have been taught in elementary school. Sometimes we forget the carry and the result is incorrect.

 In this problem, you need to evaluate the expected value of the number of times we have non-zero carry when adding two non-negative integers that contain **at most N** digits each. Note that we are adding the numbers in their **base 10** representation.

For example, the following table shows the number of carries when adding some pairs of numbers:

**A**
		**B**
		**Number of carries**

20
		4
		0

111
		119
		1

123
		923
		1

1235
		98765
		5

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.
Each test case has a single line containing an integer **N**.

### Output

For each test case, output a single line containing the required expected value.
Your answer will be accepted if the error is less than 10 -6.

### Constraints

- **1** ≤ **T** ≤ **100,000(105)**

- **1** ≤ **N** ≤ **100,000(105)**

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
0.45
0.945
1.4445
```

**Explanation**

**Example case 1.**
We have 10*10 = 100 cases of adding two 1-digit number.
The carry appears when adding 1 and 9, 2 and 9, 3 and 9 ... and so on,
there are 45 cases in total and in each case, the carry appears exactly once.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
0.45
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
0.945
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
1.4445
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/TAAPLUSB)

[Contest](http://www.codechef.com/COOK36/problems/TAAPLUSB)

# Difficulty:

Easy

# Pre-requisites:

Linearity of Expectation, basic probability

# Problem:

Find the **expected number of carries** when adding two numbers, each at most **N** digits long.

# Explanation:

let       E[i] = probability that addition at ith place results in carry.

Then                E[1] = 45/100

and            **E[i] = 45/100 + 10/100 * E[i-1]**       for i > 1

(Justification in next section)

By linearity of expectation,

**Answer[N] = E[1] + E[2] … E[N]**

Therefore, one could first pre-compute all E[i]'s and then Answer[i]'s in O(N) time overall.

This gives complexity of **O(N+T)**.

However, it is also possible to have **O(1)** time per testcase.

This can be done by rewriting the above equation as:

                **(0.5 - E[i]) = 10/100 * (0.5 - E[i-1])**

Therefore,                                              **(0.5 - E[i]) = (0.5 - E[1]) / 10i-1 = 0.00…(i times 0)…05**

So,                       **Answer[N] =  E[1] + E[2] … E[N] = 0.5 * n - 0.0555…(n times 5)…5**

# Justifications:

Adding the digits at ith place results in a carry if

-

The sum of those two digits is more than 9. All such pairs of digits are (1, 9), (2, 9), (3, 9) …, (2, 8), (3, 8), …, (3, 7), (4, 7), …, (9, 1). There are 45 such pairs, therefore probability of this happening is **45/100**.

-

The sum of those two digits is exactly 9, and there was a carry from i-1th position. The sum of digits is 9 for the pairs (0, 9), (1, 8), (2, 7), … (9, 0). The probability of this happening is **10 / 100 * E[i-1]**.

Hence **E[i] = 45/100 + 10 * E[i-1] / 100**

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/COOK36/Setter/TAAPLUSB.cpp)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/COOK36/Tester/TAAPLUSB.cpp)

</details>
