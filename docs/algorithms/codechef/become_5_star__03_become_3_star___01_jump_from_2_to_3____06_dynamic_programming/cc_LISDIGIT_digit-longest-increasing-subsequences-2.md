# Digit Longest Increasing Subsequences 2

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LISDIGIT |
| Difficulty Rating | 1297 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [LISDIGIT](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/LISDIGIT) |

---

## Problem Statement

Recently Chef learned about [Longest Increasing Subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence). To be precise, he means longest **strictly** increasing subsequence, when he talks of longest increasing subsequence.  To check his understanding, he took his favorite **n**-digit number and for each of its **n** digits, he computed the length of the longest increasing subsequence of digits ending with that digit. Then he stored these lengths in an array named **LIS**.

For example, let us say that Chef's favourite **4**-digit number is **1531**, then the **LIS** array would be **[1, 2, 2, 1]**. The length of longest increasing subsequence ending at first digit is **1** (the digit **1** itself) and at the second digit is **2** (**[1, 5]**), at third digit is also **2** (**[1, 3]**), and at the **4**th digit is **1** (the digit **1** itself).

Now Chef wants to give you a challenge. He has a valid **LIS** array with him, and wants you to find any **n**-digit number having exactly the same **LIS** array? You are guaranteed that Chef's **LIS** array is valid, i.e. there exists at least one **n**-digit number corresponding to the given **LIS** array.

### Input

The first line of the input contains an integer **T** denoting the number of test cases.

For each test case, the first line contains an integer **n** denoting the number of digits in Chef's favourite number.

The second line will contain **n** space separated integers denoting **LIS** array, i.e. **LIS1, LIS2, ..., LISn**.

### Output

For each test case, output a single **n**-digit number (without leading zeroes) having exactly the given **LIS** array. If there are multiple **n**-digit numbers satisfying this requirement, any of them will be accepted.

### Constraints

- **1** ≤ **T** ≤ **30 000**

- **1** ≤ **n** ≤ **9**

- It is guaranteed that at least one **n**-digit number having the given **LIS** array exists

---

## Examples

**Example 1**

**Input**

```text
5
1 
1
2 
1 2
2 
1 1
4
1 2 2 1
7 
1 2 2 1 3 2 4
```

**Output**

```text
7
36
54
1531
1730418
```

**Explanation**

**Example case 1.** All one-digit numbers have the same **LIS** array, so any answer from **0** to **9** will be accepted.

**Example cases 2 & 3.** For a two digit number we always have **LIS1 = 1**, but the value of **LIS2** depends on whether the first digit is strictly less than the second one. If this is the case (like for number **36**), **LIS2 = 2**, otherwise (like for numbers **54** or **77**) the values of **LIS2** is **1**.

**Example case 4.** This has already been explained in the problem statement.

**Example case 5.** **7**-digit number **1730418** has **LIS** array **[1, 2, 2, 1, 3, 2, 4]**:

index
        LIS
        length

1
        **1**730418
        1

2
        **17**30418
        2

3
        **1**7**3**0418
        2

4
        173**0**418
        1

5
        **1**7**3**0**4**18
        3

6
        173**0**4**1**8
        2

7
        **1**7**3**0**4**1**8**
        4

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
1
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
36
```



#### Test case 3

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
54
```



#### Test case 4

**Input for this case**

```text
4
1 2 2 1
```

**Output for this case**

```text
1531
```



#### Test case 5

**Input for this case**

```text
7
1 2 2 1 3 2 4
```

**Output for this case**

```text
1730418
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/COOK78/problems/LISDIGIT)

[Practice](http://www.codechef.com/problems/LISDIGIT)

**Author:** [Alexey Zayakin](http://www.codechef.com/users/alex_2oo8)

**Testers:** [Hasan Jaddouh](http://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Alexey Zayakin](http://www.codechef.com/users/alex_2oo8)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Constructive algorithms, longest increasing subsequence

### PROBLEM:

For an n-digit number x we define the LIS array as follows: i-th element of the array is the length of the longest strictly increasing subsequence of numbers x digits that ends with the i-th digit.

Given the LIS array of some n-digit number, find any x that corresponds to this LIS array.

### QUICK EXPLANATION:

We can interpret the array in the input as array of digits of x, i.e. the i-th digit of x will be equal to the i-th element of the LIS array.

### EXPLANATION:

Let’s denote the i-th digit of number x with d_i, i.e. x = \overline{d_1 d_2 \dots d_n}.

What does it means that LIS[i] = k? It means that there exists a sequence p_1 < p_2 < \dots < p_{k - 1} < i such that LIS[p_1] = 1, LIS[p_2] = 2, \dots, LIS[p_{k - 1}] = k - 1 and digits d_{p_1}, d_{p_2}, \dots, d_{p_{k - 1}}, d_i form a strictly increasing sequence. The simplest way to make this sequence increasing is to simply assign d_{p_1} = 1, d_{p_2} = 2, \dots, d_{p_{k - 1}} = k - 1, d_i = k or in other words d_j = LIS[j].

Given that n \le 9, it follows that 1 \le LIS[i] \le 9 and thus all the values of the LIS array are indeed non-zero digits.

### Time Complexity:

\mathcal{O}(n) per test case.

### Bonus:

Can you solve this problem with constraints n \le 100?

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](http://www.codechef.com/download/Solutions/COOK78/Setter/LISDIGIT.cpp)

[Tester](http://www.codechef.com/download/Solutions/COOK78/Tester/LISDIGIT.cpp)

</details>
